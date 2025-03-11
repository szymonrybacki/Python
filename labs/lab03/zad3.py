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

# Przykłady użycia funkcji z różnymi znakami
print("Dom z cegły:")
dach("#")
pietro("-")
pietro("-")

print("\nDom z gwiazdek:")
dach("*")
pietro("*")
pietro("*")