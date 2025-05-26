#Übungsaufgaben Slicing: Was wird von dem folgenden Programm ausgegeben?
a = "Buchhaltung"
b = "Python ist toll!"

print(a[5])                 # a
print(b[-1])                # !
print(a[:4])                # Buch
print(b[11:16])             # toll!
print(a[-100:100])          # Buchhaltung
print(a[-5])                # l
print(a[-12])               # IndexError (mit::-12 möglich)
print(a[4:8])               # haltung