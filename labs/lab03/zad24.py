class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    prostokat1 = Rectangle(5, 10)
    prostokat2 = Rectangle(3, 4)
    
    print(f"Pole prostokąta 1: {prostokat1.area()}")  # 50
    print(f"Pole prostokąta 2: {prostokat2.area()}")  # 12
    
    # Zmiana wymiarów prostokąta
    prostokat1.width = 7
    print(f"Pole prostokąta 1 po zmianie szerokości: {prostokat1.area()}")  # 70