import json, os
import plotext as plt

def bme680_plot(file_path):
	f = os.system("cat /run/user/1000/its/sensors-api.json")
	#with open(file_path) as f:
	data = json.load(f)
	bme680_dict = data['bme680_dump']
	bme680 = ["timestamp","temperature","humidity", "pressure","gas_resistance"]
	value = [bme680_dict[k] for k in bme680]
	plt.simple_bar(bme680, value, width = 100, title = 'BME680 Environmental readings')
	plt.show()


bme680_plot("/run/user/1000/its/sensors-api.json")