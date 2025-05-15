import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes de la fenêtre
LARGEUR, HAUTEUR = 700, 600  # Dimensions de la fenêtre de jeu
TAILLE_CASE = 100  # Taille d'une case du plateau

# Couleurs utilisées
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)
BLEU = (0, 0, 255)

# Création de la fenêtre principale
screen = pygame.display.set_mode((LARGEUR, HAUTEUR + 100))  # +100 pour l'interface en bas
pygame.display.set_caption("Puissance 4")  # Titre de la fenêtre

# Définition de la police d'écriture
FONT = pygame.font.SysFont(None, 36)

# Classe pour gérer les champs de saisie de texte
class InputBox:
    def __init__(self, x, y, w, h, placeholder='', border_color=NOIR):
        self.rect = pygame.Rect(x, y, w, h)  # Rectangle du champ
        self.color_inactive = border_color  # Couleur bord inactif
        self.color_active = border_color  # Couleur bord actif (idem ici)
        self.color = self.color_inactive  # Couleur actuelle
        self.text = ''  # Texte actuel saisi
        self.txt_surface = FONT.render(placeholder, True, NOIR)  # Texte affiché (placeholder au départ)
        self.active = False  # Champ actif ou non
        self.placeholder = placeholder  # Texte par défaut
        self.border_color = border_color  # Couleur de bord (en fonction du joueur)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)  # Active si on clique dedans
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False  # Entrée termine l'édition
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # Efface un caractère
            else:
                if len(self.text) < 12:  # Limite la longueur du nom
                    self.text += event.unicode
            self.txt_surface = FONT.render(self.text or self.placeholder, True, NOIR)  # Affiche texte

    def draw(self, screen):
        pygame.draw.rect(screen, BLANC, self.rect)  # Fond blanc du champ
        pygame.draw.rect(screen, self.border_color, self.rect, 3)  # Bord du champ
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))  # Texte

    def get_text(self):
        return self.text or self.placeholder  # Retourne le texte ou le placeholder si vide

# Fonction pour créer une grille vide (6 lignes, 7 colonnes)
def grille_vide():
    return [[0 for _ in range(7)] for _ in range(6)]

# Dessine la grille de jeu sur l'écran
def dessiner_grille(grille):
    screen.fill(BLEU)  # Fond bleu du plateau
    for i in range(6):
        for j in range(7):
            pygame.draw.rect(screen, BLEU, (j*TAILLE_CASE, i*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            couleur = BLANC  # Par défaut, case vide
            if grille[i][j] == 'R':
                couleur = ROUGE
            elif grille[i][j] == 'J':
                couleur = JAUNE
            # Dessine le pion (ou le trou vide)
            pygame.draw.circle(screen, couleur, (j*TAILLE_CASE + TAILLE_CASE//2, i*TAILLE_CASE + TAILLE_CASE//2), TAILLE_CASE//2 - 5)

# Vérifie si on peut jouer dans une colonne (si elle n'est pas pleine)
def coup_possible(grille, col):
    for i in range(5, -1, -1):  # De bas en haut
        if grille[i][col] == 0:
            return True, i  # Coup possible, retourne la ligne
    return False, None  # Colonne pleine

# Vérifie s'il y a une victoire pour un joueur
def verif_victoire(grille, pion):
    # Alignement horizontal
    for i in range(6):
        for j in range(4):
            if all(grille[i][j + k] == pion for k in range(4)):
                return True
    # Alignement vertical
    for i in range(3):
        for j in range(7):
            if all(grille[i + k][j] == pion for k in range(4)):
                return True
    # Diagonale descendante
    for i in range(3):
        for j in range(4):
            if all(grille[i + k][j + k] == pion for k in range(4)):
                return True
    # Diagonale montante
    for i in range(3):
        for j in range(3, 7):
            if all(grille[i + k][j - k] == pion for k in range(4)):
                return True
    return False

# Menu de démarrage : permet d'entrer les noms des joueurs
def menu_accueil():
    input_box1 = InputBox(50, HAUTEUR + 20, 250, 40, "Joueur 1", ROUGE)  # Champ nom joueur 1
    input_box2 = InputBox(400, HAUTEUR + 20, 250, 40, "Joueur 2", JAUNE)  # Champ nom joueur 2
    bouton_lancer = pygame.Rect(300, HAUTEUR + 70, 100, 30)  # Bouton "Jouer"

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            input_box1.handle_event(event)
            input_box2.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN and bouton_lancer.collidepoint(event.pos):
                joueur_1 = {'nom': input_box1.get_text(), 'pion': 'R'}
                joueur_2 = {'nom': input_box2.get_text(), 'pion': 'J'}
                jouer_jeu(joueur_1, joueur_2)  # Lance le jeu avec les noms
                return

        screen.fill(BLANC)
        titre = FONT.render("Entrez les noms des joueurs", True, NOIR)
        screen.blit(titre, (LARGEUR // 2 - titre.get_width() // 2, 20))

        input_box1.draw(screen)
        input_box2.draw(screen)

        pygame.draw.rect(screen, NOIR, bouton_lancer)  # Dessine le bouton "Jouer"
        txt = FONT.render("Jouer", True, BLANC)
        screen.blit(txt, (bouton_lancer.x + 10, bouton_lancer.y))

        pygame.display.flip()
        clock.tick(30)

# Fonction principale du jeu (tour par tour)
def jouer_jeu(joueur_1, joueur_2):
    grille = grille_vide()  # Initialise une nouvelle grille
    joueurs = [joueur_1, joueur_2]  # Liste des joueurs
    tour = 0  # Compteur de tours
    partie_terminee = False  # État de la partie

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Gestion du clic pour poser un pion
            if not partie_terminee and event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0] // TAILLE_CASE  # Colonne cliquée
                possible, ligne = coup_possible(grille, x)
                if possible:
                    joueur = joueurs[tour % 2]
                    grille[ligne][x] = joueur['pion']
                    if verif_victoire(grille, joueur['pion']):
                        partie_terminee = True
                        gagnant = joueur['nom']
                    elif all(grille[0][j] != 0 for j in range(7)):
                        partie_terminee = True
                        gagnant = "Match nul"
                    else:
                        tour += 1  # Changement de joueur
            # Si partie finie, un clic ramène au menu
            elif partie_terminee and event.type == pygame.MOUSEBUTTONDOWN:
                menu_accueil()
                return

        dessiner_grille(grille)  # Affiche la grille

        # Affiche le message selon l'état de la partie
        if not partie_terminee:
            joueur = joueurs[tour % 2]
            texte = FONT.render(f"À {joueur['nom']} de jouer", True, NOIR)
        else:
            texte = FONT.render(f"Fin de partie ! {gagnant}", True, NOIR)

        screen.blit(texte, (LARGEUR//2 - texte.get_width()//2, HAUTEUR + 30))
        pygame.display.flip()
        clock.tick(30)

# Lancement du programme : affiche le menu d'accueil
menu_accueil()