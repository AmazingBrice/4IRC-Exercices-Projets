##### BELDJILALI Ilies & FOLLÉAS Brice 

# Imports
import statistics 

# Création de la classe
class Etudiant:

    def __init__(self, nom, age, notes):
     self.nom = nom
     self.age = age
     self.notes = notes

    def display(self):
     print("Nom: " + self.nom)
     print("Age: " + self.nom)
     print("Notes: " + str(self.notes))

# Déclaration des étudiants
etudiants = []  

n = input("Entrer le nombre d'étudiants : ")
i = 0
j = 0
while i < int(n):
    nom = input("Entrer le nom de cet étudiant.e {}: ".format(i+1)) 
    age = int(input("Entrer l'age de cet étudiant.e {}: ".format(i+1)))
    notes = []
    while j < 5:
        note = int(input("Entrer la note du module {}".format(j+1)))
        notes.append(note)
        j += 1
    etudiants.append(Etudiant(nom, age, notes)) # Ajout d'un étudiant dans le tableau des étudiants
    j = 0 # Réinitialisation de l'indice j
    i += 1
# Affichage de tous les étudiants
i = 0
while i < int(n):
    etudiants[i].display()
    i+=1

# Récupération des notes
i = 0
notes_classe = []
while i < int(n):
    while (j < 5):
        notes_classe.append(etudiants[i].notes[j])
        j += 1
    i += 1
moy = statistics.mean(notes_classe)
max = max(notes_classe)
min = min(notes_classe)

print("La moyenne de la classe est {}".format(moy))
print("La note minimum de la classe est {}".format(min))
print("La max de la classe est {}".format(max))