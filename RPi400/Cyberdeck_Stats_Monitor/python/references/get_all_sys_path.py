import sys
print(sys.path)

try:
    from waveshare_epd import epd2in13_V3
except ModuleNotFoundError:
    print('hi') # hi is printed, since waveshare_epd epd2in13_V3 is NOT located in one of the directories listed in sys.path


# solution 1: Add this custom dir to sys.path
sys.path.insert(0, '/home/kfctr400/omgitskuei/RPiDev/RPi400/Cyberdeck_Stats_Monitor/python/library')
try:
    import epd2in13_V3 # it works!
except ModuleNotFoundError:
    print('solution1 failed wow')

# Notice that if you re-ran the script, the first part still fails, printing 'hi'.
# This means sys.path.insert(0, ...) adds the custom directory for this run
# but doesn't save the custom directory to sys.path for future runs.
# Every time you run the script, you need to do sys.path.insert(0, ...) again
