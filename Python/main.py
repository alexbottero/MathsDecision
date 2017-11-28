import random
import time
from Eleve import * ;
from Projet import * ;
from Promo import * ;
from parser import *;

matrice = parseCSV("csv.csv")
taillePromo = len(matrice)

matrice[0].remove("Nom")

pTest = ['TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB', 'TB']

p = Promo(taillePromo, len(pTest), 0, 0)

num = 0;



for i in matrice[0]:	
	print("Eleve "+str(num)+" / Nom : "+str(i))#+" / Pref eleve : "+str(matrice[num+1][1:48]))
	p.ajouterEleve(num, matrice[num+1][1:48],pTest, i)
	num += 1


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
	print("preffff e : ", i.prefEleve)
	print("prefffffe trie : ", len(i.prefEleveTrie))

#Copie de la liste d'eleve dans une liste temporaire (car sinon quicksort modifie la liste)
elevesTemp = []
for i in p.eleves:
	elevesTemp.append(i)

#Calcul du classement des elves du moins aime au plus aime
p.classementEleve = p.mentionSort()
#p.mentionSort(p.classementEleve)

#On autorise 2 camarades maximum pour un eleve 
nbCamarades = 1

#Variable qui teste si la repartition est finie
end = False

################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
print("Matrice preference eleves")
#for i in p.prefEleves:
	#print(i)
#print('\n')

################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
################################## AFFICHAGE MATRICE PREF GLOBAL ##################################

print("Matrice preference projets")
#for i in p.prefProjets:
	#print(i)
print('\n')

################################## AFFICHAGE MATRICE PREF GLOBAL ##################################
################################## AFFICHAGE MATRICE PREF GLOBAL ##################################

print("Classement eleves du moins aime au plus aime")
c=1
for i in p.classementEleve:
	print(str(c)+") "+str(i.numeroEleve+1)+" / "+str(i.note)+" : "+str(i.mention)+" / Nom : "+str(i.nom))
	c += 1
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
	
	print("Critere eleve = ", p.critereE)
	print("Critere projet = ", p.critereP)

	if(not(end)): 
		#On augmente le critere de 1 s'il n'a pas atteint le max
		if(p.critereE<p.n-2):
			p.critereE+=1;
		if(p.critereP<p.p-1):
			p.critereP+=1;
		if detail:
			print("On va parcourir tout le classement des eleves, on essaye de trouver des binome (b1, b2) tel que : b1 appartient au "+str(p.critereE)+" premiers eleves les plus preferes de b2 (et vice versa)")
			print("Si on trouver deux eleves compatible, on chercher un projet tel que : projet appartient au "+str(p.critereP)+" premiers projets preferes de b1 et b2\n")
			d = raw_input("Continuer ? ")
			detail = not(d=="Non")

		for i in p.eleves:
			if(len(i.camarades)==0):
				print(i.nom)

		#On parcourt en entier le classement d'eleve pour affecter le maximum d'eleves
		for i in p.classementEleve:
			j = 0 #Variable pour parcourir les eleves preferes de i
			binome = False
			
			#S'il reste seulement 4 eleves a repartir on baisse le nombre de camarades a 1 pour former deux binome
			if(p.n-1-p.eleveRepartis==3):
			#s'il en reste deux : on les met ensembles
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
				print(dernierE)
				dernierE[0].camarades.append(dernierE[1])
				dernierE[0].camarades.append(dernierE[2])
				dernierE[1].camarades.append(dernierE[0])
				dernierE[1].camarades.append(dernierE[2])
				dernierE[2].camarades.append(dernierE[0])
				dernierE[2].camarades.append(dernierE[1])
				dernierE[0].majProjet(dernierP)
				dernierE[1].majProjet(dernierP)
				dernierE[2].majProjet(dernierP)
				dernierP.groupe.append(dernierE[0])
				dernierP.groupe.append(dernierE[1])
				dernierP.groupe.append(dernierE[2])
				p.eleveRepartis+=3

				if detail:
					msg = "Creation dernier groupe : e"+str(dernierE[0].numeroEleve+1)+", e"+str(dernierE[1].numeroEleve+1)+", p"+str(dernierP.numeroProjet+1)+"\n"
					print(msg)




			#On regarde les eleves preferes inferieur au critere d'equite SI j'ai encore besoin de camarades
			while (j<p.critereE and not(binome) and len(i.camarades)<nbCamarades and not(end) and not(p.n-p.eleveRepartis==3)):

				if detail:
					msg = str(j+1)+") Recherche d'un camarade pour e"+str(i.numeroEleve+1)+" car il a "+str(len(i.camarades))+" camarades"
					print(msg)
					d = raw_input("Continuer ? ")
					detail = not(d=="Non")

				#Recuperation du jieme eleve prefere de i
				e2 = i.prefEleveTrie[j]
				projet = False
				if detail:
					print("e"+str(e2.numeroEleve+1)+" est l'eleve prefere numero "+str(j+1)+" de e"+str(i.numeroEleve+1))
					d = raw_input("Continuer ? ")
					detail = not(d=="Non")
				
				#Si le nombre de camarades de l'eleve prefere est nul
				if(len(e2.camarades)<nbCamarades):
					if detail:
						msg = "On regarde e"+str(e2.numeroEleve+1)+" qui a "+str(len(e2.camarades))+" camarades"
						print(msg)
						d = raw_input("Continuer ? ")
						detail = not(d=="Non")

					#Si les camarades ET l'eleve i sont valide, on continue
					if (p.binomeValide(e2, i)):
						if detail:
							msg = "Test du binome : "+str(p.binomeValide(e2, i))+" avec e"+str(i.numeroEleve+1)+" et e"+str(e2.numeroEleve+1)
							print(msg)
							d = raw_input("Continuer ? ")
							detail = not(d=="Non")

						k = 0 #Variable pour se balader dans les projet
						projet = False

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
									print("p"+str(pr.numeroProjet+1)+" est le projet numero "+str(k+1)+" de l'eleve e"+str(i.numeroEleve+1))
									d = raw_input("Continuer ? ")
									detail = not(d=="Non")

							k += 1						
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
					
					if detail:
						msg = "Creation groupe : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", p"+str(pr.numeroProjet+1)
						print(msg)
						
						d = raw_input("Continuer ? ")
						detail = not(d=="Non")
					pr.groupe.append(i)
					pr.groupe.append(e2)

					#Si on devait affecter des binome vers la fin, alors on considere les deux eleves repartis
					p.eleveRepartis += 2
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
				print(p.eleveRepartis)
				print(p.n)
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
		answer +=str(j.nom)+". " 
	print(answer)
print('\n')

fin=time.time()
temps = fin-debut
print("La repartition a duree : "+str(temps)+" secondes.\n")


