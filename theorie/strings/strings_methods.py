print(dir(str))                         # Alle Methoden für Strings werden durch diesen Befehl aufgerufen im Terminal. 
# Wir brauchen:
# zfill()
print ("Leugzim".zfill(10))             # 000Leugzim
# upper()
print ("Leugzim".upper())               # LEUGZIM
# lower()
print ("Leugzim".lower())               # leugzim
# capitalie()
print ("Leugzim".capitalize())          # Leugzim (erster Buchstabe gross)
# isupper()
print ("Leugzim".isupper())             # False
# islower()
print ("Leugzim".islower())             # False
# isnumeric()
print ("Leugzim".isnumeric())           # False
# isalpha()
print ("Leugzim".isalpha())             # True
# split()
print ("Leugzim;Saranda;Leotrim;Lirigzona;Besarta;Fatmire;Sabit".split(';'))               # ['Leugzim', 'Saranda', 'Leotrim', 'Lirigzona', 'Besarta', 'Fatmire', 'Sabit']
print ("Leugzim\nSaranda\nLeotrim\nLirigzona\nBesarta\nFatmire\nSabit".splitlines())       # ['Leugzim', 'Saranda', 'Leotrim', 'Lirigzona', 'Besarta', 'Fatmire', 'Sabit']
print ("Leugzim\nSaranda\nLeotrim\nLirigzona\nBesarta\nFatmire\nSabit")                    # Einträge untereinander.
print ("Leugzim\nSaranda\nLeotrim\nLirigzona\nBesarta\nFatmire\nSabit".split("\n"))        # ['Leugzim', 'Saranda', 'Leotrim', 'Lirigzona', 'Besarta', 'Fatmire', 'Sabit']
# strip() und replace()
print("       Leugzim  ".strip())                    # Entfernt Leerzeichen, aber nicht zwischen Strings
print("       Leu    gzim  ".replace(" ", ""))       # Alle Leerzeichen werden entfernt, auch zwischen Leu und gzim
print("       Leugzim  ".replace("u", "o"))          # Aus Leugzim wird Leogzim
#count
print("Wasserfall".count('s'))                       # Ausgabe: 2
#index
print("Wasserfall".index('fall'))                    # Ausgabe: 6
#find
print("Wasserfall".find('fall'))                     # Ausgabe: 6
print("Wasserfall".find('o'))                        # Ausgabe: -1 (Substring nicht gefunden, keine Fehlermeldung, dafür Fluchtwert -1)
#in
print("a" in "Wasserfall")                           # True