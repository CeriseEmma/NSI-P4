# Importation des bibliothèques nécessaires
import pygame  # Bibliothèque pour créer l'interface graphique
import sys     # Bibliothèque pour les fonctionnalités système (comme quitter)
import random  # Bibliothèque pour générer des nombres aléatoires

# Initialisation de Pygame
pygame.init()

# Constantes pour l'interface graphique
SCREEN_WIDTH = 1100    # Largeur de la fenêtre
SCREEN_HEIGHT = 700    # Hauteur de la fenêtre
GRID_COLS = 7          # Nombre de colonnes dans la grille de jeu
GRID_ROWS = 6          # Nombre de lignes dans la grille de jeu
CELL_SIZE = 80         # Taille d'une cellule de la grille en pixels
GRID_OFFSET_X = (SCREEN_WIDTH - GRID_COLS * CELL_SIZE) // 2  # Position X de la grille pour la centrer
GRID_OFFSET_Y = 150    # Position Y de la grille
RADIUS = CELL_SIZE // 2 - 5  # Rayon des jetons dans la grille

# Définition des couleurs en RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (50, 200, 50)
LIGHT_BLUE = (100, 200, 255)
DARK_BLUE = (0, 50, 150)
GRAY = (200, 200, 200)

# Définition des polices de texte
font = pygame.font.SysFont('Arial', 32)        # Police standard
large_font = pygame.font.SysFont('Arial', 48)  # Police plus grande
title_font = pygame.font.SysFont('Arial', 64)  # Police pour les titres
small_font = pygame.font.SysFont('Arial', 24)  # Petite police pour les champs de texte

# Création de la fenêtre principale
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puissance 4")  # Titre de la fenêtre
pygame.display.set_caption("Entrer les noms des joueurs")


class Button:
    """Classe pour créer des boutons interactifs"""
    def __init__(self, x, y, width, height, text, color, hover_color):
        # Initialisation d'un bouton avec ses propriétés
        self.rect = pygame.Rect(x, y, width, height)  # Rectangle du bouton
        self.text = text               # Texte du bouton
        self.color = color            # Couleur normale
        self.hover_color = hover_color # Couleur quand la souris est dessus
        self.is_hovered = False       # État de survol

    def draw(self, surface):
        """Dessine le bouton sur la surface donnée"""
        # Choisir la couleur en fonction de l'état de survol
        color = self.hover_color if self.is_hovered else self.color
        # Dessiner le rectangle du bouton
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        # Dessiner la bordure du bouton
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)

        # Créer et positionner le texte du bouton
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, pos):
        """Vérifie si la souris survole le bouton"""
        self.is_hovered = self.rect.collidepoint(pos)

    def is_clicked(self, pos, event):
        """Vérifie si le bouton a été cliqué"""
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pos)

class InputBox:
    """Classe pour créer des champs de saisie de texte"""
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.txt_surface = font.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Active ou désactive la boîte si on clique dessus
            self.active = self.rect.collidepoint(event.pos)
            self.color = WHITE if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return True  # Indique que la saisie est terminée
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-rend le texte
                self.txt_surface = font.render(self.text, True, BLACK)
        return False

    def draw(self, screen):
        # Dessine le texte
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Dessine le rectangle
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

