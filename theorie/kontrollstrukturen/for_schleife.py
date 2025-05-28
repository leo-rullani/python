passwörter = ["abc123", "gehe1m", "test", "123456"]

for passwort in passwörter:                         # Für jedes Passwort in der Liste soll das Passwort ausgegeben werden, und wenn die Länge kleiner als 5 ist, brechen wir aus der Schleife aus.
    print(passwort)
    if len(passwort) <5:
        break                                       # Ausgabe: abc123, geh1m, test