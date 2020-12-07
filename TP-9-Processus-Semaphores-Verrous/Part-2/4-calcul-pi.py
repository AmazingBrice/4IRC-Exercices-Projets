# coding: utf-8
# BELDJILALI Ilies & FOLLÉAS Brice

import random, time
from multiprocessing import Pool

import matplotlib
import matplotlib.pyplot as plt
import numpy as np



# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
def frequence_de_hits_pour_n_essais(nb_iteration):
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
    if x * x + y * y <= 1: count += 1
    
    
    return count


def multiprocess_hit (k, nb_total_iteration) : 
        sum=0

        n = nb_total_iteration // k
        poolArray = [n] * k
        with Pool(k) as p:
            resultArray =   p.map(frequence_de_hits_pour_n_essais , poolArray )  

        for i in resultArray: # Calcule de la somme des résulats obtenu sous forme de liste
            sum = sum + i 

        return 4 * sum / nb_total_iteration


def plot(n):
    nb_total_iteration = 100000000
    nb_process  = np.array(range(1, n))
    time_array = []

    for k in nb_process :
        t0 = time.time()
        if __name__ == '__main__':
            multiprocess_hit(k , nb_total_iteration )
        else : print("Errror in parallel calculation")
        process_time = time.time() - t0
        time_array.append(  process_time ) 
        if k == 1 :
            time_standard = process_time
    
    theorical_result =  time_standard / np.array(nb_process)

    fig, ax = plt.subplots()

    ax.set(xlabel='Number of parallel processes', ylabel='Time of calculation',title='Time span comparison of Pi calculation using Monte Carlo method')
    ax.plot(nb_process , time_array)
    ax.plot(nb_process, theorical_result)
    plt.show()

# Nombre d’essai pour l’estimation
nb_total_iteration = 100000000



'''
t0 = time.time()
#nb_hits=frequence_de_hits_pour_n_essais(nb_total_iteration)
if __name__ == '__main__':
    k = 4
    print ("valeur approché de pi avec " , k , " processsus " , multiprocess_hit (k , nb_total_iteration ))


print("Temps de calul : ", time.time() - t0 )
'''

plot(15)

