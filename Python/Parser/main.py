import random
import time
from Eleve import * ;
from Projet import * ;
from Promo import * ;
from Parser import *;

matrice = parseCSV("csv.csv")
taillePromo = len(matrice)
pTest = ['P','T','AB','AR','T']

p = Promo(taillePromo, len(pTest), 0, 0)

num = 0;
for i in matrice:
	print("Eleve "+str(num)+" Pref eleve : "+str(i))
	p.ajouterEleve(num, i,pTest)
	num += 1

################################## AJOUT ELEVES ##################################
################################## AJOUT ELEVES ##################################

#p.ajouterEleve(0, [''], ['B'])

#p.ajouterEleve(0, ['', 'AB'], ['B'])
#p.ajouterEleve(1, ['T', ''], ['AR'])

#p.ajouterEleve(0, ['', 'P', 'AB'], ['T'])
#p.ajouterEleve(1, ['AB', '', 'T'], ['AB'])
#p.ajouterEleve(2, ['AB', 'P', ''], ['AR'])

#p.ajouterEleve(0, ['', 'P', 'AB', 'AR'], ['P', 'B'])
#p.ajouterEleve(1, ['T', '', 'AB', 'B'], ['T', 'B'])
#p.ajouterEleve(2, ['T', 'AB', '', 'P'], ['P', 'AR'])
#p.ajouterEleve(3, ['B', 'AB', 'AB', ''], ['AB', 'B'])

#p.ajouterEleve(0, ['', 'P', 'AB', 'AR', 'T'], ['P', 'B'])
#p.ajouterEleve(1, ['T', '', 'AB', 'B', 'T'], ['T', 'B'])
#p.ajouterEleve(2, ['T', 'AB', '', 'P', 'AR'], ['P', 'AR'])
#p.ajouterEleve(3, ['B', 'AB', 'AB', '', 'B'], ['AB', 'B'])
#p.ajouterEleve(4, ['B', 'AB', 'AB', 'T', ''], ['P', 'AR'])

#p.ajouterEleve(0, ['', 'P', 'AB', 'AR', 'T', 'B'], ['P', 'B'])
#p.ajouterEleve(1, ['T', '', 'AB', 'B', 'T', 'AR'], ['T', 'B'])
#p.ajouterEleve(2, ['T', 'AB', '', 'P', 'AR', 'B'], ['P', 'AR'])
#p.ajouterEleve(3, ['B', 'AB', 'AB', '', 'B', 'T'], ['AB', 'B'])
#p.ajouterEleve(4, ['B', 'AB', 'AB', 'T', '', 'AR'], ['P', 'AR'])
#p.ajouterEleve(5, ['T', 'T', 'P', 'P', 'AB', ''], ['B', 'T'])

#p.ajouterEleve(0, ['', 'P', 'AB', 'AR', 'T', 'B'], ['P', 'B', 'T'])
#p.ajouterEleve(1, ['T', '', 'AB', 'B', 'T', 'AR'], ['T', 'B', 'AB'])
#p.ajouterEleve(2, ['T', 'AB', '', 'P', 'AR', 'B'], ['P', 'AR', 'B'])
#p.ajouterEleve(3, ['B', 'AB', 'AB', '', 'B', 'T'], ['AB', 'B', 'T'])
#p.ajouterEleve(4, ['B', 'AB', 'AB', 'T', '', 'AR'], ['P', 'AR', 'B'])
#p.ajouterEleve(5, ['T', 'T', 'P', 'P', 'AB', ''], ['B', 'T', 'AB'])

################################## AJOUT PROJET ##################################
################################## AJOUT PROJET ##################################
for i in range(0,len(pTest)):
	p.ajouterProjet(i)

################################## INITIALISATION ELEVES ##################################
################################## INITIALISATION ELEVES ##################################

