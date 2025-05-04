# PROJET NSI PUISSANCE 4

## 1. Description générale du projet

### 1.1 Contexte et objectifs

L'objectif principal est de concevoir et réaliser une application fonctionnelle offrant une expérience de jeu agréable avec une interface graphique épurée mais efficace. Le programme devra implémenter fidèlement les règles traditionnelles du Puissance 4 et proposer deux modes de jeu distincts : une confrontation entre deux joueurs humains et un mode où le joueur affronte l'ordinateur.

## 2. Spécifications fonctionnelles

### 2.1 Règles du jeu

Le Puissance 4 est un jeu de stratégie à deux joueurs dont les règles fondamentales sont les suivantes :

- Le jeu se déroule sur un plateau vertical composé de 7 colonnes horizontales et 6 lignes verticales, formant une grille de 42 cases au total.
- Chaque joueur dispose d'un ensemble de 21 jetons d'une couleur qui lui est propre, traditionnellement rouge pour le premier joueur et jaune pour le second.
- À tour de rôle, les joueurs choisissent une colonne dans laquelle insérer l'un de leurs jetons.
- Sous l'effet de la gravité simulée, le jeton descend jusqu'à atteindre soit le bas du plateau, soit un autre jeton déjà placé dans la même colonne.
- Le but du jeu est d'être le premier à aligner exactement quatre jetons de sa couleur, que ce soit horizontalement (sur une même ligne), verticalement (dans une même colonne) ou en diagonale.
- Si toutes les cases du plateau sont occupées sans qu'aucun des joueurs n'ait réalisé d'alignement gagnant, la partie est déclarée nulle.
- La partie prend fin immédiatement dès qu'un joueur réussit à créer un alignement de quatre jetons ou lorsque le plateau est entièrement rempli.

### 2.2 Modes de jeu

Le programme offrira deux modes de jeu distincts, permettant de varier l'expérience utilisateur :

#### 2.2.1 Mode deux joueurs humains

Ce mode classique permettra à deux personnes de s'affronter sur le même ordinateur :

- Les joueurs utiliseront alternativement la même interface pour placer leurs jetons.
- Une indication visuelle claire (texte et couleur) informera à tout moment quel joueur doit jouer son tour.
- L'interaction se fera via la souris, chaque joueur cliquant sur la colonne où il souhaite placer son jeton.
- Lorsqu'un alignement gagnant sera réalisé, le programme le mettra visuellement en évidence (surbrillance ou encadrement des jetons concernés).
- Un système de score comptabilisera les victoires de chaque joueur au cours de la session.

#### 2.2.2 Mode joueur contre ordinateur

Ce mode permettra à un joueur solitaire de défier l'application :

- Le joueur humain commencera toujours la partie avec les jetons rouges.
- L'ordinateur, contrôlant les jetons jaunes, jouera automatiquement après chaque coup du joueur.
- Pour simuler une réflexion, l'ordinateur marquera une courte pause avant de placer son jeton.
- La stratégie de l'ordinateur sera volontairement simple, basée sur un placement aléatoire des jetons parmi les colonnes disponibles.
- Le système de détection des victoires et d'affichage des scores fonctionnera de manière identique au mode deux joueurs.

### 2.3 Interface utilisateur

L'interface du jeu sera intuitive et fonctionnelle, divisée en trois écrans principaux :

#### 2.3.1 Écran d'accueil

L'écran d'accueil constituera le point d'entrée de l'application et comprendra :

- Un titre clairement visible présentant le jeu "Puissance 4".
- Deux boutons distincts permettant de lancer soit le mode deux joueurs, soit le mode contre l'ordinateur.
- Un champ de saisie optionnel permettant aux joueurs de personnaliser leurs noms (par défaut "Joueur 1" et "Joueur 2" ou "Ordinateur").
- Un bouton d'accès aux règles du jeu, affichant une fenêtre explicative avec les instructions complètes.
- Un bouton "Quitter" permettant de fermer proprement l'application.
- Une interface épurée aux couleurs rappelant l'univers du jeu (généralement bleu pour le plateau, rouge et jaune pour les jetons).

#### 2.3.2 Écran de jeu

L'écran de jeu principal affichera :

