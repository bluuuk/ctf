use std::{
    collections::BTreeMap,
    env,
    fs::{File, OpenOptions},
    io,
    io::{stdin, stdout, Read, Seek, SeekFrom, Write},
    sync::{atomic::AtomicBool, atomic::Ordering, Arc, Mutex},
    thread,
};

#[derive(Debug, Clone, Copy)]
enum IoRequest {
    // write up to 4 byte of R0 to stdout
    IoWrite(u8),
    // read up to 4 byte of stdin to low byte of R0
    IoRead(u8),
}

#[derive(Debug, Clone, Copy)]
enum IntType {
    Io(IoRequest),
}

#[derive(Debug, Clone, Copy)]
enum InsnType {
    // Treat register arguments as size X for next instruction
    // Pre8,
    // Pre16,

    // Push X to the stack
    PushR0,
    PushR1,

    // Pop X from the stack
    PopR0,
    PopR1,

    // Call the function at address and push PC to stack
    Call(u32),
    // Return to top of the stack
    Ret,

    // Jump to address in R0
    JmpR0,
    // Jump to address
    Jmp(u32),

    // Jump to address in R0 if ZERO
    JmpEqR0,
    // Jump to address if ZERO
    JmpEq(u32),

    // Jump to address in R0 if not ZERO
    JmpNeR0,
    // Jump to address if not ZERO
    JmpNe(u32),

    // R0 = R0 + R1
    Add,
    // R0 = R0 - R1
    Sub,

    // R0 = R0 & R1
    And,
    // R0 = R0 | R1
    Or,
    // R0 = R0 ^ R1
    Xor,

    // R0 = R1
    MovR0R1,
    // R1 = R0
    MovR1R0,
    // R0 = const
    MovR0(u32),
    // R1 = const
    MovR1(u32),

    // R1 = content of memory at R0
    LoadR0,
    // R1 = content of memory at given addr
    Load(u32),

    // content of memory at R0 = R1
    StoreR0,
    // cotent of memory at given addr = R1
    Store(u32),

    // do interrupt
    Int(IntType),

    // do nothing
    Nop,
    // stop execution
    Halt,
}

macro_rules! from_parsed_arg {
    ($insn_ty:ident, $reader:ident, $size:expr, $op_size:expr) => {{
        let op_size = $op_size;
        let mut addr = [0; 4];

        let nread = $reader
            .read(&mut addr[..op_size as usize])
            .ok()
            .unwrap_or(0) as u8;

        if nread != op_size {
            None
        } else {
            Some(Insn {
                ty: InsnType::$insn_ty(as_u32_le(&addr[..op_size as usize])),
                size: $size + nread as u8,
                op_size,
            })
        }
    }};
}

#[derive(Debug, Clone)]
struct Insn {
    ty: InsnType,
    size: u8,
    op_size: u8,
}

fn as_u32_le(array: &[u8]) -> u32 {
    match array.len() {
        4 => {
            ((array[0] as u32) << 0)
                + ((array[1] as u32) << 8)
                + ((array[2] as u32) << 16)
                + ((array[3] as u32) << 24)
        }
        2 => ((array[0] as u32) << 0) + ((array[1] as u32) << 8),
        1 => (array[0] as u32) << 0,
        _ => panic!("invalid array length for conversion"),
    }
}

fn write_u32_to_buf(buf: &mut [u8], value: u32, nbytes: u8) {
    let value = value & maskx(nbytes);
    buf.copy_from_slice(&value.to_le_bytes()[..nbytes as usize]);
}

fn maskx(size_in_bytes: u8) -> u32 {
    match size_in_bytes {
        1 => 0xFF,
        2 => 0xFFFF,
        _ => 0xFFFFFFFF,
    }
}

