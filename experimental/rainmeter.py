#!/usr/bin/env python3
from  gpiozero import Button
import time


rainSensor = Button(6)
BUCKET_MEASURE = 0.2794
count = 0

def bucketTipped():
    global count
    count +=1
    print(count * BUCKET_MEASURE)


def resetRain():
    global count
    count = 0

rainSensor.when_pressed = bucketTipped


while True:
   print("rain")
   time.sleep(10) 



