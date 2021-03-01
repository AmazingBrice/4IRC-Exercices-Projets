# coding: utf-8
# BELDJILALI Ilies & FOLLÉAS Brice
# Nov 2020
# Exécuter sous Linux
# Course hippique
# Version basique

# TODO : Mise en place de l'arbitre, annoncer le gagnant
# Done : Mise en place du mutex

CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCReen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné

# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc

#-------------------------------------------------------

from multiprocessing import * # Process, Value, Array
import os, time,math, random, sys
from array import array  # Attention : différent des 'Array' des Process


Nb_process = 20
arrayVal = Array('i', range(Nb_process))

sem = Semaphore()

keep_running = Value('b', True) # Fin de la course ?
lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY, CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN, \
             CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]

def effacer_ecran() : print(CLEARSCR,end='')
    # for n in range(0, 64, 1): print("\r\n",end='')

def erase_line_from_beg_to_curs() :
    print("\033[1K",end='')

def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')

def move_to(lig, col) : # No work print("\033[%i;%if"%(lig, col)) # print(GOTOYX%(x,y))
    print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='')


def un_cheval(ma_ligne : int, process_name) : # ma_ligne commence à 0
    # move_to(20, 1); print("Le cheval ", chr(ord('A')+ma_ligne), " démarre ...")
    col=1

    while col < LONGUEUR_COURSE and keep_running.value :
        move_to(ma_ligne+2,col) # pour effacer toute ma ligne # ma_ligne + 2 car on a un input
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[ma_ligne%len(lyst_colors)]) # affecte la couleur à ma ligne
        # Ajout du mutex
        with sem:
            """
            print("       ,--,")
            print(" _ ___/ /\|")
            print(";;( )__, )")
            print("; //   '\;")
            print("   \     |")
            print("    ^    ^")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            """
            print('('+chr(ord('A')+ma_ligne)+'>')
        col+=1
        arrayVal[ma_ligne] = col
        time.sleep(0.1 * random.randint(1,5))
    keep_running.value = False

def getMin():
    valMin = LONGUEUR_COURSE
    for i in range(Nb_process) :
        if arrayVal[i] < valMin :
           valMin = arrayVal[i]
           iMin = i
    return iMin

def getMax():
    valMax = 0
    for i in range(Nb_process) :
        if arrayVal[i] > valMax :
            valMax = arrayVal[i]
            iMax = i
    return iMax

def arbitre(process_name, LONGUEUR_COURSE) : # fonction d'arbitrage executée uniquement par le processus referee
    while keep_running.value :
        with sem:
            move_to(Nb_process+3, 1)
            erase_line_from_beg_to_curs()
            print('Le premier canasson est : %s le dernier canasson est : %s '% (chr(ord('A')+getMax()), chr(ord('A')+getMin())) )
        time.sleep(0.1)
    
#------------------------------------------------

if __name__ == "__main__" :
    mes_process = [0 for i in range(Nb_process)]

    LONGUEUR_COURSE = 10 #100
    effacer_ecran()
    curseur_invisible()

    guess_first = input('Qui sera le premier canasson de cette course (Rentrer une lettre) ?')

    for i in range(Nb_process):  # Lancer     Nb_process  processus
        mes_process[i] = Process(target=un_cheval, args= (i,'processus' + str(i)))
        mes_process[i].start()

    move_to(Nb_process+2, 1)
    print("tous lancés")

    referee_process = Process(target=arbitre, args=('referee',LONGUEUR_COURSE,))
    referee_process.start()
    referee_process.join()

    move_to(ord(guess_first)-ord('A')+2, 21) # Affichage à la ligne du premier

    for i in range(Nb_process): mes_process[i].join()
    if (guess_first == (chr(ord('A')+getMax())) ):
        print('Bravo !')
    else :
        print('Dommage, bien tenté !')

    move_to(24, 1)
    curseur_visible()
    print("Fini")
    