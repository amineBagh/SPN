def estimate_fine(vitesse_autorisee, vitesse_mesuree):
    speeding = vitesse_mesuree - vitesse_autorisee
    
    if speeding >= 16 and speeding <= 20:
        if vitesse_autorisee == 50 or vitesse_autorisee == 30:
            return 40
        elif vitesse_autorisee in [60, 120, 180]:
            return 20
            
    elif speeding == 21:
        if vitesse_autorisee in [50, 30, 120]:
            return 250
            
    elif speeding >= 22 and speeding <= 24:
        if vitesse_autorisee == 50:
            return 250
            
    elif speeding >= 25:
        if vitesse_autorisee in [50, 30]:
            return "Potential criminal offense"
            
    elif speeding >= 22:
        if vitesse_autorisee in [60, 120, 180]:
            return "Potential criminal offense"
            
    elif speeding >= 30 and speeding <= 59:
        if vitesse_autorisee == 30:
            return "No fine information available for this range"
        elif vitesse_autorisee in [50, 120]:
            return 600
        elif vitesse_autorisee == 180:
            return 260
            
    elif speeding >= 60:
        if vitesse_autorisee in [30, 50, 120, 180]:
            return "Potential criminal offense"
    
    return "No fine information available for this range"
