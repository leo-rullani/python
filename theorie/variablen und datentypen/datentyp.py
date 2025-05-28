#STRING
name = "Leo"

#INTEGER (GANZE ZAHLEN)
age = 100_000 #(underscore wird auch als Ganzzahl für Lesbarkeit von python interpretiert)

#FLOATS (ZAHLEN MIT KOMMA)
weight = 100.5

#BOOLEAN (Wahrheitswerte)
answer = True
answer = False

#Type-Funktion (Datentyp herauslesen)
name = "Leo"
age = "29"
weight = 99.5
married = True
print (type(name)) #Ausgabe : <class 'str' für name - mit der type-funktion wird Type ausgegeben in Terminal
#Weitere Funktsionsaufrufe
print (type(str(29))) #Ausgabe : <class 'str'> für name - mit der type-funktion wird Type ausgegeben in Terminal
print (type(int("29"))) #Ausgabe : <class 'int'>
print (type(float("2.9"))) #Ausgabe : <class 'float'>
print (float(True)) #Ausgabe: 1.0 = 1.0 für wahr, 0 für False
print (bool(0.1)) #Ausgabe: alles über 0.0 wird als True interpretiert
print (bool("")) #Ausgabe: nichts drin = false