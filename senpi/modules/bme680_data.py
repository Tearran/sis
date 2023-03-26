import bme680
import json, time

try:
  sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
  sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# Initialize sensor
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

# set heat profile
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# Get readings from sensor

gas_resistance = round(sensor.data.gas_resistance, 2)
temperature = sensor.data.temperature
pressure = sensor.data.pressure
humidity = sensor.data.humidity

sensor.get_sensor_data();

#bme680_data = {
#  'gas_resistance': gas_resistance,
#  'temperature': temperature,
#  'pressure': pressure,
#  'humidity': humidity
#}

bme680_data = {}
bme680_data['timestamp'] = int(time.time())
bme680_data['temperature'] = "{}".format(temperature).zfill(9)
bme680_data['humidity'] = "{:.1f}".format(humidity).zfill(9)
bme680_data['pressure'] = "{:.1f}".format(pressure).zfill(9)
bme680_data['gas_resistance'] = "{:.3f}".format(gas_resistance).zfill(9)
# Output the data as JSON
print(json.dumps(bme680_data))