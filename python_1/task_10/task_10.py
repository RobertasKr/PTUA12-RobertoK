"""
Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.

Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.

Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.

Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį ir iš teksto ištraukia visus el. pašto adresus.
"""
def sum_func(a: int):
    return a + a

def split_func(a: str):
    a.split()
    print(a)

def square_func(a: int):
    return a * a

def print_func(a: str):
    return print(a)

def welcome_func(a: str):
    print(f"Welcome, {a}!")

def task_2(list_words: list):
    new_list = []
    for x in list_words:
        new_list.append(x + "G")
    return print(new_list)

task_2(["vienas", "du", "trys", "keturi", "penki"])

def task_3(a: int, b: int):
    print(f"Suma: {a + b}, Atimtis: {a - b}, Dalyba: {a / b}, Daugyba: {a * b}.")

task_3(10, 5)

def task_4(list_words: list):
    for x in list_words:
        if not x.isalnum():
            print(x)

words = ["linas", "Tomas123", "Haha!", "meoW#"]
task_4(words)

def extract_email_addresses(string_sentences: str):
    list_sentences = string_sentences.split()
    for x in list_sentences:
        if "@" in x:
            print(x)

string_text = "Now for manners use has company believe parlors. Least nor party who wrote while did. Excuse formed as is agreed admire so on result parish. Tomas@gmail.lt Put use set uncommonly announcing and travelling. Allowance robertas@gmail.lt sweetness direction to as necessary. Principle oh explained excellent do my suspected conveying in. Excellent you did therefore perfectly supposing described."

extract_email_addresses(string_text)