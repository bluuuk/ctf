Postgres RESTFUL-api `application/vnd.pgrst.object+json`


Change `GET /rest/v1/users?select=*&username=eq.admin&password=eq.test HTTP/2` to  `GET /rest/v1/users?select=*&username=eq.admin&password=neq.test HTTP/2`

with neq beeing not equals

![alt text](image.png)