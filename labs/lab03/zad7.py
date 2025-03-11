import math

def odleglosc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Test działania funkcji
punkt1 = [0, 0]
punkt2 = [3, 4]
print(f"Odległość między {punkt1} i {punkt2} wynosi: {odleglosc(punkt1, punkt2)}")  # Powinno zwrócić 5.0

punkt3 = [6, 9]
punkt4 = [4, 20]
print(f"Odległość między {punkt3} i {punkt4} wynosi: {odleglosc(punkt3, punkt4)}")  # Powinno zwrócić 5.0