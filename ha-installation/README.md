
# Docker installieren

```
sudo mkdir /docker
sudo curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
groups pi
sudo pip3 install docker-compose
sudo systemctl enable docker
```

## Docker Container für Wetterstation einrichten (via Compose)

```
sudo mkdir /docker/ # Verzeichnis für alle Docker Container Daten
sudo docker-compose -f docker-compose.eshh.homeassistant.yml up -d
```

# Mosquitto Broker Konfiguration kopieren

```
/docker/mosquitto_config/mosquitto.conf
```

# Home Assistant Konfiguration

```
MQTT Integration in HA aktivieren
MQTT Broker hinterlegen -> Mosquitto Broker 
```

# Sensor Script Requirements

```
sudo pip3 install paho-mqtt
```

# Systemd Service einrichten

```
sudo systemctl daemon-reload
sudo systemctl enable es-hh_ReadingSensors.service

sudo service es-hh_ReadingSensors start
sudo service es-hh_ReadingSensors status
sudo service es-hh_ReadingSensors stop
```


# HA Lovelace Dashboard anpassen

```
Edit Dashboard -> Raw Configuration Editor
Code von Beispiel übernehmen
```

# Sonstiges

```
Wichtig, Entitiy ID für Sensoren hinterlegen -> HA Entities
```

