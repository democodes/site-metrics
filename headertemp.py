import pycurl
import sys

list  = ['http://google.com', 'http://youtube.com', 'http://gmail.com',"http://facebook.com"]
d = {}
for url in list:

	class Storage:
    		def __init__(self):
        		self.contents = ''
        		self.line = 0

    		def store(self, buf):
        		self.line = self.line + 1
        		self.contents = "%s%i: %s" % (self.contents, self.line, buf)

    		def __str__(self):
        		return self.contents
	l = []
	retrieved_body = Storage()
	#print retrieved_body
	retrieved_headers = Storage()
	c = pycurl.Curl()
	#help(c)
#	url = 'http://www.youtube.com/'
	
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, retrieved_body.store)
	c.setopt(c.HEADERFUNCTION, retrieved_headers.store)
	c.perform()
	c.close()
	k =  retrieved_headers	
	#print k
	#print k.__dict__.keys()
	#print k.__dict__[]
	#print k['1','Server']
	#print type(k)
	#print retrieved_body
	import pickle
	pickle.dump( retrieved_headers, open( "save.p", "wb" ) )
	k = []
	siteproperties = []
	count = 0
	with open("save.p", "r") as ins:
		for i in ins:
			if 'Server: ' in i:
				count = 1
#				print i
				k = i.split('Server:')
#				print k[1]
				r = k[1].split(':')
#				print r[0]
				webserver = 'webserver:' +  r[0].strip('123456789 \\n\\r')
#				print webserver
				siteproperties.append(webserver)
#	print count
		if count==0:
			siteproperties.append("Webserver details is not published")
		
			 
			
#			print k[1]
	#print siteproperties
	import urllib
	import json
	#print url
	a=urllib.urlopen(url)
	#print a.getcode()
	responsecode = 'Response code:' + str(a.getcode())
	print responsecode

	siteproperties.append(responsecode)
	print siteproperties
#	for i in siteproperties:
#		print i
#	d = {}
	d[url]=siteproperties
#print d
from pprint import pprint
pprint(json.dumps(d))
with open('result.json', 'w') as fp:
	json.dump(d, fp)
