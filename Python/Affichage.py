def affichageEleves(matrice, prefProjetTB):
	msg = "Liste des eleves" 
	d = raw_input("Afficher "+msg+" (Oui/Non)? ")
	detail = (d=="Oui")
	if detail:
		print "\nLISTE ELEVES\n"
		numero = 1;
		for i in matrice[0]:
			if (numero<10):
				print "Eleve ", numero, "  | Nom : ", i	
			else:
				print "Eleve ", numero, " | Nom : ", i	
			numero+=1
		print "\n"

def affichageClassement(p):
	msg = "Classement des eleves" 
	d = raw_input("Afficher "+msg+" (Oui/Non)? ")
	detail = (d=="Oui")
	if detail:	
		print("Classement decroissant des eleves selon leur note majoritaire\n")
		c=1
		print "nmb = Nombre de mention  en dessous de la majoritaire"
		print "npb = Nombre de mention  au dessus de la majoritaire\n"
		print "Classement |Note| Mention | nmb | npb | Nom\n"
		for i in p.classementEleve:
			msg = str(c)+")"
			if(c<10):
				msg += " "

			msg += " e"+str(i.numeroEleve+1)
			if(i.numeroEleve<10):
				msg += " "

			msg += "    | "

			parseNote = ["AR", "I", "P", "AB", "B", "TB"]
			msg += parseNote[i.note-1]

			if(len(parseNote[i.note-1])==1):
				msg += " "

			msg += " |  "
			if(i.mention != "nulle"):
				msg += "  "
			msg += i.mention
			if(i.mention != "nulle"):
				msg += "  "

			msg += "  |  "+str(i.nbMentionMoins)
			if (i.nbMentionMoins<10):
				msg += " "

			msg += "  |  "+str(i.nbMentionPlus)
			if (i.nbMentionPlus<10):
				msg += " "

			msg += "  | "+str(i.nom)

			print msg
			c += 1
	print('\n')

def affichageMatrice (matrice, libelle):
	msg = "Matrice preference " +libelle 
	d = raw_input("Afficher "+msg+" (Oui/Non)? ")
	detail = (d=="Oui")
	if detail:
		print msg
		for i in matrice:
			print(i)
	print('\n')