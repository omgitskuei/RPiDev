import gpiozero as gp
import decimal

diskU = 0;

# Note: Returns decimal
def roundDownToTwoDecimals(d):
    return decimal.Decimal(d).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)

diskU = gp.DiskUsage().usage

print(diskU)
print(type(diskU))

diskU = roundDownToTwoDecimals(diskU)
print(diskU)
print(type(diskU))

print('Current disk usage: {}%'.format(diskU))


import psutil

bytes_avail = psutil.disk_usage('/').free
gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
print('{}GB free'.format(roundDownToTwoDecimals(gigabytes_avail)))


