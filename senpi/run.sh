#!/bin/bash


# Change to the directory where this script is located
cd "$(dirname "$0")"
dir="$(pwd)"

# Check if i2c bus is enabled
i2c_status=$(sudo raspi-config nonint get_i2c)
if [ "$i2c_status" -eq 1 ]; then
  sudo raspi-config nonint do_i2c 0
fi

# Check if http.server is already running
if pgrep -f "python3 -m http.server 8000" > /dev/null; then
	echo "http.server is already running"
else
	# Start http.server
	nohup python3 -m http.server 8000 --dir "$(pwd)" > /dev/null 2>&1 &
	echo "http.server started"
fi

# Loop the sensors readings
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
#   echo $imc20948_sample > $imc20948.json
#	echo $system_info > sysinfo.json
    echo '{"icm20948":'$icm20948_sample' , "system info":'$system_info'}'  > senpi.json

done
