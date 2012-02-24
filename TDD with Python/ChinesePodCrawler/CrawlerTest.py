import sys
import os
import unittest
import urllib2
import urllib

url = "https://chinesepod.com/accounts/signin"

o = urllib2.build_opener( urllib2.HTTPCookieProcessor())
urllib2.install_opener(o)
params = {'email':'astridmariablomberg@gmail.com','password':'anniba00'}
params = urllib.urlencode(params)
f = o.open(url, params)

print f.read()