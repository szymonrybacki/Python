import math

def rysuj_kolo(promien):
    """Rysuje koło o zadanym promieniu i zwraca jego pole."""
    for y in range(-promien, promien + 1):
        line = ""
        for x in range(-promien, promien + 1):
            # Sprawdzamy czy punkt (x,y) znajduje się w kole
            if x*x + y*y <= promien*promien:
                line += "* "
            else:
                line += "  "
        print(line)
    
    pole = math.pi * promien * promien
    return pole

def rysuj_kwadrat(bok):
    """Rysuje kwadrat o zadanym boku i zwraca jego pole."""
    for i in range(bok):
        print("* " * bok)
    
    pole = bok * bok
    return pole

def rysuj_figure(figura, *parametry):
    """
    Rysuje figurę i zwraca jej pole.
    
    Args:
        figura: typ figury ('kolo' lub 'kwadrat')
        *parametry: parametry figury (promień dla koła, bok dla kwadratu)
    """
    if figura == "kolo":
        if len(parametry) != 1:
            raise ValueError("Koło wymaga jednego parametru: promienia")
        print(f"Rysowanie koła o promieniu {parametry[0]}:")
        pole = rysuj_kolo(parametry[0])
        print(f"Pole koła: {pole:.2f}")
        return pole
    
    elif figura == "kwadrat":
        if len(parametry) != 1:
            raise ValueError("Kwadrat wymaga jednego parametru: długości boku")
        print(f"Rysowanie kwadratu o boku {parametry[0]}:")
        pole = rysuj_kwadrat(parametry[0])
        print(f"Pole kwadratu: {pole}")
        return pole
    
    else:
        raise ValueError("Nieznana figura. Obsługiwane: 'kolo', 'kwadrat'")

# Testy
print("Test koła:")
rysuj_figure("kolo", 5)

print("\nTest kwadratu:")
rysuj_figure("kwadrat", 4)