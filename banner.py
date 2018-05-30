#!/usr/bin/python

import time


def banner():
    return """
 __  _____ ___ ___         _              
 \ \/ / __/ __| _ \__ _ __| |__ _ _ _ ___
  >  <\__ \__ \   / _` / _` / _` | '_/ -_)
 /_/\_\___/___/_|_\__,_\__,_\__,_|_| \___|

[+] XSSRader Start working at : {0}
""".format(time.ctime())
