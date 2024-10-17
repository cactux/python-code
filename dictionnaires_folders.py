from pathlib import Path

chemin = "/home/f292871/dev/python-code/dossier_test"
    
d = {"Films": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
        "Employes": ["Paul",
                    "Pierre",
                    "Marie"],
        "Exercices": ["les_variables",
                    "les_fichiers",
                    "les_boucles"]}
p = Path(chemin)
print(d)

if p.is_dir():
    print("===== Création de l'arborescence =====")
    for l1 in d:
        dossier = p / l1
        dossier.mkdir(exist_ok=True)
        for l2 in d[l1]:
            dossier2 = dossier / l2
            dossier2.mkdir(exist_ok=True)
            print(f" - {l1} - {l2}")
