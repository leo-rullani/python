zahlen = {1, 4, 6, 7, 0}
print(6 in zahlen)                                      # Ausgabe: True

zahlen.add(-1)
print(zahlen)                                           # Ausgabe: {0, 1, 4, 6, 7, -1}

# prim = {2, 3, 5, 8, 11}
# prim.remove(8)                                        # Ausgabe: {2, 3, 5, 11}
# print(prim)

prim = {2, 3, 5, 8, 11}
kopie = prim.copy()
print(prim)

liste = list(prim)
liste.sort()
print(list(prim))                                       # Ausgabe: [2, 3, 5, 8, 11]