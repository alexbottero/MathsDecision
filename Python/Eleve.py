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


	def elevePrefere ():
	# elevePrefere :  -> [int]
	# Donnees : 
	# Preconditions :            
	# Resultat : Retourne la liste d'eleve prefere dans l'ordre

		if (len(prefEleveTrie) == 0):
			#On creer des tableau temporaire pour recuperer les objet en fonction de la note qu'a donne ea
			T = []
			B = []
			AB = []
			P = []
			AR = []

			eleve = 0
			for i in self.prefEleve:
				if (i=='T'):
					T.append(eleve)
				elif (i=='B'):
					B.append(eleve)
				elif (i=='AB'):
					AB.append(eleve)
				elif (i=='P'):
					P.append(eleve)
				elif (i=='AR'):
					AR.append(eleve)
				eleve += 1

			#On choisit un eleve au hasard en commencant par les eleves les moins apprecie, puis on l'ajoute dans le classement
			while (len(T) != 0):
				i = random.randint(0, len(T)-1)
				prefEleveTrie.append(T[i])
				T.remove(T[i])

			while (len(B) != 0):
				i = random.randint(0, len(B)-1)
				prefEleveTrie.append(B[i])
				B.remove(B[i])

			while (len(AB) != 0):
				i = random.randint(0, len(AB)-1)
				prefEleveTrie.append(AB[i])
				AB.remove(AB[i])

			while (len(P) != 0):
				i = random.randint(0, len(P)-1)
				prefEleveTrie.append(P[i])
				P.remove(P[i])

			while (len(AR) != 0):
				i = random.randint(0, len(AR)-1)
				prefEleveTrie.append(AR[i])
				AR.remove(AR[i])

		#return [T, B, AB, P, AR]

	def projetPrefere ():
    # elevePrefere :  -> [int]
    # Donnees : 
    # Preconditions :            
    # Resultat : Retourne la liste d'eleve prefere dans l'ordre

		if (len(prefProjetTrie) == 0):
	    	#On creer des tableau temporaire pour recuperer les objet en fonction de la note qu'a donne ea
			T = []
			B = []
			AB = []
			P = []
			AR = []

			projet = 0
			for i in self.prefProjet:
				if (i=='T'):
					T.append(projet)
				elif (i=='B'):
					B.append(projet)
				elif (i=='AB'):
					AB.append(projet)
				elif (i=='P'):
					P.append(projet)
				elif (i=='AR'):
					AR.append(projet)
				eleve += 1

			#On choisit un eleve au hasard en commencant par les eleves les moins apprecie, puis on l'ajoute dans le classement
			while (len(T) != 0):
				i = random.randint(0, len(T)-1)
				prefProjetTrie.append(T[i])
				T.remove(T[i])

			while (len(B) != 0):
				i = random.randint(0, len(B)-1)
				prefProjetTrie.append(B[i])
				B.remove(B[i])

			while (len(AB) != 0):
				i = random.randint(0, len(AB)-1)
				prefProjetTrie.append(AB[i])
				AB.remove(AB[i])

			while (len(P) != 0):
				i = random.randint(0, len(P)-1)
				prefProjetTrie.append(P[i])
				P.remove(P[i])

			while (len(AR) != 0):
				i = random.randint(0, len(AR)-1)
				prefProjetTrie.append(AR[i])
				AR.remove(AR[i])

		#return [T, B, AB, P, AR]