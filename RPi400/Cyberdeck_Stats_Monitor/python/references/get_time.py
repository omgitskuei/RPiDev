from datetime import datetime

time = datetime.now()

print(time) # eg. 2022-11-07 21:45:09.853292
print(type(time)) # <class 'datetime.datetime'>
print(str(time).index('.')) # 19

time = str(datetime.now())
print(time[0:time.index('.')])