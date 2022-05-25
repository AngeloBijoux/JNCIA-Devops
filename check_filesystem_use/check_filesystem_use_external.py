#!/usr/bin/python3

from logging import exception
import multiprocessing
import time
from multiprocessing.spawn import import_main_path
from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import *
import getpass
import ipaddress
from pathlib import Path



NUM_PROCESSES = 6
hosts = []
Devices = Path(__file__).with_name('hosts.txt')
with Devices.open('r') as ip:
    for ip in Devices:
        ip = ip.strip()
        try:
            ip = ipaddress.ip_address(str(ip))
            hosts = hosts.append(ip)
        except ValueError:
            print('Invalid IP in hosts file'.format(ip))
            continue

username=input('Input the username used to access the device'),
password=getpass.getpass('Input the password used to access the device')
DIRECTORY = '/var/tmp/'

def check_filesystem_use(hosts):
    for host in hosts:
        try:
            with Device(host=host, user=username, password=password, port='37003') as dev:
                fs = FS(dev)
                print(f"Checking: {host}")
                print(fs.directory_usage(DIRECTORY))

        except ConnectionRefusedError:
            print(f'{host} - Device connection refused')
        except ConnectTimeoutError:
            print(f'{host} - Device connection timed out')
        except ConnectAuthError:
            print(f'{host} - Device authentication failure')

def main():
    time_start = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as process_pool:
        process_pool.map(check_filesystem_use, hosts)
        process_pool.close()
        process_pool.join()
        t = (time.time() - time_start)
    print(f"Finished in {t} seconds ")


if __name__ == '__main__':
    main()