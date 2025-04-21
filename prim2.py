def is_prime(num):
    """Ellenőrzi, hogy egy szám prím-e"""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    """Generálja az első n prím számot"""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Felhasználói bemenet bekérése
try:
    count = int(input("Add meg, hány prím számot szeretnél: "))
    if count <= 0:
        print("Kérlek adj meg egy pozitív egész számot.")
    else:
        print(f"Az első {count} prím szám:")
        for prime in prime_generator(count):
            print(prime)
except ValueError:
    print("Érvénytelen bevitel. Kérlek adj meg egy egész számot.")
