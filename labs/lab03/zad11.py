def fajnaFunkcja(lista: list[int]) -> tuple[int, int, int, int, int]:
    lista.sort()
    suma = sum(lista)
    srednia = suma / len(lista)
    mediana = lista[len(lista)//2] if len(lista) % 2 == 1 else (lista[len(lista)//2] + lista[len(lista)//2 - 1]) / 2
    return mediana, srednia, lista[0], lista[-1], (sum([(x - srednia)**2 for x in lista]) / len(lista))**0.5

print(fajnaFunkcja([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # (5.5, 5.5, 1, 10, 2.8722813232690143)