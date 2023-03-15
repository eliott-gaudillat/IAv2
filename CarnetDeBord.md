Etape 1

Jour 1:

On a donc ici un problème de coloration, ou l'on souhaite savoir si une coloration a N couleurs est possible
C'est Donc un problème de type SAT

pour résoudre un problème de type SAT il nous faut des formules  sous formes CNF.

Première chose a comprendre :
Fonctionner de notre toolbox SolverSat.
SolverSat prends en parametres une base ( liste de liste  qui represente les clauses)

exemple : [[-1 2][-1 -2]] en parametres équivaut en logique propositionnelle  à " (-x1 ou x2) et (-x1 ou -x2)"

donc SovlerSat "transforme" notre base en CNF, une liste est une disjonction('ou')  et chaque liste et relié par un 
'et' (conjonction)

donc dans notre liste de liste , un entier represente une variable , 1 equivaut a x1 et -1 a -x1 

Maintenant qu'on connait le fonctionnement de notre SolverSat il faut encoder notre problème en CNF.

Le problème de la coloration a été traité en cours , on a donc 2 contraintes a respecter 

1- un sommet a une seule et unique couleur (clause phi):
avec 3 couleurs : phi_i=(Ri ou Bi ou Ji) et (-Ri ou -Bi) et (-Ri ou -Ji) et (-Bi ou -Ji)

Ceci represente la contrainte de l'unicité de la couleur pour un seul sommet,
il faut donc respecter la clause phi pour tous les sommets.
cela sera representé par une liste de la base 

2- deux sommets adjacents ne sont pas de la même couleur ( clause psi):
avec 2 couleurs: psi_a_b=(-Ra ou -Rb) et (-Ba ou -Bb)
cette contrainte doit etre respecter pour tous les couples de sommet du graphe.
chaque clause psi_a_b sera une des listes de la base.

Travail pour la prochaine séance : mettre a jour la base , avec les differentes clauses

Jour 2:

De ce qu'on a pu voir  des contraintes , on en déduit que pour chaque sommet on aura 1 variable par couleur.
donc si il y a N couleurs , alors chaque sommet aura N variables.

premier problème :  associé chaque variables à chaque sommet .
Au depart j'avais pensé a utilisé une matrice de numpy , mais numpy n'est pas importé dans le projet;
donc je suis parti sur une autre méthode.
chaque sommet est representé par un nombre donc ses variables seront les entiers
N*(i-1) + 1 ; N-(i-1)+2 ; .. , N-(i-1)+N
ou N est le nombre de couleur , i la valeur du sommet 

maintenant que j'ai défini la valeur des variables de chaque sommet il me reste à mettre a jour la base
avec les clauses.

j'ai donc défini 2 fonctions clausephi   qui  ajoute a la base la clausephi sous forme de liste 
de chaque sommet et  clausepsi qui ajoute a la base la clause psi sous forme de liste de chaque couple de sommet.


il ne reste plus qu'a faire la base de l'ensemble du graphe en bouclant sur nos fonctions clausephi et clausepsi

une fois la base du graphe complete , on peut faire tourner le solver avec la base du graphe.




Etape 2:
jour 3

l'etape 2 ce compose de 3 cas differents , pour cette séance j'ai travaillé exclusivement sur le 1er cas.

dans le cas 1 , on  a ici un probleme de recherche de plus court chemin dans un graphe.

On va donc utiliser le solver Astar pour notre recherche.

Le solver Astar fonctionne avec des etats et une fonction de cout.

il faut donc refléchir à ce que represente un état dans notre probleme , 
comment savoir si un etat est solution, comment trouver les successeurs d'un etat,
comment calculer l'heuristique  et le cout du changement d'etat.

Pour representer un état , j'ai décidé de prendre le graphe en lui-même , un Sommet qui est le sommet courant 
et un second sommet qui est le sommet d'arrivée de  notre chemin.

un etat et donc solution si le sommet courant et le sommet d'arrivé sont les mêmes

pour les successeurs , deux etats sont voisins si les sommets courant sont voisins

donc un etat successeurs et un etat avec le meme graphe , le meme sommet d'arrivée et un sommet courant qui
et un sommet adjacents a celui du pere.


le cout de changement est tous simplement le cout de l'arc associés entre les deux sommets courant des 2 états

