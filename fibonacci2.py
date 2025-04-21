def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Felhasználói bemenet bekérése
try:
    limit = int(input("Add meg a Fibonacci számok felső határát: "))
    if limit < 0:
        print("Kérlek adj meg egy nem negatív egész számot.")
    else:
        print(f"Fibonacci számok {limit} értékig:")
        for fib in fibonacci_generator(limit):
            print(fib)
except ValueError:
    print("Érvénytelen bevitel. Kérlek adj meg egy egész számot.")
