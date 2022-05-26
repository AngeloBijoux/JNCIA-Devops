#!/usr/bin/python3

from logging import exception
import multiprocessing
import time
from multiprocessing.spawn import import_main_path
from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import *
import getpass
import yaml







filename = "check_filesystem_use/hosts.yml"
with open(filename) as f:
    content = yaml.full_load(f)
    hosts = yaml

for host, doc in content.items():
    print(host, ':', doc)




# {'hosts': 
# [{'hostname': 'R1', 'model': 'vMX', 'address': '66.129.234.213', 'ssh': 38005, 'netconf': 38003, 'rest': 38004},
#  {'hostname': 'R2', 'model': 'vMX', 'address': '66.129.234.213', 'ssh': 38008, 'netconf': 38006, 'rest': 38007}]}

