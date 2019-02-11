#pip install whois
#https://pypi.org/project/whois/
# this does not work on windows or ubuntu. weird.

import whois
domain = whois.query('google.com')
print(domain)
