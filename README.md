# PROJET NSI PUISSANCE 4

## 1. Description générale du projet Puissance 4

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

