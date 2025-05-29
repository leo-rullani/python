liste = [1, 2, 3, "Leo", "Sabit", "Fatmire"]

try:
    index = int(input("Bitte gib einen Index ein: "))
    print(liste[index])
except Exception as ex: 
    print(f"Es ist ein Fehler aufgetreten.\n{ex}")
finally: 
    print("Ich bin fertig!")