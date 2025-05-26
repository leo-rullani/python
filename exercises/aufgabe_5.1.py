#Was wir von dem folgenden Programm ausgegeben? 
passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper())                    # ABC123
print(passwort2.lower())                    # pass wort
print(passwort3.islower())                  # True
print(passwort2.isupper())                  # False
print(passwort1.zfill(8))                   # 00abc123
print(passwort2.strip())                    # Pass Wort
print(len(passwort3))                       # 12 (inkl. Leerzeichen)
print(passwort1.isalpha())                  # False (sind nur Buchstaben vorhanden?)
print(passwort1[3:].isnumeric())            # True (wir starten ab Index 3, vorher wird geslict)
print("a;b;c;d;e".split(';'))               # ["a", "b", "c", "d", "e"]
print("01.23.45.67.89".split(';'))          # ["01.23.45.67.89"]
print(passwort2.replace("Pass",'.'))        # . Wort
print(passwort3.count('3'))                 # Ausgabe: 2 (wie oft taucht 3 auf)
print(passwort2.count('s'))                 # Ausgabe: 2
print(passwort3.find(2+2))                  # TypeError (IndexError vermeiden)
print(passwort1.index("4"))                 # IndexError (im Hinterkopf behalten, fehleranfälliger)