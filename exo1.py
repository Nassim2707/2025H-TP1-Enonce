import datetime

# Demander le nom complet de l'utilisateur
# Demander l'âge de l'utilisateur
nom= input("Veuillez entrer votre nom complet : ")
age = int(input("Veuillez entrer votre âge : "))
# Définir l'année actuelle
annee_actuelle = datetime.datetime.now()
# Calculer l'année de naissance
annee_naissance = annee_actuelle.year - age
# Afficher un message de bienvenue avec le nom complet
print(f"Bonjour {nom}")
print(f"Vous êtes né(e) en {annee_naissance}")
# Afficher l'année de naissance
