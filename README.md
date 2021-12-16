# Weather station
School project for Embedded Systems and HH Module at FFHS


## Notes
You need some prerequisites to setup the enviroment:
- A Raspberry PI (or two - one for the station and one for Home Assistant)
- A main connector board
- A Power Source (USB C)
- Wifi or LAN
- A bunch of sensors, supported are atm:
    - BME280
    - Geiger Counter from Ali Express
    - PMSA003
    - Rain and windmeter

At the raspberry pi for the weather station, you need some dependencies.

The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

## HA installation
For Home Assistant installation see:
https://github.com/7meis/wetterstation/tree/main/ha-installation