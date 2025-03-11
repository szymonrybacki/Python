def silnia(n):
    return 1 if n == 0 else n * silnia(n - 1)

# Testy
print(silnia(0))  # 1
print(silnia(1))  # 1
print(silnia(2))  # 2
print(silnia(3))  # 6
print(silnia(4))  # 24
print(silnia(5))  # 120
