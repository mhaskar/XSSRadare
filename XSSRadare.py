#!/usr/bin/python


import sys
import urlparse
import urllib
import urllib2
import time
import os
import argparse
from termcolor import cprint
from banner import banner
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException


print banner()

arparser = argparse.ArgumentParser()

arparser.add_argument(
    "-u", "--url", required=False, help="URL to scan"
)

arparser.add_argument(
    "-v", "--view", required=False, help="view firefox (on/off)", default="on"
)

arparser.add_argument(
    '--stop', help='stop when you find a vulnerability',
    action='store_true'
)

arparser.add_argument(
    '--negative', help='show negative attempts',
    action='store_true'
)

arparser.add_argument(
    "-fi", "--file", required=False, help="name of the urls file to scan"
)

arparser.add_argument(
    "-c", "--cookies", required=False, help="cookies you want to use NAME:VALUE:PATH"
)

parser = vars(arparser.parse_args())



# global vars to control the options
url = parser["url"]
user_view = parser["view"]
stop = parser["stop"]
negative = parser["negative"]
urls_file = parser["file"]
cookies_option = parser["cookies"]
global scan_type


if urls_file is None and url is None:
    cprint("[!] You must use --url or --file\n", "red")
    sys.exit()

if urls_file is not None and url is not None:
    cprint("[!] Please choose one option --file or --url", "red")
    sys.exit()

if urls_file is not None:
    scan_type = "files"

if url is not None:
    scan_type = "url"


def check_url(url):
    if url.split(":")[0] == "http" or url.split(":")[0] == "https":
        return True
    else:
        return False


def shutdown_display():
    display = Display(visible=0, size=(800, 600))
    display.start()

if user_view == "off":
    shutdown_display()


def get_payloads():
    payload_file = open("payloads.txt", "r")
    payloads = payload_file.read().splitlines()
    return payloads


def decode_url(url):
    raw_url = urlparse.urlparse(url)
    query_string = raw_url.query
    params = dict(urlparse.parse_qsl(query_string))
    return params


def get_url(url):
    if check_url(url):
        pure_url = url.split("?")[0]
        return pure_url
    else:
        if scan_type == "url":
            cprint("[!] Please Enter a valid URL", "red")
            sys.exit(0)
        else:
            cprint(
                "[!] One of the urls is not valid , move to the next one ..", "red"
            )
            pass


def encode_url(url, params):
    params_encoded = urllib.urlencode(params)
    full_url = url + "?" + params_encoded
    return full_url


def print_positive_scan(url, params):
    unqouted_params = urllib2.unquote(params).decode('utf8')
    message = "[+] XSS Found on %s with params %s" % (url, unqouted_params)
    cprint(message, "green")


def print_negative_scan(url_to_scan):
    unqouted_url = urllib2.unquote(url_to_scan).decode('utf8')
    message = "[-]No XSS %s" % unqouted_url
    cprint(message, "red")


def print_exit():
    message = "[+] Stopping the scan after first result as required .."
    cprint(message, "yellow")


def print_negative(text):
    message = "[!] %s" % text
    cprint(message, "red")

def print_scan_finish(xssnum):
    message = "[+] Scan finished , number of found XSS : %i " % xssnum
    cprint(message, "blue")
def fuzz_get_urls(url):
    if cookies_option is not None:
        cookies = cookies_option.split(":")
        cookies_name = cookies[0]
        cookies_value= cookies[1]
        cookies_path = cookies[2]
        cookie_dict = {'name': cookies_name, 'value': cookies_value, 'path': cookies_path}
    number_of_found_xss = 0
    scan_url = get_url(url)
    params = decode_url(url)
    for payload in get_payloads():

        for param in params.keys():
            previous_value = params[param]
            params[param] = payload
            url_to_send = encode_url(scan_url, params)
            raw_params = urllib.urlencode(params)
            browser = webdriver.Firefox()
            if cookies_option is not None:
                browser.get(url)
                browser.add_cookie(cookie_dict)
            browser.get(url_to_send)
            time.sleep(1)

            try:
                if browser.switch_to.alert.text is not None:
                    if stop is True:
                        number_of_found_xss = number_of_found_xss + 1
                        print_positive_scan(scan_url, raw_params)
                        print_exit()
                        browser.quit()
                        sys.exit(0)
                    else:
                        number_of_found_xss = number_of_found_xss + 1
                        print_positive_scan(scan_url, raw_params)
            except NoAlertPresentException:
                if negative is True:
                    print_negative_scan(url_to_send)

            browser.quit()
            params[param] = previous_value
    print_scan_finish(number_of_found_xss)

def fuzz_urls_file(fi):
    if os.path.isfile(fi):
        urls_file_raw = open(fi, "r")
        urls = urls_file_raw.read().splitlines()
        for url in urls:
            fuzz_get_urls(url)

    else:
        print_negative("URLs file is not exist")

if scan_type == "url":
    fuzz_get_urls(url)

if scan_type == "files":
    fuzz_urls_file(urls_file)
