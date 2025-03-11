def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Testy
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(3))  # 2
print(fibonacci(4))  # 3
print(fibonacci(5))  # 5
print(fibonacci(10))  # 55