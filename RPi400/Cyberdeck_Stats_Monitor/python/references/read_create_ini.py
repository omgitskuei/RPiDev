import configparser
import logging

logging.basicConfig(level=logging.DEBUG)

config = configparser.ConfigParser()

# Note: each "../" means parent directory
ini_path = '../../cyberdeck_stats_monitor_config.ini'

try:
    with open(ini_path) as ini:
        logging.debug("Successfully opened ini file")
        config.read_file(ini)
except IOError:
    # ini file doesn't exist, so create ini file.
    logging.debug("Failed to open ini file")
    config['DEFAULT'] = {'version': '5',
                         'dateofupdate': '2022/11/19',
                         'tempunit': 'Celsius',
                         'enable': 'true'}
    config['Waveshare,ePaper,2.13in'] = {'displaywidth': '250',
                                         'displayheight': '122',
                                         'minimumrefresh': '3_mins'}

    with open(ini_path, 'w') as ini:
        config.write(ini)
    config.read(ini_path)

print(config.sections())
if 'Waveshare,ePaper,2.13in' in config:
    print(config['Waveshare,ePaper,2.13in']['DisplayWidth'])
