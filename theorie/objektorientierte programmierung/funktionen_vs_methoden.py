# METHODEN
class Pokemon: 
    
    def __init__(self, name):
        self.name = name
        self.lebenspunkte = 42
        self.level = 1
        
        
    def vorstellen(self): 
        print(f"{self.name}, {self.name}!")
        
bisasam = Pokemon("Bisasam")
bisasam.vorstellen()