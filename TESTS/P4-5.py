import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import copy


##########################################
# PARTIE 1: MODÈLE DU JEU (LOGIQUE)     #
##########################################

def grille_vide():
    """
    Construit un tableau à deux dimensions de taille 6 x 7 (6 lignes et 7 colonnes).
    Chaque case contient la valeur 0 (case vide).

    Returns:
        list: Un tableau 2D représentant la grille vide
    """
    grille = []
    for i in range(6):
        ligne = []
        for j in range(7):
            ligne.append(0)  # 0 représente une case vide
        grille.append(ligne)
    return grille


def coup_possible(grille, colonne):
    """
    Détermine s'il est possible de jouer dans la colonne spécifiée.

    Args:
        grille (list): La grille de jeu
        colonne (int): L'indice de la colonne à vérifier

    Returns:
        tuple: (True, ligne) si possible, (False, 0) sinon.
              'ligne' est l'indice de la première case vide de la colonne.
    """
    for i in range(6):
        if grille[i][colonne] == 0:
            return True, i
    return False, 0


def grille_pleine(grille):
    """
    Vérifie si la grille est pleine.

    Args:
        grille (list): La grille de jeu

    Returns:
        bool: True si la grille est pleine, False sinon
    """
    for j in range(7):
        if coup_possible(grille, j)[0]:
            return False
    return True


def verifier_victoire(grille, symbole):
    """
    Vérifie si le joueur avec le symbole donné a gagné.

    Args:
        grille (list): La grille de jeu
        symbole (str): Le symbole du joueur ('B' pour bleu, 'V' pour jaune/vert)

    Returns:
        bool: True si victoire, False sinon
    """
    # Vérification horizontale
    for i in range(6):
        for j in range(4):  # De 0 à 3 (pour avoir 4 cases consécutives jusqu'à la colonne 6)
            if (grille[i][j] == symbole and grille[i][j + 1] == symbole and
                    grille[i][j + 2] == symbole and grille[i][j + 3] == symbole):
                return True

    # Vérification verticale
    for i in range(3):  # De 0 à 2 (pour avoir 4 cases consécutives jusqu'à la ligne 5)
        for j in range(7):
            if (grille[i][j] == symbole and grille[i + 1][j] == symbole and
                    grille[i + 2][j] == symbole and grille[i + 3][j] == symbole):
                return True

    # Vérification diagonale (montante)
    for i in range(3):  # De 0 à 2
        for j in range(4):  # De 0 à 3
            if (grille[i][j] == symbole and grille[i + 1][j + 1] == symbole and
                    grille[i + 2][j + 2] == symbole and grille[i + 3][j + 3] == symbole):
                return True

    # Vérification diagonale (descendante)
    for i in range(3, 6):  # De 3 à 5
        for j in range(4):  # De 0 à 3
            if (grille[i][j] == symbole and grille[i - 1][j + 1] == symbole and
                    grille[i - 2][j + 2] == symbole and grille[i - 3][j + 3] == symbole):
                return True

    return False


##########################################
# PARTIE 2: IA DE L'ORDINATEUR          #
##########################################

def coup_gagnant(grille, symbole):
    """
    Vérifie si un joueur avec le symbole donné peut gagner en un coup.

    Args:
        grille (list): La grille de jeu
        symbole (str): Le symbole du joueur ('B' pour bleu, 'V' pour jaune/vert)

    Returns:
        int ou None: Le numéro de colonne pour gagner, ou None si pas de coup gagnant
    """
    # Teste chaque colonne où il est possible de jouer
    for col in range(7):
        possible, ligne = coup_possible(grille, col)
        if possible:
            # Simule le coup en créant une copie de la grille
            grille_temp = copy.deepcopy(grille)
            grille_temp[ligne][col] = symbole
            # Vérifie si ce coup est gagnant
            if verifier_victoire(grille_temp, symbole):
                return col

    return None  # Pas de coup gagnant trouvé


# ---- Mode facile ----

