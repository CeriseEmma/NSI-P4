import random
import time


def afficher_regles():
    """Affiche les règles du jeu Puissance 4"""
    print("\n" + "=" * 50)
    print("RÈGLES DU JEU PUISSANCE 4")
    print("=" * 50)
    print("1. Le jeu se joue à deux joueurs (ou contre l'ordinateur).")
    print("2. Chaque joueur place à tour de rôle un jeton dans une colonne.")
    print("3. Le jeton tombe au plus bas de la colonne choisie.")
    print("4. Le premier joueur qui aligne 4 jetons (horizontalement, verticalement ou en diagonale) gagne la partie.")
    print("5. Si la grille est remplie sans alignement de 4 jetons, la partie est déclarée nulle.")
    print("=" * 50 + "\n")
    input("Appuyez sur Entrée pour revenir au menu principal...")


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


def jouer(grille, joueur):
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


def jouer_ordi_facile(grille, pion):
    """
    L'ordinateur en mode facile joue aléatoirement dans une colonne non pleine.
    """
    colonnes_disponibles = []

    # Identifie toutes les colonnes non pleines
    for col in range(7):
        possible, _ = coup_possible(grille, col)
        if possible:
            colonnes_disponibles.append(col)

    # Si aucune colonne n'est disponible (ne devrait pas arriver normalement)
    if not colonnes_disponibles:
        return -1

    # Choisit une colonne au hasard parmi celles disponibles
    colonne_choisie = random.choice(colonnes_disponibles)

    # Trouve la ligne où placer le jeton et le place
    _, ligne = coup_possible(grille, colonne_choisie)
    grille[ligne][colonne_choisie] = pion

    print(f"L'ordinateur joue dans la colonne {colonne_choisie + 1}")
    # Ajoute un délai pour simuler la "réflexion" de l'ordinateur
    time.sleep(1)

    return colonne_choisie


def obtenir_colonnes_disponibles(grille):
    """
    Retourne la liste des colonnes où il est encore possible de jouer.
    """
    colonnes_disponibles = []
    for col in range(7):
        possible, _ = coup_possible(grille, col)
        if possible:
            colonnes_disponibles.append(col)
    return colonnes_disponibles


def simuler_coup(grille, colonne, pion):
    """
    Simule un coup dans la colonne spécifiée sans modifier la grille réelle.
    Retourne une copie de la grille avec le coup joué et l'indice de la ligne où le pion a été placé.
    """
    # Crée une copie profonde de la grille
    grille_copie = [ligne[:] for ligne in grille]

    # Vérifie si le coup est possible
    possible, ligne = coup_possible(grille, colonne)
    if not possible:
        return None, -1

    # Joue le coup sur la copie
    grille_copie[ligne][colonne] = pion

    return grille_copie, ligne


def jouer_ordi_difficile(grille, pion):
    """
    L'ordinateur en mode moyen essaie d'aligner 4 pions si possible,
    ou joue un coup aléatoire sinon.
    """
    # Détermine le pion de l'adversaire
    pion_adversaire = 'O' if pion == 'X' else 'X'

    # 1. Vérifie si l'ordinateur peut gagner en un coup
    colonnes_disponibles = obtenir_colonnes_disponibles(grille)

    # Teste chaque colonne pour voir si jouer dedans permettrait à l'ordinateur de gagner
    for col in colonnes_disponibles:
        grille_test, _ = simuler_coup(grille, col, pion)
        if grille_test and verif_victoire(grille_test, pion):
            # On peut gagner en jouant dans cette colonne
            _, ligne = coup_possible(grille, col)
            grille[ligne][col] = pion
            print(f"L'ordinateur joue dans la colonne {col + 1} et gagne !")
            time.sleep(1)
            return col

    # 2. Vérifie si l'adversaire peut gagner au prochain coup et le bloque
    for col in colonnes_disponibles:
        grille_test, _ = simuler_coup(grille, col, pion_adversaire)
        if grille_test and verif_victoire(grille_test, pion_adversaire):
            # L'adversaire pourrait gagner ici, on le bloque
            _, ligne = coup_possible(grille, col)
            grille[ligne][col] = pion
            print(f"L'ordinateur bloque votre victoire en colonne {col + 1} !")
            time.sleep(1)
            return col

    # 3. Si aucune situation critique, joue aléatoirement
    return jouer_ordi_facile(grille, pion)


