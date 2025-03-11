def konwersja_temperatury(temperatura, z_skali, do_skali):
    """
    Konwertuje temperaturę między skalami: Celsjusza (C), Fahrenheita (F) i Kelvina (K)
    
    Args:
        temperatura: wartość temperatury do konwersji
        z_skali: skala źródłowa ('C', 'F' lub 'K')
        do_skali: skala docelowa ('C', 'F' lub 'K')
    
    Returns:
        Wartość temperatury w skali docelowej
    """
    # Najpierw konwertujemy do Celsjusza jako skali pośredniej
    if z_skali == 'C':
        temp_c = temperatura
    elif z_skali == 'F':
        temp_c = (temperatura - 32) * 5/9
    elif z_skali == 'K':
        temp_c = temperatura - 273.15
    else:
        raise ValueError("Nieznana skala źródłowa")
    
    # Następnie konwertujemy z Celsjusza do skali docelowej
    if do_skali == 'C':
        return temp_c
    elif do_skali == 'F':
        return temp_c * 9/5 + 32
    elif do_skali == 'K':
        return temp_c + 273.15
    else:
        raise ValueError("Nieznana skala docelowa")

# Testy
print(f"0°C = {konwersja_temperatury(0, 'C', 'F'):.2f}°F")  # 32.00°F
print(f"100°C = {konwersja_temperatury(100, 'C', 'F'):.2f}°F")  # 212.00°F
print(f"98.6°F = {konwersja_temperatury(98.6, 'F', 'C'):.2f}°C")  # 37.00°C
print(f"0°C = {konwersja_temperatury(0, 'C', 'K'):.2f}K")  # 273.15K
print(f"0K = {konwersja_temperatury(0, 'K', 'C'):.2f}°C")  # -273.15°C