"""
Ciklai
"""
import time

i = 10

while i < 15:
    # print(i)
    i += 1
    # time.sleep(0.1)
    if i == 15:
        break
else:
    print("Spausdinti else")

for i in range(10):
    if i == 8:
        break
    if i == 5:
        continue
    print(i)

# iterable - visi listai, tuple, dict, string, 