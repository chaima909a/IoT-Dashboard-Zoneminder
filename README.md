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
- IP statique : ex. 172.29.xx.xxx/20
- Tous les appareils doivent pouvoir se pinguer

La Configuration du réseau :
Pour que l’IP du serveur reste fixe :

- Vérifie ta gateway :
ip r | grep default

- Crée un fichier netplan :
sudo nano /etc/netplan/01-netcfg.yaml
Exemple pour garder l’IP 172.29.xx.xxx :

network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:
      addresses: [172.29.xx.xxx/20]
      gateway4: 172.29.xx.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]

-Appliquer :
sudo netplan apply

## Installation ZoneMinder
- Installer Apache, MySQL, PHP
- Installer ZoneMinder
- Créer la base MySQL `zm`
- Ajouter 2 caméras via l’interface ZM
- Tester flux MJPEG via `<img src="http://IP_SERVEUR/zm/cgi-bin/nph-zms?...">`
Les étapes d' Installation de ZoneMinder :
-Étape 1 : Mettre à jour le système
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y

-Étape 2 : Ajouter le dépôt ZoneMinder
sudo add-apt-repository ppa:iconnor/zoneminder-1.36 -y
sudo apt update

-Étape 3 : Installer ZoneMinder
sudo apt install zoneminder -y

-Étape 4 : Activer et démarrer le service
sudo systemctl enable zoneminder
sudo systemctl start zoneminder
sudo systemctl status zoneminder

-Étape 5 : Configurer le service Apache
sudo a2enconf zoneminder
sudo a2enmod rewrite
sudo a2enmod cgi
sudo systemctl restart apache2

-Étape 6 : Vérifier l’accès
Ouvre ton navigateur et tape :
http://IP_DE_TON_SERVEUR/zm

Login par défaut : admin
Mot de passe : défini lors de la création du compte

## Dashboard Flask
### Packages requis
```bash
pip install flask psutil pyserial
