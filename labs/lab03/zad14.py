def czy_pierwsza(n):
    # Liczby mniejsze niż 2 nie są liczbami pierwszymi
    if n < 2:
        return False
    
    # 2 jest liczbą pierwszą
    if n == 2:
        return True
    
    # Liczby parzyste większe niż 2 nie są liczbami pierwszymi
    if n % 2 == 0:
        return False
    
    # Sprawdzanie dzielników od 3 do pierwiastka z n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

# Testy
print(czy_pierwsza(2))   # True
print(czy_pierwsza(3))   # True
print(czy_pierwsza(4))   # False
print(czy_pierwsza(17))  # True
print(czy_pierwsza(20))  # False
print(czy_pierwsza(97))  # Trueś