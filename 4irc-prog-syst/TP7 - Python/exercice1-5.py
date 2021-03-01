##### BELDJILALI Ilies & FOLLÉAS Brice 

# Imports
import csv
import numpy

popArray = []
yearArray = []

with open('./TP-Python-population.csv', "r") as csvfile:
    data = csv.reader(csvfile, delimiter=',') # setting csv delimiter
    header = next(data)
    for i in data: # foreach row as i 0 -> year / 1 -> population
        popArray.append(i[1])
        yearArray.append(i[0])

    popMin = min(popArray)
    popMax = max(popArray)

    yearMin = yearArray[popArray.index(popMin)]
    yearMax = yearArray[popArray.index(popMax)]
    popMean = numpy.mean(popArray)

print("La population moyenne sur cet intervalle de temps est de : {}".format(popMean))
print("L'année la plus peuplée est l'année ", yearMin, " avec une population de : ", popMin, " habitants.")
print("L'année la moins peuplée est l'année ", yearMax, " avec une population de : ", popMax, " habitants.")
