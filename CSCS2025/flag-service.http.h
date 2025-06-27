@host = 127.0.0.1:8000

GET / HTTP/1.1
Host: {{host}}

###

POST /api/register HTTP/1.1
Host: {{host}}
content-type: application/json

{
    "name": "name",
    "password": "password"
}

###

POST /api/request_ticket HTTP/1.1
Host: {{host}} 
content-type: application/json

{
    "user": "Administrator",
    "service": "Flag Service"
}

### 


POST /api/authenticate HTTP/1.1
Host: {{host}} 
content-type: application/json

{
    "service": "Flag Service",
    "ticket": "99e7e39d08ec68b07a069890047d95720167a663dcf914e7f7f8f3bcdcf5c72dd819c4954b8eb2264317818ffd80a62695d8574ed2c13d0e7c4be7f1b997507c1ca9f45e743c0fc25c588734e0e2d20626164595348cfd4fb4eff54a87fb935046053b0cbaaf59bf"
}