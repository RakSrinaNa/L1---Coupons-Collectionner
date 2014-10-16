import random

nombreTests = 100000 #Nombre de tests a effectuer
nombreDeJoueurs = 50 #Nombre de joueurs constituant un deck complet
nombreCartes = 1 #Nombre de cartes par paquet
resultats = [] #Variable contenant les differents resultats obtenus

for i in range(0, nombreTests):
	deck = []
	compteur = 0
	while len(deck) < nombreDeJoueurs: #Tant que le deck n'est pas complet
		lances = []
		while len(lances) < nombreCartes: #Creation du packet achete a nombreCartes cartes, sans doublons
			l = random.randint(0,nombreDeJoueurs)
			if(not(l in(lances))):
				lances.append(l)
		for l in lances:
			if not(l in(deck)): #Si la carte n'est pas deja possedee
				deck.append(l)
		compteur += 1
	resultats.append(compteur)
	print(str(compteur))


moyenne = 0.0
for i in resultats:
	moyenne += i
moyenne /= nombreTests
print(">> " + str(moyenne))