le plus compliqué a définir est l' heuristique car il faut trouver quelque chose qui se rapproche le plus possible de la 
distance  qui reste a parcourir entre le sommet courant et le sommet d'arrivée.
On ne connait pas le chemin le plus court car on le cherche mais ce qui peut se rapprocher le plus de la distance au sol 
entre 2 sommets est la distance à vol d'oiseau. l'heursitique d'un etat sera donc , la distance 
euclidienne entre le sommet courant de l'etat et le sommet d'arrivée , à partir de leur coordonnées spatiales.

fin de séance 3 , implementation cas 1 ok 
travail de la prochaine séance : vérifier résultats cas 1, commencer a réflechir voir implementer cas 2

Jour 4 :

verification cas 1 ok

Maintenant pour le cas 2 , on a un probleme du voyageur de commerce , on cherche a parcourir tous les
sommets du graphe une unique fois et revenir a notre sommet de départ.


Ici aussi on a un probleme de recherche de chemin , sur lequel on va utiliser le solver OptiAStar,
on retrouve donc les mêmes problèmes que precedemment , définition d'un etat , etat solution , successeurs,
cout de changement d'etat et heuristique.


ici pour l'etat , on garde le principe d'avoir notre graphe , un sommet courant , un sommet d'arrive mais on y ajoute 
une liste des sommets visité de l'etat initiale jusqu'a notre etat actuel

un etat est solution si , le sommet courant vaut le sommet d'arrivé et que tous les autres sommets ont été visités.

un successeurs , et un etat dont le sommet courant et un sommet adjacents au sommet courant du pere mais le sommet courant
du fils ne doit pas etre dans la liste des sommets visité du pere, le sommet d'arrivee est identique , et la liste des sommets
visité et identique avec le sommet courant du pere en plus.

le cout de changement est identique au cas 1 , on prends le cout de l'arc entre le sommet courant du pere et celui du fils

encore une fois le plus compliqué est de définir une heuristique satisfaisante .
j'ai decidé de multiplie la distance euclidienne entre notre sommet courant et le sommet d'arrivé par le nombre
de sommet manquant a visiter.

fin de seance 4 , implementation cas 2 ok
travail de la prochaine séance , reflexion plus implementation cas 3

Seance 5 :
Pour le cas 3 , on a un probleme similaire  cependant maintenant le robot peut voler , ce qui implique qu'on a un graphe complet,
chaque sommet est liées a tous les autres sommets.

donc notre representation de l'etat reste assez identique :
-le graphe
-le sommet de depart
-le sommet courant
-liste des sommets visitées

un etat successeurs et un etat qui possede le meme graphe le meme sommet de depart et donc la liste de sommet visite 
et identique avec un sommet supplementaire qui n'est pas identique a l'un des sommets deja visité.
 un etat est solutions si le sommet de depart et le sommet courant sont les mêmes est que la liste des sommets visités 
contient tous les sommets du graphe.

le cout de changement d'etat est la distance entre le sommet courant de l'etat et le sommet courant de l'etat suivant.

la aussi le plus gros probleme a été de trouver une heuristique valide.  Au debut j'aditionnais la distance des sommets
restants par rappport a l'arriveé mais cela n'est pas garanti  d'etre plus petit que l'heuristique optimal. donc mon 
heuristique n'etait pas valable. 
Apres reflexion avec le reste du groupe de tp et en lisant la doc on a trouver la fonction getPoidsMinAir
qui renvoie la plus petite distance par les airs possible entre deux ville du graphe. Donc j'ai pris pour heuristique tel que h = getPoidsMinAir*coeff
où le coeff correspondant au nombre de sommet restant à visiter , ceci garanti que h < h optimal.

Cela m'a aussi permis de voir que mon cas 2 n'etait pas bon non plus et donc pour l'heuristique du cas 2 j'ai utilise une fonction
similaire getPoidsMinTerre , qui renvoie le plus petits poids du graphe( plus petite distance par la route )


à partir du cas avec 8 villes ,l'execution deviens plutot longue environ 1min sur ma machine.


Etape 3:
Pour cette 3eme étape on chercher a gagner du temps d'execution , on ne cherche pas la solution ideale mais une solution
admissible. Donc ici comparer la l'etape précendente ou on travailler dans l'espace d'etat ici on va travailler sur 
l'espace des solutions, sur lequel on appliquera les algorithmes HillClimbing et Tabou fourni.

Il nous faut alors definir une ce qu'est une solution pour notre problème, comment on trouve les solutions voisines,
comment on évalue notre solution et comment on créer une nouvelle solution, pour faire "une reprise".

donc une solution ici est representé par le graphe des villes , le sommet de départ et le un chemin solution ( c'est a dire un
chemin qui passe par tous les sommets de graphe et qui revient au sommet de depart)

