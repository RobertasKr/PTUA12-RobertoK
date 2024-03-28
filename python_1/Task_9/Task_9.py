"""
Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.

Raskite visus skaičius iš 1-1000, kuriuose yra 9.

Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių.

Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas.

Papildoma Destytojo uzduotis:
1. Lentynoje sudeti batai:
[8.90, 4,90, 13,20, 8,80, 14,00, 12,00]
a) Paskaičiuokite kiek eurų liks žmogui, jei jis šiuo metu pirks dvejus pigiausius batus;
b) kokius dvejus batus jam nupirkti, jei jis turi 20 eurų ir nori, kad jam liktų kuo mažiau eurų;
"""
import math
def task_1():
    numbers = [number for number in range(1000) if number % 6 == 0]
    print(numbers)

def task_2():
    numbers = [number for number in range(1000) if "9" in str(number)]
    print(numbers)

def task_3():
    string_words = "Sveiki tai yra pasaka apie visiskai nieka ir visada visi galvos kad tai yra kazkas taciau tai yra vienaragis"
    splitted_words = string_words.split()
    result = [word for word in splitted_words if "e" in word]
    print(len(result))

def task_4():
    string_words = "Sveiki tai yra pasaka apie visiskai nieka ir visada visi galvos kad tai yra kazkas taciau tai yra vienaragis"
    splitted_words = string_words.split()
    result = [word for word in splitted_words if len(word) > 5]
    print(len(result))

def task_5(x):
    square_root = math.isqrt(x)
    print(True) if square_root * square_root == x else print(False)


def task_bonus_a():
    prices = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]
    result = [number for number in sorted(prices)[:2]]
    return round(20 - sum(result), 2) # Nesuprantu, kodel be round funkcijos skaiciai issidarko po kablelio...

def task_bonus_b():
    prices = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]
    cash_left = []
    result = [print(x + y) for x in prices for y in prices]
    print(result)

task_1()
task_2()
task_3()
task_4()
task_5(8)
print(task_bonus_a())
task_bonus_b()