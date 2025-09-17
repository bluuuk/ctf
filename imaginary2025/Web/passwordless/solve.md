> Didn't have time to implement the email sending feature but that's ok, the site is 100% secure if nobody knows their password to sign in!

 <span id="flag"><%- process.env.FLAG %></span>



https://www.npmjs.com/package/bcrypt
```
Security Issues And Concerns

    Per bcrypt implementation, only the first 72 bytes of a string are used. Any extra bytes are ignored when matching passwords. Note that this is not the first 72 characters. It is possible for a string to contain less than 72 characters, while taking up more than 72 bytes (e.g. a UTF-8 encoded string containing emojis). If a string is provided, it will be encoded using UTF-8.
```


```js
app.post('/user', limiter, (req, res, next) => {
    if (!req.body) return res.redirect('/login')

    const nEmail = normalizeEmail(req.body.email)

    if (nEmail.length > 64) {
        req.session.error = 'Your email address is too long'
        return res.redirect('/login')
    }
    
    // !!! so if req.body.email.length == 72 => RANDOM VALUE removed! 
    // Fix: WORK via nEmail and not req.body.email 
    const initialPassword = req.body.email + crypto.randomBytes(16).toString('hex')
    bcrypt.hash(initialPassword, 10, function (err, hash) {
        if (err) return next(err)

        const query = "INSERT INTO users VALUES (?, ?)"
        db.run(query, [nEmail, hash], (err) => {
            if (err) {
                if (err.code === 'SQLITE_CONSTRAINT') {
                    req.session.error = 'This email address is already registered'
                    return res.redirect('/login')
                }
                return next(err)
            }

            // TODO: Send email with initial password

            req.session.message = 'An email has been sent with a temporary password for you to log in'
            res.redirect('/login')
        })
    })
})
```

Taken from <https://www.npmjs.com/package/normalize-email>
```js
var normalizeEmail = require('normalize-email')
 
normalizeEmail('johnotander@GMAIL.com')         // => 'johnotander@gmail.com'
normalizeEmail('john.o.t.a.n.d.e.r@gmail.com')  // => 'johnotander@gmail.com'
normalizeEmail('johnotander@googlemail.com')    // => 'johnotander@gmail.com'
normalizeEmail('johnotander+foobar@gmail.com')  // => 'johnotander@gmail.com'
normalizeEmail('JOHN.OTANDER+OHAI@gmail.com')   // => 'johnotander@gmail.com'
```


So we need an normalized email with less than 64 chars

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@gmail.com

Know we prep it up to more chars via dots, we need $72 - 64 = 8$ dots

A.A.A.A.A.A.A.A.A.A.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@gmail.com

However, this did not worked so I added some good old `console.log` statements: 

```
A.A.A.A.A.A.A.A.A.A.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@gmail.com <- Our password
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com <- Our username
$2b$10$FmHy0KOHrVGw5JuVNSPMlemhplzsx83/XQi.5USilPpWNXNVD4He2
```

Ahhh I forgot to actually use the normalized user name ....

ictf{8ee2ebc4085927c0dc85f07303354a05}