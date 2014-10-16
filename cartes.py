import random

nombreCartes = 54
cartes = []
results = []
coups = 10000
while len(results) < coups:
	compteur = 0
	cartes = []
	for i in range(nombreCartes):
		cartes.append(i)
	while cartes[-1] != 0:
		pos = random.randint(0, nombreCartes - 1)
		cartes.insert(pos, cartes[-1])
		cartes.pop(-1)
		compteur += 1
	results.append(compteur)
	print(compteur)
moyenne = 0.0
for i in results:
	moyenne += i
moyenne /= coups
print(">> " + str(moyenne))
