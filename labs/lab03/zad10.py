import math

def odleglosc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def czy_wspolliniowe(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    
    # Obliczenie pola trójkąta ze wzoru
    pole = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    
    # Jeśli pole jest praktycznie równe 0, punkty leżą na jednej prostej
    return abs(pole) < 1e-10

def obwod_trojkata(P1, P2, P3):
    # Sprawdzenie czy punkty są współliniowe
    if czy_wspolliniowe(P1, P2, P3):
        print("UWAGA: Punkty są współliniowe i nie tworzą trójkąta!")
        return 0
    
    # Obliczanie długości boków trójkąta
    bok1 = odleglosc(P1, P2)
    bok2 = odleglosc(P2, P3)
    bok3 = odleglosc(P3, P1)
    
    return bok1 + bok2 + bok3

# Test działania funkcji
punkt1 = [0, 0]
punkt2 = [3, 0]
punkt3 = [0, 4]
print(f"Obwód trójkąta: {obwod_trojkata(punkt1, punkt2, punkt3)}")

punkt4 = [0, 0]
punkt5 = [1, 1]
punkt6 = [2, 2]
print(f"Obwód trójkąta: {obwod_trojkata(punkt4, punkt5, punkt6)}")