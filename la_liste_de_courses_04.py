import os
import json
 
dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "liste.json")
 
if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []
 
affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer

voila
"""
 
option = "0"
 
while option != "5":
    option = input(affichage)

    if option == "1":
        item_a_ajouter = input("Entrez le nom de l'élément à ajouter: ")
        liste_de_courses.append(item_a_ajouter)

    elif option == "2":
        item_a_retirer = input("Entrez le nom de l'élément à enlever: ")
        if item_a_retirer in liste_de_courses:
            liste_de_courses.remove(item_a_retirer)

    elif option == "3":
        if len(liste_de_courses) == 0:
            print("Votre liste est vide")
            
        else:
            resultat = "\n".join(liste_de_courses)
            print("Votre liste est la suivante : \n" + resultat)
        

    elif option == "4":
        liste_de_courses.clear()
        print("Votre liste a été vidée")

with open(chemin_liste, "w") as json_file:
        json.dump(liste_de_courses, json_file, indent=4)
        print("Liste enregistrée ! :)")