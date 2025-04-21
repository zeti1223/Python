import math
import time

# Start measuring time
start_time = time.time()

# Initialize denominator
k = 1

# Initialize sum
s = 0

iterations = 10**6  # 1 000 000 ciklus

for i in range(iterations):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2

# Print results in normal float format with many decimals
print(f"{s:.15f}")
print(f"{(math.pi - s):.15f}")

# Calculate and print elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"A kód futási ideje: {elapsed_time:.2f} másodperc")