# Definition von Variablen: immer mit Variablen arbeiten, damit der Code dynamisch bleibt.
name, age = "Leo", 29
# print(name) #Output im Terminal: Leo

# jdn. begrüssen
# print(f"Hallo {name}! Du bist {age} Jahre alt!") #f davor setzen, name in geschweiften Klammern. Output in Terminal: Hallo Leo! Du bist 29 Jahre alt!

#Keywörter, welche nicht als Variablen verwendet werden dürfen (Listenanzeige)
import keyword
# print(keyword.kwlist)

name = 29
alter = "Leo"
name, alter = alter, name #so kann ein VARIABLENTAUSCH gemacht werden (Variable Name wird Wert alter zugewiesen)

# print(f"Hallo {name}! Du bist {age} Jahre alt!")

w1 = "das war's"
w2 = "mit dem Finale DAHOOOOAM"
w3 = "Bayern ist ausgeschieden"

# print (f"{w1} {w2} {w3}!")

a = 42 
b = a
c = a
a = 10 
b = c  

# print (a) #10
# print (b) #42
# print (c) #42

# Gegeben folgendes Python Programm

vorname = "Misa"
nachname = "Amani"
geschlecht = "weiblich"
tag = 22
monat = "September"
jahr = "1998"

print(f"""Mein Name ist {vorname} {nachname}.\nIch bin
{geschlecht} und wurde am {tag}. {monat} {jahr} geboren.""")