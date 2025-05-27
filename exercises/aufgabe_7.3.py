a = 2.5
b = -5
c = 20 
d = "Hallo"
e = "Python"

d + " " + e             # "Hallo Python"
c % 7                   # 6
16**(a - 2)             # 4.0 (0.5 = Wurzel aus 16)
d**c                    # TypeError (Strings lassen sich nicht mit sich selbst potenzieren)
(b+c) / b               # -3.0
20**(2 * a + b)         # 1.0 (20 hoch 0.0)
2 * a * d               # TypeError (da 5.0 keine Ganzzahl, String lässt sich nur mit Integer multiplizieren)
(c - b) // 7            # 3
e // "Python"           # TypeError (Division von Strings nicht möglich)
b**2 - 25               # 0
True or False ^ True    # True (wenn False or True zusammengerechnet wird -> immer True)
0 > 1 and True ^ True   # False (wenn False and True zusammengerechnet wird -> immer False)