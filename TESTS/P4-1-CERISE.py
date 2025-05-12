import random

def demander_nom(joueur_num):
    return input(f"Joueur {joueur_num}, quel est votre nom ? : ") or f"Joueur {joueur_num}"


def grille_vide():
    '''
    Fonction grille_vide():
    La fonction construit un tableau à deux dimensions de taille 6 x 7 : 6 lignes et 7 colonnes.
    Chaque case contient la valeur 0.
    La fonction ne prend pas d'argument.
    La fonction renvoie le tableau grillle[]
    '''
    global grille
    grille = []  # Création du tableau global
    for i in range(6):
        tab = []  # Création des 6 sous tableau qui serviront à afficher les différentes lignes du tableau
        for j in range(7):
            tab.append(0)  # Chaque case de chaque ligne prend la valeur 0
        grille.append(tab)
    return grille


def affiche_grille(grille):
    '''
    Affiche la grille de jeu dans le terminal avec les indices des colonnes inversés.
    Les colonnes sont numérotées de droite à gauche (6 à 0) au lieu de gauche à droite.
    '''
    # Affichage des indices des colonne
    print(" ", end="")
    for j in range(1, 8):  # Parcourt de 0 à 6 (Croissant)
        print(f" {j}", end="")
    print()

    # Affichage des indices des lignes
    for i in range(5, -1, -1):
        print(f"{i + 1}|", end="")
        for j in range(7):  # Parcourt de 6 à 0 (Décroissant).
            # Cette inversion facilite la gestion des pions pour les fonctions futurs
            val = grille[i][j]
            print(f"{val if val != 0 else ' '}|", end="")
        print()
    # Affichage du bas de la grille
    print("-" * 17)


def coup_possible(grille, colonne):
    '''
    détermine s'il est possible de jouer dans la colonne col
    Prend en argumment la grille, tableau de 7x6, avec la position des pions des joueurs et un entier,
    le numméro de colonne entre 0 et 6
    renvois True s'il est possible de jouer dans la colonne col, False sinon.
    Il est possible de jouer dans la colenne col, s'il existe une case avec la valeur 0 dans cette colonne.
    '''
#    colonne = colonne - 1
    #Je ne sais pas pourquoi mais mes indices commencent à -1 donc j'ai due rajouter ça.
    for i in range(6):
        if grille[i][colonne] == 0:  # Parcours la colonne choisie par indice croissant
            return True, i  # Renvoie le plus petit indice de la ligne ou il est possible de jouer.
    return False, None  # Indique si la colonne est pleinne et qu'il y ai impossible de jouer.


def jouer(grille, j):
    '''
    Fonction jouer(grille, j, colonne):
    Fonction qui joue un coup du joueur j dans la colonne col de la grille. Arguments:
    grille est la grille de 7 x 6 avec les pions des joueurs
    j est un entier qui a la valeur 1 ou 2 suivant le joueur.
    colonne est un entier entre 1 et 7 et désigne une colonne non pleine de la grille.
    Si j vaut 1 la première case vide de la colonne prendra la valeur B
    Si j vaut 2 la première case vide de la colonne col prendra la valeur V
    '''
    while True:
        try:
            col = int(input(f"{joueur['nom']} ({joueur['pion']}), entrez une colonne (1-7) : ")) - 1
            if not 0 <= col <= 6:
                raise ValueError
            possible, ligne = coup_possible(grille, col)
            if possible:
                grille[ligne][col] = joueur['pion']
                return True
            else:
                print("Cette colonne est pleine, choisissez-en une autre.")
        except ValueError:
            print("Entrée invalide. Choisissez un nombre entre 1 et 7.")


def jouer_ordi(grille, col):
    grille[ligne][col] = joueur['pion']
    return True


def verif_victoire(grille, pion):
    # Horizontal
    for i in range(6):
        for j in range(4):
            if all(grille[i][j + k] == pion for k in range(4)):
                return True
    # Vertical
    for i in range(3):
        for j in range(7):
            if all(grille[i + k][j] == pion for k in range(4)):
                return True
    # Diagonale /
    for i in range(3):
        for j in range(4):
            if all(grille[i + k][j + k] == pion for k in range(4)):
                return True
    # Diagonale \
    for i in range(3):
        for j in range(3, 7):
            if all(grille[i + k][j - k] == pion for k in range(4)):
                return True
    return False


def partie_deux_joueurs():
    grille = grille_vide()
    joueur_1 = {'nom': demander_nom(1), 'pion': 'O'}
    joueur_2 = {'nom': demander_nom(2), 'pion': 'X'}
    joueurs = [joueur_1, joueur_2]
    tour = 0

    while True:
        affiche_grille(grille)
        joueur_actuel = joueurs[tour % 2]
        jouer(grille, joueur_actuel)
        if verif_victoire(grille, joueur_actuel['pion']):
            affiche_grille(grille)
            print(f"🎉 {joueur_actuel['nom']} a gagné la partie ! 🎉")
            break
        if all(grille[5][j] != 0 for j in range(7)):  # si la ligne du haut est remplie
            affiche_grille(grille)
            print("Match nul !")
            break
        tour += 1


def ordinateur_1():
    while True
    nb_colonne = randint(1,7)
    if coup_possible(grille, nb_colonne) == True:
        jouer_ordi(grille, nb_colonne)
        break

def partie_facile()
    grille = grille_vide()
    joueur_1 = {'nom': demander_nom(1), 'pion': 'O'}
    joueur_2 = {'nom': 'Ordinateur', 'pion': 'X'}
    joueurs = [joueur_1, joueur_2]
    tour = 0

    while True:
        affiche_grille(grille)
        joueur_actuel = joueurs[tour % 2]
        if joueur_actuel == joueur_1
            jouer(grille, joueur_actuel)
        if joueur_actuel == joueur_2
            jouer_ordi(grille, joueur_actuel)
        if verif_victoire(grille, joueur_actuel['pion']):
            affiche_grille(grille)
            print(f"🎉 {joueur_actuel['nom']} a gagné la partie ! 🎉")
            break
        if all(grille[5][j] != 0 for j in range(7)):  # si la ligne du haut est remplie
            affiche_grille(grille)
            print("Match nul !")
            break
        tour += 1

# Lancement direct
if __name__ == "__main__":
    partie_facile()