def coup_ordi_facile(grille):
    """
    L'ordinateur joue un coup aléatoire dans une colonne disponible.
    Mode facile - totalement aléatoire.

    Args:
        grille (list): La grille de jeu

    Returns:
        int: L'indice de la colonne choisie
    """
    # Liste des colonnes où il est possible de jouer
    colonnes_disponibles = []
    for col in range(7):
        if coup_possible(grille, col)[0]:
            colonnes_disponibles.append(col)

    # Choix aléatoire d'une colonne disponible
    if colonnes_disponibles:
        return random.choice(colonnes_disponibles)
    return None  # Ne devrait jamais arriver si la grille n'est pas pleine


# ---- Mode moyen ----

def coup_ordi_moyen(grille):
    """
    L'ordinateur joue de façon plus intelligente.
    Mode moyen - cherche à gagner ou à bloquer l'adversaire.

    Args:
        grille (list): La grille de jeu

    Returns:
        int: L'indice de la colonne choisie
    """
    # Vérifie d'abord si l'ordinateur peut gagner en un coup
    col_gagnante = coup_gagnant(grille, 'V')
    if col_gagnante is not None:
        return col_gagnante

    # Sinon, vérifie si l'adversaire peut gagner et bloque son coup
    col_bloquante = coup_gagnant(grille, 'B')
    if col_bloquante is not None:
        return col_bloquante

    # Si aucun coup critique, joue aléatoirement
    return coup_ordi_facile(grille)


# ---- Mode difficile (Minimax) ----

def evaluer_fenetre(fenetre, symbole):
    """
    Évalue la valeur d'une fenêtre de 4 cases pour le symbole donné.
    Cette fonction attribue des scores en fonction des configurations de pions.

    Args:
        fenetre (list): Une liste de 4 valeurs représentant 4 cases consécutives
        symbole (str): Le symbole du joueur à évaluer

    Returns:
        int: Score attribué à cette configuration
    """
    score = 0
    symbole_adverse = 'B' if symbole == 'V' else 'V'

    # Compte les pions du joueur et les cases vides dans la fenêtre
    count_symbole = fenetre.count(symbole)
    count_vide = fenetre.count(0)
    count_adverse = fenetre.count(symbole_adverse)

    # Attribution des scores selon les configurations
    if count_symbole == 4:
        score += 100  # Victoire
    elif count_symbole == 3 and count_vide == 1:
        score += 5  # Possibilité de gagner au prochain coup
    elif count_symbole == 2 and count_vide == 2:
        score += 2  # Possibilité de créer une menace

    # Pénalité pour les alignements adverses
    if count_adverse == 3 and count_vide == 1:
        score -= 4  # Bloquer l'adversaire est important

    return score


def evaluer_position_minimax(grille, symbole):
    """
    Évalue la valeur de la position actuelle pour le symbole donné.
    Utilise des fenêtres de 4 cases dans toutes les directions.

    Args:
        grille (list): La grille de jeu
        symbole (str): Le symbole du joueur à évaluer

    Returns:
        int: Score global de la position
    """
    score = 0

    # Score pour le centre (stratégiquement avantageux)
    centre = [grille[i][3] for i in range(6)]  # Colonne du milieu
    count_centre = centre.count(symbole)
    score += count_centre * 3  # Bonus pour les pions au centre

    # Évaluation horizontale
    for i in range(6):
        for j in range(4):
            fenetre = [grille[i][j + k] for k in range(4)]
            score += evaluer_fenetre(fenetre, symbole)

    # Évaluation verticale
    for i in range(3):
        for j in range(7):
            fenetre = [grille[i + k][j] for k in range(4)]
            score += evaluer_fenetre(fenetre, symbole)

    # Évaluation diagonale (montante)
    for i in range(3):
        for j in range(4):
            fenetre = [grille[i + k][j + k] for k in range(4)]
            score += evaluer_fenetre(fenetre, symbole)

    # Évaluation diagonale (descendante)
    for i in range(3, 6):
        for j in range(4):
            fenetre = [grille[i - k][j + k] for k in range(4)]
            score += evaluer_fenetre(fenetre, symbole)

    return score


