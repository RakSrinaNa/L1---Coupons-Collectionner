import random

tailleDeck = 20 #Taille du deck a obtenir
nombreTests = 100000 #Nombre de test a effectuer
resultats = [] #Variable contenant les differents resultats obtenus

for i in range(0, nombreTests):
	deck = []
	compteur = 0
	while len(deck) < tailleDeck: #Tant que notre deck n'est pas complet
		lance = random.randint(0,tailleDeck) #On obtient un coupon au hasard
		if not(lance in(deck)): #Si le coupon n'est pas deja possede
			deck.append(lance)
		compteur += 1
	resultats.append(compteur)
	print(str(compteur))

moyenne = 0.0
for i in resultats:
	moyenne += i
moyenne /= nombreTests
print(">> " + str(moyenne))
