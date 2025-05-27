# XOR - Verknüpfung (^)

# 10101 # <- Klartext
# 11011 # <- Schlüssel ^
# -----
# 01110 # <- Verschlüsselte Klartext
# 11011 # <- Schlüssel ^
# -----
# 10101 # <- Verschlüsselte Klartext

print(2 < 3 and 3 < 5)              # True
print(2 < 3 and 3 == 5)             # False
print(2 < 3 or 3 == 5)              # True
print(2 < 3 and 3 != 5)             # True
print((2 < 3) ^ (3 != 5))           # False
print((2 < 3) ^ (3 == 5))           # True
print (True or 2 < 3 and False)     # True
print (True and 2 < 3 and False)    # False
print ((True or 2 < 3) and False)   # False