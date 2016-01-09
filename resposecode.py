import urllib
a=urllib.urlopen('http://ftp.redhat.com/pub/redhat/linux/eal/EAL4_RHEL5/IBM/README')
print a.getcode()