class Game:
    """Classe principale du jeu"""
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        """Réinitialise le jeu à son état initial"""
        self.grid = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]  # Grille vide
        self.state = "menu"    # État initial: menu
        self.mode = None       # Mode de jeu (1: 2 joueurs, 2: facile, 3: difficile)
        self.players = []      # Liste des joueurs
        self.current_player = 0 # Index du joueur actuel
        self.winner = None     # Gagnant de la partie
        self.message = ""      # Message de fin de partie
        self.buttons = []      # Liste des boutons
        self.animation = None  # Animation (non utilisé ici)
        self.input_boxes = []  # Champs de saisie pour les noms des joueurs
        self.create_menu_buttons()  # Crée les boutons du menu

    def create_menu_buttons(self):
        """Crée les boutons pour le menu principal"""
        button_width = 400    # Largeur des boutons
        button_height = 60   # Hauteur des boutons
        start_y = 200        # Position Y de départ
        spacing = 15         # Espacement entre boutons

        # Options du menu
        options = [
            ("1. Jouer contre un autre joueur", 1),
            ("2. Jouer contre l'ordinateur (facile)", 2),
            ("3. Jouer contre l'ordinateur (difficile)", 3),
            ("4. Règles du jeu", 4),
            ("5. Quitter", 5)
        ]

        self.buttons = []
        # Création de chaque bouton
        for i, (text, value) in enumerate(options):
            y = start_y + i * (button_height + spacing)
            btn = Button(
                (SCREEN_WIDTH - button_width) // 2,
                y,
                button_width,
                button_height,
                text,
                LIGHT_BLUE,
                GREEN
            )
            btn.value = value  # Stocke la valeur associée au bouton
            self.buttons.append(btn)

    def create_player_name_input(self, num_players=2):
        """Crée les champs de saisie pour les noms des joueurs"""
        self.input_boxes = []
        box_width = 300
        box_height = 50
        spacing = 20

        for i in range(num_players):
            y = 250 + i * (box_height + spacing)
            input_box = InputBox(
                (SCREEN_WIDTH - box_width) // 2,
                y,
                box_width,
                box_height,
                f"Joueur {i+1}" if i == 0 or num_players == 2 else "Ordinateur"
            )
            self.input_boxes.append(input_box)

        # Bouton de confirmation
        confirm_btn = Button(
            (SCREEN_WIDTH - 200) // 2,
            250 + num_players * (box_height + spacing),
            200,
            60,
            "Commencer",
            LIGHT_BLUE,
            GREEN
        )
        confirm_btn.value = "confirm"
        self.buttons = [confirm_btn]

    def create_rules_buttons(self):
        """Crée le bouton pour l'écran des règles"""
        btn = Button(
            (SCREEN_WIDTH - 250) // 2,
            SCREEN_HEIGHT - 100,
            250,
            60,
            "Retour au menu",
            LIGHT_BLUE,
            GREEN
        )
        self.buttons = [btn]  # Un seul bouton pour revenir au menu

    def create_end_buttons(self):
        """Crée les boutons pour l'écran de fin de partie"""
        btn1 = Button(
            SCREEN_WIDTH // 2 - 270,
            SCREEN_HEIGHT - 100,
            250,
            60,
            "Rejouer",
            LIGHT_BLUE,
            GREEN
        )
        btn2 = Button(
            SCREEN_WIDTH // 2 + 20,
            SCREEN_HEIGHT - 100,
            250,
            60,
            "Menu principal",
            LIGHT_BLUE,
            GREEN
        )
        self.buttons = [btn1, btn2]  # Deux boutons: rejouer ou retour au menu

    def show_rules(self):
        """Affiche l'écran des règles"""
        self.state = "rules"
        self.create_rules_buttons()

    def draw_menu(self):
        """Dessine l'écran du menu"""
        screen.fill(WHITE)  # Fond blanc

        # Dessine le titre
        title = title_font.render("PUISSANCE 4", True, DARK_BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)

        # Dessine tous les boutons
        for button in self.buttons:
            button.draw(screen)

    def draw_player_names_input(self):
        """Dessine l'écran de saisie des noms des joueurs"""
        screen.fill(WHITE)

        # Titre
        title = large_font.render("Entrez les noms des joueurs", True, DARK_BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(title, title_rect)

        # Instructions
        instructions = small_font.render("Cliquez sur un champ pour le sélectionner", True, BLACK)
        instructions_rect = instructions.get_rect(center=(SCREEN_WIDTH // 2, 200))
        screen.blit(instructions, instructions_rect)

        # Champs de saisie
        for box in self.input_boxes:
            box.draw(screen)

        # Bouton
        for button in self.buttons:
            button.draw(screen)

    def draw_rules(self):
        """Dessine l'écran des règles"""
        screen.fill(WHITE)

        # Titre
        title = title_font.render("RÈGLES DU JEU", True, DARK_BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 70))
        screen.blit(title, title_rect)

        # Liste des règles
        rules = [
            "1. Le jeu se joue à deux joueurs (ou contre l'ordinateur).",
            "2. Chaque joueur place à tour de rôle un jeton dans une colonne.",
            "3. Le jeton tombe au plus bas de la colonne choisie.",
            "4. Le premier joueur qui aligne 4 jetons (horizontalement,",
            "   verticalement ou en diagonale) gagne la partie.",
            "5. Si la grille est remplie sans alignement de 4 jetons,",
            "   la partie est déclarée nulle."
        ]

        # Affichage de chaque règle
        for i, rule in enumerate(rules):
            text = font.render(rule, True, BLACK)
            screen.blit(text, (100, 150 + i * 40))

        # Bouton de retour
        self.buttons[0].draw(screen)

    def draw_grid(self):
        """Dessine la grille de jeu et les jetons"""
        # Fond de la grille (bleu)
        pygame.draw.rect(
            screen, BLUE,
            (GRID_OFFSET_X - 5, GRID_OFFSET_Y - 5,
             GRID_COLS * CELL_SIZE + 10, GRID_ROWS * CELL_SIZE + 10),
            border_radius=10
        )

        # Dessin des cases et des pions
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                # Dessin d'une case vide (cercle blanc)
                pygame.draw.circle(
                    screen, WHITE,
                    (GRID_OFFSET_X + col * CELL_SIZE + CELL_SIZE // 2,
                     GRID_OFFSET_Y + row * CELL_SIZE + CELL_SIZE // 2),
                    RADIUS
                )

                # Dessin des pions en fonction de la grille de jeu
                if self.grid[row][col] == 1:  # Joueur 1 (rouge)
                    pygame.draw.circle(
                        screen, RED,
                        (GRID_OFFSET_X + col * CELL_SIZE + CELL_SIZE // 2,
                         GRID_OFFSET_Y + row * CELL_SIZE + CELL_SIZE // 2),
                        RADIUS
                    )
                elif self.grid[row][col] == 2:  # Joueur 2 (jaune)
                    pygame.draw.circle(
                        screen, YELLOW,
                        (GRID_OFFSET_X + col * CELL_SIZE + CELL_SIZE // 2,
                         GRID_OFFSET_Y + row * CELL_SIZE + CELL_SIZE // 2),
                        RADIUS
                    )

        # Numérotation des colonnes
        for col in range(GRID_COLS):
            text = font.render(str(col + 1), True, BLACK)
            text_rect = text.get_rect(
                center=(GRID_OFFSET_X + col * CELL_SIZE + CELL_SIZE // 2,
                        GRID_OFFSET_Y + GRID_ROWS * CELL_SIZE + 30)
            )
            screen.blit(text, text_rect)

    def draw_game(self):
        """Dessine l'écran de jeu"""
        screen.fill(WHITE)

        # Titre
        title = large_font.render("PUISSANCE 4", True, DARK_BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
        screen.blit(title, title_rect)

        # Affichage du tour actuel
        if self.players:
            player = self.players[self.current_player]
            color = RED if player['id'] == 1 else YELLOW
            text = large_font.render(f"Tour: {player['name']}", True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 110))
            screen.blit(text, text_rect)

        # Dessin de la grille
        self.draw_grid()

    def draw_end(self):
        """Dessine l'écran de fin de partie"""
        self.draw_game()  # Affiche d'abord le jeu en fond

        # Superposition semi-transparente
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Message de fin
        msg = large_font.render(self.message, True, WHITE)
        msg_rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(msg, msg_rect)

        # Boutons
        for button in self.buttons:
            button.draw(screen)

    def draw(self):
        """Gère l'affichage en fonction de l'état du jeu"""
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "rules":
            self.draw_rules()
        elif self.state == "player_names":
            self.draw_player_names_input()
        elif self.state == "game":
            self.draw_game()
        elif self.state == "end":
            self.draw_end()

        pygame.display.flip()  # Met à jour l'affichage

    def is_valid_move(self, col):
        """Vérifie si un coup est valide dans une colonne"""
        return self.grid[0][col] == 0  # La case du haut doit être vide

    def make_move(self, col):
        """Place un jeton dans la colonne donnée"""
        # Trouve la première case vide en partant du bas
        for row in range(GRID_ROWS-1, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = self.players[self.current_player]['id']
                return row  # Retourne la ligne où le jeton a été placé
        return -1  # Colonne pleine

    def check_win(self, player_id):
        """Vérifie si le joueur a gagné"""
        # Vérification horizontale
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS-3):
                if (self.grid[row][col] == player_id and
                    self.grid[row][col+1] == player_id and
                    self.grid[row][col+2] == player_id and
                    self.grid[row][col+3] == player_id):
                    return True

        # Vérification verticale
        for row in range(GRID_ROWS-3):
            for col in range(GRID_COLS):
                if (self.grid[row][col] == player_id and
                    self.grid[row+1][col] == player_id and
                    self.grid[row+2][col] == player_id and
                    self.grid[row+3][col] == player_id):
                    return True

        # Vérification diagonale (bas gauche à haut droit)
        for row in range(3, GRID_ROWS):
            for col in range(GRID_COLS-3):
                if (self.grid[row][col] == player_id and
                    self.grid[row-1][col+1] == player_id and
                    self.grid[row-2][col+2] == player_id and
                    self.grid[row-3][col+3] == player_id):
                    return True

        # Vérification diagonale (haut gauche à bas droit)
        for row in range(GRID_ROWS-3):
            for col in range(GRID_COLS-3):
                if (self.grid[row][col] == player_id and
                    self.grid[row+1][col+1] == player_id and
                    self.grid[row+2][col+2] == player_id and
                    self.grid[row+3][col+3] == player_id):
                    return True

        return False  # Pas de victoire

    def is_board_full(self):
        """Vérifie si la grille est complète"""
        return all(cell != 0 for row in self.grid for cell in row)

    def computer_move_easy(self):
        """Coup de l'ordinateur en mode facile (aléatoire)"""
        valid_cols = [col for col in range(GRID_COLS) if self.is_valid_move(col)]
        return random.choice(valid_cols) if valid_cols else -1

    def computer_move_hard(self):
        """Coup de l'ordinateur en mode difficile (avec stratégie)"""
        # D'abord vérifier si l'ordinateur peut gagner
        for col in range(GRID_COLS):
            if self.is_valid_move(col):
                row = self.make_move(col)
                if self.check_win(2):
                    self.grid[row][col] = 0  # Annuler le mouvement
                    return col
                self.grid[row][col] = 0  # Annuler le mouvement

        # Ensuite vérifier si le joueur peut gagner au prochain coup
        for col in range(GRID_COLS):
            if self.is_valid_move(col):
                row = self.make_move(col)
                if self.check_win(1):
                    self.grid[row][col] = 0  # Annuler le mouvement
                    return col
                self.grid[row][col] = 0  # Annuler le mouvement

        # Sinon jouer aléatoirement
        return self.computer_move_easy()

    def start_two_player_game(self):
        """Prépare le jeu pour 2 joueurs et demande leurs noms"""
        self.state = "player_names"
        self.mode = 1
        self.create_player_name_input(2)

    def start_computer_game(self, difficulty):
        """Prépare le jeu contre l'ordinateur et demande le nom du joueur"""
        self.state = "player_names"
        self.mode = difficulty
        self.create_player_name_input(1)

    def confirm_player_names(self):
        """Confirme les noms des joueurs et commence la partie"""
        if self.mode == 1:  # 2 joueurs
            player1_name = self.input_boxes[0].text if self.input_boxes[0].text else "Joueur 1"
            player2_name = self.input_boxes[1].text if self.input_boxes[1].text else "Joueur 2"

            self.players = [
                {'id': 1, 'name': player1_name, 'color': RED},
                {'id': 2, 'name': player2_name, 'color': YELLOW}
            ]
        else:  # Contre l'ordinateur
            player_name = self.input_boxes[0].text if self.input_boxes[0].text else "Joueur"

            self.players = [
                {'id': 1, 'name': player_name, 'color': RED},
                {'id': 2, 'name': "Ordinateur", 'color': YELLOW}
            ]

            # L'ordinateur commence parfois
            if random.choice([True, False]):
                self.current_player = 1
                self.computer_turn()

        self.state = "game"

    def computer_turn(self):
        """Gère le tour de l'ordinateur"""
        if self.mode == 2:
            col = self.computer_move_easy()
        else:
            col = self.computer_move_hard()

        if col != -1:
            self.make_move(col)

            # Vérifie si l'ordinateur a gagné
            if self.check_win(2):
                self.message = "L'ordinateur a gagné !"
                self.state = "end"
                self.create_end_buttons()
            elif self.is_board_full():  # Match nul
                self.message = "Match nul !"
                self.state = "end"
                self.create_end_buttons()
            else:
                self.current_player = 0  # Passe au joueur humain

    def handle_click(self, pos):
        """Gère les clics de souris en fonction de l'état du jeu"""
        if self.state == "menu":
            # Gestion des clics dans le menu
            for button in self.buttons:
                if button.is_clicked(pos, pygame.event.Event(pygame.MOUSEBUTTONDOWN)):
                    if button.value == 1:
                        self.start_two_player_game()
                    elif button.value == 2:
                        self.start_computer_game(2)
                    elif button.value == 3:
                        self.start_computer_game(3)
                    elif button.value == 4:
                        self.show_rules()
                    elif button.value == 5:
                        pygame.quit()
                        sys.exit()

        elif self.state == "player_names":
            # Gestion des clics dans l'écran de saisie des noms
            for box in self.input_boxes:
                box.handle_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': pos}))

            for button in self.buttons:
                if button.is_clicked(pos, pygame.event.Event(pygame.MOUSEBUTTONDOWN)):
                    if button.value == "confirm":
                        self.confirm_player_names()

        elif self.state == "rules":
            # Bouton retour dans l'écran des règles
            if self.buttons[0].is_clicked(pos, pygame.event.Event(pygame.MOUSEBUTTONDOWN)):
                self.state = "menu"
                self.create_menu_buttons()

        elif self.state == "game":
            # Vérifie si le clic est dans la grille
            if (GRID_OFFSET_X <= pos[0] <= GRID_OFFSET_X + GRID_COLS * CELL_SIZE and
                GRID_OFFSET_Y <= pos[1] <= GRID_OFFSET_Y + GRID_ROWS * CELL_SIZE):

                # Détermine la colonne cliquée
                col = (pos[0] - GRID_OFFSET_X) // CELL_SIZE

                if self.is_valid_move(col):
                    self.make_move(col)

                    # Vérifie la victoire
                    if self.check_win(self.players[self.current_player]['id']):
                        self.message = f"{self.players[self.current_player]['name']} a gagné !"
                        self.state = "end"
                        self.create_end_buttons()
                    elif self.is_board_full():  # Match nul
                        self.message = "Match nul !"
                        self.state = "end"
                        self.create_end_buttons()
                    else:
                        # Passe au joueur suivant
                        self.current_player = 1 - self.current_player

                        # Si c'est le tour de l'ordinateur
                        if self.mode != 1 and self.current_player == 1:
                            pygame.time.set_timer(pygame.USEREVENT, 1000)  # Délai de 1 seconde

        elif self.state == "end":
            # Gestion des clics dans l'écran de fin
            for i, button in enumerate(self.buttons):
                if button.is_clicked(pos, pygame.event.Event(pygame.MOUSEBUTTONDOWN)):
                    if i == 0:  # Rejouer
                        if self.mode == 1:
                            self.start_two_player_game()
                        else:
                            self.start_computer_game(self.mode)
                    else:  # Retour au menu
                        self.state = "menu"
                        self.create_menu_buttons()

    def handle_keydown(self, event):
        """Gère les événements clavier pour les champs de saisie"""
        if self.state == "player_names":
            for box in self.input_boxes:
                if box.handle_event(event):
                    # Si Enter est pressé, confirme les noms
                    self.confirm_player_names()

    def run(self):
        """Boucle principale du jeu"""
        clock = pygame.time.Clock()
        running = True

        while running:
            mouse_pos = pygame.mouse.get_pos()  # Position de la souris

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(mouse_pos)
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event)
                elif event.type == pygame.USEREVENT:
                    pygame.time.set_timer(pygame.USEREVENT, 0)  # Désactive le timer
                    self.computer_turn()

            # Vérifie le survol des boutons
            for button in self.buttons:
                button.check_hover(mouse_pos)

            # Dessine l'écran approprié
            self.draw()
            clock.tick(60)  # 60 FPS

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Crée et lance le jeu
    game = Game()
    game.run()