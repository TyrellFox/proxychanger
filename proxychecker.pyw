import requests
from module import *

proxiesouttxt = open("proxies.dat",'r').read()
workingproxies = findworkingproxies(proxiesouttxt)
unworkingproxies = findunworkingproxies(proxiesouttxt)

for ip in workingproxies:
    proxies = {
        'http' : 'socks5://' + ip,
        'https' : 'socks5://' + ip,
    }
    try:
        request = requests.get('http://www.google.com',proxies = proxies)
        if request.status_code!=200:
            proxiesouttxt = worktounwork(proxiesouttxt,ip)
        else:
            continue
    except:
        proxiesouttxt = worktounwork(proxiesouttxt,ip)

for ip in unworkingproxies:
    proxies = {
        'http' : 'socks5://' + ip,
        'https' : 'socks5://' + ip,
    }
    try:
        request = requests.get('http://www.google.com',proxies = proxies)
        if request.status_code!=200:
            continue
        else:
            proxiesouttxt = worktounwork(proxiesouttxt,ip,reverse=1)
    except:
        continue

proxieswrite = open("proxies.dat",'w')
proxieswrite.write(proxiesouttxt)
proxieswrite.close()