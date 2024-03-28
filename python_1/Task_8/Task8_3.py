"""
Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10. Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100.
"""
import random

dict_numbers = {}
i = 1
while i < 11:
    dict_numbers[i] = random.randint(1, 100)
    i += 1

print(dict_numbers)