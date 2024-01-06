print("Hello IoT Python")
import sys
from Adafruit_IO import MQTTClient
import random
import time
from simple_ai import *



AIO_FEED_ID = ["ai"]
AIO_USERNAME = "teevmuas123"
AIO_KEY = "aio_vMAU99aicW0ebd5nuNEnK1ikjq07"

def connected(client):
    print("Ket noi thanh cong ...")
    for id in AIO_FEED_ID:
        client.subscribe(id)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Data is from: " + feed_id + ", Payload: " + payload)

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
counter_ai = 5
while True:
     counter_ai = counter_ai - 1
     if counter_ai <= 0:
         counter_ai = 5
         ai_result= image_detector()
         print("AI Output:  ", ai_result)
         client.publish("ai",ai_result)
         time.sleep(1)
    #if counter_sensor <=0:
        #counter_sensor = 30
        #temp = random.randint(20,40)
        #client.publish("sensor1", temp)
        #humi = random.randint(0, 100)
        #client.publish("sensor2", humi)
        #lux = random.randint(0, 400)
        #client.publish("sensor3", lux)

    # counter_ai = counter_ai - 1
    # if counter_ai <=0:ee
    #     counter_ai = 5
    #     image_capture()
    #     ai_result = image_detector()
    #     client.publish("visiondetection", ai_result)

