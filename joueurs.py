import random

test = 100000
nbreDeJoueurs = 50
nbreCartes = 1
tousLesTests = []
coupons = open("joueurs.txt", "a")

for i in range(0, test):
	resultats = []
	compteur = 0
	while len(resultats) < nbreDeJoueurs:
		lances = []
		while len(lances) < nbreCartes:
			l = random.randint(0,nbreDeJoueurs)
			if(not(l in(lances))):
				lances.append(l)
		for l in lances:
			if not(l in(resultats)):
				resultats.append(l)
		compteur += 1
	tousLesTests.append(compteur)
	print(str(compteur))
	coupons.write(str(compteur) + "\n")

coupons.close()

moyenne = 0.0
for i in tousLesTests:
	moyenne += i
moyenne /= test
print(">> " + str(moyenne))
