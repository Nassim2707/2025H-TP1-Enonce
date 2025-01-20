import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
# Demander la vitesse initiale de la boule
speed = float(input("Vitesse initiale (en m/s): "))
# Demander l'angle de lancement
angle= float(input("Angle de lancer (en degrés):"))
# Convertir l'angle en radians
angle_r= angle*math.pi/180

# Calculer la distance maximale en x
distance_max = ((speed**2)*(math.sin((angle_r)*2)))/g
# Afficher la distance maximale arrondie à 2 chiffres après la virgule
distance_arrondie = round(distance_max, 1)
print(f"Distance parcourue: {distance_arrondie}m\n")
# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m
