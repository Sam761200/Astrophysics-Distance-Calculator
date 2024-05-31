# Importer les modules nécessaires d'Astropy
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import Distance

# Définir la parallaxe de l'étoile en millisecondes d'arc
parallaxe_mas = 50.0  # Exemple de valeur en millisecondes d'arc

# Calculer la distance en parsecs
distance_pc = Distance(parallax=parallaxe_mas * u.mas).pc

# Afficher le résultat
print(f"La distance de l'étoile est de {distance_pc:.2f} parsecs")
