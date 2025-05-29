def kwargs_test(**test):
    print(test)

kwargs_test(a=1, b=2, c=3)                  # Ausgabe: dictionary - {'a': 1, 'b': 2, 'c': 3}

# def teilnehmer (vorname, nachname, alter, geschlecht): 
#    print(f"{vorname} {nachname} {alter} {geschlecht}")

# teilnehmer("Leo", "Rullani", 29, "männlich")

def teilnehmer (**daten): 
    vorname = daten.get("vorname")      # hier auch default-Werte möglich für die Eintragung.
    nachname = daten.get("nachname")
    alter = daten.get("alter")
    geschlecht = daten.get("geschlecht")
    print(f"{vorname} {nachname} {alter} {geschlecht}")

teilnehmer(geschlecht="männlich", nachname="Rullani", vorname="Leo", alter=29)               # Ausgabe: Leo Rullani 29 männlich - Reihenfolge egal, grosser Vorteil von kwargs