impl Insn {
    pub fn decode(mut reader: impl Read) -> Option<Insn> {
        let mut size = 0u8;
        let mut first = [0];

        let mut nread = reader.read(&mut first).ok().unwrap_or(0);
        if nread == 0 {
            return None;
        }

        let op_size = match first[0] as char {
            'b' => {
                size += nread as u8;
                nread = reader.read(&mut first).ok().unwrap_or(0);
                1
            }
            'h' => {
                size += nread as u8;
                nread = reader.read(&mut first).ok().unwrap_or(0);
                2
            }
            _ => 4,
        };

        if nread == 0 {
            return None;
        }

        size += nread as u8;

        match first[0] as char {
            // push r0
            'p' => Some(Insn {
                ty: InsnType::PushR0,
                size,
                op_size,
            }),
            // push r1
            'P' => Some(Insn {
                ty: InsnType::PushR1,
                size,
                op_size,
            }),

            // pop r0
            'q' => Some(Insn {
                ty: InsnType::PopR0,
                size,
                op_size,
            }),
            // pop r1
            'Q' => Some(Insn {
                ty: InsnType::PopR1,
                size,
                op_size,
            }),

            // call
            'C' if op_size == 4 => {
                from_parsed_arg!(Call, reader, size, op_size)
            }
            // return
            'R' if op_size == 4 => Some(Insn {
                ty: InsnType::Ret,
                size,
                op_size,
            }),

            // jump
            'j' if op_size == 4 => Some(Insn {
                ty: InsnType::JmpR0,
                size,
                op_size,
            }),
            'J' if op_size == 4 => {
                from_parsed_arg!(Jmp, reader, size, op_size)
            }
            // jump equal
            'e' if op_size == 4 => Some(Insn {
                ty: InsnType::JmpEqR0,
                size,
                op_size,
            }),
            'E' if op_size == 4 => {
                from_parsed_arg!(JmpEq, reader, size, op_size)
            }
            // jump not equal
            'n' if op_size == 4 => Some(Insn {
                ty: InsnType::JmpNeR0,
                size,
                op_size,
            }),
            'N' if op_size == 4 => {
                from_parsed_arg!(JmpNe, reader, size, op_size)
            }

            // add
            '+' => Some(Insn {
                ty: InsnType::Add,
                size,
                op_size,
            }),
            // sub
            '-' => Some(Insn {
                ty: InsnType::Sub,
                size,
                op_size,
            }),

            // and
            '&' => Some(Insn {
                ty: InsnType::And,
                size,
                op_size,
            }),
            // or
            '|' => Some(Insn {
                ty: InsnType::Or,
                size,
                op_size,
            }),
            // xor
            '^' => Some(Insn {
                ty: InsnType::Xor,
                size,
                op_size,
            }),

            // mov r0 -> r1
            '>' => Some(Insn {
                ty: InsnType::MovR0R1,
                size,
                op_size,
            }),
            // mov r1 -> r0
            '<' => Some(Insn {
                ty: InsnType::MovR1R0,
                size,
                op_size,
            }),

            // mov const -> r0
            'm' => {
                from_parsed_arg!(MovR0, reader, size, op_size)
            }
            // mov const -> r1
            'M' => {
                from_parsed_arg!(MovR1, reader, size, op_size)
            }

            // load r0
            'l' => Some(Insn {
                ty: InsnType::LoadR0,
                size,
                op_size,
            }),
            // load const addr
            'L' => {
                // cannot use the macro here because op_size is the load size not the size of the addr
                let mut addr = [0; 4];
                let nread = reader.read(&mut addr).ok().unwrap_or(0);

                if nread != addr.len() {
                    None
                } else {
                    size += nread as u8;

                    Some(Insn {
                        ty: InsnType::Load(as_u32_le(&addr)),
                        size,
                        op_size,
                    })
                }
            }

            // store r0
            's' => Some(Insn {
                ty: InsnType::StoreR0,
                size,
                op_size,
            }),
            // store const addr
            'S' => {
                // cannot use the macro here because op_size is the store size not the size of the addr
                let mut addr = [0; 4];
                let nread = reader.read(&mut addr).ok().unwrap_or(0);

                if nread != addr.len() {
                    None
                } else {
                    size += nread as u8;

                    Some(Insn {
                        ty: InsnType::Store(as_u32_le(&addr)),
                        size,
                        op_size,
                    })
                }
            }

            // interrupt
            '#' => {
                let mut int_ty = [0];
                let nread = reader.read(&mut int_ty).ok().unwrap_or(0);

                if nread != int_ty.len() {
                    None
                } else {
                    size += nread as u8;

                    match int_ty[0] as char {
                        'i' => Some(Insn {
                            ty: InsnType::Int(IntType::Io(IoRequest::IoRead(op_size as u8))),
                            size,
                            op_size,
                        }),
                        'o' => Some(Insn {
                            ty: InsnType::Int(IntType::Io(IoRequest::IoWrite(op_size as u8))),
                            size,
                            op_size,
                        }),
                        _ => None,
                    }
                }
            }

            // nop
            '.' | '\n' => Some(Insn {
                ty: InsnType::Nop,
                size,
                op_size,
            }),
            // halt
            'H' => Some(Insn {
                ty: InsnType::Halt,
                size,
                op_size,
            }),

            _ => None,
        }
    }