def est_terminal(grille):
    """
    Vérifie si la position est terminale (victoire ou match nul).

    Args:
        grille (list): La grille de jeu

    Returns:
        tuple: (True, valeur) si terminal, (False, 0) sinon
               'valeur' est le score attribué à cette position terminale
    """
    # Vérification de victoire
    if verifier_victoire(grille, 'V'):
        return True, 1000000  # Victoire de l'ordinateur (score très élevé)

    if verifier_victoire(grille, 'B'):
        return True, -1000000  # Victoire du joueur (score très négatif)

    # Vérification de match nul
    if grille_pleine(grille):
        return True, 0  # Match nul (score neutre)

    return False, 0  # La partie continue


def minimax(grille, profondeur, alpha, beta, maximisant):
    """
    Algorithme Minimax avec élagage alpha-beta.
    Permet de déterminer le meilleur coup à jouer.

    Args:
        grille (list): La grille de jeu
        profondeur (int): Profondeur de recherche restante
        alpha (float): Meilleur score pour le joueur maximisant
        beta (float): Meilleur score pour le joueur minimisant
        maximisant (bool): True si c'est au tour du joueur maximisant (ordinateur)

    Returns:
        tuple: (score, colonne) où 'score' est la valeur de la position et
               'colonne' est le meilleur coup à jouer
    """
    # Vérifier si la position est terminale ou si on a atteint la profondeur maximale
    terminal, valeur = est_terminal(grille)
    if profondeur == 0 or terminal:
        if terminal:
            return valeur, None
        else:
            return evaluer_position_minimax(grille, 'V'), None

    # Initialisation des valeurs
    if maximisant:
        valeur = float('-inf')  # Le plus petit score possible
        symbole = 'V'  # L'ordinateur
    else:
        valeur = float('inf')  # Le plus grand score possible
        symbole = 'B'  # Le joueur humain

    # Liste des coups possibles
    colonnes_valides = []
    for col in range(7):
        possible, _ = coup_possible(grille, col)
        if possible:
            colonnes_valides.append(col)

    # Si aucun coup n'est possible (ne devrait pas arriver)
    if not colonnes_valides:
        return 0, None

    colonne_choisie = colonnes_valides[0]

    # Évaluation de chaque coup possible
    for col in colonnes_valides:
        possible, ligne = coup_possible(grille, col)
        if possible:
            # Simulation du coup
            grille_temp = copy.deepcopy(grille)
            grille_temp[ligne][col] = symbole

            # Appel récursif pour évaluer ce coup (en alternant les joueurs)
            nouveau_score, _ = minimax(grille_temp, profondeur - 1, alpha, beta, not maximisant)

            # Mise à jour de la meilleure valeur
            if maximisant and nouveau_score > valeur:
                valeur = nouveau_score
                colonne_choisie = col
                alpha = max(alpha, valeur)
            elif not maximisant and nouveau_score < valeur:
                valeur = nouveau_score
                colonne_choisie = col
                beta = min(beta, valeur)

            # Élagage alpha-beta (optimisation)
            if alpha >= beta:
                break  # Arrêt de l'évaluation des autres coups

    return valeur, colonne_choisie


def coup_ordi_minimax(grille, difficulte):
    """
    L'ordinateur joue avec l'algorithme Minimax.
    La profondeur dépend du niveau de difficulté.

    Args:
        grille (list): La grille de jeu
        difficulte (int): Niveau de difficulté (1, 2 ou 3)

    Returns:
        int: L'indice de la colonne choisie
    """
    # Utiliser les modes facile et moyen pour les niveaux 1 et 2
    if difficulte == 1:
        return coup_ordi_facile(grille)
    elif difficulte == 2:
        return coup_ordi_moyen(grille)

    # Mode difficile (niveau 3) - Utiliser minimax
    profondeur = 5  # Profondeur de recherche pour le mode difficile

    # Vérification rapide pour un coup gagnant immédiat (optimisation)
    col_gagnante = coup_gagnant(grille, 'V')
    if col_gagnante is not None:
        return col_gagnante

    # Vérification rapide pour bloquer un coup gagnant de l'adversaire (optimisation)
    col_bloquante = coup_gagnant(grille, 'B')
    if col_bloquante is not None:
        return col_bloquante

    # Utiliser l'algorithme Minimax pour trouver le meilleur coup
    _, colonne = minimax(grille, profondeur, float('-inf'), float('inf'), True)

    return colonne


