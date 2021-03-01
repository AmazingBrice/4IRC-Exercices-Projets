# IOT

##### Editeur Python pour MicroBit : https://python.microbit.org/v/2.0
##### Compileur Python : https://hub.gke.mybinder.org/user/ipython-ipython-in-depth-pjp16t4p/notebooks/binder/Untitled.ipynb?kernel_name=python3


## TP 2 -  Interaction avec capteurs et acteurs depuis unmicro-contrôleur

##### Langage : Python
##### Puce 908
##### Binôme : 35
##### FOLLEAS Brice | VEBER Vincent

#### Doc Edge Connector Kitronik : https://resources.kitronik.co.uk/pdf/5601b_built_edge_connector_breakout_board_for_the_bbc_microbit_datasheet_v1_1.pdf

#### Test des pins / leds

``` Python
from microbit import *

while True:
    if button_a.is_pressed():
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)

    if button_b.is_pressed():
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)
```

### Exercice 1. Feu de circulation

``` Python
from microbit import *

# pin0 - RED
# pin1 - ORANGE
# pin2 - GREEN

while True:
    pin2.write_digital(1)
    sleep(5000)
    pin2.write_digital(0)
    pin1.write_digital(1)
    sleep(2500)
    pin1.write_digital(0)
    pin0.write_digital(1)
    sleep(6500)
    pin0.write_digital(0)
```

### Exercice 2. LED RGB Neopixel

#### Tutorial Neopixel : https://arduiblog.com/2019/04/08/led-adressables-et-microbit/

``` Python
from microbit import *
from neopixel import NeoPixel

# Crée l'objet "strip" pour piloter les LED
strip = NeoPixel(pin0, 1)

# Déifini les couleurs
bleu = [50, 50, 240]
blanc = [240, 240, 240]
rouge = [240, 50, 50]

while True:
    strip[0] = bleu
    strip.show() # Affiche la couleur sur la LED
    sleep(250)

    strip[0] = blanc
    strip.show() # Affiche la couleur sur la LED
    sleep(250)
    
    strip[0] = rouge
    strip.show() # Affiche la couleur sur la LED
    sleep(250)
```

#### Avec deux Neopixel LED

``` Python
from microbit import *
from neopixel import NeoPixel

# Instancie le nombre de LED
n = 2

# Crée l'objet "strip" pour piloter les LED
strip = NeoPixel(pin0, n)

# Déifini les couleurs
blue = [50, 50, 240]
white = [240, 240, 240]
red = [240, 50, 50]

# Boucle infinie
while 1:
    # boucle correspondant au nombre de LED
    for index in range(0, n):
        strip[index] = blue
        strip.show() # Affiche la couleur sur la LED
        sleep(250)
        
        strip[index] = white
        strip.show() # Affiche la couleur sur la LED
        sleep(250)
        
        strip[index] = red
        strip.show() # Affiche la couleur sur la LED
        sleep(250)
```

### Exercice 3. Interface Série

Pour voir sur quel port est branché l'USB de Micro:bit :
`dmesg | grep tty`
On obtient : `[  520.161820] cdc_acm 1-8:1.1: ttyACM0: USB ACM device`
On exécute ensuite `minicom -D /dev/ttyACM0`
Une fois le programme micro:bit lancé, les messages s'afficheront dans la console minicom.

``` Python
from microbit import *

while 1:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('Le bouton A et B sont pressés !\r\n')
        sleep(500)
    elif button_a.is_pressed():
        uart.write('Le bouton A est pressé !\r\n')
        sleep(500)
    elif button_b.is_pressed():
        uart.write('Le bouton B est pressé !\r\n')
        sleep(500)
```

### Exercice 4. Capteurs météo

Avec Mircrosoft MakeCode, on obtient ce code-ci pour lire les valeurs à une certaine adresse. Pourtant, cela ne semble pas fonctionner, tout du moins, la valeur 0 s'affiche.

``` Python
def on_forever():
    # Reads 0x53 ( = 83 ) address (TSL2561)
    basic.show_number(pins.i2c_read_number(83, NumberFormat.INT8_LE, False))

    # Reads 0xED ( = 237 ) address (BME280)
    # basic.show_number(pins.i2c_read_number(237, NumberFormat.INT8_LE, False))
    basic.show_number(BME280.temperature(BME280_T.T_C)) # En utilisant une extension pour lire la température.

    # Reads 0x71 ( = 113 ) address LSB (VEML6070)
    basic.show_number(pins.i2c_read_number(113, NumberFormat.INT8_LE, False))
    
basic.forever(on_forever)
```

##### FOLLEAS Brice
##### VEBER Vincent
