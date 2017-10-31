"""Read and iniliatize configuration parameters
"""

import json

CONFIG = {}

with open('config.json', 'r') as conf:
    CONFIG = json.load(conf)
