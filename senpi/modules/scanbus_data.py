#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smbus2


def scan_bus(bus_num):
    # Create an instance of the SMBus class
    bus = smbus2.SMBus(bus_num)

    # List of addresses to scan
    addresses = list(range(0x03, 0x78))

    # List of devices found
    devices = []

    for address in addresses:
        try:
            bus.read_byte(address)
            devices.append(address)
        except:
            pass

    return devices
