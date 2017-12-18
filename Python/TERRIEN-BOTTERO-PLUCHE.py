import random
import time
import sys
from Eleve import * ;
from Projet import * ;
from Promo import * ;
from Parser import *;
from Affichage import *;

print "\nDEBUT DU PROGRAMME\n"

# Recuperation du csv entre en ligne de commande
print "PARSER CSV"
csv = str(sys.argv[1])
matrice = parseCSV(csv)
matrice[0].remove("Nom")
print "PARSER CSV completed\n"

prefProjetTB = ['TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB']

print "INITIALISATION DONNEES"
# Initialisation des donnees de la promo
nbEleves = len(matrice[0])
nbProjets = len(prefProjetTB)
critereEleveInitial = 0
citereProjetInitial = 0

# Creation d'une promo
p = Promo(nbEleves, nbProjets, critereEleveInitial, citereProjetInitial)

################################## AJOUT LISTE ELEVES ##################################
################################## AJOUT LISTE ELEVES ##################################

numero = 0;
for i in matrice[0]:	
	prefEleveCsv = matrice[numero+1][1:48]
	p.ajouterEleve(numero, prefEleveCsv, prefProjetTB, i)
	numero += 1
	
################################## AJOUT PROJET ##################################
################################## AJOUT PROJET ##################################

for i in range(0,len(prefProjetTB)):
	p.ajouterProjet(i)

################################## INITIALISATION ELEVES ##################################
################################## INITIALISATION ELEVES ##################################

for i in p.eleves:
	p.noteMajoritaire(i)
	#Trie les eleves prefere de i dans l'ordre (plus prefere -> moins prefere)
	i.elevePrefere(p) 
	#Trie les projets prefere de i dans l'ordre (plus prefere -> moins prefere)
	i.projetPrefere(p) 

#Calcul du classement des elves du moins aime au plus aime
p.classementEleve = p.trieEleve()
#p.mentionSort(p.classementEleve)

#On autorise 2 camarades maximum pour un eleve 
nbCamarades = 2

#Calcul du nombre de trinome a former
nbTrinome = 0
nbTrinomeMax = p.calculNbTrinome()

#Variable qui teste si la repartition est finie
end = False

print "INITIALISATION DES DONNEES completed\n"
################################## AFFICHAGE ##################################
################################## AFFICHAGE ##################################
print "Taille de la promo : ", p.n
print "Nombre de trinome necessaire : ", nbTrinomeMax, "\n"

affichageEleves(matrice, prefProjetTB)
affichageMatrice(p.prefEleves, "eleves")
affichageMatrice(p.prefProjets, "projets")
affichageClassement(p)

################################## DEBUT ALGO ##################################
################################## DEBUT ALGO ##################################

if(p.n<4):
	for z in p.eleves:
		for j in p.eleves:
			z.camarades.append(j)
		z.majProjet(p.projets[0])
		p.projets[0].groupe.append(z)
		end=True

d = raw_input("Voulez-vous les details de la repartition (Oui/Non) ? ")
detail = (d=="Oui")
#a = raw_input("Voulez-vous les creations de binomes et trinomes (Oui/Non) ? ")
creation = (False)

#Temps de debut
debut=time.time()

