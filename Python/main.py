import random
from Eleve import * ;
from Projet import * ;
from Promo import * ;

p = Promo(5, 2, 0, 0)

p.ajouterEleve(0, ['', 'T', 'P', 'P', 'AB'], ['B', 'T'])
p.ajouterEleve(1, ['B', '', 'B', 'AB', 'T'], ['AB', 'P'])
p.ajouterEleve(2, ['AB', 'P', '', 'T', 'B'], ['T', 'B'])
p.ajouterEleve(3, ['T', 'AB', 'AB', '', 'AB'], ['P', 'B'])
p.ajouterEleve(4, ['AB', 'P', 'T', 'B', ''], ['AR', 'AB'])


p.ajouterProjet(0)
p.ajouterProjet(1)

for i in p.prefEleves:
	print(i)
print('\n')

#On donne calcule la note de chaque eleve
for i in p.eleves:
	p.noteMajoritaire(i)
	i.elevePrefere(p)
	i.projetPrefere(p)

#On etablie le classement
elevesTemp = []
for i in p.eleves:
	elevesTemp.append(i)

p.classementEleve = p.quickSort(elevesTemp)

nbCamarades = 2
end = False

while((p.critereE<p.n or p.critereP<p.p) and not(end)):
	print(end)
	end = p.eleveRepartis==p.n
	if(not(end)):
		
		if(p.critereE<p.n):
			p.critereE+=1;
		if(p.critereP<p.p):
			p.critereP+=1;
		

		print("Critere Eleve = "+str(p.critereE))
		print("Critere Projet = "+str(p.critereP)+"\n")
		for i in p.classementEleve:
			j = 0
			binome = False

			

			if(p.n-p.eleveRepartis==4 and p.eleveRepartis%3==0):
				nbCamarades = 1
			elif(p.n-p.eleveRepartis==2 and p.eleveRepartis%3==0):
				end = True
				dernierE = []
				dernierP = 444
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




			
			while (j<p.critereE and not(binome) and len(i.camarades)<nbCamarades and not(end)):


				msg = "Recherche d'un pote "+str(j+1)+" pour e"+str(i.numeroEleve+1)+" car il a "+str(len(i.camarades))+" pote"
				print(msg)

				e2 = i.prefEleveTrie[j]
				projet = False
				
				if(len(e2.camarades)<nbCamarades and len(i.camarades)<nbCamarades and not(i.camarades.count(e2)>0) and not(len(e2.camarades)==1 and len(i.camarades)==1)):

					msg = "On check e"+str(e2.numeroEleve+1)+" car il a "+str(len(e2.camarades))+" pote"
					print(msg)
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
								bValide = p.binomeValide(e, i)
								bValide = p.binomeValide(i,e)
								msg = "Test du binome : "+str(p.binomeValide(e, i))+" avec e"+str(i.numeroEleve+1)+" et e"+str(e.numeroEleve+1)
								print(msg)
							else:
								bValide = p.binomeValide(e, e2)
								bValide = p.binomeValide(e2, e)
								msg = "Test du binome : "+str(p.binomeValide(e, e2))+" avec e"+str(e2.numeroEleve+1)+" et e"+str(e.numeroEleve+1)
								print(msg)
					else:
						if(len(i.camarades)==0 and len(e2.camarades)==0):
							bValide = True


					if (p.binomeValide(e2, i) and bValide):

						msg = "Oh ! C'est ok le binome : "+str(p.binomeValide(e2, i))+" avec e"+str(i.numeroEleve+1)+" et e"+str(e2.numeroEleve+1)
						print(msg)

						k = 0
						projet = False

						if(len(i.camarades)==0 and len(e2.camarades)==0):
							while(k<p.critereP and projet==False):

								pr = i.prefProjetTrie[k]
							
								if (len(pr.groupe) == 0):
									projet = p.projetValide(e2, pr)

									msg = "Initiale Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(e2.numeroEleve+1)+" : "+str(projet)
									print(msg)

								k += 1
						elif (len(i.camarades)==1):
							
							pr = i.projet
							msg = "Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(e2.numeroEleve+1)+" : "+str(projet)
							print(msg)
							projet = p.projetValide(e2, pr)
						elif (len(e2.camarades)==1):
							pr = e2.projet
							msg = "Etude du projet p"+str(pr.numeroProjet+1)+" pour e"+str(i.numeroEleve+1)+" : "+str(projet)
							print(msg)
							projet = p.projetValide(i, pr)
				else:
					print("Eleve prefere e"+str(e2.numeroEleve+1)+" deja full")

				if (projet):
					i.majProjet(pr)
					e2.majProjet(pr)
					if (len(i.camarades)==0 and len(e2.camarades)==0):
						msg = "Creation groupe : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", p"+str(pr.numeroProjet+1)
						print(msg)
						
						
						pr.groupe.append(i)
						pr.groupe.append(e2)
						p.eleveRepartis += 2

					elif (len(i.camarades)==1):
						msg = "Creation trinome : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", e"+str(i.camarades[0].numeroEleve+1)+", p"+str(pr.numeroProjet+1)
						print(msg)
				
						i.camarades[0].camarades.append(e2)
						e2.camarades.append(i.camarades[0])
						
						pr.groupe.append(e2)
						p.eleveRepartis += 1
						pr.groupe.append(e2)
					elif (len(e2.camarades)==1):
					
						msg = "Creation trinome : e"+str(i.numeroEleve+1)+", e"+str(e2.numeroEleve+1)+", e"+str(e2.camarades[0].numeroEleve+1)+", p"+str(pr.numeroProjet+1)
						print(msg)
						e2.camarades[0].camarades.append(i)
						i.camarades.append(e2.camarades[0])
						
						pr.groupe.append(i)
						p.eleveRepartis += 1
					i.camarades.append(e2)
					e2.camarades.append(i)
					binome = True
					projet = False



				else:
					j += 1
					print("Eleve suivant")
				end = p.eleveRepartis==p.n
				print("\n")
		
print("Fin repartition")

#for i in p.eleves:
#	if(len(i.camarades)>0):
#		answer = "Eleve : e"+str(i.numeroEleve+1)+" Binome : e"+str(i.camarades[0].numeroEleve+1)+" Projet : p"+str(i.projet.numeroProjet+1)
#		print(answer)
#		print('\n')

