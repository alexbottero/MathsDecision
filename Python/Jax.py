tab = [1,2,3,4,5,6,7]
debut =[]
fin =[]

debut = tab[0: ((len(tab)-1)/2)]
fin = tab[(len(tab)+1)/2: len(tab)]

print(debut)
print(fin)