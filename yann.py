chemin = "./toto.txt"

with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    print(contenu)
