##### BELDJILALI Ilies & FOLLÉAS Brice 

from os import walk
import os
import argparse

parser = argparse.ArgumentParser(description='text file to read')
parser.add_argument('mypath', action='store', type=str, help='The text to parse.')
args = parser.parse_args()

#mypath = "/home/ilies/Documents/"

def lire_dossier(mypath) :
f = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
	print(dirpath, dirnames, filenames)
f.extend(filenames)

return f

lire_dossier(args.mypath)