Pour les solutions voisines , on avait vu en classe pour le probleme du sac de voyage qu'on pouvait ajouter /retirer ou échanger des objets.
ici pour notre probleme, on sait que le graphe et la ville de départ resteront identique  on ne peut que changer notre 
chemin, l'ajout ou le retrait de ville ne peut pas etre envisager car on souhaite parcourir toute les villes.
donc pour trouver les voisins on va echanger l'ordre de visite des villes dans le chemin.
mais pour que cela reste plutot proche de la solution courante on ne va echanger que 2 villes dans le chemin.
le nombre de permutations et donc de voisin possible est de complexité N^2 ou N est le nombre de villes.
pour gagner du temps d'exectution on va limiter le nombre de voisin avec une complexité d'ordre N.
j'ai testé avec plusieurs valeurs de N : 5N,3N N  au final j'ai gardé N voisins a chaque fois , car on avait des résultats
plutot satisfaisants et que pour un nombre trop grand mon ordinateur n'etait pas en capacité d'executer les algorithmes
dans un temps raisonnable.

Pour évaluer une solution , on calcul le cout/le poids du chemin tous simplement

Pour la selection des voisins j'ai utilisé la version optimsé , on selectionne directement le voisins ayant la 
plus petite évaluation car on cherche a minimiser le chemin .

Pour la creation d'une nouvelle solution, on cree de maniere aléatoire un chemin, a chaque iteration on tire au hasard
une des villes qu'on a pas encore visité et on l'ajoute au chemin.jusqu'a a avoir visité tous les sommets.


j'ai obtenu des résultats assez rapidement jusqu'au test avec 26 et 100 essais.

pour 150 villes je commence a mettre une bonne minute pour executer les 2 algorithmes avec 100 reprises. avec un resultat pas tres pertinents.
en fonction de la solution creer a la 1ere reprise on peut avoir un coup une solution correcte et la fois d'apres une solution
assez éloigné de la solution optimal. Ceci s'explique par la complexité des algorithmes Hill-Climbing et tabou.
qui a chaque solution calcul N solutions voisines.

ce 

Etape 4:

l'etape 4 est un probleme de coloration, et d'optimisation

cette étape demande seulement a utiliser le solverCSP, le solver prends en entrée le graphe ainsi que le nombre de couleurs
qu'on souhaite utiliser pour colorer notre graphe . Si la coloration est possible il nous donne une solution ou toute les solutions
en fonction de la valeur du booleen en 3eme parametres du solvers.
Si il n'existe pas de solution alors il nous informera qu'il n'existe pas de solutions.
il nous faut donc test le solver sur un même graphe avec un nombre de couleurs differents pour determiner la coloration 
minimal de notre graphe .
Pour le cas avec 10 villes on obtient une coloration avec 3 couleurs mais pas de solution avec 2 couleurs. on en déduit donc
que la coloration minimal est de 3 couleurs.


tabou : forte complexité 



etape 5:

J'ai fait cette partie en réflexion avec Bernard Parfait

 l'une des premieres choses a faire a été de lire la doc ZIMPL pour comprendre sa syntaxe et son fonctionnement.

en suite il  a fallut  reflechir a notre problème, comment on peut l'exprimer sous forme de contrainte.

On avait vu en classe , que notre probleme necessite comme variables : les sommets du graphe
les arcs du graphe , et un booleen associé a chaque arc qui dit si il appartient ou non au chemin.

on cherche a minimiser la distance de notre chemin 
donc  a minimiser la somme des arcs presents dans le chemin

l'une des contraintes du probleme et qu'on doit passer une seule fois par chaque sommet
ce qui peut se traduire que pour chaque sommet le nombre d'arc associé est de 2. un arc entrant et un arc sortant.

et la seconde contrainte  et qu'il faut eviter la creation de cycles. pour cela  on verifie , que 
chaque partition de l'ensemble, doit avoir un nombre d'arc inferieur au nombre de sommet  de notre sous ensemble.

Une fois notre fonction a minimiser et nos contraintes, on a ecrit notre fichier zpl.
On c'est servi du guide d'utilisation qui propose une implementation pour le probleme du voyageur de commerce.
On a revisité l'implementation fourni pour qu'elle correspond correctement a notre probleme.

Pour comparer l'efficacité en temps de calcul, j'ai lancé separement notre solution du cas3 avec le Astar
et notre solution zimpl pour le meme nombre de ville.
alors que avec Astar le programme mettait du temps a proposé une solution, l'implementation avec ZIMPL  prends du temps
mais est plus rapide que le Astar