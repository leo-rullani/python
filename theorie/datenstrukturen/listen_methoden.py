zahlen = [1, 2, 5, 6, 9]
weitere_zahlen = [0, 10, 12, 12]

ergebnis = zahlen + weitere_zahlen
print(ergebnis)                                 # Ausgabe: [1, 2, 5, 6, 9, 0, 10, 12, 12]

bits = [0, 1]
print(bits * 3)                                 # Ausgabe: [0, 1, 0, 1, 0, 1]

numbers = [2, 3, 1, 5, 4]
numbers.append(6)                               # Ausgabe: [2, 3, 1, 5, 4, 6]
numbers.sort()                                  # Ausgabe: [1, 2, 3, 4, 5, 6]
numbers.sort(reverse=True)                      # Ausgabe: [6, 5, 4, 3, 2, 1]
print (numbers.count(2))                        # Asugabe: 1 (wie oft ist die Zahl 2 enthalten in der Liste, geht auch falls Strings/Boolean in der Liste sind)
print(numbers)                                  # Ausgabe: [1, 2, 3, 4, 5, 6]


werte = [2, 29,"Leo", True, "Sabit", 2, 5, 6, 9]   
werte.remove(True)                              # Ausgabe: # [29, 'Leo', 'Sabit', 2, 5, 6, 9]
print(werte)                                    # Beachte: Falls remove 2, nur vorderes 2 entfernt

elemente = [0, 1, 2, 4, 5, 6, 7, 8]
elemente.insert(3, 3)                           # Neuer Wert an bestimmte Position eintragen
print(elemente)                                 # Ausgabe: [0, 1, 2, 3, 4, 5, 6, 7, 8]

elemente2 = [0, 1, 2, 4, 5, 6, 7, 8]
kopie = elemente2.copy()
elemente2.clear()
print(elemente2)

shirtnumber = [0, 1, 2, 4, 5, 6, 7, 8]
position = shirtnumber.index(5)
print(position)                                 # Ausgabe: 4  

# IST EIN ELEMENT ÜBERHAUPT IN EINER LISTE ENTHALTEN?
known_number = [0, 1, 2, 4, 5, 6, 7, 8]
3 in known_number
print(3 in known_number)                        # Ausgabe: False

select_number = ["1", "2", "3"]
print(";".join(select_number))                  # 1;2;3 (";" -> "": Ausgabe = 123)