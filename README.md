# Laptop2
The file IOT-HW3-LAptop2 has the following data:
- `main.py` - This is a MQTT client which is only a subcriber which collects all the messages sent by broker.
- `logger.py` - This program is called by main.py to write the contents into a log file.

## Objective
- A log file should be created which contains all the messages sent by the broker along with timestamp.
- Terminal will print out when the LED1 was turned on and off along with timestamp.

## Libraries used
- paho-mqtt (For establishing connection to the broker)

## How to run
-  Make sure you have the prerequisites described below before you start the experiment.

- Change the broker address from to the ip-address where the broker is hosted.


### Required installations
- Install paho- mqtt that we use for establishing a mqtt connection to the broker.
    ```
    pip3 install paho-mqtt
    ```
### Prerequisites
#### Broker     
-   We used HiveMQ MQTT Broker. For our case, we downloaded the broker and ran it in the local machine. Broker should be running on Laptop 1 before starting the Laptop 1 for the connection to be created and for subcribing and publishing.

#### Raspberry Pi A, Pi B, PiC
- All the three Raspberry Pis should be running so that the publishing and subscribing takes place and the messages sent out by the broker can be captured by Laptop 2

### Run the Laptop 2 demo
- For connecting Laptop2 to the broker run:
    ```
    python3 main.py
    ```
- For gracefully disconnecting Laptop2:
    ```
    Ctrl + C - KeyBroardInterrupt
    ```
### Output at Laptop2
- Log file will be created and data will be written into a new logfile each time Laptop2 is connected and disconnected. Log file will be named log'yyyy'-'mm'-'dd' 'hh':'mm':ss.txt. This file will be stored inside the folder IOT-HW3-Laptop2.
- Terminal output: This will have the timestamp and the LED1 status printed output each time it changes.

## What happens in Laptop2
- Laptop2 is subscribed to the following topics:
    - "lightSensor"
    - "threshold"
    - "Status/RaspberryPiA"
    - "Status/RaspberryPiC"
    - "LightStatus"
- For all the topics the logger.py method is called to write to the log file.
- For the topic "LightStatus" LED1 status is printed out.
