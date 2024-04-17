"""
7. Sukurti funkcija, kuri priimtu tris variable – dicta, reikalingus key (list), istrinamus key (listas).
Funkcija turi grazinti du variable – dicta su istrintais key ir dicta,turinti tik reikalingus key.
Pvz. jei duota:
Data = {
1: ‘vienas’,
2: ‘du’,
3: ‘trys’,
4: ‘keturi’
}
Reikaling = [1, 2]
Trinti = [3]
Grazina du dictus:
{
1: ‘vienas’,
2: ‘du’,
4: ‘keturi’
}
Ir:
{
1: ‘vienas’,
2: ‘du’,
}
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def dictionary_rework(dict_main: dict, list_removed: list, list_needed: list):
    dict_removed, dict_needed = dict_main.copy(), {}
    for i in list_removed:
        dict_removed.pop(i)
    for ii in list_needed:
        dict_needed[ii] = dict_main[ii]
    return f"Dict needed: {dict_needed}\nDict removed: {dict_removed}"


data = {1: "vienas", 2: "du", 3: "trys", 4: "keturi"}

needed = [1, 2]
removed = [3]

print(dictionary_rework(data, removed, needed))

"""
8. Parasyti funckija, kuri priimtu du vairabe – lista kartotini. Grazinti turi lista, kuriame buvo listai su kartotiniu nariu skaiciumis. Pvz. 

Data = [1, 2, 3, 4, 5, 5, 7, 8, 9] 

Kartotinis = 3 

Grazina [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
"""


def list_rework(list_data: list, frequency: int):
    list_result, list_temp = [], []
    for i in list_data:
        list_temp.append(i)
        if len(list_temp) >= frequency:
            list_result.append(list_temp)
            list_temp = []
    if len(list_temp) > 0:
        list_result.append(list_temp)
    return list_result


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
freq_int = 5

print("FINAL: ", list_rework(data, freq_int))

"""
Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą:
"""

# def move_to_end(list_numbers: list, value: int):
#     value_count, list_result = [], []
#     for i in list_numbers:
#         if i == value:
#             value_count.append(i)
#         elif i != value:
#             list_result.append(i)
#     for ii in value_count:
#         list_result.append(ii)
#     return list_result
#
# print(move_to_end([1, 3, 2, 4, 4, 1], 1))


def move_to_end(list_numbers: list, value: int):
    value_count, list_result = [], []
    for i in list_numbers:
        if i == value:
            value_count.append(i)
        elif i != value:
            list_result.append(i)
    list_result = list_result + value_count
    return list_result


input_list = [1, 3, 2, 4, 4, 1]
input_value = 1

print(move_to_end(input_list, input_value))

logging.info(f"Ivesties duomenys: {input_list}, {input_value}")
logging.info(f"Rezultato duomenys: {move_to_end(input_list, input_value)}")

"""
Sukurkite apskaitos programą , kuri paimtų metines pajamas, išlaidas, PVM tarifą (visos reikšmės turi būti kintamos) ir apskaičiuotų pelną, sumokėtus mokesčius 4 skirtingomis valiutomis (USD, EU, JPY, CNY). Visi skaičiavimai ir rezultatai turėtų būti spausdinami ekrane. Visi duomenys ir galimos klaidos turi būti registruojami į failą.
"""


def count_profit(num_inc: int, num_exp: int, num_pvm: float):
    return num_inc - (num_inc * num_pvm) - num_exp


yearly_income = 126600
yearly_expenses = 10000
# pvm_value = 0.2
pvm_usd, pvm_eu, pvm_jpy, pvm_cny = 0.3, 0.21, 0.1, 0.2
print(
    f"Pelnas Europos valiuta: {count_profit(num_inc=yearly_income, num_exp=yearly_expenses, num_pvm=pvm_eu)} eur"
)
print(
    f"Pelnas Amerikos valiuta: {count_profit(num_inc=yearly_income, num_exp=yearly_expenses, num_pvm=pvm_usd)} dol"
)
print(
    f"Pelnas Japonijos valiuta: {count_profit(num_inc=yearly_income, num_exp=yearly_expenses, num_pvm=pvm_jpy)} jpy"
)
print(
    f"Pelnas Kinijos valiuta: {count_profit(num_inc=yearly_income, num_exp=yearly_expenses, num_pvm=pvm_cny)} cny"
)
