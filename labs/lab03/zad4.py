def pietro(znak):
    print("+" + znak * 7 + "+")
    print("|" + "  ___  " + "|")
    print("|" + " |   | " + "|")
    print("|" + " |___| " + "|")
    print("|" + "       " + "|")
    print("+" + znak * 7 + "+")

def dach(znak):
    print("    /" + znak + "\\    ")
    print("   /" + znak * 2 + "\\   ")
    print("  /" + znak * 4 + "\\  ")
    print(" /" + znak * 6 + "\\ ")
    print("/" + znak * 8 + "\\")

def rysuj_dom(liczba_pieter, znak_dachu, znak_pietra):
    dach(znak_dachu)
    for _ in range(liczba_pieter):
        pietro(znak_pietra)

# Przykłady użycia funkcji z różnymi znakami
print("\nDom 3-piętrowy:")
rysuj_dom(3, "^", "=")

print("\nDom 5-piętrowy:")
rysuj_dom(5, "*", "#")