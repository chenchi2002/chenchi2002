from dns import reversename, resolver
ip = '13.229.188.59' #github.com 的ip
domain_address = reversename.from_address(ip)
print(domain_address)
qtype = 'PTR'
domain_name = str(resolver.query(domain_address, qtype)[0])
print(domain_name)
