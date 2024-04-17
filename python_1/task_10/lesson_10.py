def naujas():
    print("naujas")


def return_function(a=5):
    if a == 5:
        return 8
    if a == 8:
        return 8**2
    print("cia jau po ifo")


print(return_function())

# def yield_function():
#     print("pries yield")
#     yield 5
#     print("po yield")
#
# a = yield_function()
# print(a)
# print(next(a))
# print(next(a))
