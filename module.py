def findworkingproxies(config):
    if config.find('#') > 1:
        workingproxies = config[:config.find('#') - 1].split('\n')
    else:
        workingproxies = []
    return workingproxies


def findunworkingproxies(config):
    if len(config[config.find('#'):]) > 1:
        unworkingproxies = config[config.find('#') + 2:].split('\n')
    else:
        unworkingproxies = []
    return unworkingproxies


def worktounwork(config,ip,reverse=0):
    if reverse == 0:
        config += '\n' + ip
        if config.find(ip) > 1:
            if len(config[:config.find(ip)]) <= 1:
                config = config.replace('\n' + ip + '\n', '', 1)
            else:
                config = config.replace('\n' + ip, '', 1)
        else:
            config = config.replace(ip + '\n', '', 1)
    else:
        config = config.replace('\n' + ip,'')
        config = ip + '\n' + config
    return config