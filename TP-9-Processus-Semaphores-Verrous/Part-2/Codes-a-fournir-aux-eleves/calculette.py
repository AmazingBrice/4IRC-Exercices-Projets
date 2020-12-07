import time,os,random
def fils_calculette(rpipe_commande, wpipe_reponse):
    print('Bonjour du Fils', os.getpid())
      
    while True:
        cmd = os.read(rpipe_commande, 32)
        print("Le fils a recu ", cmd)
        res=eval(cmd)
        print("Dans fils, le résultat =", res)
        os.write(wpipe_reponse, str(res).encode())
        print("Le fils a envoyé", res)
        time.sleep(1)

    os._exit(0)
    
                
if __name__ == "__main__" :

    rpipe_reponse, wpipe_reponse = os.pipe()
    rpipe_commande, wpipe_commande = os.pipe()
    
    pid = os.fork()
    
    if pid == 0:
        fils_calculette(rpipe_commande, wpipe_reponse)
        assert False, 'fork du fils n a pas marché !'    # Si échec, on affiche un message
        
    else :
        # On ferme les "portes" non utilisées
        os.close(wpipe_reponse)
        os.close(rpipe_commande)  

        while True :
            # Le pere envoie au fils un calcul aléatoire à faire et récupère le résultat
            opd1 = random.randint(1,10)
            opd2 = random.randint(1,10)
            operateur=random.choice(['+', '-', '*', '/'])
            str_commande = str(opd1) + operateur + str(opd2)
            
            os.write(wpipe_commande, str_commande.encode())
            print("Le père va demander à faire : ", str_commande)
            res = os.read(rpipe_reponse, 32)
            print("Le Pere a recu ", res)
            print('-'* 60)
            time.sleep(1)
