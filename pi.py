# Initialize denominator
k = 1

# Initialize sum
s = 0

iterations = 1000000  # Rename variable to avoid conflict with built-in range()

for i in range(iterations):
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k  # Fix spacing issue
    else:
        # odd index elements are negative
        s -= 4/k

    # denominator is odd
    k += 2

print(s)