# SIS Architecture

SIS (Seamlessly Integrating Sensors) is a three-tiered method that is designed to seamlessly integrate sensors into a user-friendly interface. The system is made up of three decoupled layers that can be modularized for easy open-source development between languages and user preferences. The repository includes an example of a polyglot logic layer, an HTML5 stack interactive layer, and a SQLite3 data layer.

## Concepts

The SIS architecture relies on several key concepts:

- i2c bus Sensors
- Drivers
- JSON formatted dictionaries

## Frontend/Interactive Layer

The frontend layer is responsible for presenting the data to the user and allowing them to interact with the system. The user interface (UI) may be implemented using HTML, CSS, JavaScript, or other web technologies.

## Logic Layer/Sensor Integration API (SenPI)

The logic layer is responsible for processing sample data from the i2c bus, and providing a decoupled method of communicating with different layers. The inputs required by the logic layer include sample data from the i2c bus and drivers to process the data. Supported programming languages for the logic layer include Python3, Bash, and JSON. The output from the logic layer is in JSON formatted stdout, error handling, sudo automated loading of driver-device dependencies, and a JSON file that holds only one sample of each iterated device before overwriting it.

## Data Layer/Database Layer

The data layer is responsible for storing and retrieving data. The database is used to store the sensor data in a structured and efficient manner. The SQLite3 database is used in the SIS architecture.

## Scalability and Security

The SIS architecture is designed to be modular, with each layer functioning independently, allowing for easy scalability. The system is designed to be secure and is intended to be used by a user account with no admin requirements, so concerns should be in the user realm.
