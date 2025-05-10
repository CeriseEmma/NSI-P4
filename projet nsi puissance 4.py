def demander_nom(joueur_num):
    return input(f"Joueur {joueur_num}, quel est votre nom ? : ") or f"Joueur {joueur_num}"


def grille_vide():
    return [[0 for _ in range(7)] for _ in range(6)]


def affiche_grille(grille):
    print("  ", end="")
    for j in range(1, 8):
        print(f" {j}", end="")
    print()
    for i in range(5, -1, -1):
        print(f"{i + 1}|", end="")
        for j in range(7):
            val = grille[i][j]
            print(f"{val if val != 0 else ' '}|", end="")
        print()
    print("-" * 17)


def coup_possible(grille, colonne):
    for i in range(6):
        if grille[i][colonne] == 0:
            return True, i
    return False, None


def jouer(grille, joueur):
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
    joueur_1 = {'nom': demander_nom(1), 'pion': 'R'}
    joueur_2 = {'nom': demander_nom(2), 'pion': 'J'}
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


# Lancement direct
if __name__ == "__main__":
    partie_deux_joueurs()
