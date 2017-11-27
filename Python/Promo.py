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
			notes.append(self.prefEleves[i][eleve.numeroEleve])
		
		T = notes.count('TB')
		B = notes.count('B')
		AB = notes.count('AB')
		P = notes.count('P')
		I = notes.count('I')
		AR = notes.count('AR')

		score = AR + I*2 + P*3 + AB*4 + B*5 + T*6
		eleve.majNote(score)

		return score

	def noteMajoritaire2(self, eleve):
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

		nbD = 0
		nbF = 0
		if(noteM=='TB'):
			score = 6
		elif(noteM=='B'):
			nbD = len(debut)-debut.count('B')
			nbF = len(fin)-fin.count('B')
			score = 5
		elif(noteM=='AB'):
			nbD = len(debut)-debut.count('AB')
			nbF = len(fin)-fin.count('AB')
			score = 4
		elif(noteM=='P'):
			nbD = len(debut)-debut.count('P')
			nbF = len(fin)-fin.count('P')
			score = 3
		elif(noteM=='I'):
			nbD = len(debut)-debut.count('I')
			nbF = len(fin)-fin.count('I')
			score = 2
		elif(noteM=='AR'):
			score = 1

		if(nbD>nbF):
				eleve.mention='+'
		elif(nbD<nbF):
				eleve.mention='-'

		eleve.majNote(score)

		return score


	def quickSort(self, x):

		if len(x) == 1 or len(x) == 0:
			return x
		else:
			pivot = x[0]
			i = 0
			for j in range(len(x)-1):
				if x[j+1].note < pivot.note:
					x[j+1], x[i+1] = x[i+1], x[j+1]
					i += 1
			x[0], x[i] = x[i], x[0]
			first_part = self.quickSort(x[:i])
			second_part = self.quickSort(x[i+1:])
			first_part.append(x[i])

			return first_part + second_part

	def mentionSort(self):
		lTemp = []
		lMoins = []
		lNeutre = []
		lPlus = []
		for i in range(1,7):
			for j in self.eleves:
				if j.note==i:
					if j.mention=='-':
						lMoins.append(j)
			for j in self.eleves:
				if j.note==i:
					if j.mention=="nulle":
						lNeutre.append(j)
			for j in self.eleves:
				if j.note==i:
					if j.mention=='+':
						lPlus.append(j)
			while (len(lMoins) != 0):
				z = random.randint(0, len(lMoins)-1)
				lTemp.append(lMoins[z])
				lMoins.remove(lMoins[z])
			while (len(lNeutre) != 0):
				z = random.randint(0, len(lNeutre)-1)
				lTemp.append(lNeutre[z])
				lNeutre.remove(lNeutre[z])
			while (len(lPlus) != 0):
				z = random.randint(0, len(lPlus)-1)
				lTemp.append(lPlus[z])
				lPlus.remove(lPlus[z])

		return lTemp

			

	def classerEleve(self):
		#On creer des tableau temporaire pour recuperer les eleves en fonction de leurs noteMajoritaire
		T = []
		B = []
		AB = []
		P = []
		I = []
		AR = []

		indice = 0
		#Pour chaque eleve on l'ajoute dans le tableau qui lui correspond
		for i in self.eleves:
			if (self.noteMajoritaire(i)=='TB'):
				T.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='B'):
				B.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='AB'):
				AB.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='P'):
				P.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='I'):
				I.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='AR'):
				AR.append(self.eleves[indice])
			indice += 1

		#On choisit un eleve au hasard en commencant par les eleves les moins apprecie, puis on l'ajoute dans le classement
		while (len(AR) != 0):
			i = random.randint(0, len(AR)-1)
			self.classementEleve.append(AR[i])
			AR.remove(AR[i])

		while (len(I) != 0):
			i = random.randint(0, len(I)-1)
			self.classementEleve.append(I[i])
			I.remove(I[i])

		while (len(P) != 0):
			i = random.randint(0, len(P)-1)
			self.classementEleve.append(P[i])
			P.remove(P[i])

		while (len(AB) != 0):
			i = random.randint(0, len(AB)-1)
			self.classementEleve.append(AB[i])
			AB.remove(AB[i])

		while (len(B) != 0):
			i = random.randint(0, len(B)-1)
			self.classementEleve.append(B[i])
			B.remove(B[i])

		while (len(T) != 0):
			i = random.randint(0, len(T)-1)
			self.classementEleve.append(T[i])
			T.remove(T[i])


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