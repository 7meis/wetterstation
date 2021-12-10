#!/usr/bin/env python3
import time
import datetime
import RPi.GPIO as GPIO  
from collections import deque
GPIO.setmode(GPIO.BCM)


GPIO.setup(16, GPIO.IN)

count = deque()
hundredcount = 0
j305_tube_ratio = 0.00812037037037

def geigerCount(channel):
    global count, hundredcount
    timestamp = datetime.datetime.now()
    count.append(timestamp)
    #count +=1
    #print(channel, " ", count)


def resetGeiger():
    global count
    count = 0


#geiger.when_pressed = geigerCount

GPIO.add_event_detect(16, GPIO.FALLING, callback=geigerCount) 



def getData():

    loop_count = 0
    while loop_count < 10:
        try: 
            while count[0] < datetime.datetime.now() - datetime.timedelta(seconds=60):
                count.popleft()
            loop_count += 1
        except IndexError:
            # No count
            pass

    if loop_count == 10:
        cpm = int(len(count))
        usvh = cpm * j305_tube_ratio
        print("Count: ", cpm)
        print("uSv/h: ", usvh)
        return {
            "count": count,
            "uSvh": usvh
        }
