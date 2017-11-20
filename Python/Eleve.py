import random

class Eleve:

	def __init__(self, numeroE, prefE, prefP):
	# creerEleve : int -> int
	# Donnees : numeroE, le numero qui representera l'eleve cree
	# Preconditions : numeroE est compris dans [0, n[               
	# Resultat : Retourne un eleve
		self.numeroEleve = numeroE
		self.prefEleve = prefE
		self.prefEleveTrie = []
		self.prefProjet = prefP
		self.prefProjetTrie = []
		self.camarades = []
		self.projet = 'aucun'

	def majNote (self, note):
		self.note = note

	def majProjet (self, projet):
		self.projet = projet


	def elevePrefere (self, promo):
	# elevePrefere :  -> [int]
	# Donnees : 
	# Preconditions :            
	# Resultat : Retourne la liste d'eleve prefere dans l'ordre

		if (len(self.prefEleveTrie) == 0):
			#On creer des tableau temporaire pour recuperer les objet en fonction de la note qu'a donne ea
			T = []
			B = []
			AB = []
			P = []
			AR = []

			eleve = 0
			for i in self.prefEleve:
				if (i=='T'):
					T.append(promo.getEleve(eleve))
				elif (i=='B'):
					B.append(promo.getEleve(eleve))
				elif (i=='AB'):
					AB.append(promo.getEleve(eleve))
				elif (i=='P'):
					P.append(promo.getEleve(eleve))
				elif (i=='AR'):
					AR.append(promo.getEleve(eleve))
				eleve += 1

			#On choisit un eleve au hasard en commencant par les eleves les moins apprecie, puis on l'ajoute dans le classement
			while (len(T) != 0):
				i = random.randint(0, len(T)-1)
				self.prefEleveTrie.append(T[i])
				T.remove(T[i])

			while (len(B) != 0):
				i = random.randint(0, len(B)-1)
				self.prefEleveTrie.append(B[i])
				B.remove(B[i])

			while (len(AB) != 0):
				i = random.randint(0, len(AB)-1)
				self.prefEleveTrie.append(AB[i])
				AB.remove(AB[i])

			while (len(P) != 0):
				i = random.randint(0, len(P)-1)
				self.prefEleveTrie.append(P[i])
				P.remove(P[i])

			while (len(AR) != 0):
				i = random.randint(0, len(AR)-1)
				self.prefEleveTrie.append(AR[i])
				AR.remove(AR[i])

		#return [T, B, AB, P, AR]

	def projetPrefere (self, promo):
    # elevePrefere :  -> [int]
    # Donnees : 
    # Preconditions :            
    # Resultat : Retourne la liste d'eleve prefere dans l'ordre

		if (len(self.prefProjetTrie) == 0):
	    	#On creer des tableau temporaire pour recuperer les objet en fonction de la note qu'a donne ea
			T = []
			B = []
			AB = []
			P = []
			AR = []

			projet = 0
			for i in self.prefProjet:
				if (i=='T'):
					T.append(promo.getProjet(projet))
				elif (i=='B'):
					B.append(promo.getProjet(projet))
				elif (i=='AB'):
					AB.append(promo.getProjet(projet))
				elif (i=='P'):
					P.append(promo.getProjet(projet))
				elif (i=='AR'):
					AR.append(promo.getProjet(projet))
				projet += 1

			#On choisit un eleve au hasard en commencant par les eleves les moins apprecie, puis on l'ajoute dans le classement
			while (len(T) != 0):
				i = random.randint(0, len(T)-1)
				self.prefProjetTrie.append(T[i])
				T.remove(T[i])

			while (len(B) != 0):
				i = random.randint(0, len(B)-1)
				self.prefProjetTrie.append(B[i])
				B.remove(B[i])

			while (len(AB) != 0):
				i = random.randint(0, len(AB)-1)
				self.prefProjetTrie.append(AB[i])
				AB.remove(AB[i])

			while (len(P) != 0):
				i = random.randint(0, len(P)-1)
				self.prefProjetTrie.append(P[i])
				P.remove(P[i])

			while (len(AR) != 0):
				i = random.randint(0, len(AR)-1)
				self.prefProjetTrie.append(AR[i])
				AR.remove(AR[i])

		#return [T, B, AB, P, AR]