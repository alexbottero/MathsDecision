import csv


'''
	File = String pointant sur le fichier csv de la forme :
		N/A,B,AB
		TB,N/A,AR
		TB,AB,N/A
	Les valeurs du fichier sont :
		Tres bien = TB
		...
		A rejeter = AR
		Non renseigner = N/A
'''
def parseCSV(file):
	tmp = []
	with open(file, 'rb') as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	    for row in spamreader:
	    	tmp.append(', '.join(row).split(','))

	for i in tmp:
		if (i=='N/A'):
			i=''

	return tmp
	#return np.array(tmp)

'''
	Convertie une matrice de la forme :
			[[N/A,B,AB]
			 [TB,N/A,AR]
			 [TB,AB,N/A]]
	En une matrice de la forme :
			[[-1  3  2]
			 [ 4 -1  0]
			 [ 4  2 -1]] 
	Les valeurs sont :
		4 = TB
		...
		0 = AR
		-1 = N/A
'''
def convertToNull(matrice):
	res = []
	for x in range(0,np.shape(matrice)[0]):
		tmp = []
		for y in range(0,np.shape(matrice)[0]):
			if(matrice[x][y] == "N/A"):
				tmp.append(-1)
			elif(matrice[x][y] == "TB"):
				tmp.append(4)
			elif(matrice[x][y] == "B"):
				tmp.append(3)
			elif(matrice[x][y] == "AB"):
				tmp.append(2)
			elif(matrice[x][y] == "I"):
				tmp.append(1)
			elif(matrice[x][y] == "AR"):
				tmp.append(0)
			else:
				print "fuck"
		res.append(tmp)
	#return np.array(res)
	return 0
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
	    for x in repartition:
	    	spamwriter.writerow(x)

'''
	Genere une matrice carre aleatoire de taille : size
	Les valeurs sont comprises entre 0 et 4 et la diagonale = -1
'''


matrice = parseCSV("csv.csv")
print matrice


#writeCsv("csv2.csv",repartition)


