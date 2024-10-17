fichier = input("Fichier à ouvrir : ")
try:
    with open(fichier, "r") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier inexistant.")
except:
    print("Impossible d'ouvir ce fichier")
else:
    print(contenu)
