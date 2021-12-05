We have a pcap file and open it with wireshark. Then we follow the TCP stream and look for HTTP. The last http request seems interesting

```http
POST /bg.php HTTP/1.1
Host: christmaswishlist:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 267
Origin: http://christmaswishlist:8080
Connection: close
Referer: http://christmaswishlist:8080/bg.php
Upgrade-Insecure-Requests: 1

cmd=rm++%2Fvar%2Fwww%2Fhtml%2Fsites%2Fdefault%2Ffiles%2F.ht.sqlite+%26%26+echo+SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59+%3E+%2Fdev%2Fnull+2%3E%261+%26%26+ls+-al++%2Fvar%2Fwww%2Fhtml%2Fsites%2Fdefault%2Ffiles
```

The interesting part is 

```
rm  /var/www/html/sites/default/files/.ht.sqlite && echo SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59 > /dev/null 2>&1 && ls -al  /var/www/html/sites/default/files
```

It seems to be in base64, so we do the following to get the flag

```
echo SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59 | base64 -d
```