from logging import exception
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
import ruamel.yaml as yaml



def add_netconf(device_connection_info):
    ip = device_connection_info['ip']
    print(f'Connecting to {ip}')
    juniper_device = ConnectHandler(**device_connection_info)
    configure = juniper_device.config_mode()
    print(f'Applying netconf configuration to {ip}')
    add_netconf = juniper_device.send_command('set system services netconf ssh')
    try: 
        juniper_device.commit(comment='Added NETCONF service', and_quit=True)
    except exception as e: 
        print(e)
    juniper_device.disconnect()






def main():
    username = input('Enter the username for the target device')
    password = getpass('Enter your password ')
    devices = yaml.full_load('automate_netconf_service_activate/inventory.yml')
    for device in devices:
        ip = device['address']
        device_connection_info = {
            'device_type': 'juniper',
            'ip': ip,
            'username': username,
            'password': password
        }
        add_netconf(device_connection_info)
            

if __name__ == '__main__':
    main()


