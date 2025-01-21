secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees = secondes // (365 * 24 * 60 * 60)
secondes %= (365 * 24 * 60 * 60)

# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines = secondes // (7 * 24 * 60 * 60)
secondes %= (7 * 24 * 60 * 60)

# TODO: Assigner à la variable "jours" le nombre de jours restants
jours = secondes // (24 * 60 * 60)
secondes %= (24 * 60 * 60) 
# TODO: Assigner à la variable "heures" le nombre d'heures restantes
heures = secondes // (60 * 60)
secondes %= (60 * 60)
# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
minutes = secondes // 60
secondes %= 60
# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes= secondes
# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
#output = f"{annees} années, {semaines} semaines, {jours} jours, {heures} heures, {minutes} minutes, {secondes} secondes"
print(f"{annees} {semaines} {jours} {heures} {minutes} {secondes}")