import csv
import sys

'''
	File = String pointant sur le fichier csv de la forme :
		-1,B,AB
		TB,-1,AR
		TB,AB,-1
	Les valeurs du fichier sont :
		Tres bien = TB
		...
		A rejeter = AR
		Diagonale = -1
	Renvoie une liste:
		Premier argument = matrice de preferences
		Second argument = liste des eleves
'''
def parseCSV(file):
	tmp = []
	with open(file, 'rb') as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	    for row in spamreader:
	    	tmp.append(','.join(row).split(','))
	return tmp

'''
	Convertie une matrice de la forme :
			[[-1,B,AB]
			 [TB,-1,AR]
			 [TB,AB,-1]]
	En une matrice de la forme :
			[[-1  3  2]
			 [ 4 -1  0]
			 [ 4  2 -1]] 
	Les valeurs sont :
		5 = TB
		...
		0 = AR
		-1 = -1
'''

'''
	Ecrit dans un fichier csv pointant sur fichier la matrice repartition de la forme :
		[[1,2],
		 [3,4,5],
		 [6,7],
		 [8,9,10]]
	(Les chiffres representent les eleves)
'''
def writeCsv(file,repartition):
	with open(file, 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for x in xrange(0,len(repartition)):
	    	repartition[x].insert(0,x+1)
	    	spamwriter.writerow(repartition[x])

'''
	Genere une matrice carre aleatoire de taille : size
	Les valeurs sont comprises entre 0 et 4 et la diagonale = -1
'''



''' EXEMPLE D'UTILISATION '''


#writeCsv("csv2.csv",repartition)
