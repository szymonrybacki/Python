class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            print("Zniżka musi być w zakresie 0-100%")
            return False
        
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
        return True
    
    def display(self):
        return f"{self.name}: {self.price:.2f} zł"

# Test klasy
if __name__ == "__main__":
    product1 = Product("Laptop", 3500)
    product2 = Product("Telefon", 1200)
    
    print(product1.display())
    
    product1.apply_discount(15)  # 15% zniżki na laptop
    print(f"Po zniżce: {product1.display()}")
    
    product2.apply_discount(10)  # 10% zniżki na telefon
    print(f"Telefon po zniżce: {product2.display()}")