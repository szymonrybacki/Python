class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Kwota wpłaty musi być większa od zera!")
            return False
        self.balance += amount
        print(f"Wpłacono {amount}. Nowy stan konta: {self.balance}")
        return True
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Kwota wypłaty musi być większa od zera!")
            return False
        if amount > self.balance:
            print(f"Niewystarczające środki! Dostępne: {self.balance}")
            return False
        self.balance -= amount
        print(f"Wypłacono {amount}. Nowy stan konta: {self.balance}")
        return True

# Test klasy
if __name__ == "__main__":
    konto = BankAccount(100)
    print(f"Początkowy stan konta: {konto.balance}")
    
    konto.deposit(50)
    konto.withdraw(30)
    konto.withdraw(200)  # Próba wypłaty większej kwoty niż dostępna
    konto.deposit(-10)   # Próba wpłaty ujemnej kwoty