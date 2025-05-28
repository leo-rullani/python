# EINZELNE ZEICHEN AUS EINEM STRING AUSLESEN

# name = "Leugzim"

# print (len("Leo")) # len: Anz. Zeichen eines Strings werden angezeigt
# print (len(name)) # len: Anz. Zeichen eines Strings werden angezeigt

print("Leugzim"[3]) # Ausagbe: g - von vorne gezählt (bei 0 beginnen)
print("Leugzim"[-4]) #Ausgabe: g - von hinten gezählt (bei -1 beginnen)
# print("Leugzim"[9]) #Ausgabe: string index out ouf range

n = len("Leugzim")
print("Leugzim"[n-1]) # Ausgabe: letzer Buchstabe vom String, m

n = len("Leugzim")
print("Leugzim"[-1]) # Ausgabe: letzer Buchstabe vom String, m

name = "Leugzim"
print(name[2]) #Asugabe: u

#SLICING (Technik, aus einem String, Substrings herauszuschneiden)
name = "Leugzim"
print(name[0: 3]) #Startindex und Endindex: hier speziell - Indexzählung ab 1, nicht 0, Endindex ist esklusiv zu verstehen und wird nicht berücksichtigt! - Leu

name = "Leugzim"
print(name[:3]) #Startindex und Endindex: hier speziell - Indexzählung ab 1, nicht 0, Endindex ist esklusiv zu verstehen und wird nicht berücksichtigt! - Leu

name = "Leugzim"
print(name[3:7]) #Startindex und Endindex: hier speziell - Indexzählung ab 1, nicht 0, Endindex ist esklusiv zu verstehen und wird nicht berücksichtigt! - Gzim

name = "Leugzim"
print(name[3:20]) # beliebig, wird nur bis letzer Buchstabe berücksichtigt! - Gzim

x = "0123456789"
print(x[::2]) # Ausgabe: 02468

x = 29
print(f"Leo ist {x} Jahre alt!" [:11]) #Leo ist 29