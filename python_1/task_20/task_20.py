"""
Write a Python program to find if a given string starts with a given character using Lambda. Output:True or False
"""

text = "vienas du trys keturi"

result = lambda x: str(x).startswith("a")
print(result(text))

"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
"""

result = lambda x: x + 15
print(result(10))

result = lambda x, y: x * y
print(result(5, 4))

"""
Write a Python program to square and cube every number in a given list of integers using Lambda.
"""

data = [1, 2, 3]

result = lambda x: (x*2, x**2)
for i in data:
    print(result(i))

"""
Write a Python program to extract year, month, date and time using Lambda. Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""
from datetime import datetime
result = lambda x: (str(x), x.year, x.month, x.day, x.strftime("%X"))
print(result(datetime.now()))

"""
Write a Python program to sort a list of tuples using Lambda.
"""

list_of_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sorted(list_of_tuples, key=lambda x: x[1]))

"""
Write a Python program to sort a list of dictionaries buy color value using Lambda.
"""

list_of_dicts = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color':'Blue'}
]
print(sorted(list_of_dicts, key=lambda x: x["color"]))

"""
Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
"""

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(sorted(matrix2, key=lambda x: sum(x)))

"""
Write a Python program to triple all numbers of a given list of integers. Use Python map().
"""

def get_triple_numbers(x):
    return x * 3

data = [1, 2, 3]
print(list(map(get_triple_numbers, data)))

"""
Write a Python program to square the elements of a list using map() function.
"""

def get_square_numbers(x):
    return x ** 2

data = [1, 2, 3]
print(list(map(get_square_numbers, data)))

"""
Write a Python program to add three given lists using Python map and lambda
"""
print("------------TASK maps 3 ---------------")

def get_sum_lists(*args):
    return sum(sum(numbers) for numbers in args)
data_list_1 = [1, 2, 3]
data_list_2 = [4, 5, 6]
data_list_3 = [7, 8, 9]

print(get_sum_lists(data_list_1, data_list_2, data_list_3))

"""
Write a Python program to add two given lists and find the difference between lists. Use map() function.
"""
print("------------TASK maps 4 ---------------")

def get_differences(list_1: list, list_2: list):
    result = []
    result.append(set([x for x in list_1 if x not in list_2]))
    result.append(set([x for x in list_2 if x not in list_1]))
    return result


data_list_1 = [0, 1, 2, 3, 1]
data_list_2 = [2, 3, 4, 5]

print(get_differences(data_list_1, data_list_2))

"""
Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
"""
print("------------TASK maps 5 ---------------")
def get_convertion(list_1: list, tuple_1: tuple):
    temp_list = list_1 + list(tuple_1)
    result = []
    for x in temp_list:
        result.append(f"{x}")
    return result

data_list_1 = [0, 1, 2, 3]
data_list_2 = (2, 3, 4, 5)

print(get_convertion(data_list_1, data_list_2))

"""
Write a Python program to filter a list of integers using Lambda

Original list of integers:  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

Even numbers from the said list:  
[2, 4, 6, 8, 10]  

Odd numbers from the said list:  
[1, 3, 5, 7, 9]
"""
print("------------TASK maps 6 ---------------")
def get_even_and_odd_lists(data: list):
    list_odd = []
    list_even = []
    for x in data:
        if x % 2 == 0:
            list_even.append(x)
        else:
            list_odd.append(x)
    return list_odd, list_even

data_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(get_even_and_odd_lists(data_list_1))

"""
Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]

"""
print("------------TASK maps 7 ---------------")
def get_divisible_numbers(data: list):
    return [i for i in data if i % 19 == 0 or i % 13 == 0]

data_list_1 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(get_divisible_numbers(data_list_1))

"""
Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
Original arrays: 
[1, 2, 3, 5, 7, 8, 9, 10] 

Number of even numbers in the above array: 3  
Number of odd numbers in the above array: 5  
"""
print("------------TASK maps 8 ---------------")
def get_even_and_odd_count(data: list):
    list_odd = []
    list_even = []
    for x in data:
        if x % 2 == 0:
            list_even.append(x)
        else:
            list_odd.append(x)
    return len(list_even), len(list_odd)

data_list_1 = [1, 2, 3, 5, 7, 8, 9, 10]

print(get_even_and_odd_count(data_list_1))

"""
Write a python program that multiplies all the values in a given list of integers.
"""
print("------------TASK maps 9 ---------------")
from functools import reduce
def get_multiplies(x, y):
    return x * y

print(reduce(get_multiplies, [1, 2, 3, 4]))

"""
Write a python program that finds the maximum value within the given list.
"""
print("------------TASK maps 10 ---------------")
def get_maximum_value(x, y):
    return x if x > y else y

print(reduce(get_maximum_value, [1, 2, 100, 3, 77, 4, 5, 6, 55, 99]))

"""
Write a python function that given list of strings concatenates all of them together.
"""
print("------------TASK maps 11 ---------------")
def get_list_of_strings(x, y):
    return x + y

print(reduce(get_list_of_strings, ["vienas", "du", "trys", "keturi"]))

def difrence_between_lists(first: list, second: list) -> list:

    return [
        number
        for number in set(first + second)
        if not (number in first and number in second)
    ]

data_list_1 = [0, 1, 2, 3, 1]
data_list_2 = [2, 3, 4, 5]

print(difrence_between_lists(data_list_1, data_list_2))