def deux_joueur():
    joueur_1 = str(input("Joueur 1 quel est votre nom? : "))
    joueur_2 = str(input("Joueur 2 quel est votre nom? : "))
    return joueur_1, joueur_2


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
            print(f"{grille[i][j]}|", end="")
        print()
    # Affichage du bas de la grille
    print("-" * 15)


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
    return False, 0  # Indique si la colonne est pleinne et qu'il y ai impossible de jouer.


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
    colonne = int(input("Dans quelle colonne voulez vous jouez? : ")) -1

    # Input à tester pour que le joueur ne sorte pas du cadre de la grille
    # 1 -> 7 donc il faut éliminer les valeurs inférieures à 1 et celles
    # supérieures à 7

    possible, ligne = coup_possible(grille, colonne)
    if possible:
        if j == 1:
            grille[ligne][colonne] = 'B'
        if j == 2:
            grille[ligne][colonne] = 'V'
    else:
        print("Vous ne pouvez pas jouer ici")
    return grille


grille = grille_vide()
j_1, j_2 = deux_joueur()
#print(coup_possible(grille, int(input("Dans quelle colonne voulez vous jouer? : "))))

while True:
    affiche_grille(grille)
    print(f"{j_1} a vous de jouer!")
    grille = jouer(grille, 1)
    affiche_grille(grille)
    print(f"{j_2} a vous de jouer!")
    grille = jouer(grille, 2)

