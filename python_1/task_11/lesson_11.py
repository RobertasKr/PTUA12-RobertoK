"""
1. Yra sugeneruojami random pagalba 4 skaiciai (nuo 0000 iki 9999).
2. Tada paprasoma konsoleje suvesti kiek bandymų spėti turime. (Tarkim vartotojas suves 3 kartus)
3. Vartotojo prasoma meginsti atspeti skaiciu (pvz vartotojas speja 0123).
4. Sistema skaiciuoja kiek skaiciu yra karvių, ir kiek yra bulių. Karve yra toks skaicius, kuris yra teisingas, bet stovi ne savo vietoje, bulius – ir teisingas, ir teisingoje vietoje. Jei visi buliai – zaidimo pabaiga.
5. Jei skaicius neatspetas per nustatyta bandymu skaiciu – zaidimas pralostas.

Pvz kompiuris sugeneruoja 0839.
Vartotojas speja 3 kartus:
0914 -> 1 bulius,1 karve,
0849 -> 3 buliai, 1 karve,
0839 -> 4 buliai, game over.

Pagalvokite kokios turetu buti funckijos, nes cia galima ju sudelioti ne viena. ir rasykite funkcijas.
# """
from random import randint
#
# # def checking_number(rand_num: str, number_guess: str):
# #     karves = 0
# #     for number in rand_num:
# #         if number_guess.find(number) != -1:
# #             print(number)
# #
# number = random.randint(0, 10000)
# result_number = str(number).zfill(4)
# print(result_number)
# #checking_number(result_number, str(input("Ivesk skaiciu: ")))
#
# games = 10
# while games < 10:
#     type_str = str(input("Ivesk skaiciu: "))
#     x += 1
#

# print(result)
#
# for number in result:
#     buliai, karves = 0, 0
#     int_guess = str(input("Ivesk skaiciu: "))
#     if number in result:
#         print(number)

def generate_numbers():
    return ''.join([str(randint(0,9)) for _ in range(4)])

#print(generate_numbers())


def check_cows_bulls(generated_number, player_prediction):
    cows, bulls = 0, 0

    for index, value in enumerate(player_prediction):
        if value == generated_number[index]:
            bulls +=1
        elif value in generated_number:
            cows += 1

    return cows, bulls

def main():
    generated_number = generate_numbers()
    try_number = int(input("kiek kartu spesi: "))
    print(generated_number)

    for i in range(try_number):
        player_prediction = input("Pamegink atspeti: ")
        cows, bulls = check_cows_bulls(generated_number, player_prediction)
        if bulls == 4:
            return "You are the winner"
        else:
            print(f"You have {bulls} bulls and {cows} cows")
    return "Game Over"
print(main())