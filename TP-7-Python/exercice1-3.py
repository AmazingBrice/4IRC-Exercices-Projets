# BELDJILALI Ilies & FOLLÉAS Brice

import argparse

compteurLignes = 0
compteurMot = 0
compteurChar = 0
setWords = {""}

parser = argparse.ArgumentParser(description='text file to read')
parser.add_argument('textFile', action='store', type=str, help='The text to parse.')

args = parser.parse_args()
print(args.textFile)

fileName = args.textFile + ".txt"

with open(fileName,"r") as file :
for line in file:
	compteurLignes += 1

# reading each word
for word in line.split():
	compteurMot += 1
	compteurChar += len(word)
setWords.add(word)

# displaying the words
if (compteurMot <= 20):
	print(word)

print("caractères : " , compteurChar)
print("Lignes : " , compteurLignes)
print("Mots : " , compteurMot)
print("Mots distincs : " , len(setWords)- 1 )