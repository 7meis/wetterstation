#!/usr/bin/env python3
from  gpiozero import Button
import datetime


rainSensor = Button(6)
BUCKET_MEASURE = 0.2794
dayCount = 0
hourCount = 0
previousDayOfMonth = 0
previousHour = 0

def bucketTipped():
    global dayCount
    global hourCount
    global previousDayOfMonth
    global previousHour
    currentDayOdMonth = datetime.datetime.today().day
    currentHour = datetime.datetime.now().hour
    if(currentDayOdMonth == previousDayOfMonth):
        dayCount +=1
    else:
        dayCount = 0
    if(currentHour == previousHour):
        hourCount +=1
    else:
        hourCount = 0
    previousDayOfMonth = currentDayOdMonth
    previousHour = currentHour
    

def getData():
    return {
        "rain24h": round(dayCount * BUCKET_MEASURE, 4),
        "rain1h": round(hourCount * BUCKET_MEASURE, 4)
    }

def resetRain():
    global count
    count = 0

rainSensor.when_pressed = bucketTipped




