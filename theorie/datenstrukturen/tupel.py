print(len((1, 2, 3)))                       # Ausgabe: 3

test = (1, 2, 3, 4, 5, 6, 7, 8)
print((test)[4])                            # Ausgabe: 5
print((1, 2, 3, 4, 5, 6, 7, 8)[4])          # Ausgabe: 5 (andere Schreibweise, nicht empfehlenswert)

# FUNKTION
def addieren (a, b):
    summe = a + b
    return a, b, summe

ergebnis = addieren(1, 4)
print(ergebnis)                             # Ausgabe: (1, 4, 5)
print(type(ergebnis))                       # Ausgabe: <class 'tuple'> 

# FUNKTIN DYNAMISCH
def addieren (*summanden): 
    print(type(summanden))
addieren()