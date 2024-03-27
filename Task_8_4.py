"""
Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys. Reikšmę galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas, kol rasite tą, kurią įvedėte.
"""
# pin = "0064"
# i = 10000
#
# while i < 100000:
#     ats = str(i)
#     if ats[1:] == pin:
#         print(f"Nulauzete koda!"
#               f"\nKodas yra: {ats[1:]}")
#         break
#     i += 1

pin = "0064"
for i in range(10000, 100000):
    ats = str(i)
    if ats[1:] == pin:
        print(f"Nulauzete koda!"
              f"\nKodas yra: {ats[1:]}")
        break
