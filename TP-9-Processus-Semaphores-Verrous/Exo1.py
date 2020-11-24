# Ilies BELDJILALI & Brice FOLLEAS

# Imports
import multiprocessing as mp

# Fonctions
def sumArray (array):
	S_local = 0
	for i in array:
		print(i)
		S_local = S_local + i
	print('La somme local est de : ', S_local)
	verrou.acquire()
	S_shared.value = S_shared.value + S_local
	verrou.release()
if __name__ == "__main__" :

	n = 10
	evenElementsArray = []
	oddElementsArray = []

	# Declaration du tableau a diviser
	array = list(range(0, 10))
	# Declaration des sous tableaux
 	for i in array:
 		print(i)
 		if(i%2 == 0):
 			evenElementsArray.append(i)
 		else:
 			oddElementsArray.append(i)

	verrou=mp.Lock()

	S_shared = mp.Value('i',0)	
	print(S_shared.value)
	# Creation des processus
	pid1 = mp.Process(target=sumArray, args=(oddElementsArray,))
	pid1.start()
	
	pid2 = mp.Process(target=sumArray, args=(evenElementsArray,))
	pid2.start()

	# Recuperation des fils
	pid1.join(); pid2.join()

	print('La somme du tableau est de :', S_shared.value,'(doit etre',(sum(array)),' )')
