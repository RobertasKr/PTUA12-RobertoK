"""
Reikia parašyti funckiją, kuri turėtų du variable – vienas yra listas, kitas – iš kokio skaičiaus reikia kad dalintusi. Reikia grazinti visus skaicius kurie dalinasi is duoto skaiciaus.
"""

# def divide_list_numbers(list1: list, int1: int):
#     for number in list1:
#         if number % int1 != 0:
#             list.remove(number)
#     return list1
#
# print(divide_list_numbers([10, 20, 25, 30, 35, 45], 2))

"""
Parašyti funciją, į kurią padavus skaičių atspausdintų tokia tvarka kaip parodyta žemiau. Funkcija turi priimti 2 variable – nuo kurio iki kurio skaiciaus.: 
"""

# def number_printing(int1: int, int2: int):
#     numbers_list = []
#     for number in range(int1, int2):
#         i = 0
#         while i < number:
#             numbers_list.append(number)
#             i += 1
#     return numbers_list


# def number_printing(int1: int, int2: int):
#     i = 0
#     numbers_list = []
#     numbers_str = ""
#     for number in range(int1, int2):
#         i = 0
#         while i < number:
#             numbers_str += str(number)
#             i += 1
#         numbers_list.append(numbers_str)
#         numbers_str = ""
#     return numbers_list
#
# for x in number_printing(5, 7):
#     print(x)

"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order. 

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits. 
"""

# def int_separation(int1: int):
#     reversed_numbers = reversed(str(int1))
#     result = []
#     for i in reversed_numbers:
#         result.append(i)
#     return result
#
# print(" ".join(int_separation(6342)))

"""
Exercise 13: Print multiplication table from 1 to 10 
"""

def num_multiplication_table():
    for x in range(1, 11):
        result_list = []
        for i in range(1, 11):
            result_list.append(x * i)
        print(" ".join(str(a) for a in result_list))

print(num_multiplication_table())