# Exercice 14 : Fréquence des mots
# Groupe 16 - TPE Cloud Computing 2026

import string

def frequence_mots(texte):
    """
    Calcule la fréquence des mots dans un texte
    sans tenir compte de la casse ni de la ponctuation.
    """
    texte = texte.lower()

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