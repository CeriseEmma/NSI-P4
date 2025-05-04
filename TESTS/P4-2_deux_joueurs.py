def deux_joueur():
    """Demande et renvoie les noms des deux joueurs."""
    joueur_1 = input("Joueur 1 quel est votre nom? : ")
    joueur_2 = input("Joueur 2 quel est votre nom? : ")
    return joueur_1, joueur_2
    # Cette fonction demande simplement le nom des deux joueurs et les renvoie
    # sous forme de tuple (joueur_1, joueur_2)


def grille_vide():
    """
    Construit un tableau à deux dimensions de taille 6 x 7 (6 lignes et 7 colonnes).
    Chaque case contient la valeur 0.
    Renvoie le tableau grille.
    """
    grille = []  # Initialisation d'une liste vide qui va contenir notre grille
    for i in range(6):  # Boucle sur les 6 lignes
        tab = []  # Création d'une ligne vide
        for j in range(7):  # Boucle sur les 7 colonnes
            tab.append(0)  # Ajout d'un 0 dans chaque case (représente une case vide)
        grille.append(tab)  # Ajout de la ligne complète à notre grille
    return grille  # Renvoie la grille complète initialisée avec des zéros


def affiche_grille(grille):
    """
    Affiche la grille de jeu dans le terminal avec un design amélioré.
    Utilise des caractères Unicode et des couleurs ANSI si disponibles.
    """
    # Définition des codes couleurs ANSI pour les terminaux compatibles
    ROUGE = '\033[91m'  # Code pour la couleur rouge
    JAUNE = '\033[93m'  # Code pour la couleur jaune
    BLEU = '\033[94m'   # Code pour la couleur bleue
    RESET = '\033[0m'   # Code pour réinitialiser la couleur

    # Caractères pour représenter les pions et les cases vides
    VIDE = " "          # Espace pour les cases vides
    PION_B = "●"        # Cercle plein pour les pions du joueur 1 (Bleu)
    PION_V = "●"        # Cercle plein pour les pions du joueur 2 (Jaune/Vert)

    # Affichage des numéros des colonnes en haut de la grille
    print("\n     ", end="")  # Décalage initial pour aligner les colonnes
    for j in range(1, 8):     # Boucle de 1 à 7 pour numéroter les colonnes
        print(f" {j}  ", end="")  # Affiche le numéro de chaque colonne
    print()  # Saut de ligne après les numéros de colonnes

    # Dessin de la bordure supérieure de la grille avec des caractères Unicode
    print("    ┌" + "───┬" * 6 + "───┐")  # Ligne du haut avec coins et séparateurs

    # Dessin des lignes de la grille avec leur contenu
    for i in range(5, -1, -1):  # Parcours des lignes de bas en haut (5 à 0)
        print(f" {i + 1}  │", end="")  # Affiche le numéro de ligne et le bord gauche
        for j in range(7):  # Parcours des 7 colonnes
            if grille[i][j] == 0:  # Si la case est vide (contient 0)
                print(f" {VIDE} │", end="")  # Affiche un espace
            elif grille[i][j] == 'B':  # Si la case contient un pion Bleu
                print(f" {BLEU}{PION_B}{RESET} │", end="")  # Affiche un cercle bleu
            else:  # Si la case contient un pion Vert/Jaune
                print(f" {JAUNE}{PION_V}{RESET} │", end="")  # Affiche un cercle jaune
        print()  # Saut de ligne à la fin de chaque ligne

        # Dessin des séparateurs horizontaux entre les lignes
        if i > 0:  # Si ce n'est pas la dernière ligne
            print("    ├" + "───┼" * 6 + "───┤")  # Séparateur avec croix
        else:  # Pour la dernière ligne
            print("    └" + "───┴" * 6 + "───┘")  # Bordure inférieure avec coins


def coup_possible(grille, colonne):
    """
    Détermine s'il est possible de jouer dans la colonne spécifiée.
    Renvoie (True, ligne) si possible, (False, 0) sinon.
    """
    for i in range(6):  # Parcourt toutes les lignes de bas en haut
        if grille[i][colonne] == 0:  # Si la case est vide (contient 0)
            return True, i  # Retourne True et l'indice de la ligne où placer le pion
    # Si on arrive ici, c'est que la colonne est pleine
    return False, 0  # Retourne False et 0 par défaut


def verifier_victoire(grille, symbole):
    """
    Vérifie si le joueur avec le symbole donné a gagné.
    Renvoie True si victoire, False sinon.
    """
    # Vérification horizontale (alignement sur une ligne)
    for i in range(6):  # Parcourt toutes les lignes
        for j in range(4):  # Parcourt les 4 premières colonnes (pour avoir 4 cases alignées)
            if (grille[i][j] == symbole and grille[i][j + 1] == symbole and
                    grille[i][j + 2] == symbole and grille[i][j + 3] == symbole):
                return True  # Victoire trouvée

    # Vérification verticale (alignement sur une colonne)
    for i in range(3):  # Parcourt les 3 premières lignes
        for j in range(7):  # Parcourt toutes les colonnes
            if (grille[i][j] == symbole and grille[i + 1][j] == symbole and
                    grille[i + 2][j] == symbole and grille[i + 3][j] == symbole):
                return True  # Victoire trouvée

    # Vérification diagonale montante (de bas gauche à haut droite)
    for i in range(3):  # Parcourt les 3 premières lignes
        for j in range(4):  # Parcourt les 4 premières colonnes
            if (grille[i][j] == symbole and grille[i + 1][j + 1] == symbole and
                    grille[i + 2][j + 2] == symbole and grille[i + 3][j + 3] == symbole):
                return True  # Victoire trouvée

    # Vérification diagonale descendante (de haut gauche à bas droite)
    for i in range(3, 6):  # Parcourt les 3 dernières lignes
        for j in range(4):  # Parcourt les 4 premières colonnes
            if (grille[i][j] == symbole and grille[i - 1][j + 1] == symbole and
                    grille[i - 2][j + 2] == symbole and grille[i - 3][j + 3] == symbole):
                return True  # Victoire trouvée

    # Si aucune victoire n'a été trouvée
    return False


