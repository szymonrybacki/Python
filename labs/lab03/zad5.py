def szukajWLiscie(lista, a):
    count = 0
    for i in lista:
        if i == a:
            count += 1
    return count

print(szukajWLiscie([1, 2, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6], 1))  # 3