import random
from Eleve import * ;
from Projet import * ;

class Promo:

	def __init__(self, nbE, nbP, cE, cP):
    # creerEleve : int -> int
    # Donnees : numeroE, le numero qui representera l'eleve cree
    # Preconditions : numeroE est compris dans [0, n[               
    # Resultat : Retourne un eleve
		self.eleves = []
		self.projets = []

		self.n = nbE
		self.p = nbP

		self.prefEleves = []
		self.prefProjets = []

		self.classementEleve = []
		self.eleveRepartis = 0
		self.critereE = cE
		self.critereP = cP

	def ajouterEleve (self, numero, prefE, prefP, nom):
		e = Eleve(numero, prefE, prefP, nom)
		self.eleves.append(e)
		self.prefEleves.append(prefE)
		self.prefProjets.append(prefP)

	def ajouterProjet (self, numero):
		p = Projet(numero)
		self.projets.append(p)


	def noteMajoritaire(self, eleve):
	# noteMajoritaire : int -> str
    # Donnees : eleve, le numero de l'eleve a noter
    # Preconditions :               
    # Resultat : retourne la note majoritaire de l'eleve
		notes = []

		for i in range(len(self.prefEleves)):
			note=self.prefEleves[i][eleve.numeroEleve]
			if(note=='TB'):
				notes.append(self.prefEleves[i][eleve.numeroEleve])
		for i in range(len(self.prefEleves)):
			note=self.prefEleves[i][eleve.numeroEleve]
			if(note=='B'):
				notes.append(self.prefEleves[i][eleve.numeroEleve])
		for i in range(len(self.prefEleves)):
			note=self.prefEleves[i][eleve.numeroEleve]
			if(note=='AB'):
				notes.append(self.prefEleves[i][eleve.numeroEleve])
		for i in range(len(self.prefEleves)):
			note=self.prefEleves[i][eleve.numeroEleve]
			if(note=='P'):
				notes.append(self.prefEleves[i][eleve.numeroEleve])
		for i in range(len(self.prefEleves)):
			note=self.prefEleves[i][eleve.numeroEleve]
			if(note=='I'):
				notes.append(self.prefEleves[i][eleve.numeroEleve])
		for i in range(len(self.prefEleves)):
			note=self.prefEleves[i][eleve.numeroEleve]
			if(note=='AR'):
				notes.append(self.prefEleves[i][eleve.numeroEleve])
		
		debut=[]
		fin=[]

		if(len(notes)%2==0):
			noteM=notes[(len(notes)/2)]
			debut=notes[0:(len(notes))/2]
			fin=notes[(len(notes)/2)+1: len(notes)]

		else:
			noteM=notes[(len(notes)/2)+1]
			debut=notes[0:(len(notes)-1)/2]
			fin=notes[(len(notes)+1)/2: len(notes)]

		nbMentionMoins = 0
		nbMentionPlus = 0
		if(noteM=='TB'):
			score = 6
			nbMentionMoins += notes.count('B')
			nbMentionMoins += notes.count('AB')
			nbMentionMoins += notes.count('P')
			nbMentionMoins += notes.count('I')
			nbMentionMoins += notes.count('AR')

			nbMentionPlus = 0
		elif(noteM=='B'):
			nbD = len(debut)-debut.count('B')
			nbF = len(fin)-fin.count('B')
			score = 5
			nbMentionMoins += notes.count('AB')
			nbMentionMoins += notes.count('P')
			nbMentionMoins += notes.count('I')
			nbMentionMoins += notes.count('AR')
			nbMentionPlus += notes.count('TB')
		elif(noteM=='AB'):
			nbD = len(debut)-debut.count('AB')
			nbF = len(fin)-fin.count('AB')
			score = 4
			nbMentionMoins += notes.count('P')
			nbMentionMoins += notes.count('I')
			nbMentionMoins += notes.count('AR')
			nbMentionPlus += notes.count('B')
			nbMentionPlus += notes.count('TB')
		elif(noteM=='P'):
			nbD = len(debut)-debut.count('P')
			nbF = len(fin)-fin.count('P')
			nbMentionMoins += notes.count('I')
			nbMentionMoins += notes.count('AR')

			nbMentionPlus += notes.count('AB')
			nbMentionPlus += notes.count('B')
			nbMentionPlus += notes.count('TB')
			score = 3
		elif(noteM=='I'):
			nbD = len(debut)-debut.count('I')
			nbF = len(fin)-fin.count('I')
			nbMentionMoins += notes.count('AR')
			nbMentionPlus += notes.count('P')
			nbMentionPlus += notes.count('AB')
			nbMentionPlus += notes.count('B')
			nbMentionPlus += notes.count('TB')
			score = 2
		elif(noteM=='AR'):
			nbMentionMoins = 0
			nbMentionPlus += notes.count('I')
			nbMentionPlus += notes.count('P')
			nbMentionPlus += notes.count('AB')
			nbMentionPlus += notes.count('B')
			nbMentionPlus += notes.count('TB')
			score = 1

		if(nbMentionMoins>nbMentionPlus):
				eleve.mention='-'
		elif(nbMentionMoins<nbMentionPlus):
				eleve.mention='+'

		eleve.majNote(score, nbMentionMoins, nbMentionPlus)

		return score

	def trieEleve(self):
		eleveTrie = []
		lMoins = []
		lNeutre = []
		lPlus = []
		mentionTab = [lMoins, lNeutre, lPlus]

		for i in range(1,7):
			for j in self.eleves:
				if j.note==i:
					if j.mention=='-':
						lMoins.append(j)
					elif j.mention=="nulle":
						lNeutre.append(j)
					elif j.mention=='+':
						lPlus.append(j)
			j = 0
			while (len(mentionTab[0]) != 0 or len(mentionTab[1]) != 0 or len(mentionTab[2]) !=0):
				if (len(mentionTab[j]) == 0):
					j += 1
				else: 
					eleveChoisit = mentionTab[j][0]
					for k in range(1, len(mentionTab[j])):
						r = mentionTab[j][k]
						if r.nbMentionPlus-r.nbMentionMoins < eleveChoisit.nbMentionPlus-eleveChoisit.nbMentionMoins:
							eleveChoisit = r
					eleveTrie.append(eleveChoisit)
					mentionTab[j].remove(eleveChoisit)				

		return eleveTrie

	def binomeValide(self, e2, e1): #e2 , #e5

		l = e2.prefEleve

		nb = 0
		resultat = False

		if (l[e1.numeroEleve] == 'TB'):
			resultat = True
		else:
			nb += l.count('TB')
		
		if (nb < self.critereE and l[e1.numeroEleve] == 'B'):
			resultat = True		
		else:
			nb += l.count('B')

		if(nb < self.critereE and l[e1.numeroEleve] == 'AB'):
			resultat = True		
		else:
			nb += l.count('AB')

		if(nb < self.critereE and l[e1.numeroEleve] == 'P'):
			resultat = True
		else:
			nb += l.count('P')

		if(nb < self.critereE and l[e1.numeroEleve] == 'I'):
			resultat = True
		else:
			nb += l.count('I')

		if(nb < self.critereE and l[e1.numeroEleve] == 'AR'):
			resultat = True
		else:
			nb += l.count('AR')

		return resultat

	def projetValide(self, e, p):


		l = e.prefProjet

		nb = 0
		resultat = False

		if (l[p.numeroProjet] == 'TB'):
			resultat = True
		else:
			nb += l.count('TB')
		
		if (nb < self.critereP and l[p.numeroProjet] == 'B'):
			resultat = True		
		else:
			nb += l.count('B')

		if(nb < self.critereP and l[p.numeroProjet] == 'AB'):
			resultat = True		
		else:
			nb += l.count('AB')

		if(nb < self.critereP and l[p.numeroProjet] == 'P'):
			resultat = True
		else:
			nb += l.count('P')

		if(nb < self.critereP and l[p.numeroProjet] == 'I'):
			resultat = True
		else:
			nb += l.count('I')

		if(nb < self.critereP and l[p.numeroProjet] == 'AR'):
			resultat = True
		else:
			nb += l.count('AR')

		return resultat

	def getEleve(self, i):

		eleve = self.eleves[i]
		return eleve

	def getProjet(self, i):

		projet = self.projets[i]
		return projet

	def calculNbTrinome (self):
		if (self.n<=54 and self.n>=36):
			trinome = self.n%18
		elif (self.n<36):
			trinome = self.n%2
		return trinome