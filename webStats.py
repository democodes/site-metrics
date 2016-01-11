#!/usr/bin/env python

import dns.name
import dns.resolver

n = dns.name.from_text('www.dnspython.org')
o = dns.name.from_text('dnspython.org')
print(n.is_subdomain(o))        # True


answers = dns.resolver.query('nominum.com', 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
