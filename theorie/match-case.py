# MATCH-CASE-ANWEISUNG
note = [1,2,3]
note = int(input("Gib die Note ein: "))
match note: 
    case [1,2,3]: 
        print("Tolle Liste!")
    case 2: 
        print("Gut!")
    case 3: 
        print("Befriedigend.")
    case 4: 
        print("Ausreichend.")
    case 5: 
        print("Mangelhaft!")
    case 6:                                         # Default-Case -> case _:
        print("Ungenügend!!!")