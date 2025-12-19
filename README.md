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

---

## Répartition des tâches
- DJERANE MODESTE : Exercice 13 – Décalage d’une liste  
- MBAIHAM NEHEMIE : Exercice 14 – Fréquence des mots  
- DIMOUNGNA Clément : Exercice 17 – Estimation de π (Monte Carlo)  
- DA'AYANG LANDRY : Contribution à la rédaction du README  
- EKANGO EWE EDOUARD GASPARD : Vérification, tests et organisation du dépôt  

---

## Exercice 13 : Décalage d’une liste

### Problème
Il s’agit de décaler les éléments d’une liste vers la droite ou vers la gauche de manière circulaire.

### Démarche de résolution
Nous avons utilisé le découpage de listes (slicing) en Python.  
L’opérateur modulo (%) permet de gérer correctement les cas où le nombre de décalages dépasse la taille de la liste.

### Résultat
Le programme affiche les nouvelles listes obtenues après le décalage circulaire.

---

## Exercice 14 : Fréquence des mots

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

### Problème
Estimer la valeur de π à l’aide d’une méthode probabiliste.

### Démarche de résolution
Des points aléatoires sont générés dans un carré de côté 1.  
On compte le nombre de points situés à l’intérieur du quart de cercle.  
La formule π ≈ 4 × (nombre de points dans le cercle / nombre total de points) est appliquée.

### Résultat
Le programme affiche une valeur approchée de π.