telefonbuch = {
    "Junus" :   "0764563434",
    "Florian"   :   "0795722756"
}

# print(telefonbuch.get("Junus"))
print(len(telefonbuch))

#EINZELNE WERTE AUS EINEM DICTIONARY AUSLESEN

passwort_hashes = {
    "abce123"   :   " wqöefdiz31870z134hkru1347381",
    "1337"      :   " iopjqfr20384oiqöth13up718344 ",
    "love"      :   " vxc8907as0d9vn0q048809n0f93ad "
}

print(passwort_hashes["abce123"])           # wqöefdiz31870z134hkru1347381
print(passwort_hashes.get("ultrageheim"))   # None (lieber diese Ausgabe, um Fehler im laufenden Programm zu vermeiden)

#EINZELNE WERTE AUS EINEM DICTIONARY UPDATEN

telefonummern = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}

telefonummern["Deniz"] = "0141414515"          
print(telefonummern)

telefonummern2 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}

telefonummern2["Eva"] = "097148914"          
print(telefonummern2)

telefonummern3 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}

telefonummern3.update({"Sabit" : "1312345123"})       
print(telefonummern3)

# EINZELNE SCHLÜSSEL (MIT DAZUGEHÖRIGEM WERT) AUS EINEM DICTIONARY LÖSCHEN

telefonummern4 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}

del telefonummern4["Deniz"]
print(telefonummern4)

# ALLES LÖSCHEN
telefonummern5 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}
telefonummern5.clear()
print(telefonummern5)

# RICHTIGE KOPIE ERZEUGEN
telefonummern6 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}
kopie = telefonummern6.copy()
print(telefonummern6)

# WELCHE NUMMERN BEFINDEN SICH IN MEINEM DICTIONNARY?
telefonummern7 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}

print(telefonummern7.keys())                # Ausgabe: dict_keys(['Sabit', 'Deniz', 'Fatmire']) -> Schlüsselwertpaare

# WELCHE WERTE BEFINDEN SICH IN MEINEM DICTIONNARY?
telefonummern8 = {
    "Sabit"     :       "0767884510",
    "Deniz"     :       "0914144114",
    "Fatmire"   :       "0414951841"
}

print(telefonummern8.values())                # Ausgabe: dict_values(['0767884510', '0914144114', '0414951841']) -> Schlüsselwertpaare