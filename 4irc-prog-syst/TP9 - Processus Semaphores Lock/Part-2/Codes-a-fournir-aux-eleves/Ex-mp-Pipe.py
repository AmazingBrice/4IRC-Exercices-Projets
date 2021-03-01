# Nov 2020, CPE concurrent Python
# Exemple du cours 
# Somme parallèle avec fork d'abor
# Ici  somme avec "array" + Pipe (pas "Array" mais "array" comme numpy)
"""
Extrait doc Python sur mp.Pipe() :
Note that data in a pipe may become corrupted if two processes (or threads) try to read from or write 
to the same end of the pipe at the same time. Of course there is no risk of corruption from processes 
using different ends of the pipe at the same time.
"""
import array
import os
import multiprocessing as mp # pour Value, Pipe

# La fonction des fils
def somme(num_process, table, debut, fin_exclue, cote_pere_read, cote_fils_write) :
    print("Je suis le fils num ", num_process, "et je fais la somme du tableau ", tableau[debut: fin_exclue] )
     
    S_local=0
    for i in range(debut, fin_exclue) :
        S_local += tableau[i]
    
    cote_pere_read.send(S_local) # Non bloquant
    print(f"le fils num {num_process}, envoie par send {S_local}")
    
if __name__ == "__main__" :
    taille = 10
    
    # Plus efficace que les listes
    tableau = array.array('i',[i for i in range(taille)])
    print(tableau[:])
    
    cote_pere_read, cote_fils_write=mp.Pipe()
     
    id_fils1 = os.fork()
    if not id_fils1 : # Je suis le fils1
        somme(1, tableau, 0, taille // 2, cote_pere_read, cote_fils_write)
        os._exit(0)
    else : # Le père  
        id_fils2 = os.fork()
        if not id_fils2 : # Je suis le fils2
            somme(2, tableau, taille // 2, taille,cote_pere_read, cote_fils_write) # taille car on commence à 0
            os._exit(0)
    # Le fils revient pas
    moitie1=cote_fils_write.recv() # Blocks until there is something to receive.
    moitie2=cote_fils_write.recv()
    # On peut laisser "wait" mais inutile dans ce cas car "recv()" est bloquant et les fils terminent 
    # avec send (non bloquants)
    os.wait(); os.wait()
    print("La somme totale du tableau est ", moitie1+moitie2)
    print(f"LE pere vérifie que la somme doit être {sum(tableau)}")
 