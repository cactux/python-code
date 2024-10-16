# https://www.docstring.fr/glossaire/dictionnaire/?utm_source=udemy&utm_campaign=glossary-dictionary
films = {"Le Seigneur des Anneaux" : 12,
  "Harry Potter" : 9,
  "Blade Runner" : 7.5}
prix = 0

for film in films:
    prix += films[film]
print(prix)

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes.get("id01")["age"]
print(employes)
print(age_paul)

