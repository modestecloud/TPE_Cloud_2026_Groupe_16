# Exercice 17 : Estimation de Pi par la méthode de Monte Carlo
# Groupe 16 - TPE Cloud Computing 2026

import random

def estimation_pi(n):
    """
    Estime la valeur de Pi à l'aide de la méthode de Monte Carlo.
    """
    points_dans_cercle = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            points_dans_cercle += 1

    return 4 * points_dans_cercle / n

# Programme principal
nombre_points = 100000
pi = estimation_pi(nombre_points)

print("Valeur estimée de Pi :", pi)