# coding: utf-8
# BELDJILALI Ilies & FOLLÉAS Brice

"""
Split d'une image (Mono−Process)
"""

# Imports
import multiprocessing as mp
from PIL import Image  # Importation de la librairie d'image PIL
from math import sqrt
import os
import time
import numpy as np
from multiprocessing import shared_memory

image_ = None  # sera chargée dans la partie Main (ici, on la 'pré−déclare')
width, height = None, None  # respectivement, la largeur et la hauteur de l'image
MAX_PROCESS = mp.Value('i', 12)

ALL_DONE = mp.Value('b', False)
matrice_pixels = None




def GetPixel(x, y):
    return matrice_pixels[x, y]


def PutPixel(x, y, r, g, b):
    matrice_pixels[x, y] = int(r), int(g), int(b)  # Il faut des ints !


def PutRegion(x, y, width, height, triplet_color):
    for i in range(x, x+width):
        for j in range(y, y+height):
            PutPixel(i, j, triplet_color[0],
                     triplet_color[1], triplet_color[2])


def Average(corner_x, corner_y, region_w, region_h):
    sum_red, sum_green, sum_blue = 0, 0, 0  # Initialisation des compteurs
    area = region_w*region_h  # Calcul de la superficie de la région

    for i in range(corner_x, corner_x+region_w):
        for j in range(corner_y, corner_y+region_h):
            # Nous lisons les données r, v, b d'un pixel
            r, g, b = GetPixel(i, j)
            sum_red += r  # somme de chaque composant
            sum_green += g
            sum_blue += b

    # Normalisation
    sum_red /= area
    sum_green /= area
    sum_blue /= area
    return(sum_red, sum_green, sum_blue)  # Retour des valeurs r, g, b moyennes


def Mesures_Std_et_Mu(corner_x, corner_y, region_w, region_h):
    av_red, av_blue, av_green = Average(corner_x, corner_y, region_w, region_h)
    sum_red2, sum_green2, sum_blue2 = 0.0, 0.0, 0.0

    for i in range(corner_x, corner_x+region_w):
        for j in range(corner_y, corner_y+region_h):
            red, green, blue = GetPixel(i, j)
            sum_red2 += (red**2)
            sum_green2 += (green**2)
            sum_blue2 += (blue**2)
    area = region_w*region_h*1.0
    r, g, b = 0, 0, 0
    r = sqrt(abs(sum_red2 / area - av_red**2))
    g = sqrt(abs(sum_green2 / area - av_green**2))
    b = sqrt(abs(sum_blue2 / area - av_blue**2))

    return ((av_red, av_blue, av_green), (r+b+g)/3.0)


def Decouper_en4(x, y, width, height, threshold_alpha ,  nbProcess):

    if height*width < 4:
        return  # rien à découper

    # Cas de région uniforme : une couleur uniforme est affectée à la partition
    color, rm = Mesures_Std_et_Mu(x, y, width, height)
    if rm < threshold_alpha:  # Affectation de la couleur moyenne à la partition
        PutRegion(x, y, width, height, color)
    # Dans le cas contraire, la partition non−uniforme est coupée en 4 (récursivement)
    else:

        # mettre en place un array avec les args pour chaque process + pere
        array = [[x+width//2, y], [x, y+height//2], [x+width//2, y+height//2]]

        mes_process = [*range(3)]  # Création de 3 processus
        

          # Créer un processus
        print("nbProcess.value " , nbProcess.value)

          
        for i in range(3):
            
            if ( 0 < nbProcess.value or nbProcess.value  < MAX_PROCESS.value - 1  ):
                print("création du process " , i)

                mes_process[i] = mp.Process(target=Decouper_en4, args=(
                    array[i][0], array[i][1], width//2, height//2, threshold_alpha , nbProcess))
                nbProcess.value += 1
                print("nb process  " , nbProcess.value )

                mes_process[i].start()

            else :
                Decouper_en4(array[i][0], array[i][1], width//2, height//2, threshold_alpha, nbProcess)

        Decouper_en4(x, y, width//2, height//2, threshold_alpha, nbProcess)
        for i in range(3):    
            mes_process[i].join()
            print("fin du process " , i )
            nbProcess.value -= 1
            print("nb process  " , nbProcess.value )
                





        


def controller(max_process):
    '''
    while not ALL_DONE.value:
        if (NB_PROCESS.value < 0 or NB_PROCESS.value > max_process ):
            print('Il y a une erreur dans la gestion des processus.')
    '''

# −−−−−−−−−−−−−−−−−−−− Principale −−−−−−−−−−−−−−−−−−−−−−−−−−


if __name__ == '__main__':
    dir_image = "./ressources"
    nom_fic_image = "balls.png"
    nom_fic_in = dir_image+'/'+nom_fic_image

    try:
    # nécessaire pour une image "png"
        image_ = Image.open(nom_fic_in).convert("RGB")  
        width, height = image_.size
        matriceSize = width * height
        matrice_pixels = shared_memory.SharedMemory(
        create=True,  size=matriceSize)
        matrice_pixels = image_.load()  # Importation des pixels de l'image

    except:
        print("Problème avec le fichier ", nom_fic_in)
        quit(1)


    NB_PROCESS = mp.Value('i', 0)
    print("controller start...")
    process_controller = mp.Process(
        target=controller, args=(MAX_PROCESS.value,))
    process_controller.start()

    # tester avec les seuils différents 3, 10, 15, 20, ...
    print("decouper en 4 start...")
    print("width height" , width , height )
    
    Decouper_en4(0, 0, width, height, 15, NB_PROCESS)
    image_.show()

    print("controller end...")

    process_controller.join()
    # On sauvegarde le résultat
    # On construit le nom de l'image sauvegardée
    nom_fic_out = dir_image+'/'+"out_"+nom_fic_image
    image_.save(nom_fic_out)
