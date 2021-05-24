### Spliting


Le calcul du chemin Eulerien d'une ville aussi grande que montréal serait vraiment très long, de plus on considère qu'un seul drone mettrai beaucoup trop de temps a parcourir la ville.

C'est pourquoi, nous proposons cette algorithme qui va separer la ville en fonction du nombre de drones disponibles.

plus le nombres de drones disponibles sera important plus le calculs de leur parcours respectif sera rapide.



NB_DRONES = 0

while True:
    try:
        NB_DRONES = int(input("Please indicate how many drones are available to scan the city: "))
        break
    except:
        continue

print("\n\nYou have %d drones available" % NB_DRONES)
