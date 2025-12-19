# TPE Cloud Computing 2026

## Projet académique – TPE Cloud Computing 2026

## Nom du groupe
Groupe 16

---

## Membres du groupe
1. DJERANE MODESTE – 18A803FS  
2. MBAIHAM NEHEMIE – 22A952FS  
3. DIMOUNGNA Clément – 22B197FS  
4. DA'AYANG LANDRY – 22B442FS  
5. EKANGO EWE EDOUARD GASPARD – 22B831FS  
6. NADIA KIRO MANGA TAMANDA 22A787FS
---

## Répartition des tâches
- DJERANE MODESTE : Exercice 13 – Décalage d’une liste  
- MBAIHAM NEHEMIE : Exercice 14 – Fréquence des mots  
- DIMOUNGNA Clément : Exercice 17 – Estimation de π (Monte Carlo)  
- DA'AYANG LANDRY : Contribution à la rédaction du README  
- EKANGO EWE EDOUARD GASPARD : Vérification, tests et organisation du dépôt  
- NADIA KIRO MANGA TAMANDA 22A787FS : Relecture finale, corrections et synthèse du projet
---

## Exercice 13 : Décalage d’une liste

# Exercice 13 : Décalage circulaire d'une liste

def decalage_liste(liste, k):
    """
    Cette fonction décale une liste de k positions vers la droite
    de manière circulaire.
    """
    n = len(liste)
    k = k % n  # pour éviter les erreurs si k > taille de la liste
    return liste[-k:] + liste[:-k]


# Programme principal
liste = [1, 2, 3, 4, 5]
k = 2

print("Liste initiale :", liste)
print("Liste après décalage de", k, "positions :", decalage_liste(liste, k))

### Problème
Il s’agit de décaler les éléments d’une liste vers la droite ou vers la gauche de manière circulaire.

### Démarche de résolution
Nous avons utilisé le découpage de listes (slicing) en Python.  
L’opérateur modulo (%) permet de gérer correctement les cas où le nombre de décalages dépasse la taille de la liste.

### Résultat
Le programme affiche les nouvelles listes obtenues après le décalage circulaire.

---

## Exercice 14 : Fréquence des mots

# Exercice 14 : Calcul de la fréquence des mots

import string

def frequence_mots(texte):
    """
    Cette fonction calcule la fréquence des mots dans un texte
    sans tenir compte de la casse ni de la ponctuation.
    """
    # Conversion en minuscules
    texte = texte.lower()

    # Suppression de la ponctuation
    for caractere in string.punctuation:
        texte = texte.replace(caractere, "")

    mots = texte.split()
    frequences = {}

    for mot in mots:
        if mot in frequences:
            frequences[mot] += 1
        else:
            frequences[mot] = 1

    return frequences


# Programme principal
texte = "Le Cloud computing est le futur du Cloud et du computing."
resultat = frequence_mots(texte)

print("Fréquence des mots :")
print(resultat)

### Problème
Déterminer le nombre d’apparitions de chaque mot dans un texte, sans tenir compte de la casse ni de la ponctuation.

### Démarche de résolution
Le texte est converti en minuscules afin d’ignorer la casse.  
La ponctuation est supprimée à l’aide du module `string`.  
Un dictionnaire est ensuite utilisé pour compter la fréquence de chaque mot.

### Résultat
Le programme affiche un dictionnaire associant chaque mot à son nombre d’occurrences.

---

## Exercice 17 : Estimation de π par la méthode de Monte Carlo

# Exercice 17 : Estimation de Pi par la méthode de Monte Carlo

import random

def estimation_pi(n):
    """
    Cette fonction estime la valeur de Pi
    en utilisant la méthode de Monte Carlo.
    """
    points_dans_cercle = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            points_dans_cercle += 1

    pi_estime = 4 * points_dans_cercle / n
    return pi_estime


# Programme principal
nombre_points = 100000
pi = estimation_pi(nombre_points)

print("Valeur estimée de Pi :", pi)
### Problème
Estimer la valeur de π à l’aide d’une méthode probabiliste.

### Démarche de résolution
Des points aléatoires sont générés dans un carré de côté 1.  
On compte le nombre de points situés à l’intérieur du quart de cercle.  
La formule π ≈ 4 × (nombre de points dans le cercle / nombre total de points) est appliquée.

### Résultat
Le programme affiche une valeur approchée de π.