#!/usr/bin/env python3
from  gpiozero import Button
import datetime
import yaml
from yaml.loader import SafeLoader
from os.path import exists

# initialize rain sensor as button
rainSensor = Button(6)

# specify data file and read if it exists
dataFile = "data/rainmeterData.yml"
if(exists(dataFile)):
    with open(dataFile, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
    print(yaml.dump(data))
else:
    data = {
        'BUCKET_MEASURE': 0.2794,
        'previousMonth': 0,
        'previousDayOfMonth': 0,
        'previousHour': 0,
        'dayCount': 0,
        'hourCount': 0,
        'monthCount': 0,
        'bucketTipTotalCount': 0,
        'bucketTipPreviousCount': 0
    }

def bucketTipped():
    """set counters if bucket is tipped"""
    global data
    data['dayCount'] +=1
    data['hourCount'] +=1
    data['monthCount'] +=1
    data['bucketTipTotalCount'] +=1
    with open(dataFile, 'w') as f:
      yaml.dump(data, f, sort_keys=False, default_flow_style=False)


# whenn button is pressed call bucketTipped to count
rainSensor.when_pressed = bucketTipped


def monthValue():
    """calculate and return month value"""
    global data
    currentMonth = datetime.datetime.today().month
    if(currentMonth == data['previousMonth']):
        return round(data['monthCount'] * data["BUCKET_MEASURE"], 4)
    else:
        data['previousMonth'] = currentMonth
        data['monthCount'] = 0
        return 0


def dayValue():
    """calculate and return day value"""
    global data
    currentDayOdMonth = datetime.datetime.today().day
    if(currentDayOdMonth == data['previousDayOfMonth']):
        return round(data['dayCount'] * data['BUCKET_MEASURE'], 4)
    else:
        data['previousDayOfMonth'] = currentDayOdMonth
        data['dayCount'] = 0
        return 0


def hourValue():
    """calculate and return hour value"""
    global data
    currentHour = datetime.datetime.now().hour
    if(currentHour == data['previousHour']):
        return round(data['hourCount'] * data['BUCKET_MEASURE'], 4)
    else:
        data['previousHour'] = currentHour
        data['hourCount'] = 0
        return 0


def getData():
    """gather sensor data and return it as dictionary"""
    with open(dataFile, 'w') as f:
      yaml.dump(data, f, sort_keys=False, default_flow_style=False)
    return {
        "rainmonth": monthValue(),
        "rain24h": dayValue(),
        "rain1h": hourValue()
    }
    


