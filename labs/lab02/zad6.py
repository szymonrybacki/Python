def fibonacci_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]