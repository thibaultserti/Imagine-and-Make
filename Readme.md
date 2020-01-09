# Description du projet

Ce projet vise à construire un casier qui puisse communiquer avec un serveur central qui gère plusieurs états des casiers (réservé, verrouillé, déverrouillé)

Le casier possède deux LEDs :
* un indicateur de l'état de réservation
* un indicateur de l'état de verrouillage

## BOUTON UNLOCK : 

* déreserve la chambre (envoi de l'information au serveur)
* déverouille le casier

## LECTEUR NFC

* si verrouillé, déverouille
* si déverrouillé, verrouille

## Schéma

![alt text](https://github.com/thibaultserti/Imagine-and-Make/blob/master/schema.png "Schema")

## Installation

``` bash
sudo apt install php php-sqlite3
```
Il faut activer les drivers sqlite dans `/etc/php/7.3/apache2/php.ini`

puis
``` bash
php -S 127.0.0.1:8080
```

