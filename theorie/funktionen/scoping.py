level = 0                                               # GLOABL SCOPE

def level_up(): 
    level = 5                                           # LOCAL SCOPE
    print(f"Dein Level ist: {level}")

level_up()

def level_up( level = 5 ):                              # LOCAL SCOPE
    print(f"Dein Level ist: {level}")

level_up(3)

def level_up():                                         # LOCAL SCOPE
    global level
    level += 1

level_up()
level_up()
level_up()
level_up()
level_up()
level_up()                                              # Dein Level ist 6
print(f"Dein Level ist {level}")