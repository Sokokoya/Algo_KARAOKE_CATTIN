
###########################################################################################################
############################################## CLASSE PLAYER ##############################################
###########################################################################################################

class Player:

    #### CONSTRUCTEUR #####
    def __init__(self, name, scores):
        self.__nom = name
        self.__scores = scores



    ##### METHODES #####

    # Méthode qui retourne Vrai si la chanson a déjà été essayée (donc score != 0), sinon, retorune Faux
    def chansonEssayee(self, chanson):
        if self.__scores[chanson] == 0:
            return False

        return True


    # Méthode calculant la moyenne des scores, sans compter les chansons qui n'ont pas été essayées
    def moyenne(self):

        add = 0
        compteur = 0

        # on ne prend en compte que les chansons qui ont été essayées dans la moyenne, puis on additionne
        # tous leurs scores ensemble
        for i in range (0, len(self.__scores)):
            if self.chansonEssayee(i):
                add += self.__scores[i]
                compteur += 1

        # on divise l'addition des scores par le nombre de chansons qui ont été essayées
        return add / compteur

    
    # Méthode calculant le score total du joueur
    def scoreTotal(self):

        somme = 0

        for i in range (0, len(self.__scores)):
            somme += self.__scores[i]

        return somme


    # Méthode affichant le numéro de la chanson ayant eu le meilleur score
    def chansonMeilleurScore(self):

        # on initailise le numero de la chanson avec le meilleur score a 0
        numero = 0

        # comme on a initialisé la variable à 0, on la compare avec la deuxième du tableau scores, soit 1
        for i in range(1, len(self.__scores)):

            # si le score de i est supérieur au score de numéro, la valeur de i écrase numéro
            if self.__scores[i] > self.__scores[numero]:
                numero = i

        return numero


    # Méthode affichant le numéro de la chanson ayant eu le pire score
    def chansonPireScore(self):

        # on initailise le numero de la chanson avec le pire score a 0
        numero = 0

        # comme on a initialisé la variable à 0, on la compare avec la deuxième du tableau scores, soit 1
        for i in range(1, len(self.__scores)):

            # si le score de i est inférieur au score de numéro, la valeur de i écrase numéro
            if self.__scores[i] < self.__scores[numero]:
                numero = i

        return numero


    # Méthode affichant les scores du joueur
    def afficherScores(self):

        # Pour chaque chanson on affiche l'identifiant et le score
        for i in range(0, len(self.__scores)):
            print("Chanson", i, " :", self.__scores[i], "/ 100")


    # Méthode ajoutant un nouveau score
    def ajoutScore(self, chanson, score):

        # Si le nouveau score passé en paramètre est supérieur au meilleur score enregistré pour cette chanson,
        # on remplace le score dans le tableau du joueur avec le nouveau
        # Sinon, l'ancien score reste
        if self.__scores[chanson] < score:
            self.__scores[chanson] = score


    # Méthode affichant toutes les caractéristiques d'un joueur
    def afficherJoueur(self):
        print(self.__nom)
        self.afficherScores()
        print()
        print("Chanson avec le pire score : Chanson", self.chansonPireScore())
        print("Chanson avec le meilleur score : Chanson", self.chansonMeilleurScore())
        print()
        print("--- Moyenne :", self.moyenne(), "/ 100")
        print("--- Score Total :", self.scoreTotal())




    ##### GETTERS #####

    def getNom(self):
        return self.__nom

    def getScores(self):
        return self.__scores



###########################################################################################################
########################################### PROGRAMME PRINCIPAL ###########################################
###########################################################################################################


##### DECLARATION DES VARIABLES #####

# Tableaux de scores pour chaque joueur, ils sont initialisés avec des valeurs aléatoires
scoresJean = [0, 89, 70, 0, 52]
scoresMarie = [90, 68, 75, 0, 0]
scoresAnne = [0, 78, 0, 85, 63]

# Initialisation des joueurs
jean = Player("Jean", scoresJean)
marie = Player("Marie", scoresMarie)
anne = Player("Anne", scoresAnne)


##### DEBUT DU PROGRAMME #####

# On affiche chaque joueur
jean.afficherJoueur()
print()
marie.afficherJoueur()
print()
anne.afficherJoueur()


# On ajoute de nouveaux scores à chaque joueurs
jean.ajoutScore(4, 78)
jean.ajoutScore(4, 67)

marie.ajoutScore(3, 56)

anne.ajoutScore(3, 75)
anne.ajoutScore(4, 75)


# On réaffiche les scores une fois les nouveaux scores ajoutés
input()

jean.afficherJoueur()
print()
marie.afficherJoueur()
print()
anne.afficherJoueur()