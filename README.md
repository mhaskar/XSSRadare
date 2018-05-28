# XSSRadare (beta version)


### Cross Site Scripting (XSS) scanner based on selenium webdriver

using XSSRadare you can scan a single URL or mulitple URLs from XSS by using selenuim web driver as a fuzzing interface , XSSRadare will help you to identify any XSS vulnerability in your web application.



### Requirements

You can install all the dependencies for XSSRadare using the following commands : 

```askar@hackbook : sudo ./system_requirments.sh ```

And make sure to add this line to your ```.bashrc``` file manually :

``` export PATH=$PATH:/opt/geckodriver ```

This line will make sure to link the geckodriver path to your current ```PATH``` so the XSSRadare can recognize it.

After installing all the dependencies , you can run this command to start XSSRadare :

``` 
askar@hackbook : python XSSRadare.py  -h

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


```


You can start a simple XSS scan for a url using the following command : 

```
askar@hackbook : python XSSRadare.py --url "http://localhost/xss.php?name=askar&age=21"
 __  _____ ___ ___         _
 \ \/ / __/ __| _ \__ _ __| |___ _ _
  >  <\__ \__ \   / _` / _` / -_) '_|
 /_/\_\___/___/_|_\__,_\__,_\___|_|

[+] XSSRader Start working at : Tue May 29 01:49:22 2018

[+] XSS Found on http://localhost/xss.php with params age=21&name=<script>alert("XSSED:D:")</script>
[+] Scan finished , number of found XSS : 1 

askar@hackbook : 


```
