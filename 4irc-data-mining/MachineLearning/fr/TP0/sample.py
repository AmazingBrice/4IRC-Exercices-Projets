import re

html = ''
line_count = 0

with open("sample.html", "r") as file:
    for line in file:
    	html += line
    	line_count +=1
file.close()

print(html)

soup = re.split('<.+?>|[\s]+', html)
print(soup)


words = list(filter(None, soup))

words_no_duplicates = list(dict.fromkeys(words))

print("Ce fichier contient "+str(len(html))+ " caractères.\n")
print("Ce fichier contient "+str(line_count)+ " lignes.\n")
print("Ce fichier contient "+str(len(words))+ " mots.\n")
print("Les 20 premiers mots de ce fichier : \n")
print(words[:20])
print("Les mots unique de ce fichier: \n")
print(words_no_duplicates)