for i in p.eleves:
	p.noteMajoritaire2(i)
	i.elevePrefere(p) #Trie les eleves prefere de i dans l'ordre (plus prefere -> moins prefere)
	i.projetPrefere(p) #Trie les projets prefere de i dans l'ordre (plus prefere -> moins prefere)

#Copie de la liste d'eleve dans une liste temporaire (car sinon quicksort modifie la liste)
elevesTemp = []
for i in p.eleves:
	elevesTemp.append(i)

#Calcul du classement des elves du moins aime au plus aime
p.classementEleve = p.quickSort(elevesTemp)
p.mentionSort(p.classementEleve)

#On autorise 2 camarades maximum pour un eleve 
nbCamarades = 2

#Variable qui teste si la repartition est finie
end = False

################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
print("Matrice preference eleves")
for i in p.prefEleves:
	print(i)
print('\n')

################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
################################## AFFICHAGE MATRICE PREF GLOBAL ##################################

print("Matrice preference projets")
for i in p.prefProjets:
	print(i)
print('\n')

################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
################################## AFFICHAGE MATRICE PREF GLOBAL ##################################

print("Classement eleves du moins aime au plus aime")
c=1
for i in p.classementEleve:
	print(str(c)+") "+str(i.numeroEleve+1)+" / "+str(i.note)+" : "+str(i.mention))
print('\n')

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

#Temps de debut
debut=time.time()

