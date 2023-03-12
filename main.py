import paho.mqtt.client as mqtt

import os
import datetime
from logger import StateLogger

client = mqtt.Client(client_id="LaptopA")
log = None

def on_connect(client, userdata, flags, rc):
    global log
    print("Connected with result code " + str(rc))
    client.subscribe("lightSensor", qos=2)
    client.subscribe("threshold", qos=2)
    client.subscribe("Status/RaspberryPiA", qos=2)
    client.subscribe("Status/RaspberryPiC", qos=2)
    client.subscribe("LightStatus", qos=2)

    log_path = os.getcwd()   
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_name = "log" + timestamp + ".txt"
    log = StateLogger(log_path, log_name)

def on_disconnect(client, userdata,  rc):
    log.close()
    print("Disconnectedwith result code " + str(rc))

def on_message(client, userdata, msg):
    if msg.topic == "lightSensor":
        log.log_data(msg)
        #print (timestamp, "->", msg.topic, msg.payload)
    if msg.topic == "threshold":
        log.log_data(msg)
        #print (timestamp, "->", msg.topic, msg.payload)
    if msg.topic == "Status/RaspberryPiA":
        log.log_data(msg)
        #print (timestamp, "->", msg.topic, msg.payload)
    if msg.topic == "Status/RaspberryPiC":
        log.log_data(msg)
        #print (timestamp, "->", msg.topic, msg.payload)
    if msg.topic == "LightStatus":
        log.log_data(msg)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if msg.payload == b"TurnOff":
            print(timestamp, "-> LED1 turned off")
        if msg.payload == b"TurnOn":
            print(timestamp, "-> LED1 turned on")

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("169.254.180.48", 1883, 60)
try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()