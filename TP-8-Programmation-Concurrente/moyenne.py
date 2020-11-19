# FOLLEAS Brice

# Imports
import numpy, sys

if (sys.argv > 1): # Verification qu'il ya bien plus qu'un seul argument
	i = 1
	notes = []
	while i < len(sys.argv):
		note = int(sys.argv[i])
		if (note > 1 or note < 20):
			notes.append(note) # Ajout des notes dans un tableau
		else: 
			print("Note non valide :", note)
		i += 1
else:
	print("Aucune moyenne a calculer")

mean = numpy.mean(notes)
print("Moyenne = %.2f" % mean)
