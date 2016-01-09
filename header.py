import pycurl
import sys

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
c.setopt(c.URL, 'http://ftp.redhat.com/pub/redhat/linux/eal/EAL4_RHEL5/IBM/README')
c.setopt(c.WRITEFUNCTION, retrieved_body.store)
c.setopt(c.HEADERFUNCTION, retrieved_headers.store)
c.perform()
c.close()
print retrieved_headers
#print retrieved_body
