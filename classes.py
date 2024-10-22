class Fichier:
    nom = "fichier"
    extension = "txt"
    taille = "1000"

fichier_01 = Fichier()
print(fichier_01.nom)
fichier_01.nom = "toto"
print(fichier_01.nom)
Fichier.nom = "titi"
print(fichier_01.nom)
fichier_02 = Fichier()
print(fichier_02.nom)
