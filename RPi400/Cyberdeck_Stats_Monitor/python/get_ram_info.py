import os

# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

ramInfo = getRAMinfo()
# print(type(ramInfo)) # ramInfo is a list
# print(ramInfo)
print(type(ramInfo[0])) # str

ramTot = int(ramInfo[0])/1000
ramUsd = int(ramInfo[1])/1000
ramFre = int(ramInfo[2])/1000

print("Total RAM = {}MB, Used RAM = {}MB, Free RAM = {}MB".format(ramTot, ramUsd, ramFre))
print(str(ramUsd/ramTot*100) + "% Used")
