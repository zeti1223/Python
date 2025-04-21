import math
import time

# Start measuring total time
start_time = time.time()

# Tároló az eredményeknek
results = []

# 10^1-től 10^8-ig
for power in range(1, 9):
    iterations = 10 ** power
    k = 1
    s = 0

    for i in range(iterations):
        if i % 2 == 0:
            s += 4 / k
        else:
            s -= 4 / k
        k += 2

    difference = math.pi - s
    results.append((iterations, s, difference))

# Kiírás tizedespontossággal
print("\nEredmények:\n")
for iterations, s, diff in results:
    print(f"Iterációk: {iterations:>10} | Közelítés: {s:.15f} | Eltérés: {diff:.15f}")

# Összes futási idő kiírása
end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nA teljes kód futási ideje: {elapsed_time:.2f} másodperc")