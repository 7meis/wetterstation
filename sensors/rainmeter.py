#!/usr/bin/env python3
from  gpiozero import Button
import datetime
import yaml
from os.path import exists

rainSensor = Button(6)
dataFile = "data/rainmeterData.yml"
if(exists(dataFile)):
    with open(dataFile, 'w') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
else:
    data = {
        "BUCKET_MEASURE": 0.2794,
        "previousMonth": 0,
        "previousDayOfMonth": 0,
        "previousHour": 0,
        "dayCount": 0,
        "hourCount": 0,
        "monthCount": 0,
        "bucketTipTotalCount": 0,
        "bucketTipPreviousCount": 0
    }

def bucketTipped():
    global data
    data["dayCount"] +=1
    data["hourCount"] +=1
    data["monthCount"] +=1
    data["bucketTipTotalCount"] +=1
    with open(dataFile, 'w') as f:
      yaml.dump(data, f, sort_keys=False, default_flow_style=False)


def monthValue():
    global data
    currentMonth = datetime.datetime.today().month
    if(currentMonth == data["previousMonth"]):
        return round(data["monthCount"] * data["BUCKET_MEASURE"], 4)
    else:
        data["previousMonth"] = currentMonth
        data["monthCount"] = 0
        return 0


def dayValue():
    global data
    currentDayOdMonth = datetime.datetime.today().day
    if(currentDayOdMonth == data["previousDayOfMonth"]):
        return round(data["dayCount"] * data["BUCKET_MEASURE"], 4)
    else:
        data["previousDayOfMonth"] = currentDayOdMonth
        data["dayCount"] = 0
        return 0


def hourValue():
    global data
    currentHour = datetime.datetime.now().hour
    if(currentHour == data["previousHour"]):
        return round(data["hourCount"] * data["BUCKET_MEASURE"], 4)
    else:
        data["previousHour"] = currentHour
        data["hourCount"] = 0
        return 0


def getData():
    with open(dataFile, 'w') as f:
      yaml.dump(data, f, sort_keys=False, default_flow_style=False)
    return {
        "rainmonth": monthValue(),
        "rain24h": dayValue(),
        "rain1h": hourValue()
    }
    

rainSensor.when_pressed = bucketTipped
