import math

def creer_liste(N):
	i = 0
	liste = []
	while i < N:
		element = input("Entrez un element : ")
		liste.append(element)
		i += 1
	return liste

# ~ liste = creer_liste(3)

# ~ print("La liste créée : ")
# ~ print(liste)

liste = [1, -3, 5, 1, 6, 5, 5, 2]
def compte(e, L):
	i=0
	for element in L:
		if element == e:
			i+=1
	return i

# ~ n=compte(5, liste)
# ~ print(n)

def Echange(L,i,j):
	tmp = L[i]
	L[i] = L[j]
	L[j] = tmp
	return L

# ~ print("Liste avant :")
# ~ print(liste)
# ~ liste = Echange(liste, 1, 2)
# ~ print("Liste après :")
# ~ print(liste)

def lmult(k,n):
	for i in range(n):
		print(k*(i+1))

# ~ lmult(50,50)

def estpremier(p):
	if p == 1 or p == 2:
		return True
	n=2
# 	print(math.sqrt(p))
	while n < math.sqrt(p):
		if p % n == 0:
			return False
		n+=1
	return True

# myp = input("Entrez un entier à tester : ")
# myp = int(myp)
# print(estpremier(myp))
# 
# for i in range(100):
# 	print(i, ":", estpremier(i))

def liste_prem(N):
	for i in range(N):
# 		print(i)
		if estpremier(i):
			print(i)

# N = input("Entiers jusqu'à ?")
# N = int(N)
# liste_prem(N)

def Fibo(N):
	if N == 0:
		return 0
	if N == 1:
		return 1
	fibo1 = 0
	fibo2 = 1
	for i in range(2, N+1):
		fibo = fibo1 + fibo2
		fibo1 = fibo2
		fibo2 = fibo
	return fibo

# N = input("Fibonacci")
# print(Fibo(int(N)))
# for i in range(100):
# 	print(Fibo(i))

def U(N):
	return (1+1/N)**N

def listeU(n):
	for i in range(n):
		print(U(i+1))

# ~ N = input("N ?")
# ~ print(listeU(int(N)))

def doublon(liste1):
	i = 1
	liste2 = []
	liste2.append(liste1[0])
	while i < len(liste1):
		# ~ print("liste1", i, "=", liste1[i])
		j = 0
		trouve = 0
		while j < len(liste2):
			# ~ print("    liste2", j, "=", liste2[j])
			if liste1[i] == liste2[j]:
				trouve = 1
				break
			j += 1
		if trouve == 0:
			liste2.append(liste1[i])
		i += 1
	return liste2

def compte_elem(L):
		compte_elem = []
		L_simple = doublon(L)
		L_retour = []
		for i in range(len(L_simple)):
			print("i = ", i)
			print(L[i])
			print(compte(L_simple[i], L))
			print("")
			L_retour.append((L_simple[i],compte(L_simple[i], L)))
		return L_retour

liste = [1, -3, 5, 1, 6, 5, 5, 2]
print(liste)
print(doublon(liste))
print(compte_elem(liste))

