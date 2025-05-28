# Ausgangslage -> wie kriegen wir es hin, dass es dynamisch wird (viel zu viele Variablen eklig)
# def addieren (summand1, summand2):
#    summe = summand1 + summand2
#    print(summe)

#  addieren(1,2,3,4,5,6,7)

# ARGS-PARAMETER (ARGS = flexible Variablenlänge)
def addieren(*summanden): 
    print(sum(summanden))
    
addieren(1, 2, 3, 4, 5, 6, 7, 8)

# ARGS-PARAMETER MIT POSITIONAL ARGUMENT
def lotto_spielen(vorname, nachname, *lottozahlen):                # Reihenfolge immer so: positional arguments zuerst, danach optionale Paramter (*args)
    print(f"Hallo {vorname} {nachname}")
    print(f"Deine Zahlen lauten: {lottozahlen}")
    
lotto_spielen("Leo", "Rullani", 4, 8, 15, 16, 23, 42)              # Ausgabe: Hallo Leo Rullani - Deine Zahlen lauten: (4, 8, 15, 16, 23, 42)