import httplib, urllib
conn = httplib.HTTPConnection("rant4fun.tumblr.com")
headers =   {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
params = urllib.urlencode( { "email": "stephan.wallentin@gmail.com",
							"password": "surface"} )
conn.request("HEAD", "/api/read/json", params, headers)
res = conn.getresponse()
print res.status, res.reason
print res.getheaders()
data = res.read()
conn.close()
print len(data)
