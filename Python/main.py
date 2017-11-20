import random
from Eleve import * ;
from Projet import * ;
from Promo import * ;

p = Promo(4, 2)

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

for i in p.classementEleve:
	j = 0
	binome = False
	
	while (j<len(i.prefEleve)-1 and binome==False):
		
		e2 = i.prefEleveTrie[j]
		
		if(len(e2.camarades) == 0 and len(i.camarades) == 0):
			if (p.binomeValide(e2, i)):

				k = 0
				projet = False

				while(k<len(i.prefProjetTrie) and projet==False):

					pr = i.prefProjetTrie[k]
					if (len(pr.groupe) == 0):
						print(len(pr.groupe))
						print(pr.numeroProjet)
						projet = p.projetValide(e2, pr)
					k += 1

		if (projet):
			i.camarades.append(e2)
			e2.camarades.append(i)
			i.majProjet(pr)
			e2.majProjet(pr)
			pr.groupe.append(i)
			pr.groupe.append(e2)
			binome = True
		else:
			j += 1





for i in p.classementEleve:
	print(i.numeroEleve)
	print(i.note)
	print('\n')
print('\n')

for i in p.eleves:
	answer = "Eleve : e"+str(i.numeroEleve+1)+" Binome : e"+str(i.camarades[0].numeroEleve+1)+" Projet : p"+str(i.projet.numeroProjet+1)
	print(answer)
	print('\n')

for i in p.projets:
	answer = "Projet : p"+str(i.numeroProjet+1)+" Mec : e"+str(i.groupe[0].numeroEleve+1)+" Mec : e"+str(i.groupe[1].numeroEleve+1)
	print(answer)
	print('\n')