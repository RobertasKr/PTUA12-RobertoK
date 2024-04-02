"""
Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį. Programa taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.
"""
numbers = input().split()

sum_numbers = 0
for x in numbers:
    sum_numbers += int(x)
print(f"Vidurkis: {sum_numbers / len(numbers)}"
      f"\nListas: {numbers}")