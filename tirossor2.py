# -*- coding: cp1252 -*-


import random
import time

# variables et liste
recommencer = ""
boucle = 1;
commencer = ""
donnee_utilisateur = []
invitation = "entrez un nom : "
tirage = ""
ajouter = ""
intro = "Bienvenue dans TIROSSOR ! TIROSSOR choisit au hasard un nom !"

#fonction principale main
print(intro)
recommencer = raw_input("Voulez vous commencer un tirage ? oui / non\n")

if recommencer == "oui":
    while recommencer != "non":
        del donnee_utilisateur[:]
        ajouter = ""
        if commencer != "non":
            while ajouter != "non":
                ajouter = raw_input("voulez vous ajouter un nom ? oui / non\n")
                if ajouter == "oui":
                    donnee_utilisateur.append(raw_input(invitation))    

                else:
                    nbr_item_in_list = len(donnee_utilisateur)
                    if nbr_item_in_list == 0:
                        error = raw_input("Vous n'avez mis aucune valeur ! Fin du programme. Appuyez sur la touche Q de votre clavier pour quitter ! \n")
                        while True:
                            if error == "q": 
                                print ('au revoir !')
                                time.sleep(0.7)
                                quit()

                            error = raw_input("Que voulez vous faire ? Si vous voulez quittter tirossor, appuyer sur Q. Si vous voulez continuer le programme, appuyer sur C \n")
                            if error == "q":
                                print ('au revoir !')
                                time.sleep(0.7)
                                quit()

                            elif error == "c":
                                print('OK, on continue !')
                                time.sleep(0.7)
                                break

                            else:
                                print('Vous ne respectez pas les regles de tirossor. Je suis donc dans l\'obligation de fermer Tirossor ! A une prochaine fois peut-etre !\n')
                                time.sleep(4)
                                quit()
                            
                             
                                

                            
                        

                    else:
                        print("vous avez saisi : ")
                        print(donnee_utilisateur[:])
                        print("TIROSSOR a choisit : "+random.choice(donnee_utilisateur) + " !")
                        recommencer = raw_input("\nVoulez vous recommencer un tirage ? oui / non \n")
                        
        
    print("Au revoir")
    raw_input('appuyer sur une touche pour quitter ')
        
                
else :
    if recommencer == "non":
        print("Au revoir")
        raw_input('appuyer sur une touche pour quitter ')
        
        
    else:
        raw_input("Saisie invalide")

        
