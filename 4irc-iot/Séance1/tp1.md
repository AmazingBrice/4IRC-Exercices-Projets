# IOT

##### Editeur Python pour MicroBit : https://python.microbit.org/v/2.0
##### Compileur Python : https://hub.gke.mybinder.org/user/ipython-ipython-in-depth-pjp16t4p/notebooks/binder/Untitled.ipynb?kernel_name=python3

## TP 1 - Prise en main d’un micro-contrôleur 

### Exercice 1. Étude du système

#### Question 1 Rechercher les caractéristiques des diverses cartes en question et les micro-contrôleurs utilisés
par chacune d’entre elles. 
Passé

C8051F02x de SiliconLabs

    - Capteur de température

    - 32 ou 64 entrées / sorties

Arduino Uno
STM32 de ST Micro-electronics
Micro :bit

### Exercice 2. Documentations techniques

Liste des documentations :
- https://microbit-micropython.readthedocs.io/en/v1.0.1/
- https://microbit.org/get-started/user-guide/python/
- https://python.microbit.org/v/2.0
- https://makecode.microbit.org/docs

##### Question 1. Rechercher les différents documentations techniques pour la carte Micro :bit et de ses com-
posants. Est-ce que le site du distributeur (BBC) propose des documentations plus complètes que ceux des
fabricants des composants ?

Oui, la documentation est la suivante : https://microbit-micropython.readthedocs.io/en/v1.0.1/

#### Question 2. Quels sont les outils dont j’aurais besoin pour passer de mon code source à un système
fonctionnant avec la carte Micro-bit ?

Un compileur.

#### Test à réaliser
Vous allez tester l’environnement de développement avec quelques exercices d’accès au différents capteurs
intégrés.

#### Exercice 3. Test du module

Commencez par vérifier que votre module fonctionne (rien de plus frustrant que d’essayer de programmer
un micro-contrôleur qui ne réponds pas).

```
from microbit import *
while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    sleep(2000)
```

#### Exercice 4. Interaction avec les LEDs embarquées

Tester l’écran des LEDs embarquées en affichant un message qui va changer une fois les boutons intégrés
sont pressés.

```
from microbit import *
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)
```

#### Exercice 5. Capteur de température

Tester l’accès au capteur de température et affichez la valeur et une alerte si la température dépasse un
seuil de 30 degrés.

```
from microbit import *

while True:

    if temperature() > 30 :
        display.scroll('Il fait trop chaud ! ')
        display.show(Image.SAD)
    else :
        display.scroll('La température est bonne ! ')
        display.show(Image.HAPPY)
        
    sleep(2000) """ Permet de laisser le temps au mc d'afficher l'image """
```

#### Exercice 6. Capteur accéléromètre

Le capteur mesure les données des mouvements en trois axes (x,y,z), faites une application qui affiche le
nombre de fois que le capteur est incliné à sa gauche.

```
from microbit import *

count = 0
while True:
    x = accelerometer.get_x()
    
    if x < 0:
        count += 1
    display.scroll(count)
    sleep(1000)
```

#### Exercice 7. Capteur boussole

Créer une application boussole en utilisant le capteur magnétomètre intégré est affichant le Nord dans la
matrice de LEDs

`̀``
from microbit import *
compass.calibrate()
while True:
    orientation = compass.heading()
    if orientation < 22.5 or orientation > 337.5:
        display.show('N')
    elif orientation < 67.5 and orientation > 22.5:
        display.show('NE')
    elif orientation < 112.5 and orientation > 67.5:
        display.show('E')
    elif orientation < 157.5 and orientation > 112.5:
        display.show('SE')
    elif orientation < 202.5 and orientation > 157.5:
        display.show('S')
    elif orientation < 247.5 and orientation > 202.5:
        display.show('SO')
    elif orientation < 292.5 and orientation > 247.5:
        display.show('O')
    elif orientation < 338.5 and orientation > 292.5:
        display.show('NO')
        ```

##### FOLLEAS Brice
##### VEBER Vincent
