#!/usr/bin/env python


import pexpect

def getwhoisinfo(site='shafiulla.info'):
    child = pexpect.spawn('whois '+site)
    child.expect(pexpect.EOF)
    print(child.before)

def dnsinfo(site='shafiulla.info'):
    '''
       host -t cname files.cyberciti.biz
       host -t mx cyberciti.biz
       host -t mx shafiulla.info
       host -t a shafiulla.info
       host -t cname shafiulla.info
    :return:
    '''

getwhoisinfo()
