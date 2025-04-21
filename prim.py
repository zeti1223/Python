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

def prime_generator(limit):
    """Generálja a prím számokat a megadott határig"""
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Felhasználói bemenet bekérése
try:
    limit = int(input("Add meg a prím számok felső határát: "))
    if limit < 2:
        print("Kérlek adj meg egy 2-nél nagyobb számot.")
    else:
        print(f"Prím számok {limit} értékig:")
        for prime in prime_generator(limit):
            print(prime)
except ValueError:
    print("Érvénytelen bevitel. Kérlek adj meg egy egész számot.")
