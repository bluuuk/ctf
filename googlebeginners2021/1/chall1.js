
var k = [
    52037,
    52077,
    52077,
    52066,
    52046,
    52063,
    52081,
    52081,
    52085,
    52077,
    52080,
    52066,
]

//const p = Array.from(password).map(a => 0xCafe + a.charCodeAt(0));
const c = Array.from(k).map(a => String.fromCharCode(a - 0xCafe)).join("")
console.log(c) // GoodPassword
