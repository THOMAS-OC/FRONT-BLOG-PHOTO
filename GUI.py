# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
from tkinter import ttk
import os
import json

def updateGithub():
	os.system("git add .")
	os.system("git commit -m 'Mise à jour de la BDD'")
	os.system("git push origin main")

def updateWebsite():
	os.system("npm run build")
	os.system("firebase deploy")

def writeJson():
	print(altInput.get())
	print(urlCompressedInput.get())
	print(urlDownload.get())

	# Ouvrir et convertir le fichier json en liste python

	fileRead = open("src/assets/photos.json", "r")
	jsonContent = fileRead.read()
	list_photos = json.loads(jsonContent)
	fileRead.close()

	# Ajouter un élément à la liste

	mydict = {"urlFileCompressed":urlCompressedInput.get(), "urlDownload":urlDownload.get(), "alt":altInput.get(), "categorie":liste1.get()}
	list_photos.append(mydict)

		# Convertir la liste en json

	jsonStr = json.dumps(list_photos)

		# reecrire le fichier json à partir de la liste python

	jsonWrite = open("src/assets/photos.json", "w")
	jsonWrite.write(jsonStr)
	jsonWrite.close()

# def writeJson() :


# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()

# Ajout d'un titre à la fenêtre principale :
fenetre.title("update blog-photo software")

# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x400")

# Limiter les dimensions d’affichage de la fenêtre principale :
fenetre.maxsize(640,400)
fenetre.minsize(640,400)

# Création des champs de saisie de l'utilisateur dans la fenêtre :
# Ajout d'un texte dans la fenêtre :
altLabel = Label (fenetre, text = "Texte alternatif")
altLabel.grid(row = 0, column = 0, sticky = W, pady = 20, padx=(10, 10))

altInput = Entry(fenetre)
altInput.grid(row = 0, column = 1, sticky = W, pady = 20)

urlCompressedLabel = Label (fenetre, text = "URL d'affichage")
urlCompressedLabel.grid(row = 1, column = 0, sticky = W, pady = 20, padx=(10, 10))

urlCompressedInput = Entry(fenetre)
urlCompressedInput.grid(row = 1, column = 1, sticky = W, pady = 20)

urlDownloadLabel = Label (fenetre, text = "URL Download :")
urlDownloadLabel.grid(row = 2, column = 0, sticky = W, pady = 20, padx=(10, 10))

urlDownload = Entry(fenetre)
urlDownload.grid(row = 2, column = 1, sticky = W, pady = 20)

# Création de la liste déroulante pour sélectionner le type de photo
listeLabel = Label (fenetre, text = "Type de photo : ")
listeLabel.grid(row = 3, column = 0, sticky = W, pady = 20, padx=(10, 10))

listeProduits=["animalier", "black-and-white", "macro", "paysage"]
liste1 = ttk.Combobox(fenetre, values=listeProduits)
liste1.current(0)
liste1.grid(row = 3, column = 1, sticky = W, pady = 20)

# Texte mise à jour
actionLabel = Label (fenetre, text = "Mise à jour")
actionLabel.grid(row = 6, columnspan= 1, padx=(10, 10), sticky = W, pady = 20)

# Ajout d'un bouton d'update dans la fenêtre :
btnGithub = Button(
  fenetre,
  text = "Update Github", 
  command = updateGithub
)
btnGithub.grid(row = 7, column = 0, sticky = W, pady = 20, padx=(10, 10))

btnDeploy = Button(
  fenetre,
  text = "Update website", 
  command = updateWebsite
)
btnDeploy.grid(row = 7, column=1)

btnDB = Button(
  fenetre,
  text = "Update Databases", 
  command = writeJson
)
btnDB.grid(row = 7, column = 2, sticky = W, pady = 20)



# Affichage de la fenêtre créée :
fenetre.mainloop()