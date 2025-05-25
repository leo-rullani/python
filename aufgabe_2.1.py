# 2.1: Welche der folgenden Umwandlungen sind möglich und was ist das Ergebnis? 
int(42.5)           # 42
float(-1)           # -1.0
str(0.5)            # "0.5"
bool(0.001)         # TRUE (alle Werte, die von 0 abweichen)
str("False")        # "False"
int(False)          # 0 (False = 0, TRUE = 1)
float("10")         # 10.0
bool('0')           # TRUE (False nur, wenn "leerer String" > "")
int("False")        # ValueError
float("True")       # ValueError