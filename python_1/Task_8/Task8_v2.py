"""
Duotas listas skaiciu – [1, 2, 3, 4, 5, 6, 18, 90, 118, 991,  196151]. Grazinti dicta, kuris butu suskaiciuota kiek is siu skaiciu yra lyginiu, kiek nelyginiu:

{

‚lyginiu_skaiciu_suma‘: suskaiciuotas kiekis‘,



‚nelyginiu_skaiciu_suma‘: suskaiciuotas kiekis‘

}
"""

list_numbers = [1, 2, 3, 4, 5, 6, 18, 90, 118, 991, 196151]

dict_result = {
    "lyginiu_skaiciu_suma": 0,
    "nelyginiu_skaiciu_suma": 0,
}

for x in list_numbers:
    if x % 2 == 0:
        dict_result["lyginiu_skaiciu_suma"] += x
    else:
        dict_result["nelyginiu_skaiciu_suma"] += x

print(dict_result)
