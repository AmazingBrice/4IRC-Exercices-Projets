## TP 3 -  Communication Rf avec le micro-contrôleur

##### Langage : Python
##### Puce 908
##### Binôme : 35
##### FOLLEAS Brice | VEBER Vincent

#### Utilisation de la puce nRF51822.

#### Doc Edge Connector Kitronik : https://resources.kitronik.co.uk/pdf/5601b_built_edge_connector_breakout_board_for_the_bbc_microbit_datasheet_v1_1.pdf

### Exercice 1. Une application simple

Question 1. Quelle est la fonction que vous utilisez pour l’envoie des données par radio fréquence ?

On utilise la fonction `radio.on()` pour d'abord allumer la radio, puis `radio.send()` de la librairie radio de python et `radio.receive()` pour le recevoir et enfin `radio.off()` pour l'éteindre. A chaque message reçu, une queue se forme et `radio.receive()` permet de libérer une place en lisant la première arrivée (FIFO).

``` Python
    import radio
    from microbit import *

    # La radio ne marchera pas sauf si on l'allume !
    radio.on()

    # Boucle événementielle.
    while True:
        # Le bouton A envoie un message "Hello World !"
        if button_a.was_pressed():
            radio.send('Hello World !')

        # On lit tous les messages entrant
        incoming = radio.receive()
        
        if incoming != None:

            # Si il y a un message "Hello World !" entrant

            sleep(500)

            display.scroll(incoming)

            display.show(Image.HEART)

```

Question 2. Pouvez-vous choisir le destinataire ?

Non mais on peut choisir le canal où envoyer le message.

Question 3. Quelle fréquence est utilisé pour la configuration de la carte RF ?

On part de 2400 MHz(2,4GHz), avec 83 canaux de 1 MHz chacun. Jusqu'à 2483MHz.

Question 4. Quelle est la taille maximale de chaque message envoyé/reçu ?

La taille maximale de chaque message est définie par la variable  `length` (par défaut = 32 octets) pour les messages envoyés en radio. Cela peut atteindre les 251 octets de longueur. (254 octets - 3 octets pour S0, LENGTH et  S1).

### Exercice 2. Affichage température distante

``` Python
from microbit import *
import radio 

radio.on()

while True:
    tempLocal = str(temperature())
    
    # Le bouton A envoie un message
    if button_a.was_pressed():
        radio.send(tempLocal)
        display.scroll(tempLocal)

    # On lit tous les messages entrant
    tempDist = radio.receive()
    
    if incoming != None:
        sleep(500)
        display.scroll(tempDist)
```

### Exercice 3. Protocole de communication

#### Question 1.

Commencez d’abord par identifier les composants d’une trame : 

Sachant que la taille maximale d'un paquet est de 251 octets, l'adresse source est sur 32 bits (4 octets) d'adressage et de même pour l'adresse destination et le groupe sur 8 bits (1 octet). La longueur du message peut être défini sur 8 bits (1 octet) sachant que cela représente une taille maximale de longueur du message de xxx bits (32 octets) et qu'il nous reste donc  bits de données (Ce qui est bien inférieur à 256 la taille maximale de la trame).

longueur x telle que

Au début 254 octets auquel on enlève 3 octets pour SO, S1 et LENGTH.
On enlève 4 octets pour l’adresse (32bits) : il reste 247 octets.
On enlève 1 autre octet pour le groupe : il reste 246 octets.
On enlève encore 1 octet pour la taille du message à envoyer : il reste 245 octets.
On pourrait enlever de nouveau 1 octet pour le checksum... Mais pas ici.
On obtient finalement une taille de message maximale de 244 octets.

Quelques valeurs par défaut de la doc (`radio.config`) : https://microbit-micropython.readthedocs.io/en/v1.0.1/radio.html?highlight=receive#radio.receive

//TODO

#### Question 2.

//TODO
