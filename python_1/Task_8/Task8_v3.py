"""
Yra stringas; ‚1asdg16asdg1wg16ewrg1er6gw1‘. Suskaiciuoti ir grazinti dicte kiek yra skaiciu ir kiek yra raidziu.
"""

string_random = "1asdg16asdg1wg16ewrg1er6gw1"
dict_result = {
    "Skaiciai": 0,
    "Raides": 0,
}

for x in string_random:
    if x.isalpha():
        dict_result["Raides"] += 1
    if x.isdigit():
        dict_result["Skaiciai"] += 1

print(dict_result)
