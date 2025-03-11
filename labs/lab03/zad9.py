import math

def odleglosc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def czy_wspoliniowe(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    
    pole = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    
    return abs(pole) < 1e-10

def obwodTrojkata(P1, P2, P3):
    if czy_wspoliniowe(P1, P2, P3):
        raise ValueError("Punkty leżą na jednej prostej i nie tworzą trójkąta!")
    
    bok1 = odleglosc(P1, P2)
    bok2 = odleglosc(P2, P3)
    bok3 = odleglosc(P3, P1)
    
    return bok1 + bok2 + bok3

try:
    punkt1 = [0, 0]
    punkt2 = [3, 0]
    punkt3 = [0, 4]
    print(f"Obwód trójkąta: {obwodTrojkata(punkt1, punkt2, punkt3)}")

    punkt4 = [0, 0]
    punkt5 = [1, 1]
    punkt6 = [2, 2]
    print(f"Obwód trójkąta: {obwodTrojkata(punkt4, punkt5, punkt6)}")
except ValueError as e:
    print(f"Błąd: {e}")