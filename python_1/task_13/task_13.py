"""
Sukurkite paprastą skaičiavimo programą kaip skriptą ir kaip modulį.

Sukurkite programą su 3 skirtingais moduliais:

Pirma, atlikti pagrindines užduotis su string

antra, pagrindinius uždavinius su list.

trečias, pagrindiniai uždaviniai su float/ int

Importuokite juos kaip modulius į main.py modulį ir parodykite skaičiavimus.

Sukurkite modulį ir importuokite bet kurį pasirinktą PIP paketą. Tada sukurkite funkciją, kuri jį naudotų. Importuokite tą funkciją į main.py modulį ir ją naudokite.

"Python" modulis os suteikia galimybę naudotis nuo operacinės sistemos priklausančiomis funkcijomis, pvz., skaityti arba rašyti į failų sistemą. Jūsų užduotis yra:

Importuoti os modulį.

Sukurti funkciją, kuri išvardytų visus dabartiniame kataloge esančius failus.

Sukurti funkciją, kuri sukuria naują katalogą.

Sukurti funkciją, kuri pervadina failą.

Sukurkite funkciją, kuri perkelia failą iš vieno katalogo į kitą.

Sukurkite funkciją, kuri ištrina failą.
"""

from module_functions import (
    string_actions,
    int_actions,
    list_actions,
    get_joke,
    name_all_files,
)
from module_functions import create_new_catalog, rename_file, move_file, remove_file


print(string_actions("Robertas"))
print(int_actions(66))
print(list_actions([6, 7, 8, 9, 10, "asd"]))

print(get_joke())
print(name_all_files())
# create_new_catalog()
# rename_file("C:/Users/Robertas/Desktop/new_catalog")
# move_file()
# remove_file()
