"""
Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.
"""
i = 1
ats = 0
while True:
    number = int(input(f"Iveskite sveika skaiciu ({i}/10): "))
    ats += number
    i += 1
    if i == 11:
        print(f"Skaiciu suma: {ats}"
              f"\nSkaiciu vidurkis: {int(ats / 10)}")
        break