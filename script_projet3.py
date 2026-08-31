# Nettoyage des Distances à 0 et 0 mn:

Run_Net = Run[(Run['distance'] >= 1) & (Run['duration'] > 0)]

# Définir une colonne 'vitesses' :
Run_Net['vitesse'] = Run_Net['distance']/(Run_Net['duration'] / 60)

# Définir une colonne 'allure'(min/km)
Run_Net['allure'] = Run_Net['duration']/Run_Net['vitesse']
