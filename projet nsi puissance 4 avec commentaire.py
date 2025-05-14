# Fonction pour demander le nom d'un joueur, avec un nom par défaut si l'utilisateur ne saisit rien
def demander_nom(joueur_num):
    return input(f"Joueur {joueur_num}, quel est votre nom ? : ") or f"Joueur {joueur_num}"

# Fonction qui génère une grille vide de 6 lignes sur 7 colonnes, remplie de zéros (cases vides)
def grille_vide():
    return [[0 for _ in range(7)] for _ in range(6)]

# Fonction pour afficher la grille de jeu dans la console
def affiche_grille(grille):
    print("  ", end="")  # Affiche l'en-tête avec les numéros de colonne
    for j in range(1, 8):
        print(f" {j}", end="")  # Affiche les numéros de colonnes (1 à 7)
    print()
    for i in range(5, -1, -1):  # Affiche les lignes de bas en haut (lignes 6 à 1)
        print(f"{i + 1}|", end="")  # Affiche le numéro de ligne
        for j in range(7):  # Parcourt chaque colonne
            val = grille[i][j]  # Récupère la valeur de la case
            print(f"{val if val != 0 else ' '}|", end="")  # Affiche le pion ou un espace vide
        print()
    print("-" * 17)  # Affiche une ligne de séparation

# Vérifie si un coup est possible dans une colonne donnée (c'est-à-dire s'il y a une case vide)
def coup_possible(grille, colonne):
    for i in range(6):  # Parcourt les lignes de bas en haut
        if grille[i][colonne] == 0:  # Si la case est vide
            return True, i  # Le coup est possible, retourne la ligne
    return False, None  # Si aucune case vide, le coup est impossible

# Fonction qui gère le tour d'un joueur
def jouer(grille, joueur):
    while True:
        try:
            # Demande à l'utilisateur de saisir un numéro de colonne
            col = int(input(f"{joueur['nom']} ({joueur['pion']}), entrez une colonne (1-7) : ")) - 1
            if not 0 <= col <= 6:
                raise ValueError  # Déclenche une erreur si la colonne est hors limites
            possible, ligne = coup_possible(grille, col)  # Vérifie si un coup est possible dans cette colonne
            if possible:
                grille[ligne][col] = joueur['pion']  # Place le pion dans la grille
                return True
            else:
                print("Cette colonne est pleine, choisissez-en une autre.")
        except ValueError:
            print("Entrée invalide. Choisissez un nombre entre 1 et 7.")

# Vérifie s'il y a une victoire pour un pion donné
def verif_victoire(grille, pion):
    # Vérifie les alignements horizontaux
    for i in range(6):
        for j in range(4):  # Seulement jusqu'à la 4e colonne
            if all(grille[i][j + k] == pion for k in range(4)):
                return True
    # Vérifie les alignements verticaux
    for i in range(3):  # Seulement jusqu'à la 3e ligne
        for j in range(7):
            if all(grille[i + k][j] == pion for k in range(4)):
                return True
    # Vérifie les diagonales montantes (/)
    for i in range(3):
        for j in range(4):
            if all(grille[i + k][j + k] == pion for k in range(4)):
                return True
    # Vérifie les diagonales descendantes (\)
    for i in range(3):
        for j in range(3, 7):
            if all(grille[i + k][j - k] == pion for k in range(4)):
                return True
    return False  # Aucune victoire détectée

# Fonction principale qui gère une partie entre deux joueurs humains
def partie_deux_joueurs():
    grille = grille_vide()  # Création de la grille vide
    joueur_1 = {'nom': demander_nom(1), 'pion': 'R'}  # Joueur 1 avec le pion rouge
    joueur_2 = {'nom': demander_nom(2), 'pion': 'J'}  # Joueur 2 avec le pion jaune
    joueurs = [joueur_1, joueur_2]  # Liste des joueurs
    tour = 0  # Compteur de tours

    while True:
        affiche_grille(grille)  # Affiche l'état actuel de la grille
        joueur_actuel = joueurs[tour % 2]  # Détermine quel joueur doit jouer
        jouer(grille, joueur_actuel)  # Fait jouer le joueur
        if verif_victoire(grille, joueur_actuel['pion']):  # Vérifie s'il a gagné
            affiche_grille(grille)
            print(f"2 {joueur_actuel['nom']} a gagné la partie ! ")
            break  # Fin de la partie
        if all(grille[5][j] != 0 for j in range(7)):  # Vérifie si la grille est pleine (match nul)
            affiche_grille(grille)
            print("Match nul !")
            break
        tour += 1  # Passe au tour suivant

# Exécution du jeu si le script est lancé directement
if __name__ == "__main__":
    partie_deux_joueurs()
