#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from smbus2 import SMBus
import sys
import os
import time

def scan(bus_num, start=0x03, end=0x78):
    # Read devices from JSON file
    with open('devices.json', 'r') as f:
        devices = json.load(f)

    try:
        bus = SMBus(bus_num)
    except PermissionError:
        print("Permission error!")
        sys.exit()
    except FileNotFoundError:
        print("Error: Unable to locate I2C bus")
        file_exists = exists("/usr/bin/raspi-config")
        if file_exists:
            try:
                print("raspi-config found:\n\tEnabling i2c bus")
                os.system("sudo raspi-config nonint do_i2c 0 ; sleep 1")
                bus = SMBus(bus_num)
            except:
                print("Unknown ERROR:")
                sys.exit()
        else:
            print("Enable I2C first")
            sys.exit()

    found_devices = []
    for i in range(start, end):
        val = 1
        try:
            bus.read_byte(i)
        except OSError as e:
            val = e.args[0]
        finally:
            if val != 5:    # No device
                if val == 1:
                    found_address = hex(i)
                    for device in devices:
                        if device['address'] == found_address:
                            found_devices.append(device)
                            break
                    else:
                        found_devices.append({
                            "address": found_address,
                            "friendly_name": "Unknown device",
                            "part_number": "Unknown",
                            "category": "",
                            "url_module": "Join our discrod to sugest a module",
                            "sub_category": ""
                        })
                elif val == 16:
                    pass
                elif val == 110:
                    pass
                elif val == 121:
                    pass
                else:
                    pass

    # Print results
    for device in found_devices:
        print(device['address'], '"'+device['part_number']+'"', '"'+device['url_module']+'"')

if __name__ == "__main__":
    scan(1)
