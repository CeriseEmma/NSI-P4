# Mini Guide des Commandes Principales de Git

Git est un système de contrôle de version qui vous permet de suivre les modifications de vos fichiers au fil du temps. Voici un guide pédagogique des commandes essentielles pour débuter avec Git.

## Configuration initiale

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"
```
Ces commandes configurent votre identité pour tous vos projets Git.

## Démarrer un projet

```bash
git init
```
Cette commande crée un nouveau dépôt Git dans votre dossier actuel. Imaginez que vous créez un carnet pour noter toutes les modifications de votre projet.

```bash
git clone https://github.com/utilisateur/nom-du-projet.git
```
Cette commande télécharge une copie complète d'un projet existant. C'est comme emprunter un livre à la bibliothèque avec tout son historique inclus.

## Les commandes quotidiennes

```bash
git status
```
Montre l'état actuel de votre projet. C'est comme regarder dans votre sac pour voir ce qui a changé.

```bash
git add fichier.txt
```
Prépare un fichier spécifique pour être enregistré. Vous mettez le fichier dans une "salle d'attente" avant l'enregistrement officiel.

```bash
git add .
```
Prépare tous les fichiers modifiés pour être enregistrés.

```bash
git commit -m "Description claire de vos modifications"
```
Enregistre officiellement vos modifications préparées dans l'historique. C'est comme prendre une photo de l'état actuel de votre projet.

## Travailler avec des branches

```bash
git branch
```
Affiche toutes les branches de votre projet. Pensez aux branches comme à des univers parallèles de votre projet.

```bash
git branch nom-de-branche
```
Crée une nouvelle branche, mais reste sur la branche actuelle.

```bash
git checkout nom-de-branche
```
Bascule vers une branche existante. Vous changez d'univers parallèle.

```bash
git checkout -b nouvelle-branche
```
Crée une nouvelle branche et bascule dessus immédiatement. C'est comme créer un nouvel univers et y entrer directement.

## Synchroniser avec un dépôt distant

```bash
git remote add origin https://github.com/utilisateur/depot.git
```
Connecte votre dépôt local à un dépôt distant. C'est comme établir un pont entre votre ordinateur et GitHub.

```bash
git pull origin nom-de-branche
```
Récupère les dernières modifications depuis le dépôt distant. C'est comme mettre à jour votre livre avec les nouvelles pages écrites par d'autres.

```bash
git push origin nom-de-branche
```
Envoie vos modifications locales vers le dépôt distant. Vous partagez vos changements avec les autres.

## Examiner l'historique

```bash
git log
```
Affiche l'historique des commits. C'est comme feuilleter le journal de bord du projet.

```bash
git diff
```
Montre les différences entre votre version de travail et la dernière version enregistrée.

## Annuler des changements

```bash
git checkout -- fichier.txt
```
Annule les modifications d'un fichier non encore préparé (avant git add).

```bash
git reset HEAD fichier.txt
```
Retire un fichier de la zone de préparation (après git add, avant git commit).

```bash
git revert HEAD
```
Crée un nouveau commit qui annule les modifications du dernier commit.
