# https://www.docstring.fr/blog/gerer-des-chemins-de-fichiers-avec-pathlib/
# === Créer le fichier prenoms.txt :
# Charlotte, Raphaël,  Jade, Justin, Zoe Jeanne, Elsa
# Mathis, Sara, David. Chloe, Ludovic, Nicolas, Léo, Mathieu, Charles, Apolline, Noemie, Heloïse, Anaïs, Philippe, Antoine, Lina, Laura
# Pauline, Simon
# Maxime, Victoire, Noah,
# Emilie, Gabrielle, Louise, Nathan, Logan, Margaux, Clemence, Inès, Tommy, Isaac, Malik, Yasmine, Lena, Juliette, Eva, Elisa, Lisa, Salome, Ambre, Emma, Marie, Maya, Dylan, Mathilde, Noa, Christopher, Anna, Alexis, Elise, Guillaume, Adam, Alexandre, Victor, Sarah, Lou, Lucas, Lola, Victoria, Capucine, Jonathan, Clara, Camille, Lea, Félix, Gabriel, Cédric, Josephine, Alex, Sofia, Benjamin, Loïc, Thomas, Elliot, Romane, Agathe, Alix, Manon, Vincent, Alice, Samuel, Hugo, Diane, Julien, Jacob, Margot, Nina, Valentine, Rose, Jérémy, Julie, Anthony, Julia, Tristan
#  Olivier, Louis, Adèle, Michaël, Lucie,
# ===

prenoms = []
with open("prenoms.txt", "r") as f:
    contenu = f.read()
    prenoms1 = contenu.split()
    for prenom in prenoms1:
        prenom = prenom.strip(" ,.")
        # print(prenom)
        prenoms.append(prenom)
prenoms.sort()
with open("prenoms_triés.txt", "a") as f:
    for prenom in prenoms:
        f.write(f"{prenom}\n")
