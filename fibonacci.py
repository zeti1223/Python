def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Felhasználói bemenet bekérése
try:
    count = int(input("Add meg, hány Fibonacci számot szeretnél: "))
    if count <= 0:
        print("Kérlek adj meg egy pozitív egész számot.")
    else:
        print(f"Az első {count} Fibonacci szám:")
        for fib in fibonacci_generator(count):
            print(fib)
except ValueError:
    print("Érvénytelen bevitel. Kérlek adj meg egy egész számot.")
