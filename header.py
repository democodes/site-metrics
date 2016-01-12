
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
	retrieved_headers = Storage()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, retrieved_body.store)
	c.setopt(c.HEADERFUNCTION, retrieved_headers.store)
	c.perform()
	c.close()
	k = str(retrieved_headers)
	import pickle
	import codecs
	pickle.dump( retrieved_headers, open( "save.p", "wb" ) )
	siteproperties = []
	count = 0
	import re
	if 'Server:' in k:
		count = 1
		string = k.split('Server:')
		r = string[1].split(':')
		test = r[0]
		final =  re.sub('[^a-z]', ' ', test)
		finallast = final.split(' r')
		cleaning =  finallast[0].strip('  ')
		siteproperties.append(cleaning)
	if count==0:
		siteproperties.append("Webserver details is not published")
	import pycurl
	try:
    	    from io import BytesIO
	except ImportError:
    	    from StringIO import StringIO as BytesIO

	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()

	print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
	responsecode = c.getinfo(c.RESPONSE_CODE)
	c.close()
	siteproperties.append(responsecode)
	d[url]=siteproperties

import json
from pprint import pprint
pprint(json.dumps(d))
with open('result.json', 'w') as fp:
	json.dump(d, fp)
