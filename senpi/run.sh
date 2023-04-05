#!/bin/bash

## Change to the directory where this script is located
#cd "$(dirname "$0")"
#dir="$(pwd)"
##start a python3 simple server
#$(nohup python3 -m http.server 8000 --dir "$(pwd)" &) &

# Change to the directory where this script is located
cd "$(dirname "$0")"
dir="$(pwd)"

# Check if http.server is already running
if pgrep -f "python3 -m http.server 8000" > /dev/null; then
  echo "http.server is already running"
else
  # Start http.server
  nohup python3 -m http.server 8000 --dir "$(pwd)" > /dev/null 2>&1 &
  echo "http.server started"
fi

# Rest of your script goes here


while true; do
    # load the eviromental data scripts
    icm20948_sample=$(python3 -c "$(cat $dir/modules/icm20948_data.py)")
	# Get CPU temperature
	cpu_temp=$( /usr/bin/vcgencmd measure_temp | awk -F "[=']" '{print($2)}' )
	# Get free RAM
	free_mem=$(free -m | awk 'NR==2{printf "\"total_mem\": %s, \"free_mem\": %s", $2,$4}')
	# Output results in JSON format
	system_info='{"cpu_temp": '$cpu_temp', '$free_mem'}' #> cpu.json


	# Save the data to a JSON file
#	echo $bme680_sample > bme680.json
#	echo $bmp280_sample > bmp280.json
#   echo $imc20948_sample > $imc20948.json
#	echo $system_info > sysinfo.json

#	echo '{"imc20948":'$imc20948_sample' , "system info":'$system_info'}' > senpi.json
#   echo '{"bme680":'$bme680_sample' , "bmp280":'$bmp280_sample' , "system info":'$system_info'}' > senpi.json
    echo '{"icm20948":'$icm20948_sample' , "system info":'$system_info'}'  > senpi.json

done

