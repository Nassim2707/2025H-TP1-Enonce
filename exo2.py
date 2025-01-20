# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
batterie = float(input("Entrez le niveau de charge actuel de la batterie : "))
# Vérifiez si le niveau de charge est valide
if batterie > 100 or batterie < 0 :
    print("Erreur : niveau de charge invalide. ")
else: 

# Arrondir le pourcentage à la dizaine la plus proche
    batterie_arrondie = int(round(batterie, -1))

# Calculer le nombre de barres
    barres = "❚" * (batterie_arrondie // 10)
    espaces = " " * (10 - (batterie_arrondie // 10))
# Afficher la représentation graphique de la charge de la batterie
print(f"[{barres}{espaces}]\n{batterie}%\n")
# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%