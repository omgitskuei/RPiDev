import os

# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMInfo_V1():
    p = os.popen('free')
    print(type(p)) # <class 'os._wrap_close'>
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            print(line[0:-1]) # NOTE: last char is CARRIAGE-RETURN/ENTER, eg. Mem:         3931052      267968     3048656      105252      614428     3426800
            return(line.split()[1:4])

ramInfo = getRAMInfo_V1()
# print(type(ramInfo)) # ramInfo is a list
# print(ramInfo)
print(type(ramInfo[0])) # str

ramTot = int(ramInfo[0])/1000
ramUsd = int(ramInfo[1])/1000
ramFre = int(ramInfo[2])/1000

print("Total RAM = {}MB, Used RAM = {}MB, Free RAM = {}MB".format(ramTot, ramUsd, ramFre))
print(str(ramUsd/ramTot*100) + "% Used")


# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM 
def getRAMInfo_V2():
    p = os.popen('free')
    print(type(p)) # <class 'os._wrap_close'>
    p.readline() # first line is unused
    return p.readline().split()[1:4]

ramInfo = getRAMInfo_V2()
# print(type(ramInfo)) # ramInfo is a list
# print(ramInfo)
print(type(ramInfo[0])) # str

ramTot = int(ramInfo[0])/1000
ramUsd = int(ramInfo[1])/1000
ramFre = int(ramInfo[2])/1000

print("Total RAM = {}MB, Used RAM = {}MB, Free RAM = {}MB".format(ramTot, ramUsd, ramFre))
print(str(ramUsd/ramTot*100) + "% Used")


import psutil

psutil_ramInfo = psutil.virtual_memory()
print(type(psutil_ramInfo)) # <class 'psutil._pslinux.svmem'>
print(psutil_ramInfo)
# svmem(
# total=4025397248, available=3499692032,
# percent=13.1, used=274006016, 
# free=3112206336, active=229851136,
# inactive=446173184, buffers=41828352,
# cached=597356544, shared=117514240,
# slab=46387200
# )
print(psutil_ramInfo[3]) # 272936960

def getRAMInfo_V3():
    ramInfo_raw = psutil.virtual_memory()
    return {
        "total" : ramInfo_raw[0],
        "available" : ramInfo_raw[1],
        "percent" : ramInfo_raw[2],
        "used" : ramInfo_raw[3],
        "free" : ramInfo_raw[4],
        "active" : ramInfo_raw[5],
        "inactive" : ramInfo_raw[6],
        "buffers" : ramInfo_raw[7],
        "cached" : ramInfo_raw[8],
        "shared" : ramInfo_raw[9],
        "slab" : ramInfo_raw[10],
        }

ram_dict = getRAMInfo_V3()
print(ram_dict)
print(type(ram_dict)) # <class 'dict'>
print(ram_dict['percent']) # 13.1
print(type(ram_dict['percent'])) # <class 'float'>
print(ram_dict['total'] / 1024 / 1024 / 1024) # 3.748943328857422 (GB)