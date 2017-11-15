# MathsDecision
OBJET ELEVE

Méthodes pour l’élève:

# Retourne la note majoritaire d’un élève à partir des notes des autres.
noteMajoritaire : élève x élèves []  → String (Alex) 
noteMajoritaire : élève x élèves [] → int  (Cyril)

#Retourne la liste de préférence de l’éléve
getElevePref : élève → élève[]

#Retourne true si l’élève 2 appartient à la première partie des préférences de l’élève1
eleveValide : élève1 x élève2 → bool


#Retourne true si le projet  appartient à la première partie des préférences de l’élève
projetValide : élèves x projet → bool

#Retourne le nombre de camarade
nbCamarades : élève → int

#Retourne la liste des camarades
getCamarades : élèves → élèves[]


OBJET PROMO

Fonction pour promo: 

#Classe les élèves par note majoritaire décroissante
classerEleves : élèves[] →  élève[] 

#Retourne le classement de l’élève
getClassementEleve : → élève

#Retourne le classement des l’élèves
getClassement : →  élèves[]

#Retourne l’ensemble des élèves de la promo
getAllEleves : → élèves[]

#Retourne l’ensemble des projets de la promo
getAllProjets : → projets[]

#Ajoute un élève à la classe
ajouterEleve : élève x projet → void
#Retourne le Nombre de trinôme à faire 
calculNbTrinome : élèves[] x projet[] → int

#Supprime le trinôme
supprimerTrinome : élève x élève x élève x projet x  in/out élèves[] x int/out projet[] → void


OBJET PROJET 

Fonction pour projet: 

#Retourne les élèves appartement au projet
getElevesProjet : projet → élèves[]

#Ajoute un élève au projet 
ajouterEleve : élève x projet → void






STRUCTURE DE DONNÉE

ELEVE

Atrributs
idEleve int 
prefEleves Array List
prefProjets Array List
noteMaj String/int
camarades Array List
projet Projet
aEtudier bool


PROMO

Attributs
nom String 
listeEleves ArrayList{} Eleve
listeProjet ArrayList {} Projet
classementEleves ArrayList{} Eleve
listeFinale[élèves[3 or 2], projet]

