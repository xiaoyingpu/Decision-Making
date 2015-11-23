# Monitors all topics on the network
# Fake n_back client to send PAUSE message
# Could persist the messages to a csv (flyloop does that too)

import threading
from paho.mqtt.client import Client
from paho.mqtt.publish import single
import csv
import time


# sending fake pauses emulating the n-back calibrator


def on_message(mqttc, obj, msg):
	print(msg.payload)

if __name__ == "__main__":
	client = Client()
	client.on_message = on_message
	#client.connect("broker.mqttdashboard.com")
	client.connect("mqtt.bucknell.edu")
	# "#" is the wildcard for all topics
	# need to subscribe to a specific one
	client.subscribe("#")
	client.loop_forever()
