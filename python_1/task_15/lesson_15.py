"""
Exercise 1:	Write a Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
"""


def find_common_elements(words: str):
    list_result = []
    for i in set(words):
        list_result.append((i, words.count(i)))
    list_result.sort(key=lambda x: x[1], reverse=True)
    return list_result[:3]


print(find_common_elements("lkseropewdssafsdfafkpwe"))

"""
Exercise 2: Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""

# def slice_two_lists(l1: list, l2: list):
#     list_result = []
#     for i in range(1, len(l1), 2):
#         list_result.append(l1[i])
#     for i in range(0, len(l2), 2):
#         list_result.append(l2[i])
#     return list_result


def slice_two_lists(l1: list, l2: list):
    return l1[1::2] + l2[0::2]


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print(slice_two_lists(l1, l2))

"""
Exercise 3: Create a Python set such that it shows the element from both lists in a pair
Given:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:

Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)
"""

# def join_two_lists(l1: list, l2:list):
#     result = []
#     for i in range(0, len(l1)):
#         result.append((i, l2[i]))
#     return set(result)


def join_two_lists(l1: list, l2: list):
    return set(zip(l1, l2))


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print(join_two_lists(first_list, second_list))

"""
Exercise 4: Iterate a given list and check if a given element exists as a keyâ€™s value in a dictionary. If not, delete it from the list
Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:

After removing unwanted elements from list [47, 69, 76, 97]
"""

# def check_dictionary_key(l1: list, d1: dict):
#     list_result = []
#     for value in d1.values():
#         if value in l1:
#             list_result.append(value)
#     return list_result


def check_dictionary_key(l1: list, d1: dict):
    return [value for value in d1.values() if value in l1]


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

print("ATS(one liner): ", check_dictionary_key(roll_number, sample_dict))

"""
Exercise 5: Get all values from the dictionary and add them to a list but don’t add duplicates
Given:
 
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
Expected Outcome:
 
[47, 52, 44, 53, 54]
"""


def change_dict_to_list(d1: dict):
    list_result = []
    for value in d1.values():
        if value not in list_result:
            list_result.append(value)
    return list_result


speed = {
    "jan": 47,
    "feb": 52,
    "march": 47,
    "April": 44,
    "May": 52,
    "June": 53,
    "july": 54,
    "Aug": 44,
    "Sept": 54,
}

print(change_dict_to_list(speed))
