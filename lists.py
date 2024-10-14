def creer_liste(N):
	i = 0
	liste = []
	while i < N:
		element = input("Entrez un element : ")
		liste.append(element)
		i += 1
	return liste

liste = creer_liste(3)

print("La liste créée : ")
print(liste)
