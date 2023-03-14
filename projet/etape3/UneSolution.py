"""  module pour la classe UneSolution """
import random

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution


class UneSolution(Solution):
    """  
    Classe pour definir une solution pour le cas 3 de la tache 2 (hérite de Solution)
    """

    #    attributs
    #    A COMPLETER
    #    //////////////////////////////////////////////
    tg: GrapheDeLieux
    chemin: list
    """  le graphe representant le monde """

    #    constructeurs
    #    A ECRIRE/COMPLETER
    #    //////////////////////////////////////////////
    def __init__(self, tg: GrapheDeLieux, sommetDepart=0, chemin=None):
        """  constructeur d'une solution a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        """
        #    A ECRIRE en completant eventuellement par des parametres optionnels
        self.tg = tg
        self.SommetDepart = sommetDepart
        if (chemin == None):
            sol = self.nelleSolution()
            self.chemin=sol.chemin.copy()
        else:
            self.chemin = chemin

    #    methodes de la classe abstraite Solution
    #    //////////////////////////////////////////////
    def lesVoisins(self):
        """  methode recuperant la liste des voisins de la solution courante
        
        :return liste des voisins de la solution courante
        """
        #    A ECRIRE et MAJ la valeur retournee
        Voisins = []
        nombrePermutation = len(self.chemin)

        while nombrePermutation > 0:
            indice_a = random.randint(1, len(self.chemin) - 2)
            indice_b = random.randint(1, len(self.chemin) - 2)
            while (indice_a == indice_b):
                indice_b = random.randint(1, len(self.chemin) - 2)
            nouveau_chemin = self.chemin.copy()
            nouveau_chemin[indice_a], nouveau_chemin[indice_b] = nouveau_chemin[indice_b], nouveau_chemin[indice_a]
            voisin = UneSolution(self.tg, self.SommetDepart, nouveau_chemin)
            Voisins.append(voisin)
            nombrePermutation -= 1

        return Voisins

    def unVoisin(self):
        """  methode recuperant un voisin de la solution courante
        
        :return voisin de la solution courante
        """
        #    A ECRIRE et MAJ la valeur retournee
        meilleurVoisin = self
        for voisin in self.lesVoisins():
            if (voisin.eval() < meilleurVoisin.eval()):
                meilleurVoisin = voisin
        return [meilleurVoisin]

    def eval(self):
        """  methode recuperant la valeur de la solution courante
        
        :return valeur de la solution courante
        """
        #    A ECRIRE et MAJ la valeur retournee
        val = 0
        for indice in range(len(self.chemin) - 1):
            val+=GrapheDeLieux.dist(self.chemin[indice],self.chemin[indice+1],self.tg)
        return val

    def nelleSolution(self):
        """  methode generant aleatoirement une nouvelle solution 
        a partir de la solution courante
        
        :return nouvelle solution generee aleatoirement a partir de la solution courante
        """
        #    A ECRIRE et MAJ la valeur retournee
        Sommet_Non_Visite = self.tg.getSommets()
        Sommet_Non_Visite.remove(self.SommetDepart)
        Sommet_Visite = [self.SommetDepart]
        while Sommet_Non_Visite:
            position = random.randint(0, len(Sommet_Non_Visite) - 1)
            sommet_courant = Sommet_Non_Visite[position]
            Sommet_Visite.append(sommet_courant)
            Sommet_Non_Visite.remove(sommet_courant)
        Sommet_Visite.append(self.SommetDepart)
        return UneSolution(self.tg,self.SommetDepart,Sommet_Visite)

    def displayPath(self):
        """  methode affichant la solution courante comme un chemin dans le graphe
        """
        #    A ECRIRE
        print("la meilleure solution est :", self.chemin," avec un cout de :", self.eval())

    #    methodes pour pouvoir utiliser cet objet dans des listes et des map
    #    //////////////////////////////////////////////
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

        if not isinstance(o, UneSolution):
            return False
        if self.SommetDepart != o.SommetDepart:
            return False
        if len(self.chemin) != len(o.chemin):
            return False

        constante = True
        for i in range(len(self.chemin)):
            if self.chemin[i] != o.chemin[i]:
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
        return "chemin" + str(self.chemin) + " cout : " + str(self.eval())
