# IoT Dashboard + ZoneMinder

## Objectif
Créer un dashboard IoT pour une salle serveur avec :
- 2 caméras IP (téléphones ou webcams)
- Mesures de température, humidité et son via Arduino
- Alertes email si seuils dépassés

## Matériel utilisé
- Ubuntu Server (VM ou physique)
- 2 téléphones comme caméras IP
- Arduino avec capteurs : DHT11/DHT22 (temp/hum), capteur son
- PC client pour le dashboard

## Réseau
- Serveur Ubuntu en mode **bridge**
- IP statique : ex. 172.29.87.247/20
- Tous les appareils doivent pouvoir se pinguer

## Installation ZoneMinder
- Installer Apache, MySQL, PHP
- Installer ZoneMinder
- Créer la base MySQL `zm`
- Ajouter 2 caméras via l’interface ZM
- Tester flux MJPEG via `<img src="http://IP_SERVEUR/zm/cgi-bin/nph-zms?...">`

## Dashboard Flask
### Packages requis
```bash
pip install flask psutil pyserial
