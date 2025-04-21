def decimal_to_binary(decimal_num):
    binary_str = format(int(decimal_num), 'b')
    return binary_str

# Szám bekérése a felhasználótól
decimal_num = int(input("Kérem, adjon meg egy decimális számot: "))

# Decimális szám átalakítása bináris számmá és kiíratása
binary_representation = decimal_to_binary(decimal_num)
print(f"A(z) {decimal_num} decimális szám bináris alakja: {binary_representation}")
