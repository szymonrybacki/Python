def sortowanie(lista, kierunek) -> list:
    if kierunek == "0":
        lista.sort(reverse=True)
    elif kierunek == "1":
        lista.sort()
    else:
        return "Niepoprawny kierunek sortowania"
    return lista


kierunek = input("Jeśli chcesz sortować malejąco wybierz 0, jeśli rosnąco wybierz 1: ")
lista = [1, 2, 1, 8, 2, 2, 3, 3, 4, 5, 6, 6]

print(sortowanie(lista, kierunek))