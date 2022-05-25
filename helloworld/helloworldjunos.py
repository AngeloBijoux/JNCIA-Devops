from pprint import pprint
from jnpr.junos import Device
import getpass

host = None
target_host_file = None
user = None
password = None 
ssh_key = './id_rsa_mx80'

# dev = Device(host=input('Input the IP address of the device'),
#     user=input('Input the username used to access the device'),
#     password=getpass.getpass('Input the password used to access the device') )
# dev.open()
# pprint(dev.facts)
# dev.close()


def get_bgp_peers(host):
    peers_established = 0
    peers_other = 0 
    with Device(host) as dev:
        bgp_info = dev.rpc.get_bgp_summary_information()
        neighbor_states = bgp_data.xpath('bgp-peer/peer-state')
        for state in neighbor_states:
            if state.text == 'Established':
                peers_established += 1
            else:
                peers_other += 1
    return(peers_established,peers_other)
      