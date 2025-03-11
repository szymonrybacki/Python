class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        
    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} i mam {self.wiek} lat.")

# Test klasy
if __name__ == "__main__":
    osoba1 = Person("Anna", 25)
    osoba2 = Person("Jan", 30)
    
    osoba1.przedstaw_sie()
    osoba2.przedstaw_sie()