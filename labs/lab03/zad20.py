def szyfruj_cezar(tekst, klucz):
    """
    Szyfruje tekst za pomocą szyfru Cezara.
    
    Args:
        tekst: tekst do zaszyfrowania
        klucz: liczba pozycji, o którą przesuwamy litery
    
    Returns:
        Zaszyfrowany tekst
    """
    wynik = ""
    
    for znak in tekst:
        if znak.isalpha():  # Sprawdzamy czy znak jest literą
            # Określamy kod ASCII i zakres (małe czy wielkie litery)
            if znak.isupper():
                # Wielkie litery (ASCII 65-90)
                przesuniecie = (ord(znak) - ord('A') + klucz) % 26
                wynik += chr(ord('A') + przesuniecie)
            else:
                # Małe litery (ASCII 97-122)
                przesuniecie = (ord(znak) - ord('a') + klucz) % 26
                wynik += chr(ord('a') + przesuniecie)
        else:
            # Znaki niebędące literami pozostają bez zmian
            wynik += znak
            
    return wynik

def deszyfruj_cezar(tekst, klucz):
    """
    Deszyfruje tekst zaszyfrowany szyfrem Cezara.
    
    Args:
        tekst: zaszyfrowany tekst
        klucz: liczba pozycji użyta do szyfrowania
    
    Returns:
        Odszyfrowany tekst
    """
    return szyfruj_cezar(tekst, -klucz)

# Testy
tekst_jawny = "Hello, World!"
klucz = 3

tekst_zaszyfrowany = szyfruj_cezar(tekst_jawny, klucz)
print(f"Tekst jawny: {tekst_jawny}")
print(f"Zaszyfrowany: {tekst_zaszyfrowany}")
print(f"Odszyfrowany: {deszyfruj_cezar(tekst_zaszyfrowany, klucz)}")

tekst_jawny2 = "Python Programming"
klucz2 = 13
tekst_zaszyfrowany2 = szyfruj_cezar(tekst_jawny2, klucz2)
print(f"\nTekst jawny: {tekst_jawny2}")
print(f"Zaszyfrowany: {tekst_zaszyfrowany2}")
print(f"Odszyfrowany: {deszyfruj_cezar(tekst_zaszyfrowany2, klucz2)}")