from gpiozero import CPUTemperature

def getCPUTemp_gpio():
    return CPUTemperature().temperature


import os

def getCPUTemp_os():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


# main...
print(type(getCPUTemp_gpio()))
print(getCPUTemp_gpio())
print(type(getCPUTemp_os()))
print(getCPUTemp_os())