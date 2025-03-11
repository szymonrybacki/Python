import math

def odleglosc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def obwodTrojkata(P1, P2, P3):
    bok1 = odleglosc(P1, P2)
    bok2 = odleglosc(P2, P3)
    bok3 = odleglosc(P3, P1)
    
    return bok1 + bok2 + bok3

punkt1 = [0, 0]
punkt2 = [3, 0]
punkt3 = [0, 4]
print(f"Obwód trójkąta: {obwodTrojkata(punkt1, punkt2, punkt3)}")  # Powinno zwrócić 12.0