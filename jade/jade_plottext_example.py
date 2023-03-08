#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os, time
import plotext as plt

#os.system('clear')
apath = "/run/user/1000/senpi/sensors-api.json"

def bme680_plot(file_path):
	f = open(file_path, 'r')
	data = json.load(f)
	bme680_dict = data['bme680_dump']
	bme680 = ["temperature","humidity", "pressure"]
	value = [bme680_dict[k] for k in bme680]
	plt.simple_bar(bme680, value, width = 100, title = f'BME680 samples')
	plt.show()

def bmp280_plot(file_path):
	f = open(file_path, 'r')
	data = json.load(f)
	bme680_dict = data['bmp280_dump']
	bme680 = ["temperature", "pressure"]
	value = [bme680_dict[k] for k in bme680]
	plt.simple_bar(bme680, value, width = 100, title = f'BMP280 samples')
	plt.show()

#while True:
try:
	current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
	print("\033[H\033[3J", end="")
	print(f"Environmental samples {current_time}")
	bme680_plot(apath)

	bmp280_plot(apath)
	time.sleep(1)

except OSError as e:
	print(f"Error: {e}")