- Le plateau de jeu occupant la majeure partie de l'écran, présentant clairement la grille de 7×6 cases.
- Les jetons déjà placés, avec une distinction visuelle évidente entre les deux couleurs.
- Une zone d'information indiquant le nom et la couleur du joueur dont c'est le tour.
- Un compteur de score affichant le nombre de parties gagnées par chaque joueur durant la session.
- Un bouton "Abandonner" permettant de terminer prématurément la partie en cours.
- Un bouton "Nouvelle partie" permettant de réinitialiser le plateau sans revenir au menu principal.
- Un bouton "Menu principal" pour revenir à l'écran d'accueil.
- Un bouton d'aide permanent donnant accès aux règles du jeu à tout moment, sans interrompre la partie en cours.
- Optionnellement, une zone indiquant le nombre de jetons restants pour chaque joueur.

#### 2.3.3 Écran de fin de partie

Lorsqu'une partie se termine, un écran ou une fenêtre contextuelle s'affichera pour :

- Annoncer clairement le résultat (victoire d'un joueur ou match nul).
- Dans le cas d'une victoire, mettre en évidence l'alignement gagnant sur le plateau.
- Afficher le score mis à jour après cette partie.
- Proposer trois options au(x) joueur(s) :
    - "Rejouer" pour démarrer une nouvelle partie avec les mêmes paramètres.
    - "Changer de mode" pour revenir à l'écran de sélection du mode de jeu.
    - "Menu principal" pour retourner à l'écran d'accueil.

## 3. Spécifications techniques

### 3.1 Architecture du programme

#### 3.1.1 Approche simplifiée avec séparation des responsabilités

Pour faciliter le développement et la maintenance du code, le programme adoptera une architecture simple mais efficace, divisant les responsabilités entre plusieurs modules complémentaires :

- **Module principal (`main.py`)**: Ce module constitue l'épine dorsale du programme et remplit plusieurs fonctions essentielles :
    
    - Point d'entrée unique du programme, initialisant l'environnement Python et les bibliothèques nécessaires
    - Configuration initiale de Pygame (dimensions de la fenêtre, titre, icône, etc.)
    - Implémentation de la boucle de jeu principale (game loop) gérant les événements, les mises à jour et le rendu
    - Orchestration des différents états du jeu (menu principal, partie en cours, fin de partie)
    - Gestion du timing et de la fréquence d'images (FPS)
    - Coordination entre les différents modules pour assurer leur interaction harmonieuse
- **Module de logique de jeu (`game_logic.py`)**: Ce module encapsule toutes les règles et mécanismes fondamentaux du jeu :
    
    - Définition et initialisation de la structure de données représentant le plateau de jeu
    - Implémentation des fonctions de placement des jetons dans les colonnes
    - Calcul des positions finales des jetons après leur chute dans une colonne
    - Algorithmes de vérification des conditions de victoire (alignements horizontaux, verticaux et diagonaux)
    - Détection des situations de match nul (plateau rempli sans alignement)
    - Gestion de l'alternance des tours entre les joueurs
    - Fonctions de réinitialisation du plateau pour une nouvelle partie
- **Module d'affichage (`display.py`)**: Ce module gère tous les aspects visuels du jeu :
    
    - Création et gestion des différents écrans (accueil, jeu, fin de partie)
    - Dessin du plateau de jeu et des jetons avec leurs couleurs appropriées
    - Rendu des éléments d'interface (boutons, zones de texte, compteurs)
    - Affichage des informations textuelles (nom du joueur actif, scores, messages)
    - Mise en évidence visuelle des alignements gagnants
    - Gestion des transitions entre les différents écrans
    - Rafraîchissement de l'affichage à chaque cycle de la boucle de jeu
- **Module de l'ordinateur (`computer_player.py`)**: Ce module implémente le comportement de l'adversaire artificiel :
    
    - Algorithme de sélection aléatoire d'une colonne disponible
    - Gestion du délai de "réflexion" avant le placement d'un jeton
    - Interface permettant au programme principal d'obtenir le coup choisi par l'ordinateur
- **Module utilitaire (`utils.py`)**: Ce module regroupe les fonctionnalités transversales et les éléments de configuration :
    
    - Définition des constantes globales (dimensions, couleurs, textes)
    - Fonctions auxiliaires réutilisables par les autres modules
    - Fonctionnalités de sauvegarde et chargement des parties
    - Gestion des statistiques de jeu
    - Fonctions de journalisation pour le débogage

#### 3.1.2 Organisation des fichiers

La structure du projet sera organisée comme suit pour faciliter la navigation et la maintenance :

```
puissance4/
│
├── main.py            # Programme principal et boucle de jeu
├── game_logic.py      # Logique du jeu et règles
├── display.py         # Fonctions d'affichage
├── utils.py           # Fonctions utilitaires et constantes
├── computer_player.py # Stratégie de l'ordinateur (simple)
│
├── saves/             # Dossier contenant les sauvegardes de parties
│   └── saved_games.dat
│
└── assets/            # Ressources graphiques minimales
    ├── red_token.png
    ├── yellow_token.png
    ├── board.png
    ├── background.png
    └── icon.png
```

Cette organisation claire permettra un développement modulaire et facilitera les éventuelles modifications ou améliorations futures.

### 3.2 Spécifications du plateau de jeu

Le plateau de jeu constitue l'élément central du programme et sera représenté de manière précise :

- **Représentation interne**: Matrice bidimensionnelle de dimensions 7×6 (colonnes × lignes)
- **Système de coordonnées**: L'origine (0,0) sera située en haut à gauche du plateau, les colonnes s'étendant horizontalement (de 0 à 6) et les lignes verticalement (de 0 à 5)
- **Valeurs possibles** pour chaque case de la matrice :
    - 0: Case vide, aucun jeton présent
    - 1: Jeton du joueur 1 (généralement rouge)
    - 2: Jeton du joueur 2 ou de l'ordinateur (généralement jaune)
- **Accès aux éléments**: L'état d'une case sera accessible via la notation plateau[colonne][ligne]
- **Représentation visuelle**: Sur l'interface graphique, le plateau sera dessiné avec :
    - Une structure bleue comportant des emplacements circulaires vides
    - Des jetons rouges pour le joueur 1
    - Des jetons jaunes pour le joueur 2 ou l'ordinateur
    - Une taille suffisante pour que les jetons soient clairement visibles

### 3.3 Stratégie pour l'ordinateur

Pour ce projet, l'ordinateur adoptera une stratégie intentionnellement simple :

- **Stratégie aléatoire**:
    - À chaque tour, l'ordinateur identifiera toutes les colonnes non pleines (celles où il est encore possible de placer un jeton)
    - Parmi ces colonnes disponibles, il en sélectionnera une de manière totalement aléatoire
    - Cette sélection utilisera le module `random` de Python, et plus spécifiquement la fonction `random.choice()`
    - Un délai artificiel de 0,5 à 1,5 seconde sera introduit pour simuler une "réflexion"
    - Cette approche produira un adversaire imprévisible mais sans intelligence stratégique particulière

### 3.4 Algorithmes clés

Plusieurs algorithmes essentiels devront être implémentés pour assurer le bon fonctionnement du jeu :

- **Détection des alignements**: Cet algorithme crucial vérifiera après chaque coup si le joueur vient de réaliser un alignement gagnant :
    
    - Parcours horizontal : vérification des lignes pour détecter 4 jetons identiques consécutifs
    - Parcours vertical : vérification des colonnes pour détecter 4 jetons identiques consécutifs
    - Parcours diagonal descendant (haut-gauche vers bas-droite) : vérification des diagonales descendantes
    - Parcours diagonal montant (bas-gauche vers haut-droite) : vérification des diagonales montantes
    - Optimisation possible : limiter la vérification aux lignes, colonnes et diagonales affectées par le dernier coup joué
- **Simulation de gravité**: Cet algorithme déterminera la position finale d'un jeton dans une colonne :
    
    - Vérification préalable que la colonne n'est pas déjà remplie
    - Parcours de la colonne du haut vers le bas pour trouver la première case occupée
    - Placement du jeton dans la case vide située juste au-dessus
    - Gestion du cas particulier où la colonne est entièrement vide (placement en bas de la colonne)
- **Détection de plateau plein**: Cet algorithme simple mais nécessaire vérifiera si toutes les cases du plateau sont occupées pour détecter les situations de match nul :
    
    - Vérification que toutes les cases de la rangée supérieure sont occupées, ou
    - Comptage du nombre total de jetons placés (égal à 42 si le plateau est plein)

### 3.5 Bibliothèques Python recommandées

Pour développer ce jeu, plusieurs bibliothèques Python seront particulièrement utiles :

- **Pygame (v2.5+)**: Cette bibliothèque incontournable pour le développement de jeux en Python offrira :
    
    - Un système complet de gestion des fenêtres graphiques
    - Des fonctionnalités de dessin 2D performantes pour l'affichage du plateau et des jetons
    - Un système robuste de gestion des événements (clics souris, clavier, fermeture de fenêtre)
    - Des fonctionnalités de chargement et d'affichage d'images pour les ressources graphiques
    - Des outils de gestion du timing et de contrôle de la fréquence d'images
    - Des capacités de rendu de texte pour l'affichage des informations
    - Installation via la commande : `pip install pygame`
    - Documentation complète disponible sur https://www.pygame.org/docs/
- **NumPy (v1.25+)**: Cette bibliothèque de calcul numérique facilitera la manipulation du plateau de jeu :
    
    - Création et manipulation efficace de tableaux multidimensionnels pour représenter le plateau
    - Fonctions puissantes pour analyser les configurations du plateau (recherche d'alignements)
    - Opérations vectorielles optimisées pour améliorer les performances de détection
    - Installation via la commande : `pip install numpy`
    - Documentation disponible sur https://numpy.org/doc/
- **Pygame-menu (v4.4+)**: Cette extension de Pygame simplifiera considérablement la création des interfaces :
    
    - Système prêt à l'emploi pour créer des menus interactifs et esthétiques
    - Widgets intégrés (boutons, champs de texte, sélecteurs) pour l'interface utilisateur
    - Gestion automatique des événements pour les éléments de menu
    - Thèmes personnalisables pour harmoniser l'apparence des interfaces
    - Installation via la commande : `pip install pygame-menu`
    - Documentation accessible sur https://pygame-menu.readthedocs.io/

Ces bibliothèques offrent un excellent compromis entre simplicité d'utilisation et puissance des fonctionnalités, parfaitement adaptées au niveau de complexité de ce projet.

## 4. Plan de développement

Le développement du jeu sera organisé en phases progressives et logiques :

### 4.1 Phase 1: Fondations et logique du jeu

Cette phase initiale établira les mécanismes fondamentaux du jeu :

- Création du fichier `game_logic.py` implémentant la représentation interne du plateau
- Définition des fonctions de base pour initialiser et afficher l'état du plateau (version console)
- Implémentation des mécanismes de placement des jetons avec simulation de la gravité
- Développement des algorithmes de détection des alignements dans les quatre directions
- Création de la fonction de vérification des conditions de victoire
- Implémentation de la détection des situations de match nul
- Tests unitaires pour valider chaque aspect de la logique du jeu

À la fin de cette phase, le jeu sera fonctionnel en mode console, permettant de vérifier la solidité des règles avant d'ajouter l'interface graphique.

### 4.2 Phase 2: Interface graphique basique

Cette phase transformera le jeu console en application graphique :

- Création du fichier `display.py` pour gérer l'affichage
- Configuration de l'environnement Pygame (taille de fenêtre, couleurs, titre)
- Implémentation du rendu basique du plateau de jeu
- Création des représentations graphiques des jetons
- Dessin de la grille et des emplacements des jetons
- Gestion des événements utilisateur (clic de souris pour sélectionner une colonne)
- Mise en place de la boucle de jeu principale

À l'issue de cette phase, le joueur pourra voir le plateau et placer des jetons via l'interface graphique.

### 4.3 Phase 3: Mode deux joueurs

Cette phase implémentera le premier mode de jeu complet :

- Développement du système d'alternance des tours entre les deux joueurs
- Ajout d'indicateurs visuels pour informer du joueur actif
- Implémentation de la mise en évidence des alignements gagnants
- Création de l'écran d'annonce de victoire ou de match nul
- Développement du système de comptage des scores
- Ajout des fonctionnalités de réinitialisation pour une nouvelle partie

Cette phase permettra à deux joueurs humains de s'affronter via l'interface graphique avec toutes les fonctionnalités nécessaires.

### 4.4 Phase 4: Mode joueur contre ordinateur

Cette phase ajoutera le second mode de jeu :

- Création du fichier `computer_player.py`
- Implémentation de l'algorithme de sélection aléatoire de colonne
- Développement du mécanisme de "réflexion" temporisée
- Intégration du joueur ordinateur dans le déroulement de la partie
- Adaptation de l'interface pour distinguer clairement le mode de jeu actif
- Tests d'équilibrage et ajustements

À la fin de cette phase, les deux modes de jeu seront pleinement fonctionnels.

### 4.5 Phase 5: Fonctionnalités additionnelles

Cette phase finale complètera l'application avec les éléments supplémentaires :

- Création des écrans de menu (accueil, sélection du mode, aide)
- Implémentation du système de sauvegarde et chargement de parties
- Ajout de l'aide contextuelle accessible à tout moment
- Tests approfondis dans différents scénarios
- Correction des bugs identifiés
- Optimisations de performance si nécessaire
- Documentation détaillée du code source

Cette phase finalisera le projet en le rendant complet, robuste et convivial pour l'utilisateur final.

## 5. Bibliothèques Python nécessaires et facultatives

### 5.1 Bibliothèques essentielles

Ces bibliothèques constituent le cœur technique du projet et devront impérativement être installées :

- **Pygame (v2.5+)**: Bibliothèque fondamentale pour le développement de jeux en Python, Pygame fournira toutes les fonctionnalités graphiques et interactives nécessaires au projet.
    
    - Installation: `pip install pygame`
    - Dépendances: SDL (Simple DirectMedia Layer), installée automatiquement
    - Compatibilité: Windows, macOS, Linux
    - Fonctionnalités principales utilisées:
        - `pygame.display`: gestion de la fenêtre et de l'affichage
        - `pygame.draw`: fonctions de dessin primitives (cercles, rectangles)
        - `pygame.image`: chargement et manipulation d'images
        - `pygame.font`: rendu de texte
        - `pygame.event`: capture et traitement des événements utilisateur
        - `pygame.time`: contrôle du timing et des FPS
    - Documentation officielle: https://www.pygame.org/docs/
    - Tutoriels recommandés: https://www.pygame.org/wiki/tutorials
- **NumPy (v1.25+)**: Cette bibliothèque de calcul numérique optimisera le traitement des données du plateau et les algorithmes de détection.
    
    - Installation: `pip install numpy`
    - Fonctionnalités principales utilisées:
        - `numpy.array`: création et manipulation de tableaux multidimensionnels
        - `numpy.zeros`: initialisation de tableaux vides
        - `numpy.where`: recherche conditionnelle d'éléments
        - Opérations vectorielles pour l'analyse du plateau
    - Documentation officielle: https://numpy.org/doc/
    - Guide de démarrage: https://numpy.org/doc/stable/user/absolute_beginners.html

### 5.2 Bibliothèques facultatives mais recommandées

Ces bibliothèques, bien que non strictement indispensables, faciliteront considérablement le développement :

- **Pygame-menu (v4.4+)**: Cette extension de Pygame simplifiera la création des menus et interfaces.
    
    - Installation: `pip install pygame-menu`
    - Fonctionnalités principales:
        - Création de menus interactifs avec plusieurs niveaux
        - Widgets préconçus (boutons, étiquettes, sélecteurs)
        - Thèmes personnalisables et transitions
        - Gestion automatique des événements pour les éléments d'interface
    - Documentation: https://pygame-menu.readthedocs.io/
    - Exemples: https://github.com/ppizarror/pygame-menu/tree/master/pygame_menu/examples
- **Pickle** (bibliothèque standard): Ce module intégré à Python permettra d'implémenter la sauvegarde des parties.
    
    - Déjà disponible dans l'installation standard de Python
    - Fonctionnalités principales:
        - Sérialisation et désérialisation d'objets Python
        - Sauvegarde de l'état du jeu dans un fichier binaire
        - Chargement ultérieur des parties sauvegardées
    - Documentation: https://docs.python.org/3/library/pickle.html
- **JSON** (bibliothèque standard): Alternative à Pickle pour la sauvegarde dans un format plus portable.
    
    - Déjà disponible dans l'installation standard de Python
    - Fonctionnalités principales:
        - Conversion de structures de données Python en format texte JSON
        - Format lisible et éditable manuellement
        - Interopérabilité avec d'autres langages et plateformes
    - Documentation: https://docs.python.org/3/library/json.html