    pub fn execute(&self, regs: &mut Registers, memory: &mut Memory) -> Option<Execution> {
        let mut assume = PartialRegisters::new(regs.pc);
        regs.pc += self.size as u32;

        // an execution which always fails validation
        const INVALID_EXECUTION: Option<Execution> = Some(Execution {
            assume: PartialRegisters {
                pc: 0,
                sp: None,
                r0: None,
                r1: None,
                zero: None,
            },
            result: ExecutionResult {
                regs: Registers {
                    pc: 0,
                    sp: 0,
                    r0: 0,
                    r1: 0,
                    zero: true,
                },
                read_at: None,
                write_at: None,
                io_request: None,
            },
        });

        match self.ty {
            // Push X to the stack
            InsnType::PushR0 => {
                assume.sp = Some(regs.sp);
                assume.r0 = Some(regs.r0);
                regs.sp += 4;

                if let Some(top) = memory.fetch_mut(regs.sp, 4) {
                    write_u32_to_buf(top, regs.r0, self.op_size);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: None,
                        write_at: assume.sp,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }
            InsnType::PushR1 => {
                assume.sp = Some(regs.sp);
                assume.r1 = Some(regs.r1);
                regs.sp += 4;

                if let Some(top) = memory.fetch_mut(regs.sp, 4) {
                    write_u32_to_buf(top, regs.r1, self.op_size);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: None,
                        write_at: assume.sp,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }

            // Pop X from the stack
            InsnType::PopR0 => {
                assume.sp = Some(regs.sp);
                if let Some(top) = memory.fetch(regs.sp, 4) {
                    regs.sp -= 4;
                    regs.r0 = as_u32_le(top);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: assume.sp,
                        write_at: None,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }
            InsnType::PopR1 => {
                assume.sp = Some(regs.sp);
                if let Some(top) = memory.fetch(regs.sp, 4) {
                    regs.sp -= 4;
                    regs.r1 = as_u32_le(top);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: assume.sp,
                        write_at: None,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }

            // Call the function at address and push PC to stack
            InsnType::Call(addr) => {
                assume.sp = Some(regs.sp);
                regs.sp += 4;

                if let Some(top) = memory.fetch_mut(regs.sp, 4) {
                    write_u32_to_buf(top, regs.pc, 4);
                    regs.pc = addr;

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: None,
                        write_at: assume.sp,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }
            // Return to top of the stack
            InsnType::Ret => {
                assume.sp = Some(regs.sp);
                if let Some(top) = memory.fetch(regs.sp, 4) {
                    regs.sp -= 4;
                    regs.pc = as_u32_le(top);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: assume.sp,
                        write_at: None,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }

            // Jump to address in R0
            InsnType::JmpR0 => {
                assume.r0 = Some(regs.r0);
                regs.pc = regs.r0;
                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // Jump to address
            InsnType::Jmp(addr) => {
                regs.pc = addr;
                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }

            // Jump to address in R0 if ZERO
            InsnType::JmpEqR0 => {
                assume.zero = Some(regs.zero);

                if regs.zero {
                    assume.r0 = Some(regs.r0);
                    regs.pc = regs.r0;
                }

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // Jump to address if ZERO
            InsnType::JmpEq(addr) => {
                assume.zero = Some(regs.zero);

                if regs.zero {
                    regs.pc = addr;
                }

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }

            // Jump to address in R0 if not ZERO
            InsnType::JmpNeR0 => {
                assume.zero = Some(regs.zero);

                if !regs.zero {
                    assume.r0 = Some(regs.r0);
                    regs.pc = regs.r0;
                }

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // Jump to address if not ZERO
            InsnType::JmpNe(addr) => {
                assume.zero = Some(regs.zero);

                if !regs.zero {
                    regs.pc = addr;
                }

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }

            // R0 = R0 + R1
            InsnType::Add => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r0 = (regs.r0 & !mask) | ((regs.r0.overflowing_add(regs.r1).0) & mask);

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // R0 = R0 - R1
            InsnType::Sub => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r0 = (regs.r0 & !mask) | ((regs.r0.overflowing_sub(regs.r1).0) & mask);
                regs.zero = (regs.r0 & mask) == 0;

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }

            // R0 = R0 & R1
            InsnType::And => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r0 = (regs.r0 & !mask) | ((regs.r0 & regs.r1) & mask);

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // R0 = R0 | R1
            InsnType::Or => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r0 = (regs.r0 & !mask) | ((regs.r0 | regs.r1) & mask);

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // R0 = R0 ^ R1
            InsnType::Xor => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r0 = (regs.r0 & !mask) | ((regs.r0 ^ regs.r1) & mask);

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }

            // R0 = R1
            InsnType::MovR0R1 => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r0 = (regs.r0 & !mask) | (regs.r1 & mask);

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // R1 = R0
            InsnType::MovR1R0 => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                let mask = maskx(self.op_size);

                regs.r1 = (regs.r1 & !mask) | (regs.r0 & mask);

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // R0 = const
            InsnType::MovR0(constant) => {
                regs.r0 = constant;
                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }
            // R1 = const
            InsnType::MovR1(constant) => {
                regs.r1 = constant;
                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                };

                Some(Execution { assume, result })
            }

            // R1 = content of memory at R0
            InsnType::LoadR0 => {
                assume.r0 = Some(regs.r0);

                if let Some(mem) = memory.fetch(regs.r0, self.op_size as u32) {
                    regs.r1 = as_u32_le(mem);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: assume.r0,
                        write_at: None,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }
            // R1 = content of memory at given addr
            InsnType::Load(addr) => {
                if let Some(mem) = memory.fetch(addr, self.op_size as u32) {
                    regs.r1 = as_u32_le(mem);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: Some(addr),
                        write_at: None,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }

            // content of memory at R0 = R1
            InsnType::StoreR0 => {
                assume.r0 = Some(regs.r0);
                assume.r1 = Some(regs.r1);

                if let Some(mem) = memory.fetch_mut(regs.r0, self.op_size as u32) {
                    write_u32_to_buf(mem, regs.r1, self.op_size);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: None,
                        write_at: assume.r0,
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }
            // cotent of memory at given addr = R1
            InsnType::Store(addr) => {
                assume.r1 = Some(regs.r1);

                if let Some(mem) = memory.fetch_mut(addr, self.op_size as u32) {
                    write_u32_to_buf(mem, regs.r1, self.op_size);

                    let result = ExecutionResult {
                        regs: regs.clone(),
                        read_at: None,
                        write_at: Some(addr),
                        io_request: None,
                    };

                    Some(Execution { assume, result })
                } else {
                    INVALID_EXECUTION
                }
            }

            // do interrupt
            InsnType::Int(IntType::Io(io_request)) => {
                // no need to assume here because io is handled in-order
                // assume.r0 = Some(regs.r0)

                let result = ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: Some(io_request),
                };

                Some(Execution { assume, result })
            }

            // do nothing
            InsnType::Nop => Some(Execution {
                assume,
                result: ExecutionResult {
                    regs: regs.clone(),
                    read_at: None,
                    write_at: None,
                    io_request: None,
                },
            }),
            // stop execution
            InsnType::Halt => None,
        }
    }
}

struct InstructionFetcher {
    start_addr: u32,
    instruction_buffer: [Option<Insn>; 8],
}

impl InstructionFetcher {
    pub fn new(start_addr: u32) -> Self {
        Self {
            start_addr,
            instruction_buffer: [None, None, None, None, None, None, None, None],
        }
    }

    pub fn get_current_insn(&mut self, pc: u32, mem: &mut Memory) -> Option<Insn> {
        let rv = self.get_insn_from_buffer(pc);
        if rv.is_some() {
            return rv;
        }

        let mut reader = MemoryReader::new(pc, mem);
        for insn in self.instruction_buffer.iter_mut() {
            if let Some(decoded) = Insn::decode(&mut reader) {
                insn.replace(decoded);
            } else {
                break;
            }
        }
        self.start_addr = pc;

        self.get_insn_from_buffer(pc)
    }

    fn get_insn_from_buffer(&mut self, pc: u32) -> Option<Insn> {
        if pc == self.start_addr {
            if let Some(insn) = self.instruction_buffer[0].take() {
                self.instruction_buffer.rotate_left(1);
                self.start_addr += insn.size as u32;

                Some(insn)
            } else {
                None
            }
        } else {
            None
        }
    }
}

const CACHE_ENTRY_SIZE: u32 = 16;

#[derive(Debug, Clone, Copy)]
enum Perm {
    RW,
    RX,
    None,
}

impl Perm {
    fn is_writeable(&self) -> bool {
        match self {
            Perm::RW => true,
            _ => false,
        }
    }

    fn is_readable(&self) -> bool {
        match self {
            Perm::RW | Perm::RX => true,
            _ => false,
        }
    }

    fn is_executable(&self) -> bool {
        match self {
            Perm::RX => true,
            _ => false,
        }
    }
}

#[derive(Debug)]
struct CacheEntry {
    addr: u32,
    memory: [u8; CACHE_ENTRY_SIZE as usize],
    size: u32,
    is_dirty: bool,
}

#[derive(Debug)]
struct Mapping {
    begin: u32,
    size: u32,
}

impl Mapping {
    fn path(&self) -> String {
        format!("map{:#08x}", self.begin)
    }
}

struct Memory {
    maps: Vec<Mapping>,
    cache: [Option<CacheEntry>; 4],
}

struct MemoryReader<'m> {
    memory: &'m mut Memory,
    addr: u32,
}

impl<'m> MemoryReader<'m> {
    pub fn new(addr: u32, memory: &'m mut Memory) -> Self {
        Self { memory, addr }
    }
}

impl<'m> Read for MemoryReader<'m> {
    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
        let max_size = buf.len();

        let mem = self.memory.fetch(self.addr, max_size as u32);
        if let Some(mem) = mem {
            buf.copy_from_slice(mem);
            self.addr += mem.len() as u32;
            Ok(mem.len())
        } else {
            Ok(0)
        }
    }
}

fn read_memory_from_disk(path: &str, addr: u32, mem: &mut [u8]) -> usize {
    let mut f = File::open(path).expect("could not open memory?");
    f.seek(SeekFrom::Start(addr as u64))
        .expect("could not seek address?");

    let nread = f.read(mem).expect("could not read memory?");

    nread
}

fn write_memory_to_disk(path: &str, addr: u32, mem: &[u8]) {
    let mut f = OpenOptions::new()
        .write(true)
        .open(path)
        .expect("could not open memory?");
    f.seek(SeekFrom::Start(addr as u64))
        .expect("could not seek address?");

    f.write_all(mem).expect("could not write memory?");
}

impl Memory {
    pub fn new() -> Self {
        let cache = [None, None, None, None];
        Self {
            maps: Vec::new(),
            cache,
        }
    }

    pub fn fetch(&mut self, addr: u32, size: u32) -> Option<&[u8]> {
        let size = size.min(16);

        if self.update_cache_for_fetch(addr, size) {
            return Some(self.first_cache_entry(addr, size));
        }

        self.pre_fetch(addr);

        if self.update_cache_for_fetch(addr, size) {
            Some(self.first_cache_entry(addr, size))
        } else {
            None
        }
    }

    pub fn fetch_mut(&mut self, addr: u32, size: u32) -> Option<&mut [u8]> {
        let size = size.min(16);

        if self.update_cache_for_fetch(addr, size) {
            return Some(self.first_cache_entry_mut(addr, size));
        }

        self.pre_fetch(addr);

        if self.update_cache_for_fetch(addr, size) {
            Some(self.first_cache_entry_mut(addr, size))
        } else {
            None
        }
    }

    pub fn invalidate_cache(&mut self) {
        for entry in self.cache.iter_mut() {
            *entry = None
        }
    }

    fn first_cache_entry(&self, addr: u32, size: u32) -> &[u8] {
        let entry = self.cache[0].as_ref().unwrap();

        let begin = (addr - entry.addr) as usize;

        &entry.memory[begin..begin + size as usize]
    }

    fn first_cache_entry_mut(&mut self, addr: u32, size: u32) -> &mut [u8] {
        let entry = self.cache[0].as_mut().unwrap();
        entry.is_dirty = true;

        let begin = (addr - entry.addr) as usize;

        &mut entry.memory[begin..begin + size as usize]
    }

    fn update_cache_for_fetch(&mut self, addr: u32, size: u32) -> bool {
        for (i, entry) in self.cache.iter().enumerate() {
            if let Some(entry) = entry {
                if entry.addr <= addr && entry.addr + entry.size >= addr + size {
                    let k = self.cache.len() - i;
                    self.cache.rotate_right(k);
                    return true;
                }
            }
        }

        false
    }

    fn map_for_addr(&self, addr: u32) -> Option<&Mapping> {
        for map in self.maps.iter() {
            if map.begin <= addr && map.begin + map.size >= addr {
                return Some(map);
            }
        }

        None
    }

    pub fn pre_fetch(&mut self, addr: u32) {
        if let Some(map) = self.map_for_addr(addr) {
            let path = map.path();

            let mut memory = [0; CACHE_ENTRY_SIZE as usize];
            let size = read_memory_from_disk(&path, addr - map.begin, &mut memory) as u32;

            let last = self.cache.last_mut().unwrap();

            let evicted = last.replace(CacheEntry {
                addr,
                memory,
                size,
                is_dirty: false,
            });

            if let Some(CacheEntry {
                addr,
                memory,
                size,
                is_dirty,
            }) = evicted
            {
                if is_dirty {
                    let map = self.map_for_addr(addr).unwrap();
                    let path = map.path();
                    write_memory_to_disk(&path, addr - map.begin, &memory[0..size as usize]);
                }
            }
        }
    }
}

#[derive(Debug, Clone)]
struct Registers {
    pc: u32,
    sp: u32,

    r0: u32,
    r1: u32,

    zero: bool,
}

#[derive(Debug, Clone)]
struct PartialRegisters {
    pc: u32,
    sp: Option<u32>,

    r0: Option<u32>,
    r1: Option<u32>,

    zero: Option<bool>,
}

impl PartialEq<Registers> for PartialRegisters {
    fn eq(&self, other: &Registers) -> bool {
        self.pc != 0
            && self.pc == other.pc
            && self.sp.map_or(true, |v| v == other.sp)
            && self.r0.map_or(true, |v| v == other.r0)
            && self.r1.map_or(true, |v| v == other.r1)
            && self.zero.map_or(true, |v| v == other.zero)
    }
}

impl PartialRegisters {
    pub fn new(pc: u32) -> Self {
        PartialRegisters {
            pc: pc,
            sp: None,
            r0: None,
            r1: None,
            zero: None,
        }
    }
}

#[derive(Debug, Clone)]
struct ExecutionResult {
    regs: Registers,
    read_at: Option<u32>,
    write_at: Option<u32>,
    io_request: Option<IoRequest>,
}

#[derive(Debug, Clone)]
struct Execution {
    assume: PartialRegisters,
    result: ExecutionResult,
}

#[derive(Debug)]
struct Verifier {
    permissions: BTreeMap<u32, Perm>,
}

#[derive(Debug, Copy, Clone)]
enum VerificationResult {
    Ok,
    IoRequest((IoRequest, u32)),
    Reset(bool),
    Fault,
}

#[derive(Debug, Clone)]
struct ExecutorReset {
    regs: Registers,
    reset_caches: bool,
}

impl Verifier {
    pub fn new() -> Self {
        Self {
            permissions: BTreeMap::new(),
        }
    }

    fn verify_execution(&self, regs: &Registers, execution: &Execution) -> VerificationResult {
        if &execution.assume == regs {
            let mut errors = false;

            if let Some(addr) = execution.result.write_at {
                if !self.perm_for_addr(addr).is_writeable() {
                    errors = true;
                }
            }

            if let Some(addr) = execution.result.read_at {
                if !self.perm_for_addr(addr).is_readable() {
                    errors = true;
                }
            }

            if !self.perm_for_addr(regs.pc).is_executable() {
                errors = true;
            }

            if errors {
                VerificationResult::Fault
            } else if let Some(req) = execution.result.io_request {
                VerificationResult::IoRequest((req, execution.result.regs.pc))
            } else {
                VerificationResult::Ok
            }
        } else {
            VerificationResult::Reset(execution.result.write_at.is_some())
        }
    }

    fn perm_for_addr(&self, addr: u32) -> Perm {
        if let Some(perm) = self
            .permissions
            .range((std::ops::Bound::Unbounded, std::ops::Bound::Included(addr)))
            .next_back()
        {
            *perm.1
        } else {
            Perm::None
        }
    }
}

fn mmap_unchecked(addr: u32, size: u32, perm: Perm, mem: &mut Memory, verifier: &mut Verifier) {
    let map = Mapping { begin: addr, size };

    let f = File::create(map.path()).expect("could not create memory?");
    f.set_len(size as u64)
        .expect("could not initialize memory?");

    mem.maps.push(map);
    verifier.permissions.insert(addr, perm);
}

fn mmap_unchecked_with_content(
    addr: u32,
    content: &[u8],
    perm: Perm,
    mem: &mut Memory,
    verifier: &mut Verifier,
) {
    let size = content.len() as u32;
    let map = Mapping { begin: addr, size };

    let mut f = File::create(map.path()).expect("could not create memory?");
    f.write(content).expect("could not initialize memory?");

    mem.maps.push(map);
    verifier.permissions.insert(addr, perm);
}

struct Args {
    code_buf: Vec<u8>,
}

fn parse_args() -> Args {
    let mut args = env::args().skip(1);

    let program = args.next().expect("Usage: ./vm <program>");

    let mut f = File::open(program).expect("could not open program");
    let mut program = Vec::new();
    f.read_to_end(&mut program).expect("could not read program");

    program.truncate(0x1000);

    Args { code_buf: program }
}

fn validator_force_reset(
    recv: &crossbeam_channel::Receiver<Option<Execution>>,
    registers: &Registers,
    reset: &Arc<Mutex<Option<ExecutorReset>>>,
    check_reset: &Arc<AtomicBool>,
    mut reset_caches: bool,
) {
    let mut reset = reset.lock().unwrap();
    check_reset.store(true, Ordering::Relaxed);

    while let Some(exec) = recv.try_recv().ok().flatten() {
        if exec.result.write_at.is_some() {
            reset_caches = true;
        }
    }

    *reset = Some(ExecutorReset {
        regs: registers.clone(),
        reset_caches,
    });
}

fn validator_handle_io(req: IoRequest, next_pc: u32, regs: &Registers) -> Registers {
    let mut regs = regs.clone();
    regs.pc = next_pc;

    match req {
        IoRequest::IoRead(n) => {
            assert!(n <= 4);

            let mut buf = [0; 4];
            stdin()
                .read_exact(&mut buf[..n as usize])
                .expect("could not read stdin");

            regs.r0 = as_u32_le(&buf[..n as usize]);
        }
        IoRequest::IoWrite(n) => {
            assert!(n <= 4);

            let mut buf = [0; 4];
            write_u32_to_buf(&mut buf[..n as usize], regs.r0, n);

            stdout()
                .write_all(&buf[..n as usize])
                .expect("could not write stdout");
            stdout().flush().expect("could not write stdout");
        }
    }

    regs
}

fn main() {
    let args = parse_args();

    let pc = 0x100000u32;
    let sp = 0x200000u32;
    let xx = 0x300000u32;
    let mm = 0x400000u32;

    let mut memory = Memory::new();
    let mut verifier = Verifier::new();

    mmap_unchecked_with_content(pc, &args.code_buf, Perm::RX, &mut memory, &mut verifier);
    mmap_unchecked(sp, 0x1000, Perm::RW, &mut memory, &mut verifier);
    mmap_unchecked(mm, 0x1000, Perm::RW, &mut memory, &mut verifier);

    let flag = env::var("CSCG_VM_FLAG").unwrap_or("CSCG{redacted}".to_string());
    mmap_unchecked_with_content(xx, flag.as_bytes(), Perm::None, &mut memory, &mut verifier);

    let do_run_validator = Arc::new(AtomicBool::new(true));
    let do_run_executor = do_run_validator.clone();
    let check_reset_validator = Arc::new(AtomicBool::new(false));
    let check_reset_executor = check_reset_validator.clone();

    let (send, recv) = crossbeam_channel::bounded::<Option<Execution>>(8);

    let mut registers = Registers {
        pc,
        sp,
        r0: 0,
        r1: 0,
        zero: true,
    };

    let initial = registers.clone();
    let reset_validator = Arc::new(Mutex::<Option<ExecutorReset>>::new(None));
    let reset_executor = reset_validator.clone();

    let executor = thread::spawn(move || {
        let mut instruction_fetcher = InstructionFetcher::new(pc);

        let mut regs = initial;

        loop {
            if !do_run_executor.load(Ordering::Relaxed) {
                break;
            }

            let insn = instruction_fetcher.get_current_insn(regs.pc, &mut memory);

            let result = if let Some(insn) = insn {
                insn.execute(&mut regs, &mut memory)
            } else {
                None
            };

            let is_write = result
                .as_ref()
                .map_or(false, |exec| exec.result.write_at.is_some());

            if check_reset_executor.load(Ordering::Relaxed) {
                let mut reset = reset_executor.lock().unwrap();
                if let Some(reset) = reset.take() {
                    if reset.reset_caches || is_write {
                        memory.invalidate_cache();
                    }
                    regs = reset.regs;

                    check_reset_executor.store(false, Ordering::Relaxed);
                    continue;
                }
            }

            if send.send(result).is_err() {
                break;
            }
        }
    });

    loop {
        let execution = recv
            .recv()
            .expect("could not fetch next instruction result");

        if let Some(execution) = execution {
            match verifier.verify_execution(&registers, &execution) {
                VerificationResult::Ok => {
                    registers = execution.result.regs;
                }
                VerificationResult::IoRequest((req, next_pc)) => {
                    registers = validator_handle_io(req, next_pc, &registers);
                }
                VerificationResult::Reset(reset_caches) => {
                    validator_force_reset(
                        &recv,
                        &registers,
                        &reset_validator,
                        &check_reset_validator,
                        reset_caches,
                    );
                }
                VerificationResult::Fault => {
                    println!("execution stopped: fault with invalid permissions");
                    do_run_validator.store(false, Ordering::Relaxed);
                    break;
                }
            }
        } else {
            do_run_validator.store(false, Ordering::Relaxed);
            break;
        }
    }

    executor.join().expect("executor did not run?");
}
