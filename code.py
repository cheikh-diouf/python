#variables 

prenom = " Charles " # Du texte ( String )
experience = 0 # Un nombre entier ( Int )
motivation = 100.0 # Un nombre a virgule ( Float )
 # On affiche le contenu des boites
print ( " Je m ’ appelle " , prenom )
print ( " Ma motivation est a " , motivation , " % " )

#les boucles
#boucle for
print ( " Debut du compte a rebours ... " )

 # range (1 , 4) va compter : 1 , 2 , 3 ( le 4 est exclu )
for i in range (1 , 4) :
    print ( " Tour numero : " , i )

print ( " Partez ! " )
#boucle while
compteur = 0

 # Tant que le compteur est inferieur a 3
while compteur < 3:
    print ( " Compteur actuel : " , compteur )
# important : Il faut modifier le compteur
    compteur = compteur + 1

print ( " Boucle terminee . " )

#decouper un mot
mot = " PYTHON "

 # 1. Prendre le tout dernier element

dernier = mot [ -1]

 # 2. Prendre entre le 2 eme et le 4 eme element
 # On veut les index 1 , 2 et 3.
 # En Python on ecrit [ debut : fin ( exclue ) ]
morceau = mot [1:4]

print ( " Le mot complet : " , mot )
print ( " Derniere lettre : " , dernier )
print ( " Le coeur du mot : " , morceau )
##decouper une phrase