"""
Yra duotas listas su domenimis:

[3, 2, ‚‘m‘, ‚lele‘, (1, 2, 3), [1, 2, 3], {‚vienas‘: 1,‘du‘: 2})

Reikai gražinti diktą, kuriame raktas butu reiksme duota reiksme, o rezultatas:

Jei stringas – simboliu skaicius

Jei integeris – kvadratas

Jei listas = suma

Jei dictas – value suma.

Jei tuple = sudauginti visus skaicius

Turi grazinti

{

3: 9,

‘m’: 1,

‘lele’: 4,

(3, 2, 3): 18,

[1, 2, 3]: 6,

{‚vienas‘: 1,‘du‘: 2}: 3

}

Prisiminkite ka sakiau apie mutable ir unmutuble – kurybos reiks
"""

my_list = [3, 2, "m", "lele", (1, 2, 3), [1, 2, 3], {"vienas": 1, "du": 2}]

dict_result = {}

for x in my_list:
    if isinstance(x, str):
        dict_result[x] = len(str(x))
    elif isinstance(x, int):
        dict_result[x] = x * x
    elif isinstance(x, list):
        numbers_sum = 0
        for y in x:
            numbers_sum += y
        dict_result[str(x)] = numbers_sum
    if isinstance(x, dict):
        numbers_sum = 0
        for y in x:
            numbers_sum += x.get(y)
        dict_result[str(x)] = numbers_sum
    if isinstance(x, tuple):
        numbers_multiply = 1
        for y in x:
            numbers_multiply *= y
        dict_result[x] = numbers_multiply


print(dict_result)
