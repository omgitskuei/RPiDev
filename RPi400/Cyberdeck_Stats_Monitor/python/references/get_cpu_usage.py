import psutil
import os
from gpiozero import LoadAverage

def get_CPU():
    return psutil.cpu_percent()

print(get_CPU())


def getCPUuse():
    return str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline())

print(getCPUuse())


la = LoadAverage(min_load_average=0, max_load_average=2)

print(type(la)) # <class 'gpiozero.internal_devices.LoadAverage'>
print(la)