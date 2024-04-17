# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)
#
# squares = [number * number for number in range(10)]
# print(squares)

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])

# squares = {key: value for key, value in enumerate(range(10, 20))}
# print(squares)
#
# result = {}
# for key, value in enumerate(range(10, 20)):
#     print(f"key: {key}, value: {value}")
#     result[key] = value
#
# print(result)

# b = 5
# c = 7
# function = "5 + 8 + 9 + 14 + b + c"
# print(eval(function))

# map/filter -------------------------------

# data_1 = [1, 2, 3, 10]
#
# def dauginti(x):
#     return x * x
#
# print(list(map(dauginti, data_1)))
# print([dauginti(x) for x in data_1])
# map/filter -------------------------------


# ----------------------------FUNCTIONS------------------------------
def print_word():
    print("Swx")


def return_word(word):
    return word


print_word()
