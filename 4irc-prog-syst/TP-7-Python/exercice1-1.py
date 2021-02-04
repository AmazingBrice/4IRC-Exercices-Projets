# BELDJILALI Ilies & FOLLÉAS Brice 

n = int(input("Entrer une valeur pour faire une pyramide : "))
i = 1

while (i <= n): # nombre de lignes
    j = 1
    while (j <= i): # numéros par lignes
        print(j, end = '')
        j += 1
    print("")
    i += 1