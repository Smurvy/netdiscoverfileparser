import sys
import re

txtFile = sys.argv[1]
ipList = []

with open(txtFile) as f:
    for line in f:
        ipAddr = re.search("^\s(\d{2,3}.\d{2,3}.\d{1,3}.\d{1,3})",line)
        
        if ipAddr is not None:
            ipList.append(ipAddr.groups()[0])

    f.close()

ipList = list(set(ipList))



with open("output.txt", "w") as f:
    for ip in ipList:
        f.write(f"{ip}\n")
    f.close()
            
