#!/bin/bash

# Function to clear the screen and save the cursor position
function clear_screen() {
	tput civis
  	tput clear
  	tput cup 0 0
}

# Function to restore the cursor position and draw the bottom bar
function draw_bottom_bar() {
  	tput cup $((LINES-2)) 0
  	tput setaf 2 # Set the text color to green
  	printf 'Press q to quit'

#  echo "Press q to quit"
	tput setab 0
    tput setaf 7

}

# Save the terminal state
tput smcup
  clear_screen
# Loop indefinitely
while true; do

    #tput setaf 3 # Set the text color to green
    tput cup 0 0
    tput setab 7
	printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
    tput setab 0
  # Load the JSON file
  json=$(cat /run/user/1000/senpi/sensors-api.json)

  # Iterate through each key-value pair in the JSON object
  for key in $(echo $json | jq -r 'keys[]'); do
    value=$(echo $json | jq -r ".$key")

    # If the value is a nested object, format it as a table
    if [[ $(echo $value | jq -r 'type') == "object" ]]; then
      table=""
      for subkey in $(echo $value | jq -r 'keys[]'); do
        subvalue=$(echo $value | jq -r ".$subkey")
        table="$table\t$subkey\t$subvalue\n"
      done
      echo -e "$key:\n$table"
    else
      # If the value is not a nested object, output it as-is
      echo -e "$key:\t$value"
    fi
  done

  # Draw the bottom bar
  draw_bottom_bar

  # Wait for user input
  read -t 1 -N 1 input
  if [[ $input == "q" ]]; then
    tput cnorm
    break
  fi

  # Wait for a short delay before refreshing the screen
  sleep 1
done

# Restore the terminal state
tput rmcup
