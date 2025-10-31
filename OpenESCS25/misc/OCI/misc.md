❯ ffuf -w /usr/share/wordlists/fuff/common.txt -u "https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/FUZZ"

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/fuff/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

docs                    [Status: 200, Size: 955, Words: 152, Lines: 31, Duration: 136ms]
v2                      [Status: 307, Size: 0, Words: 1, Lines: 1, Duration: 141ms]
:: Progress: [4686/4686] :: Job [1/1] :: 280 req/sec :: Duration: [0:00:17] :: Errors: 0 ::

```sh
❯ curl -s -X 'GET' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/tags/list?n=100' \
  -H 'accept: application/json' | jq '.'
{
  "name": "nginx",
  "tags": [
    "alpine",
    "secret"
  ]
}
```

```sh
❯ curl -i -X 'HEAD' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/manifests/alpine' \
  -H 'accept: application/json'
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the way you want. Consider using -I/--head instead.
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/vnd.oci.image.manifest.v1+json
Date: Tue, 30 Sep 2025 03:11:12 GMT
Docker-Content-Digest: sha256:3d70e5ff6ceeaaf42ef4249b02b8786f670dd5c4fd53753a1b1ab43857fbf10f
Server: uvicorn
```

```sh
❯ curl -i -X 'HEAD' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/manifests/secret' \
  -H 'accept: application/json'
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the way you want. Consider using -I/--head instead.
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/vnd.oci.image.manifest.v1+json
Date: Tue, 30 Sep 2025 03:11:32 GMT
Docker-Content-Digest: sha256:7fce5ff81fa995e5ae1284fe85f1fec4fc4142b82af92c61b92ce5d0c376a733
Server: uvicorn
```

❯ diff <(jq --sort-keys . secret.json) <(jq --sort-keys . alpine.json) > diff.txt

The last three layers of `secret.json` are different

```
<       "digest": "sha256:b153e3b4cda6f6cf6530d363993424af6ea2de996a8a33a90403185a8a9d114e",
<       "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
<       "size": 234
<     },
<     {
<       "digest": "sha256:0899dc162465d95f179bef3d6e3096618c503fc8b634cc688560c583c3694b69",
<       "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
<       "size": 238
<     },
<     {
<       "digest": "sha256:ed14ee4edc82783d49e5dfee29bcd8649dc701051bcca1fb1dd90f40d0da9038",
<       "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
<       "size": 250
```

However, downloading them was a smoke gun:
❯ curl -o "1.tar.gz" -X 'GET' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/blobs/sha256%3Ab153e3b4cda6f6cf6530d363993424af6ea2de996a8a33a90403185a8a9d114e' \
  -H 'accept: application/json'
❯ curl -o "2.tar.gz" -X 'GET' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/blobs/sha256%0899dc162465d95f179bef3d6e3096618c503fc8b634cc688560c583c3694b69' \
  -H 'accept: application/json'

  -H 'accept: application/json'
❯ curl -o "3.tar.gz" -X 'GET' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/blobs/sha256%ed14ee4edc82783d49e5dfee29bcd8649dc701051bcca1fb1dd90f40d0da9038' \
  -H 'accept: application/json'

They had no secrets, see 1/2/3

However, I also observed the `x-injected-secret` which looks like base64

 content-length: 250  content-type: application/octet-stream  date: Tue,30 Sep 2025 03:23:33 GMT  docker-content-digest: sha256:ed14ee4edc82783d49e5dfee29bcd8649dc701051bcca1fb1dd90f40d0da9038  server: uvicorn  x-injected-secret: T3BlbkVDU0N7YzNydDFmMWVkLTBDMV9kM3ZlbDBwZXJfMjAyNV83ZDVjMmYyN2JiZWN9

 ❯ curl -o "secret.config.json" -X 'GET' \
  'https://217e21a0-6028-41ba-ba7f-def877a221c6.openec.sc:1337/v2/nginx/blobs/sha256%3A0e228305fbf306ac95206e8bdb3daf56e2917fbb2ad006699b2a4af9ce7cca2d' \
  -H 'accept: application/json'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11669  100 11669    0     0  14366      0 --:--:-- --:--:-- --:--:-- 14353

Base64 decoding yield `OpenECSC{c3rt1f1ed-0C1_d3vel0per_2025_7d5c2f27bbec}`

# Other things I tried

- Comparing the manifests
- Asking myself why the have a localhost version of alpine
- comparing that for ages ....
  - Compare that one with the remote ....   