def grille_pleine(grille):
    """
    Vérifie si la grille est pleine.
    Renvoie True si pleine, False sinon.
    """
    for j in range(7):  # Parcourt toutes les colonnes
        if coup_possible(grille, j)[0]:  # Vérifie si on peut jouer dans cette colonne
            return False  # Si au moins une colonne permet de jouer, la grille n'est pas pleine
    return True  # Si aucune colonne ne permet de jouer, la grille est pleine


def jouer(grille, j, j_nom):
    """
    Joue un coup du joueur j dans la colonne choisie.
    Renvoie la grille mise à jour et un booléen indiquant si le coup a été joué.
    """
    while True:  # Boucle infinie jusqu'à ce qu'un coup valide soit joué
        try:  # Bloc try/except pour gérer les erreurs de saisie
            # Demande la colonne au joueur (1-7) et convertit en indice (0-6)
            colonne = int(input(f"{j_nom}, dans quelle colonne voulez-vous jouer? (1-7) : ")) - 1

            # Vérification que la colonne est valide (entre 0 et 6)
            if colonne < 0 or colonne > 6:
                print("Erreur: Veuillez entrer un nombre entre 1 et 7.")
                continue  # Retourne au début de la boucle pour une nouvelle saisie

            # Vérifie si le coup est possible dans la colonne choisie
            possible, ligne = coup_possible(grille, colonne)
            if possible:  # Si le coup est possible
                if j == 1:  # Si c'est le joueur 1
                    grille[ligne][colonne] = 'B'  # Place un pion Bleu
                else:  # Si c'est le joueur 2
                    grille[ligne][colonne] = 'V'  # Place un pion Vert/Jaune
                return grille, True  # Retourne la grille mise à jour et True (coup joué)
            else:  # Si la colonne est pleine
                print("Cette colonne est pleine. Veuillez choisir une autre colonne.")
                # Continue la boucle pour une nouvelle saisie
        except ValueError:  # Gère les erreurs de conversion (si l'utilisateur n'entre pas un nombre)
            print("Erreur: Veuillez entrer un nombre valide.")
            # Continue la boucle pour une nouvelle saisie


def puissance4():
    """Fonction principale du jeu Puissance 4."""
    print("\n===== PUISSANCE 4 =====\n")  # Affiche le titre du jeu
    j_1, j_2 = deux_joueur()  # Demande les noms des joueurs
    grille = grille_vide()   # Initialise la grille vide
    tour = 0  # Compteur de tours initialisé à 0

    while True:  # Boucle principale du jeu
        tour += 1  # Incrémente le compteur de tours
        affiche_grille(grille)  # Affiche l'état actuel de la grille

        # Tour du joueur 1
        print(f"\nTour {tour}: {j_1} (B) à vous de jouer!")  # Annonce le tour du joueur 1
        grille, coup_joue = jouer(grille, 1, j_1)  # Le joueur 1 joue son coup
        if not coup_joue:  # Si le coup n'a pas été joué (ne devrait pas arriver avec la boucle dans jouer())
            continue  # Passe au tour suivant

        affiche_grille(grille)  # Affiche la grille après le coup du joueur 1

        # Vérification de victoire du joueur 1
        if verifier_victoire(grille, 'B'):  # Vérifie si le joueur 1 a gagné
            print(f"\nFélicitations! {j_1} a gagné en {tour} tours!")  # Message de victoire
            break  # Fin de la partie

        # Vérification de match nul
        if grille_pleine(grille):  # Vérifie si la grille est pleine (match nul)
            print("\nMatch nul! La grille est pleine.")  # Message de match nul
            break  # Fin de la partie

        # Tour du joueur 2
        print(f"\nTour {tour}: {j_2} (V) à vous de jouer!")  # Annonce le tour du joueur 2
        grille, coup_joue = jouer(grille, 2, j_2)  # Le joueur 2 joue son coup
        if not coup_joue:  # Si le coup n'a pas été joué
            continue  # Passe au tour suivant

        # Vérification de victoire du joueur 2
        if verifier_victoire(grille, 'V'):  # Vérifie si le joueur 2 a gagné
            affiche_grille(grille)  # Affiche la grille finale
            print(f"\nFélicitations! {j_2} a gagné en {tour} tours!")  # Message de victoire
            break  # Fin de la partie

        # Vérification de match nul après le coup du joueur 2
        if grille_pleine(grille):  # Vérifie si la grille est pleine
            affiche_grille(grille)  # Affiche la grille finale
            print("\nMatch nul! La grille est pleine.")  # Message de match nul
            break  # Fin de la partie

    # Proposition de rejouer une fois la partie terminée
    rejouer = input("\nVoulez-vous rejouer? (o/n) : ")  # Demande si les joueurs veulent rejouer
    if rejouer.lower() == 'o':  # Si la réponse est oui (o ou O)
        puissance4()  # Relance une nouvelle partie (appel récursif)
    else:  # Si la réponse est non
        print("\nMerci d'avoir joué! À bientôt!")  # Message de fin


# Point d'entrée du programme
if __name__ == "__main__":  # Vérifie si le script est exécuté directement (et non importé)
    puissance4()  # Lance le jeu