#Tant que le critere d'equite n'a pas etait etendu au maximum on cherche
while((p.critereE<p.n or p.critereP<p.p) and not(end)):
	if detail:
		print("Fin repartition ? "+str(end)+"\n")
	end = p.eleveRepartis==p.n #Si on a repartie tout les eleves alors : fin
	

	if(not(end)): 
		#On augmente le critere de 1 s'il n'a pas atteint le max
		if(p.critereE<p.n):
			p.critereE+=1;
		if(p.critereP<p.p):
			p.critereP+=1;
		if detail:
			print("Critere Eleve = "+str(p.critereE))
			print("Critere Projet = "+str(p.critereP)+"\n")

		#On parcourt en entier le classement d'eleve pour affecter le maximum d'eleves
		for i in p.classementEleve:
			j = 0 #Variable pour parcourir les eleves preferes de i
			binome = False
			
			#S'il reste seulement 4 eleves a repartir on baisse le nombre de camarades a 1 pour former deux binome
			if(p.n-p.eleveRepartis==4 and p.eleveRepartis%3==0):
				nbCamarades = 1
			elif(p.n-p.eleveRepartis==2 and p.eleveRepartis%3==0 and not(p.n%5==0)): #s'il en reste deux : on les met ensembles
				end = True
				dernierE = []
				dernierP = -1

				#on recupere les deux dernier eleves qui n'ont aucun camarades
				for x in p.eleves:
					if(len(x.camarades)==0):
						dernierE.append(x)
				for y in p.projets:
					if(len(y.groupe)==0):
						dernierP=y

				dernierE[0].camarades.append(dernierE[1])
				dernierE[1].camarades.append(dernierE[0])
				dernierE[0].majProjet(dernierP)
				dernierE[1].majProjet(dernierP)
				dernierP.groupe.append(dernierE[0])
				dernierP.groupe.append(dernierE[1])
				p.eleveRepartis+=2
				if detail:
					msg = "Creation dernier groupe : e"+str(dernierE[0].numeroEleve+1)+", e"+str(dernierE[1].numeroEleve+1)+", p"+str(dernierP.numeroProjet+1)+"\n"
					print(msg)




			#On regarde les eleves preferes inferieur au critere d'equite SI j'ai encore besoin de camarades
			while (j<p.critereE-1 and not(binome) and len(i.camarades)<nbCamarades and not(end)):

				if detail:
					msg = str(j+1)+") Recherche d'un camarade pour e"+str(i.numeroEleve+1)+" car il a "+str(len(i.camarades))+" camarades"
					print(msg)

				#Recuperation du jieme eleve prefere de i
				e2 = i.prefEleveTrie[j]
				projet = False
				
				#Si le nombre de camarades des deux eleves permet un groupe de 3 (ou 2 si on arrive a la fin) on continue
				if(len(e2.camarades)<nbCamarades and len(i.camarades)<nbCamarades and not(i.camarades.count(e2)>0) and not(len(e2.camarades)==1 and len(i.camarades)==1)):
					if detail:
						msg = "On regarde e"+str(e2.numeroEleve+1)+" qui a "+str(len(e2.camarades))+" camarades"
						print(msg)

					#Si l'un des deux a deja des camarades, on verifie que tous les camarades sont compatibles avec l'eleve prefere
					if(not(nbCamarades==4)):
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

						k = 0 #Variable pour se balader dans les projet
						projet = False

						#Si aucun n'a de camarades => aucun n'a de projet, on recherche un projet commun valide
						if(len(i.camarades)==0 and len(e2.camarades)==0):
							while(k<p.critereP and projet==False):
								
								pr = i.prefProjetTrie[k] #on recupere projet prefere i
								if (len(pr.groupe) == 0): #S'il n'a personne d'affecter on regarde s'i lest valide
									projet = p.projetValide(e2, pr)
									if detail:
										msg = "Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(e2.numeroEleve+1)+" : "+str(projet)
										print(msg)

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

				else:
					if detail:
						print("Eleve e"+str(e2.numeroEleve+1)+" possede deja "+str(len(e2.camarades))+" camarades")
				#Si le projet convient alors on peut affecter les eleves
				if (projet):
					#On Sauvegarde le projet pour les deux eleves
					i.majProjet(pr)
					e2.majProjet(pr)

					#Si on creer un binome alors on sauvegarde le binome dans le projet
					if (len(i.camarades)==0 and len(e2.camarades)==0):
						if detail:
							msg = "Creation groupe : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", p"+str(pr.numeroProjet+1)
							print(msg)
						pr.groupe.append(i)
						pr.groupe.append(e2)

						#Si on devait affecter des binome vers la fin, alors on considere les deux eleves repartis
						if(p.p-p.eleveRepartis==4):
							p.eleveRepartis += 2

					#Si i avait un camarades, on sauvegarde juste l'eleve prefere dans le projet
					elif (len(i.camarades)==1):
						if detail:
							msg = "Creation trinome : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", e"+str(i.camarades[0].numeroEleve+1)+", p"+str(pr.numeroProjet+1)
							print(msg)
				
						i.camarades[0].camarades.append(e2)
						e2.camarades.append(i.camarades[0])						
						pr.groupe.append(e2)
						p.eleveRepartis += 3

					#Si l'eleve prefere avait un cmarades, on sauvegarde juste i dans le projet
					elif (len(e2.camarades)==1):
						if detail:
							msg = "Creation trinome : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", e"+str(e2.camarades[0].numeroEleve+1)+", p"+str(pr.numeroProjet+1)
							print(msg)
						e2.camarades[0].camarades.append(i)
						i.camarades.append(e2.camarades[0])
						pr.groupe.append(i)
						p.eleveRepartis += 3

					#on met a jour les camarades
					i.camarades.append(e2)
					e2.camarades.append(i)
					binome = True
					projet = False
				else:
					if detail:
						print("Creation invalide\n")
						print("Eleve suivant")
					j += 1						

				end = p.eleveRepartis==p.n
				if detail:
					print("\n")
		

################################## FIN ALGO ##################################
################################## FIN ALGO ##################################
#Affichage

print("Fin repartition\n")
print("REPARTITION\n")
for i in p.projets:
	answer = "Projet : p"+str(i.numeroProjet+1)+". Eleve : "
	for j in i.groupe:
		answer += "e"+str(j.numeroEleve+1)+". " 
	print(answer)
print('\n')

fin=time.time()
temps = fin-debut
print("La repartition a duree : "+str(temps)+" secondes.\n")


