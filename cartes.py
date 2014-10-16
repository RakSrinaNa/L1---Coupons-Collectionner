import random

nombreCartes = 54 #Nombre de cartes dans le paquet
cartes = [] #Variable contenant le jeu de cartes
results = [] #Variable contenant les differents resultats obtenus
nombreMelanges = 10000 #Nombre de repetitions de l'operation
while len(results) < nombreMelanges:
	compteur = 0
	cartes = []
	for i in range(nombreCartes): #Initialisation du paquet
		cartes.append(i)
	while cartes[-1] != 0: #Tant que la carte du dessous n'est pas au dessus
		pos = random.randint(0, nombreCartes - 1) #Choix de la position d'insertion de la carte du dessus
		cartes.insert(pos, cartes[-1]) #Insertion de la carte a la position choisie
		cartes.pop(-1) #Suppresion de la carte replacee du dessus du paquet
		compteur += 1
	results.append(compteur)
	print(compteur)
moyenne = 0.0
for i in results:
	moyenne += i
moyenne /= nombreMelanges
print(">> " + str(moyenne))
