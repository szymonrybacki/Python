def szukajWLiscie(lista, a):
    # Ustalenie wartości do wyszukiwania na podstawie typu a
    if isinstance(a, (int, float)):
        search_value = a
    elif isinstance(a, str):
        try:
            # Dla stringów reprezentujących liczby - szukamy tej liczby
            search_value = int(a)
        except ValueError:
            try:
                search_value = float(a)
            except ValueError:
                # Dla innych stringów - suma kodów ASCII
                search_value = sum(ord(char) for char in a)
    elif isinstance(a, bool):
        # Dla wartości logicznych - szukamy 0 (False) lub 1 (True)
        search_value = 1 if a else 0
    else:
        # Dla innych typów - błąd
        raise TypeError("Nieobsługiwany typ danych")
    
    # Wyszukiwanie w liście
    count = 0
    for i in lista:
        if i == search_value:
            count += 1
            
    return count

print(szukajWLiscie([1, 2, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6], 1))  # 3