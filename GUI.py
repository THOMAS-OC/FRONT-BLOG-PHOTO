# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
import os
import json

def updateGithub():
	os.system("git add .")
	os.system("git commit -m 'Mise à jour de la BDD'")
	os.system("git push origin main")

def updateWebsite():
	os.system("firebase deploy")

def writeJson():
	print(altInput.get())
	print(urlCompressedInput.get())
	print(urlDownload.get())
	categorie = ""
	for i in liste1.curselection():
		categorie = liste1.get(i)
		print(categorie)

	# Ouvrir et convertir le fichier json en liste python

	fileRead = open("src/assets/photos2.json", "r")
	jsonContent = fileRead.read()
	list_photos = json.loads(jsonContent)
	fileRead.close()

	# Ajouter un élément à la liste

	mydict = {"urlFileCompressed":urlCompressedInput.get(), "urlDownload":urlDownload.get(), "alt":altInput.get(), "categorie":categorie}
	list_photos.append(mydict)

		# Convertir la liste en json

	jsonStr = json.dumps(list_photos)

		# reecrire le fichier json à partir de la liste python

	jsonWrite = open("src/assets/photos2.json", "w")
	jsonWrite.write(jsonStr)
	jsonWrite.close()

# def writeJson() :


# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()

# Ajout d'un titre à la fenêtre principale :
fenetre.title("update blog-photo software")

# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")

# Limiter les dimensions d’affichage de la fenêtre principale :
fenetre.maxsize(800,600)
fenetre.minsize(300,400)

# Création des champs de saisie de l'utilisateur dans la fenêtre :
# Ajout d'un texte dans la fenêtre :
altLabel = Label (fenetre, text = "Texte alternatif")
altLabel.pack()

altInput = Entry(fenetre)
altInput.pack()

urlCompressedLabel = Label (fenetre, text = "URL d'affichage")
urlCompressedLabel.pack()

urlCompressedInput = Entry(fenetre)
urlCompressedInput.pack()

urlDownloadLabel = Label (fenetre, text = "URL de téléchargement")
urlDownloadLabel.pack()

urlDownload = Entry(fenetre)
urlDownload.pack()

# Création des cases à cocher "Radiobutton" dans la fenêtre :
liste1 = Listbox (fenetre)
liste1.insert(1, "animalier")
liste1.insert(2, "macro")
liste1.insert(3, "black-and-white")
liste1.insert(4, "paysage")
liste1.pack()

# Ajout d'un bouton d'update dans la fenêtre :
btnGithub = Button(
  fenetre,
  text = "Update Github", 
  command = updateGithub
)
btnGithub.pack()

btnDeploy = Button(
  fenetre,
  text = "Update website", 
  command = updateWebsite
)
btnDeploy.pack()

btnTest = Button(
  fenetre,
  text = "Update Databases", 
  command = writeJson
)
btnTest.pack()

# Affichage de la fenêtre créée :
fenetre.mainloop()