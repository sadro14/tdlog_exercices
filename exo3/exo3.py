"""
Une méthode agile est une approche itérative et collaborative pour
mener à bien un projet.
Elle génère un produit de haute qualité tout en prenant en compte
l’évolution des besoins des clients.

La méthode la plus connue est Scrum.

Au début d'un projet un « backlog », ensemble de tache à réaliser
est défini avec le client.
Ce « backlog » évolue dans le temps en fonction du besoin de client.
On peut y rajouter des taches comme on peut en enlever.

Durant le projet, une réunion avec l'équipe technique et l'équipe
opérationnelle est organisée à chaque
« sprint » (unité de temps composé de quelques semaines).
Lors cette réunion, le client valide ou non les taches
qui ont été réalisées durant la période de « sprint ».

Dans ce challenge, vous devez déterminer si à la date de la livraison
finale, le client obtient la totalité de son produit.


Format des données

Entrée
Ligne 1 : un entier N correspondant au nombre de sprints(réunion).
Ligne 2 : un entier T correspondant au nombre de taches dans le « backlog »
        initial.
Ligne 3 à N+2 : un entier V et un entier U séparés par un espace où V est
le nombre de taches validées
et U le nombre de taches à ajouter (si U est positif) ou à supprimer
(si U est négatif) dans le « backlog ».

Sortie
La chaîne OK si le backlog est vide. Sinon retourner la chaîne KO.

"""



def processLines(lines) -> str:
    # Récupération des données
    N = int(lines[0])  # Nombre de sprints
    backlog = int(lines[1])  # Nombre initial de tâches

    # Traiter chaque sprint
    for i in range(2, N + 2):
        V, U = map(int, lines[i].split())

        backlog -= V
        backlog += U

    return "OK" if backlog == 0 else "KO"

def lire_fichier(fichier):
    with open(fichier, 'r') as f:
        # Lire toutes les lignes et les stocker dans une liste, en supprimant les retours à la ligne
        lines = [line.strip() for line in f.readlines()]
    return lines

# Exemple d'utilisation
lines = lire_fichier('exo3\\sample\\input1.txt')
print(f"input1 : {processLines(lines)}")
lines = lire_fichier('exo3\\sample\\input1.txt')
print(f"input2 : {processLines(lines)}")