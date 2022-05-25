import imp
from telnetlib import Telnet
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from initial_config_push import default_config


host = None
target_host_file = None
user = None
password = None 


with Device(
    host=input('Input the IP address of the device'),
    user='root',
    password='password',
    mode = 'telnet',
    port = '23',
    gather_facts = True ) as dev:

    cu = Config(dev)
    cu.load(path=default_config, format='xml', overwrite=True)
    print('Configuration committed:', cu.commit())



