def do_something(a, b, c, *args, **kwargs):
    # print("funkcija")
    # print(a, b, c)
    # print(args, type(args))
    # print(kwargs, type(kwargs))
    if "word" in kwargs:
        print("word exist")
    print("Viskas")

def another_function(a, **kwargs):
    print(a)
    print(kwargs)

do_something(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, z=420, word=69)

another_function(a=9, nesamone=10)