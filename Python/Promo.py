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

	def ajouterEleve (self, numero, prefE, prefP):
		e = Eleve(numero, prefE, prefP)
		self.eleves.append(e)
		self.prefEleves.append(prefE)

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
		
		T = notes.count('T')
		B = notes.count('B')
		AB = notes.count('AB')
		P = notes.count('P')
		AR = notes.count('AR')

		score = AR + P*2 + AB*3 + B*4 + T*5
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
			

	def classerEleve(self):
		#On creer des tableau temporaire pour recuperer les eleves en fonction de leurs noteMajoritaire
		T = []
		B = []
		AB = []
		P = []
		AR = []

		indice = 0
		#Pour chaque eleve on l'ajoute dans le tableau qui lui correspond
		for i in self.eleves:
			if (self.noteMajoritaire(i)=='T'):
				T.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='B'):
				B.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='AB'):
				AB.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='P'):
				P.append(self.eleves[indice])
			elif (self.noteMajoritaire(i)=='AR'):
				AR.append(self.eleves[indice])
			indice += 1

		#On choisit un eleve au hasard en commencant par les eleves les moins apprecie, puis on l'ajoute dans le classement
		while (len(AR) != 0):
			i = random.randint(0, len(AR)-1)
			self.classementEleve.append(AR[i])
			AR.remove(AR[i])

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


	def binomeValide(self, e1, e2):

		l = e2.prefEleve

		nb = 0
		resultat = False

		if (l[e1.numeroEleve] == 'T'):
			resultat = True
		else:
			nb += l.count('T')
		
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

		if(nb < self.critereE and l[e1.numeroEleve] == 'AR'):
			resultat = True
		else:
			nb += l.count('AR')

		return resultat

	def projetValide(self, e, p):


		l = e.prefProjet

		nb = 0
		resultat = False

		if (l[p.numeroProjet] == 'T'):
			resultat = True
		else:
			nb += l.count('T')
		
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