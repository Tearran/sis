#!/bin/bash

# Get the directory path of the current script
cd "$(dirname "$0")" ; dir=$(pwd) ;

# Get the array of device addresses from the output of `its-i2cScan 1`
devices=$(its-i2cScan 1 | grep -E '^0x[0-9A-Fa-f]{2}$')
addresses=($devices)

# Get the array of file names from the `*_data.py` files in the `module` directory
files=$(ls "$dir/module"/*_data.py)
declare -a data_files=()

# Iterate through each file and check if it matches the `part_number` field in `devices.json`
for file in $files
do
    # Extract the part number from the file name
    part_number=$(echo "$file" | sed -e "s#$dir/module/##" -e "s#_data.py##" | tr '[:upper:]' '[:lower:]')
    # Check if the part number is in the `devices.json` file
    if grep -q "\"part_number\": \"$part_number\"" "$dir/json/devices.json"; then
        # If it is, add the file name to the `data_files` array
        data_files+=("$file")
    fi
done

# Create an array of device addresses that match the `address` field in `devices.json`
declare -a device_addresses=()
for address in "${addresses[@]}"
do
    if grep -q "\"address\": \"$address\"" "$dir/json/devices.json"; then
        device_addresses+=("$address")
    fi
done

# Print the resulting arrays
echo "Data files: ${data_files[@]}"
echo "Device addresses: ${device_addresses[@]}"
