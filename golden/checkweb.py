import urllib.request
try:
    status = urllib.request.urlopen('http://portal.goldennet.com.tw/UOF/').code
    print(status)
except urllib.error.HTTPError as err:
    print(err.code)