import re

def isExistKey(key, dict):
    if key in dict.keys():
        return True
    else:
        return False

def groupIps(file):
    groupedIps = {}
    with open(file, 'r') as f:
        ips = [ip for ip in re.findall(r"\d+\.\d+\.\d+\.\d+", f.read())]
        for i in range(len(ips)):
            common = '.'.join(ips[i].split('.')[0:-1])
            if not isExistKey(common, groupedIps):
                groupedIps[common] = list(set(x for x in ips if common in x))
    return groupedIps

def writeIps(dict):
    for common in dict:
        print("Common = ",common)
        for ip in dict[common]:
            print(" ",ip)

if __name__ == '__main__':
    ips = groupIps('access.log')
    writeIps(ips)
