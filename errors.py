a = 5
b = 0

try:
    resultat = a / b
except ZeroDivisionError:
    print("Division par 0 !")
except NameError:
    print("Pas de b")
else:
    print(resultat)
finally:
    print("Terminé")
