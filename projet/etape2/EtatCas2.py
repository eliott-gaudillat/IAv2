"""
module pour l'état de l'etape 2 ds le cas 2
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas2(Etat) :
    """ 
    Classe pour definir un etat pour le cas 2 de la tache 2
    """ 
       
    # attributs
    # A COMPLETER
    # //////////////////////////////////////////////
    tg : GrapheDeLieux
    """ le graphe representant le monde """ 
    
    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux,  SommetDepart : int ,  SommetCourant : int ,SommetVisite:list) :
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        
        :param param1: a definir eventuellement
        
        :param param2: a definir eventuellement
        """ 
        self.tg = tg
        self.SommetDepart = SommetDepart
        self.SommetCourant=SommetCourant
        self.SommetVisite = []
        for l in SommetVisite:
            self.SommetVisite.append(l)


        # a completer pour tenir compte de la presence ou pas des deux derniers parametres
     
    
    # methodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self) :
        """ methode detectant si l'etat est une solution

        :return true si l'etat courant est une solution, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence0000
        if(self.SommetCourant==self.SommetDepart):
            if(len(self.SommetVisite)==(len(self.tg.getSommets()))):
                return True

        return False
    
    
    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        listeEtatSuccesseurs = []
        successeurs = self.tg.getAdjacents(self.SommetCourant)
        listSommetVisite = []

        for sv in self.SommetVisite:
            listSommetVisite.append(sv)
        listSommetVisite.append(self.SommetCourant)

        for s in successeurs:
            if(s not in self.SommetVisite):
                etat = EtatCas2(self.tg, self.SommetDepart,s,listSommetVisite)
                listeEtatSuccesseurs.append(etat)
            if(s==self.SommetDepart and (len(self.SommetVisite)==(self.tg.getNbSommets()-1))):
                etat = EtatCas2(self.tg, self.SommetDepart, s, listSommetVisite)
                listeEtatSuccesseurs.append(etat)
        # A ECRIRE et MODIFIER le return en consequence
        return listeEtatSuccesseurs
    
    
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        coeff=self.tg.getNbSommets()-len(self.SommetVisite)
        h=coeff*self.tg.getPoidsMinTerre()

        return h
    
    
    def k(self, e) :
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        
        :param e: un etat
        
        :return cout du passage de l'etat courant à l'etat e
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return self.tg.getCoutArete(self.SommetCourant,e.SommetCourant)


    def displayPath(self):
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres

        :param pere: map donnant pour chaque etat, son pere
        """
        # A ECRIRE
        print(self.SommetVisite)

        # methodes pour pouvoir utiliser cet objet dans des listes et des map
        # //////////////////////////////////////////////

    def __hash__(self):
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
        if self.SommetCourant != o.SommetCourant:
            return False
        if len(self.SommetVisite) != len(o.SommetVisite):
            return False

        constante = True
        for i in range(len(self.SommetVisite)):
            if self.SommetVisite[i] != o.SommetVisite[i]:
                constante = False

        return constante





        # methode pour affichage futur (heritee d'Object)
        # //////////////////////////////////////////////

    def __str__(self):
        """ methode mettant l'etat courant sous la forme d'une
        chaine de caracteres en prevision d'un futur affichage

        :return representation de l'etat courant sour la forme d'une
        chaine de caracteres
        """
        # A ECRIRE et MODIFIER le return en consequence
        return "sommet n" + str(self.SommetCourant)

