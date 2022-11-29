# IP returned by hostname -I might be ###.###.##.###, or it might also have ' ' space followed by more numbers and ':'
# Need to parse and remove the stuff after the space, otherwise it won't fit on the display

# CASE 1
ip = '192.168.43.109 2402:7500:479:7ecf:fec8:fd26:dfaf:9f96'

print(ip[0:ip.index(' ')])


# CASE 2
ip = '192.168.43.109'

try:
    print(ip[0:ip.index(' ')])
except ValueError as ve:
    print(ip)