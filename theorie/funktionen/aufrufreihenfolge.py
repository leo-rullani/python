# WELCHE REIHENFOLGE FÜR POSITIONAL ARGUMENTS, ARGS & KWARGS BEI FUNKTIONSDEFINITION
# 1. POSITIONAL ARGUMENTS - 2. ARGS - 3. KWARGS
def daten_erfassen(id, vorname, nachname, *geo, **daten): 
    pass

daten_erfassen(10, "Leugzim", "Rullani", email="leugzimrullani@outlook.com")