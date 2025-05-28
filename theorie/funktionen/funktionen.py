# SayHello
def sag_hallo(firstname, lastname):
    print(f"Hallo {firstname} {lastname}!")

sag_hallo("Leo", "Rullani")

# Addition
def addieren(a, b):
    summe = a + b
    print(summe)

addieren(10, 19)

# Zwischenergebnis
def addieren2(a, b):
    summe = a + b
    return summe

s = addieren2(10, 19)
print(f"Summe: {s}")