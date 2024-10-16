import random

MAX_NB = 100
vies = 5
nombre = int(MAX_NB * random.random())
# print(nombre)

while vies > 0:
    print(f"Il vous reste {vies} essais.")
    essai = input("Entrez un nombre : ")
    if essai.isdigit():
        essai = int(essai)
        vies -= 1
        if essai == nombre:
            print("Vous avez trouvé bravo !")
            vies = 0
        elif essai < nombre and vies > 0:
            print("Trop petit, essaie plus grand")
        elif essai > nombre and vies > 0:
            print("Trop grand, essaie plus petit")
        else:
            print(f"Perdu, le nombre était {nombre}")
    else:
        print("C'est un nombre qu'il faut entrer !")
        continue
print("Fin")
