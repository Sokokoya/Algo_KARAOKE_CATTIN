
###########################################################################################################
######################################### CLASSE PLAYER MODIFIEE ##########################################
###########################################################################################################

class Player:

    #### CONSTRUCTEUR #####
    def __init__(self, name, scores):
        self.__nom = name
        self.__scores = scores



    ##### METHODES #####

    # Méthode qui retourne Vrai si la chanson a déjà été essayée (donc score != 0), sinon, retorune Faux
    def chansonEssayee(self, chanson):

        # La liste des scores sera sous forme de dictionnaire donc on pourra utiliser la chanson pour indexer
        # les scores
        
        if self.__scores[chanson] == 0:
            return False

        return True


    # Méthode calculant la moyenne des scores, sans compter les chansons qui n'ont pas été essayées
    def moyenne(self, chansons):

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
    # TODO : modifier ici pour faire en sorte d'integrer le dictionnaire
    def chansonMeilleurScore(self):

        # on initailise le numero de la chanson avec le meilleur score a 0
        numero = 0

        # comme on a initialisé la variable à 0, on la compare avec la deuxième du tableau scores, soit 1
        for i in range(1, len(self.__scores)):

            # si le score de i est supérieur au score de numéro, la valeur de i écrase numéro
            if self.__scores[i] > self.__scores[numero]:
                numero = i

        return numero


    # Méthode affichant le nom de la chanson ayant eu le pire score
    # TODO : modifier ici pour faire en sorte d'integrer le dictionnaire
    def chansonPireScore(self):

        # on initailise le numero de la chanson avec le pire score a 0
        numero = 0

        # comme on a initialisé la variable à 0, on la compare avec la deuxième du tableau scores, soit 1
        for i in range(1, len(self.__scores)):

            # si le score de i est inférieur au score de numéro, la valeur de i écrase numéro
            if self.__scores[i] < self.__scores[numero]:
                numero = i

        return numero


    # Méthode affichant les scores du joueur en fonction de la liste de chansons passée en paramètre
    def afficherScores(self, chansons):

        # Pour chaque chanson on affiche le titre et le score
        for i in range(0, len(self.__scores)):
            print(chansons[i], ":", self.__scores[i], "/ 100")


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

    def getScoreChanson(self, chanson):
        return self.__scores[self.__scores.index(chanson)]




###########################################################################################################
############################################# CLASSE KARAOKE ##############################################
###########################################################################################################

class Karaoke:

    ##### CONSTRUCTEUR #####
    def __init__(self, chansons, joueurs):
        self.__chansons = chansons  # Tableau de chansons
        self.__joueurs = joueurs    # Tableau de joueurs
        self.__nbChansons = len(self.__chansons) - 1



    ##### METHODES #####

    # Méthode ajoutant une chanson passée en paramètre dans la liste de chansons du karaoké
    def ajoutChanson(self, chanson):
        self.__chansons.append(chanson)
        self.__nbChansons += 1


    # Méthode ajoutant un joueur passé en paramètre dans la liste de joueurs du karaoké
    def ajoutJoueur(self, joueur):
        self.__joueurs.append(joueur)



    # Méthode retirant un joueur passé en paramètre dans la liste de joueurs du karaoké
    def retirerJoueur(self, joueur):

        # Si le joueur est dans la liste de joueurs, on le retire
        # Sinon, il ne se passe rien
        if joueur in self.__joueurs:
            self.__joueurs.remove(joueur)



    # Méthode retournant le meilleur score d'une chanson
    def meilleurScoreChanson(self, titreChanson):

        meilleurScore = self.__joueurs[0].getScores(self.__joueurs[0].chansonMeilleurScore())

        for i in range(1, len(self.__joueurs)):
            if self.__joueurs[i].getScores(self.__joueurs[i].chansonMeilleurScore()) > meilleurScore:
                meilleurScore = self.__joueurs[i].getScores(self.__joueurs[i].chansonMeilleurScore())

        return meilleurScore


    # Méthode retournant le meilleur score toutes chansons confondues
    def meilleurScore(self):

        meilleurScore = self.__joueurs[0].getScores()[self.__joueurs[0].chansonMeilleurScore()]

        for i in range(1, len(self.__joueurs)):
            if self.__joueurs[i].getScores()[self.__joueurs[i].chansonMeilleurScore()] > meilleurScore:
                meilleurScore = self.__joueurs[i].getScores()[self.__joueurs[i].chansonMeilleurScore()]

        return meilleurScore


    # Méthode affichant toutes les caractéristiques du karaoké
    def afficherStatsKaraoke(self):
        print("Joueurs en jeu :", self.__joueurs)
        print()
        print("Chansons jouables :", self.__chansons)
        print()
        print("--- Meilleur score total :", self.meilleurScore())
        print("--- Meilleure moyenne :", self.meilleureMoyenne())

    
    # Méthode permettant d'afficher tous les scores d'une chanson
    def afficherScoresChanson(self, chanson):
        if chanson in self.__chansons:

            for i in range(0, len(self.__joueurs)):
                print(self.__joueurs[i].getName(), ":", self.__joueurs[i].getScoreChanson(chanson))



    # Méthode retournant la meilleure moyenne tout joueurs confondus
    def meilleureMoyenne(self):

        meilleureMoyenne = self.__joueurs[0].moyenne()

        for i in range(1, len(self.__joueurs)):
            if self.__joueurs[i].moyenne() > meilleureMoyenne:
                meilleureMoyenne = self.__joueurs[i].moyenne()

        return meilleureMoyenne



    ##### GETTERS #####

    def getChansons(self):
        return self.__chansons

    def getJoueurs(self):
        return self.__joueurs

    def getNbChansons(self):
        return self.__nbChansons


    

###########################################################################################################
########################################### PROGRAMME PRINCIPAL ###########################################
###########################################################################################################


##### DECLARATION DES VARIABLES #####

# Liste de scores pour chaque joueur, ils sont initialisés avec des valeurs aléatoires
scoresJean = [0, 89, 70, 0, 52, 0]
scoresMarie = [90, 68, 75, 0, 0, 0]
scoresAnne = [0, 78, 0, 85, 63, 0]
scoresJules = [0, 0, 0, 0, 0, 0]

# Initialisation des joueurs
jean = Player("Jean", scoresJean)
marie = Player("Marie", scoresMarie)
anne = Player("Anne", scoresAnne)
jules = Player("Jules", scoresJules)

# Liste des joueurs
joueurs = [jean, marie, anne]

# Liste de chansons
chansons = ["Imagine", "Satisfaction", "Stronger", "Tecnologic", "Aerodynamic", "Sacrifice"]

# Initialisation du karaoké
karaoke = Karaoke(chansons, joueurs)


##### DEBUT DU PROGRAMME #####

# On affiche le karaoke
karaoke.afficherStatsKaraoke()


# On ajoute un nouveau joueur puis on réaffiche le karaoke
karaoke.ajoutJoueur(jules)
karaoke.afficherStatsKaraoke()

# On ajoute une nouvelle chanson au karaoke
karaoke.ajoutChanson("1993")

# On affiche les scores d'une ancienne chanson, puis de la chanson qui vient d'être ajoutée
karaoke.afficherScoresChanson("Imagine")
karaoke.afficherScoresChanson("1993")

# On supprime un joueur et on reaffiche le karaoke
karaoke.retirerJoueur(marie)
karaoke.afficherStatsKaraoke()