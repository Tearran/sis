#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smbus2
import os
import json
import time
from modules import system_data
from modules import bme680_data
from modules import ina260_data
from modules import bmp280_data
from modules import scanbus_data


# Set the I2C bus number
bus_num = 1

# Scan the bus for attached devices
devices = scanbus_data.scan_bus(bus_num)


# Set the path for the RAM disk and the output file
ram_disk_path = "/run/user/1000/"
output_file = os.path.join(ram_disk_path, "senpi/sensors-api.json")

# Check if the directory exists and create it if it doesn't
if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))

# Set the I2C bus number
bus_num = 1

# Create an instance of the SMBus class
bus = smbus2.SMBus(bus_num)

# List of I2C addresses to scan
addresses = devices

# Initialize an empty dictionary to store sensor data
data = {}
i = 0
# Open the output file for writing
with open(output_file, 'w') as f:
    while True:
        try:
            # Scan the I2C bus for connected devices
            for address in addresses:
                try:
                    bus.read_byte(address)
                    # If the sensor is present at the address, retrieve data from it
                    if address == 0x77:
                        bme680_dump = json.loads(bme680_data.get_bme680_data())
                        data["bme680_dump"] = bme680_dump
                    elif address == 0x76:
                        bmp280_dump = json.loads(bmp280_data.get_bmp280_data())
                        data["bmp280_dump"] = bmp280_dump
                    elif address == 0x40:
                        ina260_data_dump = json.loads(ina260_data.get_ina260_data())
                        data["ina260_dump"] = ina260_data_dump
                except:
                    # If the sensor is not present at the address, skip it
                    print(f"passing, {address}")
                    pass

            i=1+i
            data["Uptime"] = json.loads(str(i))
            # Convert dictionary to JSON string
            json_data = json.dumps(data)

            # Write JSON string to file
            f.seek(0)
            f.write(json_data)
            f.truncate()
            #print(json_data)

            time.sleep(1)
        except OSError as e:
            print(f"Error: {e}")
            time.sleep(1)
            pass
