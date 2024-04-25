"""
Write a Python program to create a generator that generates the squares of numbers up to a given number.
"""
from random import randint
def get_squares(number: int):
    current = 1
    for i in range(number):
        yield current ** 2
        current += 1


for value in get_squares(5):
    print(value)

"""
Write a Python program to create a generator that yields "n" random numbers between a low and high number that are inputs.
"""

print("---------Task 2-----------")
def get_random_values(low: int, high: int, steps: int):
    # result = randint(low, high)
    for value in range(steps):
        yield randint(low, high)

for value in get_random_values(10, 20, 5):
    print(value)

"""
Write a Python program to create a generator that iterates over a string.
"""

print("---------Task 3-----------")

def generator_string(text: str):
    for value in text:
        yield value

text = "123456789"
for value in generator_string(text):
    print(value)

"""
Write a Python program to create a Fibonacci series generator.
"""

print("---------Task 4-----------")

def fibonacci_sequence(n: int):
    a = 0
    b = 1
    for i in range(n):
        yield b
        a, b = b, a + b

obj = fibonacci_sequence(10)

for i in obj:
    print(i)

"""
Write a Python program to create a generator from a list that yields item from the list if it is a number.
"""

print("---------Task 5-----------")

def get_number_from_list(list_data: list):
    for value in list_data:
        if type(value) == int:
            yield value

list_data = [1, "2", 3, [4], {5}, (6), 7]
obj = get_number_from_list(list_data)

for i in obj:
    print(i)

"""
Create a list of tuples, each representing a person's information. Each tuple contains the following information: (name: str, age: int, city: str, salary: float). Your task is to create Python generators to perform the following tasks:

Filtering Generator: Create a generator function that filters the people who are below a certain age threshold.
Mapping Generator: Create a generator function that maps the names of people to uppercase.
Aggregation Generator: Create a generator function that calculates the average salary of the selected group.
"""
print("---------Task 6-----------")

list_of_tuples = [
    ("Linas", 20, "Kaunas", 690.69),
    ("Tomas", 15, "Vilnius", 666.66),
    ("Paulius", 32, "Marijampole", 777.77),
    ("Petras", 32, "Vilnius", 123.21),
    ("Jonas", 20, "Kaunas", 800.85),
    ("Julius", 12, "Marijampole", 420.69),
]

def get_age_filtering_generator(list_data: list):
    for value in list_data:
        if value[1] > 18:
            yield value

def get_uppercase_names_generator(list_data: list):
    for value in list_data:
        yield value[0].upper(), *value[1:]

def get_average_salary_from_group_generator(list_data: list, check_variable: str):
    result = 0
    count = 0
    for value in list_data:
        if value[2] == check_variable:
            result += value[3]
            count += 1
    yield result / count



obj = get_age_filtering_generator(list_of_tuples)
for i in obj:
    print(i)
obj = get_uppercase_names_generator(list_of_tuples)
for i in obj:
    print(i)
obj = get_average_salary_from_group_generator(list_of_tuples, "Kaunas")
for i in obj:
    print(i)