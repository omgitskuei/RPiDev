import gpiozero as gp

disk = gp.DiskUsage()
print(disk.usage)

print('Current disk usage: {}%'.format(disk.usage))
