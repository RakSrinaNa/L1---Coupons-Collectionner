import random

test = 100000 
tousLesTests = []
coupons = open("coupons.txt", "a")

for i in range(0, test):
	resultats = []
	compteur = 0
	while len(resultats) < 20:
		lance = random.randint(0,20)
		if not(lance in(resultats)):
			resultats.append(lance)
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
