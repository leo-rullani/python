ergebnis = (1, 2, 3) + (4, 5)
print(ergebnis)                                 # Ausgabe: (1, 2, 3, 4, 5)

tupel = (2, 3, 4, 5, 6, 7, 8, 25, 2, 5, 2)

n = tupel.count(7)
print(n)                                        # Ausgabe: 1 (1x vorhanden)

m = tupel.index(7)
print(m)                                        # Ausgabe: 5 (Stelle 5)

zahlen = (5, 2, 3, 1, 4)
liste = list(zahlen)
liste.sort()
print(liste)                                    # Ausgabe: [1, 2, 3, 4, 5], zuerst in Liste umwandeln, da Tupel unveränderbar.

