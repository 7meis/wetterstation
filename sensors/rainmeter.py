#!/usr/bin/env python3
from  gpiozero import Button
import datetime


rainSensor = Button(6)
BUCKET_MEASURE = 0.2794
dayCount = 0
hourCount = 0
monthCount = 0
previousMonth = 0
previousDayOfMonth = 0
previousHour = 0
bucketTipTotalCount = 0
bucketTipPreviousCount = 0

def bucketTipped():
    global monthCount
    global dayCount
    global hourCount
    global bucketTipTotalCount
    dayCount +=1
    hourCount +=1
    monthCount +=1
    bucketTipTotalCount +=1


def monthValue():
    global monthCount
    global previousMonth
    currentMonth = datetime.datetime.today().month
    if(currentMonth == previousMonth):
        return round(monthCount * BUCKET_MEASURE, 4)
    else:
        previousMonth = currentMonth
        monthCount = 0
        return 0


def dayValue():
    global dayCount
    global previousDayOfMonth
    currentDayOdMonth = datetime.datetime.today().day
    if(currentDayOdMonth == previousDayOfMonth):
        return round(dayCount * BUCKET_MEASURE, 4)
    else:
        previousDayOfMonth = currentDayOdMonth
        dayCount = 0
        return 0


def hourValue():
    global hourCount
    global previousHour
    currentHour = datetime.datetime.now().hour
    if(currentHour == previousHour):
        return round(hourCount * BUCKET_MEASURE, 4)
    else:
        previousHour = currentHour
        hourCount = 0
        return 0


def getData():
    return {
        "rainmonth": monthValue(),
        "rain24h": dayValue(),
        "rain1h": hourValue()
    }


rainSensor.when_pressed = bucketTipped