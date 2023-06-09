"""
module pour l'état de l'etape 2 ds le cas 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas1(Etat) :
    """ Classe pour definir un etat pour le cas 1 de la tache 2 (hérite de Etat)
    """ 
    
    # attributs
    # A COMPLETER
    # //////////////////////////////////////////////
    tg : GrapheDeLieux
    """ le graphe representant le monde """ 
    
    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux, depart : int  , arrivee : int) :
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        
        :param depart: ville de depart du chemin
        
        :param arrivee: ville d'arrivee du chemin
        """ 
        self.tg = tg
        self.depart=depart
        self.arrivee=arrivee
        # a completer pour tenir compte de la presence ou pas des deux derniers parametres
     
    
    # methodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self) :
        """ methode detectant si l'etat est une solution
        
        :return true si l'etat courant est une solution, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return self.depart==self.arrivee
    
    
    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """
        listeEtatSuccesseurs=[]
        successeurs=self.tg.getAdjacents(self.depart)
        for s in successeurs:
            etat=EtatCas1(self.tg,s,self.arrivee)
            listeEtatSuccesseurs.append(etat)

        # A ECRIRE et MODIFIER le return en consequence
        return listeEtatSuccesseurs
    
    
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """

        return GrapheDeLieux.dist(self.depart,self.arrivee,self.tg)
    
    
    def k(self, e) :
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        
        :param e: un etat
        
        :return cout du passage de l'etat courant à l'etat e
        """ 
        # A ECRIRE et MODIFIER le return en consequence

        return self.tg.getCoutArete(self.depart,e.depart)
    
    
    def displayPath(self, pere) :
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres
        
        :param pere: map donnant pour chaque etat, son pere 
        """ 
        # A ECRIRE
        print("resultat trouve : ")
        e = self
        while pere[e] != None:
            print(e, "<-", pere[e])
            e = pere[e]

    
    
    
    # methodes pour pouvoir utiliser cet objet dans des listes et des map
    # //////////////////////////////////////////////
    def __hash__(self) :
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage
        
        :return code de hachage
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return 0

    def __eq__(self, o):
        """ methode de comparaison de l'etat courant avec l'objet o

        :param o: l'objet avec lequel on compare

        :return true si l'etat courant et o sont egaux, false sinon
        """
        # A ECRIRE et MODIFIER le return en consequence
        if not isinstance(o, Etat):
            return False
        return self.depart == o.depart

    # methode pour affichage futur (heritee d'Object)
    # //////////////////////////////////////////////
    def __str__(self) :
        """ methode mettant l'etat courant sous la forme d'une
        chaine de caracteres en prevision d'un futur affichage

        :return representation de l'etat courant sour la forme d'une
        chaine de caracteres
        """
        # A ECRIRE et MODIFIER le return en consequence
        return "sommet n" + str(self.depart)