def verif_victoire(grille, pion):
    """
    Vérifie si le joueur avec le pion spécifié a gagné.
    Retourne True s'il y a une victoire, False sinon.
    """
    # Vérification horizontale
    for i in range(6):
        for j in range(4):  # Jusqu'à l'indice 3, car on vérifie 4 positions consécutives
            if all(grille[i][j + k] == pion for k in range(4)):
                return True

    # Vérification verticale
    for i in range(3):  # Jusqu'à l'indice 2, car on vérifie 4 positions consécutives
        for j in range(7):
            if all(grille[i + k][j] == pion for k in range(4)):
                return True

    # Vérification diagonale ascendante (/)
    for i in range(3):  # Lignes 0, 1, 2
        for j in range(4):  # Colonnes 0, 1, 2, 3
            if all(grille[i + k][j + k] == pion for k in range(4)):
                return True

    # Vérification diagonale descendante (\)
    for i in range(3):  # Lignes 0, 1, 2
        for j in range(3, 7):  # Colonnes 3, 4, 5, 6
            if all(grille[i + k][j - k] == pion for k in range(4)):
                return True

    return False


def verif_match_nul(grille):
    """
    Vérifie si la grille est complètement remplie (match nul).
    """
    return all(grille[5][j] != 0 for j in range(7))


def partie_deux_joueurs():
    '''
    Fontion qui assemble les autres fonction (grille vide, afficher la grille, jouer ou encore victoire)
    pour pouvoir jouer contre un autre joueur
    '''
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


def partie_contre_ordi(difficulte):
    """
    Gère une partie contre l'ordinateur.
    difficulte : 1 = facile, 2  = difficile
    """
    grille = grille_vide()
    joueur = {'nom': demander_nom(1), 'pion': 'O'}
    ordi = {'nom': 'Ordinateur', 'pion': 'X'}

    # Détermine qui commence
    joueur_commence = None
    while joueur_commence == None:
        choix = input("Voulez-vous jouer en premier ? (O/N) : ").upper()
        if choix == 'O':
            joueur_commence = True
        elif choix == 'N':
            joueur_commence = False
        else:
            print("Choix invalide.")
#    joueur_commence = choix == 'O' or choix == 'N' or choix == ''

    tour = 0 if joueur_commence == True else 1

    modes = {1: "facile", 2: "moyen", 3: "difficile"}
    print(f"\nPartie contre l'ordinateur en mode {modes[difficulte]}...")

    while True:
        affiche_grille(grille)

        if tour % 2 == 0:  # Tour du joueur humain
            jouer(grille, joueur)
            joueur_actuel = joueur
        else:  # Tour de l'ordinateur
            print(f"Tour de {ordi['nom']}...")
            if difficulte == 1:
                jouer_ordi_facile(grille, ordi['pion'])
                joueur_actuel = ordi
            if difficulte == 2:
                jouer_ordi_difficile(grille, ordi['pion'])
                joueur_actuel = ordi

        if verif_victoire(grille, joueur_actuel['pion']):
            affiche_grille(grille)
            if joueur_actuel == joueur:
                print(f"🎉 Bravo ! Vous avez gagné contre l'ordinateur ! 🎉")
            else:
                print(f"L'ordinateur a gagné la partie !")
            break

        if verif_match_nul(grille):
            affiche_grille(grille)
            print("Match nul !")
            break

        tour += 1


def menu_principal():
    """
    Affiche le menu principal et gère les choix de l'utilisateur.
    """
    while True:
        print("\n" + "=" * 30)
        print("PUISSANCE 4 - MENU PRINCIPAL")
        print("=" * 30)
        print("1. Jouer contre un autre joueur")
        print("2. Jouer contre l'ordinateur (facile)")
        print("3. Jouer contre l'ordinateur (difficile)")
        print("4. Règles du jeu")
        print("5. Quitter")
        print("=" * 30)

        try:
            choix = int(input("Votre choix : "))

            if choix == 1:
                partie_deux_joueurs()
            elif choix == 2:
                partie_contre_ordi(difficulte=1)
            elif choix == 3:
                partie_contre_ordi(difficulte=2)
            elif choix == 4:
                afficher_regles()
            elif choix == 5:
                print("Merci d'avoir joué à Puissance 4 !")
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")


# Point d'entrée du programme
if __name__ == "__main__":
    # Initialise le générateur de nombres aléatoires
    random.seed()

    # Affiche un message de bienvenue
    print("\n" + "*" * 50)
    print("*" + " " * 18 + "JEU DE PUISSANCE 4" + " " * 17 + "*")
    print("*" * 50 + "\n")

    # Lance le menu principal
    menu_principal()