import random
from Eleve import * ;
from Projet import * ;
from Promo import * ;

p = Promo(5, 2)

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
	i.elevePrefere()
	i.projetPrefere()

#On etablie le classement
p.classementEleve = p.quickSort(p.eleves)

for i in p.classementEleve:
	j = 0
	binome == False
	
	while (j<len(i.prefEleve) and binome==False):
		
		e2 = i.prefEleve[j]
		
		if(len(e2.camarades) == 0 and len(i.camarades) == 0):
			if (p.binomeValide(e2, i)):

				k = 0
				projet = False

				while(k<len(i.prefProjetTrie) and projet==False)

					p = i.prefProjet[k]
					if (len(p.groupe) == 0)
						projet = p.projetValide(e2, p)
					k += 1

		if (projet):
			i.camarades.append(e2)
			e2.camarades.append(i)
			i.projet.append(p)
			e2.projet.append(p)
			p.groupe.append(i)
			p.groupe.append(e2)
			binome = True
		else:
			j += 1





for i in p.classementEleve:
	print(i.numeroEleve)
	print(i.note)
	print('\n')
print('\n')