##########################################
# PARTIE 3: INTERFACE GRAPHIQUE (GUI)    #
##########################################

class Puissance4:
    """
    Classe principale du jeu Puissance 4.
    Gère l'interface graphique et la logique du jeu.
    """

    def __init__(self, root):
        """
        Initialise le jeu Puissance 4.

        Args:
            root: La fenêtre principale de l'application Tkinter
        """
        self.root = root
        self.root.title("Puissance 4")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        self.root.config(bg="#1E3D59")

        # Variables du jeu
        self.grille = grille_vide()
        self.joueur_actuel = 1  # 1 pour joueur 1, 2 pour joueur 2 ou ordinateur
        self.partie_en_cours = False
        self.mode_jeu = None  # 1 pour 2 joueurs, 2 pour joueur vs ordinateur
        self.difficulte = None  # Niveau de difficulté
        self.joueur_1 = ""
        self.joueur_2 = ""
        self.tour = 0

        # Couleurs et style
        self.BLEU = "#4A92E5"  # Couleur des pions du joueur 1
        self.JAUNE = "#FFD700"  # Couleur des pions du joueur 2 / ordinateur
        self.BLANC = "#FFFFFF"  # Couleur des cases vides
        self.GRIS = "#CCCCCC"  # Couleur secondaire

        # Création du menu principal
        self.creer_menu_principal()

    def creer_menu_principal(self):
        """Crée l'interface du menu principal."""
        # Supprimer tous les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()

        # Titre du jeu
        titre = tk.Label(self.root, text="PUISSANCE 4", font=("Arial", 28, "bold"),
                         bg="#1E3D59", fg="#FFFFFF")
        titre.pack(pady=40)

        # Cadre pour les boutons
        cadre_boutons = tk.Frame(self.root, bg="#1E3D59")
        cadre_boutons.pack(pady=20)

        # Boutons du menu
        btn_2joueurs = tk.Button(cadre_boutons, text="Joueur contre Joueur", font=("Arial", 14),
                                 width=25, height=2, bg="#4A92E5", fg="#000000",
                                 command=self.configurer_2joueurs)
        btn_2joueurs.pack(pady=10)

        btn_vs_ordi = tk.Button(cadre_boutons, text="Joueur contre Ordinateur", font=("Arial", 14),
                                width=25, height=2, bg="#4A92E5", fg="#000000",
                                command=self.configurer_vs_ordi)
        btn_vs_ordi.pack(pady=10)

        btn_quitter = tk.Button(cadre_boutons, text="Quitter", font=("Arial", 14),
                                width=25, height=2, bg="#E95D0F", fg="#000000",
                                command=self.root.quit)
        btn_quitter.pack(pady=10)

        # Crédits
        credits = tk.Label(self.root, text="Développé en Python avec Tkinter",
                           font=("Arial", 10), bg="#1E3D59", fg="#FFFFFF")
        credits.pack(side=tk.BOTTOM, pady=10)

    def configurer_2joueurs(self):
        """Configure le mode 2 joueurs."""
        self.mode_jeu = 1  # Mode 2 joueurs

        # Demander les noms des joueurs avec boîte de dialogue
        self.joueur_1 = simpledialog.askstring("Nom du Joueur 1", "Joueur 1, quel est votre nom?:",
                                               parent=self.root) or "Joueur 1"
        self.joueur_2 = simpledialog.askstring("Nom du Joueur 2", "Joueur 2, quel est votre nom?:",
                                               parent=self.root) or "Joueur 2"

        # Démarrer la partie
        self.demarrer_partie()

    def configurer_vs_ordi(self):
        """Configure le mode joueur contre ordinateur."""
        # Supprimer tous les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()

        self.mode_jeu = 2  # Mode joueur vs ordinateur

        # Configure l'écran de sélection de difficulté
        self.root.title("Puissance 4 - Choisir la difficulté")

        # Demander le nom du joueur d'abord
        self.joueur_1 = simpledialog.askstring("Nom du Joueur", "Quel est votre nom?:",
                                               parent=self.root) or "Joueur 1"
        self.joueur_2 = "Ordinateur"

        # Titre principal
        titre = tk.Label(self.root, text="PUISSANCE 4", font=("Arial", 28, "bold"),
                         bg="#1E3D59", fg="#FFFFFF")
        titre.pack(pady=20)

        # Sous-titre pour la difficulté
        sous_titre = tk.Label(self.root, text=f"Bonjour {self.joueur_1}, choisissez la difficulté:",
                              font=("Arial", 16), bg="#1E3D59", fg="#FFFFFF")
        sous_titre.pack(pady=20)

        # Cadre pour les boutons
        cadre_boutons = tk.Frame(self.root, bg="#1E3D59")
        cadre_boutons.pack(pady=20)

        # Fonction pour sélectionner la difficulté
        def select_difficulte(niveau):
            self.difficulte = niveau
            self.demarrer_partie()

        # Boutons de difficulté
        btn_facile = tk.Button(cadre_boutons, text="Facile (aléatoire)", font=("Arial", 14),
                               width=30, height=2, bg="#4A92E5", fg="#000000",
                               command=lambda: select_difficulte(1))
        btn_facile.pack(pady=10)

        btn_moyen = tk.Button(cadre_boutons, text="Moyen (détecte les coups gagnants)", font=("Arial", 14),
                              width=30, height=2, bg="#4A92E5", fg="#000000",
                              command=lambda: select_difficulte(2))
        btn_moyen.pack(pady=10)

        btn_difficile = tk.Button(cadre_boutons, text="Difficile (minimax)", font=("Arial", 14),
                                  width=30, height=2, bg="#4A92E5", fg="#000000",
                                  command=lambda: select_difficulte(3))
        btn_difficile.pack(pady=10)

        # Bouton pour revenir au menu principal
        btn_retour = tk.Button(cadre_boutons, text="Retour au menu", font=("Arial", 12),
                               width=25, height=1, bg="#E95D0F", fg="#000000",
                               command=self.creer_menu_principal)
        btn_retour.pack(pady=20)

    def demarrer_partie(self):
        """Initialise et démarre une nouvelle partie."""
        # Réinitialiser l'état du jeu
        self.grille = grille_vide()
        self.joueur_actuel = 1  # Premier joueur
        self.partie_en_cours = True
        self.tour = 0

        # Créer l'interface de jeu
        self.creer_interface_jeu()

        # Mettre à jour l'affichage
        self.mettre_a_jour_status()

    def creer_interface_jeu(self):
        """Crée l'interface graphique du jeu."""
        # Supprimer tous les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cadre principal
        self.cadre_principal = tk.Frame(self.root, bg="#1E3D59")
        self.cadre_principal.pack(fill=tk.BOTH, expand=True)

        # Cadre pour le statut (en haut)
        self.cadre_statut = tk.Frame(self.cadre_principal, bg="#1E3D59", height=50)
        self.cadre_statut.pack(fill=tk.X, padx=10, pady=10)

        self.label_statut = tk.Label(self.cadre_statut, text="", font=("Arial", 14),
                                     bg="#1E3D59", fg="#FFFFFF")
        self.label_statut.pack(side=tk.LEFT, padx=20)

        # Cadre pour la grille (au centre)
        self.cadre_grille = tk.Frame(self.cadre_principal, bg="#1E3D59")
        self.cadre_grille.pack(pady=10)

        # Création des boutons pour chaque colonne
        self.cadre_boutons = tk.Frame(self.cadre_principal, bg="#1E3D59")
        self.cadre_boutons.pack(pady=5)

        self.boutons_colonne = []
        for j in range(7):
            btn = tk.Button(self.cadre_boutons, text="↓", font=("Arial", 16, "bold"),
                            width=4, height=1, bg="#4A92E5", fg="#000000",
                            command=lambda col=j: self.jouer_coup(col))
            btn.grid(row=0, column=j, padx=5)
            self.boutons_colonne.append(btn)

        # Création du canevas pour la grille
        self.canevas = tk.Canvas(self.cadre_grille, width=490, height=420, bg="#0F4C81", highlightthickness=0)
        self.canevas.pack()

        # Dessiner la grille
        self.cellules = {}
        for i in range(6):
            for j in range(7):
                x = j * 70 + 35
                y = (5 - i) * 70 + 35  # Inverser l'axe y pour que (0,0) soit en bas à gauche
                cercle = self.canevas.create_oval(x - 30, y - 30, x + 30, y + 30,
                                                  fill="#FFFFFF", outline="#0F4C81", width=2)
                self.cellules[(i, j)] = cercle

        # Cadre pour les boutons de contrôle (en bas)
        self.cadre_controle = tk.Frame(self.cadre_principal, bg="#1E3D59")
        self.cadre_controle.pack(fill=tk.X, pady=10)

        self.btn_nouvelle_partie = tk.Button(self.cadre_controle, text="Nouvelle Partie", font=("Arial", 12),
                                             bg="#4A92E5", fg="#000000", command=self.nouvelle_partie)
        self.btn_nouvelle_partie.pack(side=tk.LEFT, padx=20, pady=10)

        self.btn_menu = tk.Button(self.cadre_controle, text="Menu Principal", font=("Arial", 12),
                                  bg="#E95D0F", fg="#000000", command=self.creer_menu_principal)
        self.btn_menu.pack(side=tk.RIGHT, padx=20, pady=10)

    def mettre_a_jour_status(self):
        """Met à jour le statut du jeu."""
        if self.joueur_actuel == 1:
            self.label_statut.config(text=f"Tour {self.tour}: {self.joueur_1} (Bleu), à vous de jouer!")
        else:
            self.label_statut.config(text=f"Tour {self.tour}: {self.joueur_2} (Jaune), à vous de jouer!")

    def mettre_a_jour_grille(self):
        """Met à jour l'affichage de la grille."""
        for i in range(6):
            for j in range(7):
                if self.grille[i][j] == 0:
                    self.canevas.itemconfig(self.cellules[(i, j)], fill="#FFFFFF")
                elif self.grille[i][j] == 'B':
                    self.canevas.itemconfig(self.cellules[(i, j)], fill=self.BLEU)
                else:  # 'V'
                    self.canevas.itemconfig(self.cellules[(i, j)], fill=self.JAUNE)

    def jouer_coup(self, colonne):
        """
        Joue un coup dans la colonne spécifiée.

        Args:
            colonne (int): L'indice de la colonne où jouer
        """
        if not self.partie_en_cours:
            return

        # Incrémenter le compteur de tours (seulement quand le joueur 1 joue)
        if self.joueur_actuel == 1:
            self.tour += 1

        # Vérifier si la colonne est jouable
        possible, ligne = coup_possible(self.grille, colonne)
        if not possible:
            messagebox.showinfo("Colonne pleine", "Cette colonne est pleine. Veuillez choisir une autre colonne.")
            return

        # Déterminer la couleur du pion
        couleur = self.BLEU if self.joueur_actuel == 1 else self.JAUNE

        # Animer la chute du pion
        self.animer_pion(colonne, ligne, couleur)

    def animer_pion(self, colonne, ligne_finale, couleur):
        """
        Anime la chute d'un pion dans la grille.

        Args:
            colonne (int): L'indice de la colonne
            ligne_finale (int): L'indice de la ligne finale
            couleur (str): La couleur du pion
        """
        # Désactiver les boutons pendant l'animation
        for btn in self.boutons_colonne:
            btn.config(state=tk.DISABLED)

        # Animation de la chute
        ligne_courante = 0

        def animation_etape():
            nonlocal ligne_courante

            # Si on n'a pas atteint la position finale
            if ligne_courante <= ligne_finale:
                # Uniquement si la case est vide dans le modèle de données
                if self.grille[ligne_courante][colonne] == 0:
                    # Afficher le pion à sa position actuelle
                    self.canevas.itemconfig(self.cellules[(ligne_courante, colonne)], fill=couleur)

                    # Effacer le pion de sa position précédente si elle existe et est vide
                    if ligne_courante > 0 and self.grille[ligne_courante - 1][colonne] == 0:
                        self.canevas.itemconfig(self.cellules[(ligne_courante - 1, colonne)], fill="#FFFFFF")

                    ligne_courante += 1
                    self.root.after(100, animation_etape)  # Appel récursif après 100ms
                else:
                    # Si la case n'est pas vide, passer à la suivante
                    ligne_courante += 1
                    animation_etape()
            else:
                # Animation terminée, finaliser le coup
                self.finaliser_coup(ligne_finale, colonne, couleur)

        # Démarrer l'animation
        animation_etape()

    def finaliser_coup(self, ligne, colonne, couleur):
        """
        Finalise le coup après l'animation.
        Met à jour le modèle, vérifie la victoire et change de joueur.

        Args:
            ligne (int): L'indice de la ligne
            colonne (int): L'indice de la colonne
            couleur (str): La couleur du pion
        """
        # Réactiver les boutons
        for btn in self.boutons_colonne:
            btn.config(state=tk.NORMAL)

        # Mettre à jour le modèle interne de la grille
        if self.joueur_actuel == 1:
            self.grille[ligne][colonne] = 'B'  # Bleu
            symbole = 'B'
        else:
            self.grille[ligne][colonne] = 'V'  # "Vert" (Jaune)
            symbole = 'V'

        # Vérifier si le joueur a gagné
        if verifier_victoire(self.grille, symbole):
            self.partie_en_cours = False
            joueur_nom = self.joueur_1 if self.joueur_actuel == 1 else self.joueur_2
            messagebox.showinfo("Victoire", f"Félicitations ! {joueur_nom} a gagné en {self.tour} tours !")
            return

        # Vérifier si la grille est pleine (match nul)
        if grille_pleine(self.grille):
            self.partie_en_cours = False
            messagebox.showinfo("Match nul", "Match nul ! La grille est pleine.")
            return

        # Changer de joueur
        self.joueur_actuel = 3 - self.joueur_actuel  # 1 -> 2, 2 -> 1

        # Mettre à jour le statut
        self.mettre_a_jour_status()

        # Si c'est au tour de l'ordinateur
        if self.mode_jeu == 2 and self.joueur_actuel == 2 and self.partie_en_cours:
            self.root.after(500, self.jouer_coup_ordi)  # Délai pour un effet plus réaliste

    def jouer_coup_ordi(self):
        """
        Fait jouer l'ordinateur selon le niveau de difficulté choisi.
        """
        if not self.partie_en_cours:
            return

        # Changer le libellé pour indiquer que l'ordinateur réfléchit
        self.label_statut.config(text=f"Tour {self.tour}: {self.joueur_2} (Jaune) réfléchit...")
        self.root.update()  # Force la mise à jour de l'interface

        # Déterminer quelle colonne jouer selon la difficulté
        if self.difficulte == 1:
            colonne = coup_ordi_facile(self.grille)
        elif self.difficulte == 2:
            colonne = coup_ordi_moyen(self.grille)
        else:  # difficulte == 3
            colonne = coup_ordi_minimax(self.grille, self.difficulte)

        # Jouer le coup
        self.jouer_coup(colonne)

    def nouvelle_partie(self):
        """
        Démarre une nouvelle partie avec les mêmes paramètres.
        """
        if messagebox.askyesno("Nouvelle partie", "Voulez-vous démarrer une nouvelle partie?"):
            self.tour = 0  # Réinitialiser le compteur de tours
            self.demarrer_partie()


##########################################
# PARTIE 4: POINT D'ENTRÉE DU PROGRAMME  #
##########################################

if __name__ == "__main__":
    # Point d'entrée du programme
    root = tk.Tk()  # Création de la fenêtre principale
    app = Puissance4(root)  # Création de l'application
    root.mainloop()  # Lancement de la boucle principale
