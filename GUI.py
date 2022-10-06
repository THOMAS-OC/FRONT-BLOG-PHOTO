# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
import os

# fonction d'update
def update():
    os.system("git add .")
    os.system("git commit -m 'Mise à jour de la BDD'")
    os.system("git push origin main")

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
altLabel = Label (fenetre, text = "Texte décrivant l'image")
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
bouton1 = Button (fenetre, text = "mise à jour BDD")
btn = Button(
  fenetre,
  text = "Cliquez ici!", 
  command = update()
)
bouton1.pack()

# Affichage de la fenêtre créée :
fenetre.mainloop()