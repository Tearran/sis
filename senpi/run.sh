#!/bin/bash

# Change directory to script folder
cd "$(dirname "$0")"

# Copy contents to /run/user/1000/senpi/
cp -r . /run/user/1000/senpi/

# Run __main__.py in the background
python3 __main__.py &

# Run http server on port 8000
#python3 -m http.server 8000 &
cd /run/user/1000/senpi/ && python3 -m http.server 8080 > /dev/null 2>&1 &
clear

echo "SenPi is running. Open your browser to http://localhost:8080 to view the dashboard."
echo "Press 'q' to exit."

# Wait for user input to exit
while true; do
    read -rsn1 input
    if [ "$input" = "q" ]; then
        echo "Exiting SenPi..."
        # Kill the background processes and exit
        pkill -f "__main__.py"
        pkill -f "python3 -m http.server 8000"
        exit 0
    fi
done
