from pprint import pprint
from jnpr.junos import Device


dev = Device(host=input('Input the IP address of the device'),
    user=input('Input the username used to access the device'),
    password=input('Input the password used to access the device') )
dev.open()
pprint(dev.facts)
dev.close()