"""
Sukurkite bent 5 skirtingas funkcijas ir pabandykite apdoroti bent 5 integruotas "Python" išimtis.

Python kalboje, dalijant iš nulio, gauname ZeroDivisionError. Jūsų užduotis - sukurti funkciją, kuri:

    Kaip argumentus priima du skaičius.

    Mėgina padalyti pirmąjį skaičių iš antrojo.

    Jei antrasis skaičius yra nulis, ji turėtų sugauti ZeroDivisionError ir grąžinti pasirinktinį klaidos pranešimą.

    Jei dalijimas sėkmingas, turėtų būti grąžinamas rezultatas.

    Nepriklausomai nuo to, ar dalijimas pavyko, ar ne, turėtų būti išspausdintas pranešimas "Attempted division". Jei įvesties duomenys nėra skaičiai, pateikiamas TypeError pranešimas. Funkcija pagauna šią TypeError ir grąžina pasirinktinį klaidos pranešimą.

Sukurkite mini "Python" programą, kuri įvestų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą. Tvarkykite visas galimas klaidas.

Atnaujinkite ankstesnę užduotį su galimomis raise išimtimis.
"""


def multiply_func_task_1(a: int):
    try:
        return a * a
    except TypeError:
        print("Ivestas ne sk")
        raise TypeError("Ivestas ne skaicius")


# print(sum_func_task_1("253"))
def split_func_task_1(a: str):
    try:
        a.split()
        print(a)
    except AttributeError:
        raise AttributeError("Ivestas ne string")


# print(split_func_task_1("asdfafafs"))


def divide_numbers(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Dalyba is 0 negalima!!!")
    except TypeError:
        raise TypeError("Ivestas ne skaicius!!! TYPEERROR")
    except ValueError:
        raise ValueError("Ivestas ne skaicius!!! VALUEERROR")
    finally:
        print("Attempted division")


# print(divide_numbers(10, 5))


def task_3(a: int, b: int):
    try:
        print(f"Suma: {a + b}, Atimtis: {a - b}, Dalyba: {a / b}, Daugyba: {a * b}.")
    except TypeError:
        raise TypeError("Ivestas ne skaicius!!!")
    except ZeroDivisionError:
        raise ZeroDivisionError("Dalyba is 0 negalima!!!")
    # return a, b


# try:
#     task_3(4, asfgr)
# except NameError:
#     raise NameError("Kazkas negerai")
