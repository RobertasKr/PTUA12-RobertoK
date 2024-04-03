"""
Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento prideda antrojo listpirmąjį elementą, antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro tą patį skaičių. Priešingu atveju grąžinama False. Pavyzdys:
"""

def puzzle_pieces(list_numbers_1: list, list_numbers_2: list):
    list_result = []
    print(list_numbers_2, list_numbers_1)
    x = 0
    if len(list_numbers_1) == len(list_numbers_2):
        while x < len(list_numbers_1):
            list_result.append(list_numbers_1[x] + list_numbers_2[x])
            x += 1
        return print(list_result[0] == sum(list_result) / len(list_result))
    return print(False)


puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1])
puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6])
puzzle_pieces([1, 2], [-1, -1])
puzzle_pieces([9, 8, 7], [7, 8, 9, 10])

"""
Tarp lyginių ir nelyginių skaičių vyksta didelis karas. Šiame kare jau žuvo daug skaičių, todėl tavo užduotis - jį nutraukti. Jūs turite nustatyti, kurios grupės sumos didesnės: lyginių ar nelyginių. Laimi didesnė grupė.

Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą, atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas, tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.
"""

def war_of_numbers(list: list):
    even_numbers = []
    odd_numbers = []
    for number in list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    if sum(even_numbers) > sum(odd_numbers):
        result = sum(even_numbers) - sum(odd_numbers)
    elif sum(even_numbers) < sum(odd_numbers):
        result = sum(odd_numbers) - sum(even_numbers)
    else:
        result = "Karas pasibaige lygiosiomis"
    return print(result)

war_of_numbers([2, 8, 7, 5])
war_of_numbers([12, 90, 75])
war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243])

"""
Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją, kuri grąžintų True, jei iš šio masyvo galima rasti kiekvieną bigramą bent vieną kartą žodžių masyve.
"""

def can_find(bigrams: list, words: list):
    words_sentence = " ".join(words)
    for bigram in bigrams:
        if bigram not in words_sentence:
            return print(False)
    return print(True)



can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"])
can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"])
# # "cu" nėra nė viename iš žodžių.
can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"])
can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks", "cooks"])

"""
Sukurkite funkciją, kuri priima eilučių sąrašą ir grąžina naują sąrašą, kuriame yra tik tos eilutės, kurios prasideda balsiu. Naudokite lambda funkcijas, kad įgyvendintumėte logiką, tikrinančią, ar eilutė prasideda balsiu.
"""

def printing_sentences(list_sentences: list, vowels: str):
    lines_starts_with_vowels = []
    # for line in list_sentences:
    #     if str(line).startswith(vowels):
    pass

vowels = "AaEeIiOoUu"
"""
multiplication= lambda x,y : x * y
print(multiplication(2,3))
>>> 6
"""