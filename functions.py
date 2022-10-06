# fonction d'update
import os

def update():
    os.system("git add .")
    os.system("git commit -m 'Mise à jour de la BDD'")
    os.system("git push origin main")

