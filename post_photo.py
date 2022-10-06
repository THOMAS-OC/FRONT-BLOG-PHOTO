import json
import os


program = 1

while program :

    user_input = int(input(" 1 : Ajouter une photo \n 2 : Mise à jour BDD \n 3 : Quitter le programme\n >>> "))
    
    if user_input == 1 :
        alt_txt = input("Texte alternatif : \n >>> ")
        link_view = input("Liens d'affichage : \n >>> ")
        link_download = input("Lien de téléchargement : \n >>> ")
        categorie_picture = input("Type de photos : (macro, paysage, noir-et-blanc) \n >>> ")
        
        # Ouvrir et convertir le fichier json en liste python
        fileRead = open("src/assets/photos.json", "r")
        jsonContent = fileRead.read()
        list_photos = json.loads(jsonContent)
        fileRead.close()

        # Ajouter un élément à la liste

        mydict = {"urlFileCompressed":link_view, "urlDownload":link_download, "alt":alt_txt, "categorie" :categorie_picture}
        list_photos.append(mydict)

        # Convertir la liste en json

        jsonStr = json.dumps(list_photos)
        print(jsonStr)

        # reecrire le fichier json à partir de la liste python

        jsonWrite = open("src/assets/photos.json", "w")
        jsonWrite.write(jsonStr)
        jsonWrite.close()

    elif user_input == 2 :
        os.system("git add .")
        os.system("git commit -m 'Mise à jour de la BDD'")
        os.system("git push origin main")
        os.system("npm run build")
        os.system("firebase deploy")
        print("Mise à jour BDD : OK")

    elif user_input == 3 :
        program = 0    
