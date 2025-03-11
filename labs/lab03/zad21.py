import random

def gra_kamien_papier_nozyce():
    opcje = ["kamien", "papier", "nozyce"]
    wyniki = {"wygrane": 0, "przegrane": 0, "remisy": 0}
    
    print("=== GRA W KAMIEŃ, PAPIER, NOŻYCE ===")
    print("Zasady: kamień > nożyce, nożyce > papier, papier > kamień")
    
    while True:
        # Wybór komputera
        wybor_komputera = random.choice(opcje)
        
        # Wybór użytkownika
        print("\nWybierz swój ruch:")
        for i, opcja in enumerate(opcje, 1):
            print(f"{i}. {opcja.capitalize()}")
        
        try:
            wybor = int(input("Twój wybór (1-3): "))
            if wybor < 1 or wybor > 3:
                print("Nieprawidłowy wybór. Wybierz liczbę od 1 do 3.")
                continue
            wybor_uzytkownika = opcje[wybor - 1]
        except ValueError:
            print("Nieprawidłowe dane. Wprowadź liczbę.")
            continue
            
        print(f"\nTwój wybór: {wybor_uzytkownika.capitalize()}")
        print(f"Wybór komputera: {wybor_komputera.capitalize()}")
        
        # Ustalenie wyniku
        if wybor_uzytkownika == wybor_komputera:
            print("REMIS!")
            wyniki["remisy"] += 1
        elif (wybor_uzytkownika == "kamien" and wybor_komputera == "nozyce") or \
             (wybor_uzytkownika == "nozyce" and wybor_komputera == "papier") or \
             (wybor_uzytkownika == "papier" and wybor_komputera == "kamien"):
            print("WYGRAŁEŚ!")
            wyniki["wygrane"] += 1
        else:
            print("PRZEGRAŁEŚ!")
            wyniki["przegrane"] += 1
            
        # Wyświetlenie aktualnych wyników
        print(f"\nWyniki: Wygrane: {wyniki['wygrane']}, Przegrane: {wyniki['przegrane']}, Remisy: {wyniki['remisy']}")
        
        # Pytanie o kontynuację gry
        kontynuuj = input("\nCzy chcesz zagrać jeszcze raz? (t/n): ")
        if kontynuuj.lower() != 't' and kontynuuj.lower() != 'tak':
            break
            
    print("\nDziękujemy za grę!")
    print(f"Końcowe wyniki: Wygrane: {wyniki['wygrane']}, Przegrane: {wyniki['przegrane']}, Remisy: {wyniki['remisy']}")
    
# Uruchomienie gry
if __name__ == "__main__":
    gra_kamien_papier_nozyce()