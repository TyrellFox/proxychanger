from module import *

def findvalue(str,config):
    value = config[config.find(str)-1:(config[config.find(str):].find(';')+config.find(str)-1)]
    value = value[value.find(',')+2:]
    value = value.replace('"','')
    return value


prefsin = open("/home/fckthscty/.mozilla/firefox/bst6uso9.default/prefs.js", 'r').read()
prefsout= open("/home/fckthscty/.mozilla/firefox/bst6uso9.default/prefs.js", 'w')
proxiesin = open("proxies.dat",'r').read()
proxiesout = open("proxies.dat",'w')

proxy_socks_ip = findvalue("network.proxy.socks",prefsin)
proxy_socks_port = findvalue("network.proxy.socks_port",prefsin)

workingproxies = findworkingproxies(proxiesin)
nextproxy = workingproxies[0]
next_proxy_socks_ip = nextproxy[:nextproxy.find(':')]
next_proxy_socks_port = nextproxy[nextproxy.find(':')+1:]

if len(workingproxies) > 1:
    proxiesin = proxiesin.replace(nextproxy + '\n','')
    proxiesin = proxiesin[:proxiesin.find('#')] + nextproxy + '\n' + proxiesin[proxiesin.find('#'):]

proxiesout.write(proxiesin)
proxiesout.close()

prefsin = prefsin.replace(proxy_socks_ip,next_proxy_socks_ip)
prefsin = prefsin.replace(proxy_socks_port,next_proxy_socks_port)

prefsout.write(prefsin)
prefsout.close()
