# SISTER

SISTER (Seamlessly Integrating Sensor Architecture) is a three-tiered system designed to seamlessly integrate sensors into a user-friendly interface. The system is made up of three main components:

1. [Frontend/ Another Dashboard (adash)](#front)
2. [Logic Layer/ Sensor Integration API (SenPI)](#senpi)
3. [Data Layer](#data)

## Concepts

SISTER relies on several key concepts:

1. I2Cbus Sensors
2. Drivers
3. JSON formatted dictionaries
4. Decoupled architecture for increased compatibility
5. Modular for scalability

## Frontend/dashboard<a name="front"></a>

The frontend layer is responsible for presenting the data to the user and allowing them to interact with the system. The user interface (UI) may be implemented using HTML, CSS, JavaScript, or other technologies such as pygame, .

## Logic Layer/Sensor Integration API (SenPI) <a name="senpi"></a>

The logic layer is responsible for processing sample data from I2Cbus sensors and providing a decoupled method of communicating with different layers. The layer requires inputs such as sample data from I2Cbus sensors and drivers to perform its functions. The layer can be developed using Python3, Bash, JSON, and said drivers. The output from the layer is JSON formatted stdout, error handling, and sudo automated loading of driver-device dependency. A JSON file that holds only one sample of each iterated device before overwriting it is also used. The layer is scalable and modular to allow for compatibility with various languages and user preferences. Security considerations are focused on the user account with no admin requirements.

## Data Layer <a name="data"></a>

The data layer is responsible for storing and retrieving data. The layer can be developed using various technologies such as SQLite3. The data layer is decoupled from the other layers for easy open-source development and modularity.
