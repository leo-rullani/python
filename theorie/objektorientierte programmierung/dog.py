class mammal: 
    def __init__(self, farbe, rasse, name): 
        self.farbe = farbe
        self.rasse = rasse
        self.name = name
    
    def vorstellen(self): 
        print(f"Ich bin {self.name}")
        
    def essen(self): 
        pass
    
    def laufen(self):
        pass

class Hund(mammal): 
    def essen(self): 
        pass
    
    def bellen(self): 
        pass
    
class Katze(mammal):
    def miauen(self):
        print("Miau!!!")

dog1 = Hund("white-creamy", "Pomerian", "Coco")
dog2 = Hund("brown", "Pomerian", "Bella")

dog1.vorstellen()