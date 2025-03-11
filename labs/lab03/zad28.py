class User:
    def __init__(self):
        # Słownik do przechowywania danych użytkowników (username -> password)
        self.users = {}
    
    def register(self, username, password):
        # Sprawdź czy użytkownik już istnieje
        if username in self.users:
            print(f"Użytkownik {username} już istnieje")
            return False
        
        # Sprawdzenie minimalnych wymagań dla hasła
        if len(password) < 6:
            print("Hasło musi mieć co najmniej 6 znaków")
            return False
        
        # Zapisz użytkownika
        self.users[username] = password
        print(f"Użytkownik {username} został zarejestrowany")
        return True
    
    def login(self, username, password):
        # Sprawdź czy użytkownik istnieje
        if username not in self.users:
            print(f"Użytkownik {username} nie istnieje")
            return False
        
        # Sprawdź poprawność hasła
        if self.users[username] != password:
            print("Niepoprawne hasło")
            return False
        
        print(f"Zalogowano jako {username}")
        return True

# Test klasy
if __name__ == "__main__":
    user_system = User()
    
    # Rejestracja użytkowników
    user_system.register("jan123", "haslo123")
    user_system.register("anna456", "qwerty")
    user_system.register("jan123", "inne_haslo")  # Próba ponownej rejestracji
    
    # Próby logowania
    user_system.login("jan123", "haslo123")  # Powinno się powieść
    user_system.login("jan123", "złe_hasło")  # Powinno się nie powieść
    user_system.login("nieznany", "haslo123")  # Powinno się nie powieść