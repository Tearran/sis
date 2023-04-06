#!/bin/bash

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

while true; do
    # load the eviromental data scripts
    icm20948_sample=$(python3 -c "$(cat $dir/modules/icm20948_data.py)")
	echo -e '{"imc20948":'$imc20948_sample' , "system info":'$system_info'}' > senpi.json
#   echo '{"bme680":'$bme680_sample' , "bmp280":'$bmp280_sample' , "system info":'$system_info'}' > senpi.json
done