#Tant que le critere d'equite n'a pas etait etendu au maximum on cherche
while((p.critereE<p.n or p.critereP<p.p) and not(end)):

	end = p.eleveRepartis==p.n #Si on a repartie tout les eleves alors : fin

	if(not(end)): 
		#On augmente le critere de 1 s'il n'a pas atteint le max
		if(p.critereE<p.n-2):
			p.critereE+=1;
		if(p.critereP<p.p-1):
			p.critereP+=1;
		if detail:
			print "\nMETHODE DE L'ALGORITHME\n"
			print "A chaque tour de l'algorithme, nous parcourons tout le classement d'eleves ET nous formons des binomes qui respecte un critere particulier.\n"
			print "Ce critere est un entier, initialement egal a 1, qui augmente a chaque tour.\n"
			print "EXEMPLE : Critere = 12, alors deux eleves (e1, e2) forment un binome SI :\n"
			print "                 e1 appartient au 12 premiers eleves preferes de e2\n"
			print "                 e2 appartient au 12 premiers eleves preferes de e1\n"
			print "Comme nous savons combien de trinomes nous devons former, lorsque l'on etudie la compatibilite de deux eleves, si l'un deux possede deja un binome on essaye alors de former un trinome qui respecte le critere decrit juste avant.\n"

			d = raw_input("Continuer ? ")
			detail = not(d=="Non")

		#for i in p.eleves:
			#if(len(i.camarades)==0):
				#print(i.nom)

		#On parcourt en entier le classement d'eleve pour affecter le maximum d'eleves
		for i in p.classementEleve:
			j = 0 #Variable pour parcourir les eleves preferes de i
			binome = False

			if(nbTrinome == nbTrinomeMax):
				nbCamarades = 1
			
			#S'il reste seulement 4 eleves a repartir on baisse le nombre de camarades a 1 pour former deux binome
			if(p.n-p.eleveRepartis==1 and nbTrinome<nbTrinomeMax):
			#s'il en reste deux : on les met ensembles
				
				dernierE = []
				dernierP = -1

				#on recupere les deux dernier eleves qui n'ont aucun camarades
				for x in p.eleves:
					if(len(x.camarades)==0):
						dernierE.append(x)
				#for y in p.projets:
				#	if(len(y.groupe)==0):
				#		dernierP=y
				if detail:
					print " Dernier Eleve trouves : ",dernierE[0].nom
					d = raw_input("Continuer ? ")
					detail = not(d=="Non")
				while not(end) and p.critereE<p.n:
					for u in range(0,len(dernierE[0].prefEleveTrie)):
						y = dernierE[0].elevePrefereRandom(u)
						if(p.binomeValide(y,dernierE[0]) and len(y.camarades)<2 and len(dernierE[0].camarades)<2 and not(end)):
							for o in y.camarades:
								valid = p.binomeValide(o,dernierE[0])
							if valid:
								dernierE[0].camarades.append(y)
								y.camarades.append(dernierE[0])
								dernierE[0].majProjet(y.projet)
								y.projet.groupe.append(dernierE[0])
								end = True
					p.critereE+=1
					


					p.eleveRepartis+=1

				if creation and end:
					msg = "Creation dernier groupe : e"+str(dernierE[0].numeroEleve+1)+", e"+str(dernierE[0].numeroEleve+1)+", p"+str(dernierP.numeroProjet+1)+"\n"
					print(msg)
					d = raw_input("Continuer ? ")
					creation = not(d=="Non")




			#On regarde les eleves preferes inferieur au critere d'equite SI j'ai encore besoin de camarades
			while (j<p.critereE and not(binome) and len(i.camarades)<nbCamarades and not(end)):

				if detail:
					msg = str(j+1)+") Recherche d'un camarade pour e"+str(i.numeroEleve+1)+" car il a "+str(len(i.camarades))+" camarades"
					print(msg)
					d = raw_input("Continuer ? ")
					detail = not(d=="Non")

				#Recuperation du jieme eleve prefere de i
				e2 = i.elevePrefereRandom(j)
				projet = False
				if detail:
					print("e"+str(e2.numeroEleve+1)+" est l'eleve prefere numero "+str(j+1)+" de e"+str(i.numeroEleve+1))
					d = raw_input("Continuer ? ")
					detail = not(d=="Non")
				
				#Si le nombre de camarades de l'eleve prefere est nul
				if(len(e2.camarades)<nbCamarades and not(i.camarades.count(e2)>0) and not(len(e2.camarades)==1 and len(i.camarades)==1)):
					if detail:
						msg = "On regarde e"+str(e2.numeroEleve+1)+" qui a "+str(len(e2.camarades))+" camarades"
						print(msg)
						d = raw_input("Continuer ? ")
						detail = not(d=="Non")

					#Si l'un des deux a deja des camarades, on verifie que tous les camarades sont compatibles avec l'eleve prefere
					if(not(nbCamarades==1)):
						if(len(i.camarades)==0):
							eTest = e2.camarades
							iTest = True
						elif (len(e2.camarades)==0):
							eTest = i.camarades
							iTest = False
						bValide = True
						for e in eTest:
							if (iTest):
								bValide = p.binomeValide(e, i) and p.binomeValide(i,e)
								if detail:
									msg = "Test du binome : "+str(p.binomeValide(e, i))+" avec e"+str(i.numeroEleve+1)+" et e"+str(e.numeroEleve+1)
									print(msg)
							else:
								bValide = p.binomeValide(e, e2) and p.binomeValide(e2, e)
								if detail:
									msg = "Test du binome : "+str(p.binomeValide(e, e2))+" avec e"+str(e2.numeroEleve+1)+" et e"+str(e.numeroEleve+1)
									print(msg)
					else:
						if(len(i.camarades)==0 and len(e2.camarades)==0):
							bValide = True

					#Si les camarades ET l'eleve i sont valide, on continue
					if (p.binomeValide(e2, i) and bValide):
						if detail:
							msg = "Test du binome : "+str(p.binomeValide(e2, i))+" avec e"+str(i.numeroEleve+1)+" et e"+str(e2.numeroEleve+1)
							print(msg)
							d = raw_input("Continuer ? ")
							detail = not(d=="Non")

						k = 0 #Variable pour se balader dans les projet
						projet = False

						if(len(i.camarades)==0 and len(e2.camarades)==0):
							#Si aucun n'a de camarades => aucun n'a de projet, on recherche un projet commun valide
							while(k<p.critereP and projet==False):
								pr = i.prefProjetTrie[k] #on recupere projet prefere i
								if detail:
									print("p"+str(pr.numeroProjet+1)+" est le projet numero "+str(k+1)+" de l'eleve e"+str(i.numeroEleve+1))
									d = raw_input("Continuer ? ")
									detail = not(d=="Non")
								if (len(pr.groupe) == 0): #S'il n'a personne d'affecter on regarde s'i lest valide
									projet = p.projetValide(e2, pr)
									if detail:
										msg = "Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(e2.numeroEleve+1)+" : "+str(projet)
										print(msg)
										d = raw_input("Continuer ? ")
										detail = not(d=="Non")

								k += 1
						elif (len(i.camarades)==1): #Si i a deja un projet, on regarde s'il plait a l'eleve prefere
							pr = i.projet
							projet = p.projetValide(e2, pr)
							if detail:
								msg = "Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(e2.numeroEleve+1)+" : "+str(projet)
								print(msg)

						elif (len(e2.camarades)==1): #Si l'eleve prefere a deja un projet, on regarde s'il plait a l'eleve i
							pr = e2.projet
							projet = p.projetValide(i, pr)
							if detail:
								msg = "Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(i.numeroEleve+1)+" : "+str(projet)
								print(msg)						
					else:
						if detail:
							msg = "Test du binome : "+str(p.binomeValide(e2, i))+" avec e"+str(i.numeroEleve+1)+" et e"+str(e2.numeroEleve+1)
							print(msg)
							d = raw_input("Continuer ? ")
							detail = not(d=="Non")

				else:
					if detail:
						print("Eleve e"+str(e2.numeroEleve+1)+" possede deja "+str(len(e2.camarades))+" camarades")
						
						d = raw_input("Continuer ? ")
						detail = not(d=="Non")
				#Si le projet convient alors on peut affecter les eleves
				if (projet):
					#On Sauvegarde le projet pour les deux eleves
					i.majProjet(pr)
					e2.majProjet(pr)

					#Si on creer un binome alors on sauvegarde le binome dans le projet
					if (len(i.camarades)==0 and len(e2.camarades)==0):
						p.eleveRepartis += 2

						if creation:
							msg = "Creation groupe : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", p"+str(pr.numeroProjet+1)
							print(msg)						
							d = raw_input("Continuer ? ")
							creation = not(d=="Non")
						pr.groupe.append(i)
						pr.groupe.append(e2)

					#Si i avait un camarades, on sauvegarde juste l'eleve prefere dans le projet
					elif (len(i.camarades)==1):
						if creation:
							msg = "Creation trinome : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", e"+str(i.camarades[0].numeroEleve+1)+", p"+str(pr.numeroProjet+1)
						
							d = raw_input("Continuer ? ")
							creation = not(d=="Non")
				
						i.camarades[0].camarades.append(e2)
						e2.camarades.append(i.camarades[0])						
						pr.groupe.append(e2)
						p.eleveRepartis += 1
						nbTrinome += 1

					#Si l'eleve prefere avait un cmarades, on sauvegarde juste i dans le projet
					elif (len(e2.camarades)==1):
						if creation:
							msg = "Creation trinome : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", e"+str(e2.camarades[0].numeroEleve+1)+", p"+str(pr.numeroProjet+1)
							print(msg)
							d = raw_input("Continuer ? ")
							creation = not(d=="Non")
						e2.camarades[0].camarades.append(i)
						i.camarades.append(e2.camarades[0])
						pr.groupe.append(i)
						p.eleveRepartis += 1
						nbTrinome += 1

					#on met a jour les camarades
					i.camarades.append(e2)
					e2.camarades.append(i)
					binome = True
					projet = False
				else:
					if detail:
						print("Creation invalide\n")
						print("Eleve suivant")
						
						d = raw_input("Continuer ? ")
						detail = not(d=="Non")
					j += 1						

				end = p.eleveRepartis==p.n
				
				if detail:
					print("\n")
	if detail:
		print("Fin repartition ? "+str(end)+"\n")
		d = raw_input("Continuer ? ")
		detail = not(d=="Non")

		

################################## FIN ALGO ##################################
################################## FIN ALGO ##################################
#Affichage

print("Fin repartition\n")

repartition = []
for i in p.projets:
	repartition.append(i.groupe)

writeCsv2("GROUPES.csv", repartition)

print("REPARTITION\n")
for i in p.projets:
	answer = "Projet : p"+str(i.numeroProjet+1)+". Eleve : "
	for j in i.groupe:
		answer +=str(j.nom)+". " 
	print(answer)
print('\n')

fin=time.time()
temps = fin-debut
print("La repartition a duree : "+str(temps)+" secondes.\n")


###################### Satisfaction ######################
###################### Satisfaction ######################

eleveHeureux = 0
p.critereE = 1
for i in p.eleves:
	for j in i.camarades:
		heureux = p.binomeValide(i,j)
	if heureux:
		eleveHeureux += 1
ratio = (eleveHeureux*100/p.n)
print "Nombre eleves satisfaits : ", eleveHeureux, " sur ", p.n, " elves."
print "Pourcentage de satisfaction : ", ratio, "%."
