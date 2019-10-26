# XSSRadare (beta version)


### Cross Site Scripting (XSS) scanner based on selenium webdriver

using XSSRadare you can scan a single URL or mulitple URLs from XSS by using selenuim web driver as a fuzzing interface , XSSRadare will help you to identify any XSS vulnerability in your web application.

XSSRadare will use some hardcoded payloads to test for XSS , for now we prefer to write payload that conatins ```alert``` javascript function because we already implemented the fuzzer to test for any alert triggered in the scaned page.

### Requirements :

You can install all the dependencies for XSSRadare using the following commands :

```askar@hackbook:~# sudo ./system_requirments.sh ```

And make sure to add this line to your ```.bashrc``` file manually :

``` export PATH=$PATH:/opt/geckodriver ```

This line will make sure to link the geckodriver path to your current ```PATH``` so the XSSRadare can recognize it.

##### Note : sometimes you need to check your firefox compatibility with geckodriver in order to run the script correctly (currently we are using the latest one "geckodriver-v0.26.0 x64" version)

### Usage :

After installing all the dependencies , you can run this command to start XSSRadare :

```
askar@hackbook:~# python3 XSSRadare.py  -h

 \ \/ / __/ __| _ \__ _ __| |___ _ _
  >  <\__ \__ \   / _` / _` / -_) '_|
 /_/\_\___/___/_|_\__,_\__,_\___|_|

[+] XSSRader Start working at : Tue May 29 01:39:59 2018

usage: XSSRadare.py [-h] [-u URL] [-v VIEW] [--stop] [--negative] [-fi FILE]

optional arguments:
-h, --help            show this help message and exit
-u URL, --url URL     URL to scan
-v VIEW, --view VIEW  view firefox (on/off)
--stop                stop when you find a vulnerability
--negative            show negative attempts
-fi FILE, --file FILE
                      name of the urls file to scan
-c COOKIES, --cookies COOKIES
                      cookies you want to use NAME:VALUE:PATH
-f, --full            use 666 payloads
-t TIMEOUT, --timeout TIMEOUT
                      set timeout between request and alert() check, in
                      seconds


```

This command can be explained as following :

- -h : to show this help banner.
- --url : the URL you want to scan.
- --view : to choose if you want to show the firefox browser during the fuzzing , you can control it by use (on / off) flags.
- --stop : XSSRadare will stop fuzzing once it found any XSS.
- --negative : to show the negative scan results (something like verbose).
- --file : file name that contains all URLs that you want to scan.

- --cookies : if you have any cookies you can add them using this option
-  -f, --full            use 666 payloads
-  -t TIMEOUT, --timeout TIMEOUT
                        set timeout between request and alert() check, in
                        seconds



You can start a simple XSS scan for a url using the following command :

```
askar@hackbook:~# python3 XSSRadare.py --url "http://localhost/xss.php?name=askar&age=21"
 __  _____ ___ ___         _
 \ \/ / __/ __| _ \__ _ __| |___ _ _
  >  <\__ \__ \   / _` / _` / -_) '_|
 /_/\_\___/___/_|_\__,_\__,_\___|_|

[+] XSSRader Start working at : Tue May 29 01:49:22 2018

[+] XSS Found on http://localhost/xss.php with params age=21&name=<script>alert("XSSED:D:")</script>
[+] Scan finished , number of found XSS : 1

askar@hackbook:~#
```

### Screenshots :
![Test Kali Image](ScanKaliWithView.png)

![Test Ubuntu Image without view](ScanWithoutView.png)
