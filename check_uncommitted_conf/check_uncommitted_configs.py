from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import getpass

host = None
target_host_file = None
user = None
password = None 


dev = Device(
    host=input('Input the IP address of the device'),
    user=input('Input the username used to access the device'),
    password=getpass.getpass('Input the password used to access the device') )
dev.open()

confutil = Config(dev)

diff = confutil.diff()
if diff:
    confutil.rollback

dev.close()