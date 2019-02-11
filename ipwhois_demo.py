
#pip install ipwhois

from ipwhois import IPWhois
obj = IPWhois('74.125.225.229')
res=obj.lookup_whois()
print ("country:", res["nets"][0]['country'])
from pprint import pprint
pprint(res)
