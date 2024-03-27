"""
Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį. Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį. Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.
"""
print("------------------Task 1------------------")
list_names = ["Robertas", "Linas", "Paulius"]
list_passwords = ["12345", "54321", "67890"]

while True:
    name = str(input("Iveskite varda: "))
    password = str(input("Iveskite slaptazodi: "))
    if list_names.index(name) == list_passwords.index(password):
        print("Sveiki prisijunge!")
        break
    else:
        print("Neteisingi prisijungimo duomenys.")
