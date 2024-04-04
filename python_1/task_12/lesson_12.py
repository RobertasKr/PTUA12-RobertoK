DATA = {
    1: "vienas",
    2: "du",
    3: "trys",
}

# ------------------------------- pavyzdys 1 --------------------------
# def enter_numbers():
#     while True:
#         try: # apsaugoja programa nuo luzimo
#             value = int(input("Ivesk skaiciu: "))
#         except ValueError: # apsaugo programa nuo luzimo
#             print("Ivesk skaiciu, o ne kitus simbolius") #apsaugos zinute
#             raise ValueError("Suvestas ne skaicius")
#         if value > 10:
#             print("Daugiau nei 10")
#         else:
#             print("Maziau nei 10")
#
#         if value == 15:
#             break
#
# enter_numbers()
# ------------------------------- pavyzdys 1 --------------------------

# ------------------------------- pavyzdys 2 --------------------------
# def enter_numbers():
#     while True:
#         try: # apsaugoja programa nuo luzimo
#             value = int(input("Ivesk skaiciu: "))
#             print(DATA[value])
#         except ValueError: # apsaugo programa nuo luzimo
#             raise ValueError("Suvestas ne skaicius")
#         except KeyError:
#             raise KeyError("Neteisingas raktas!")
#         #except(KeyError, ValueError): <-- Sitoks variantas GALIMAS
#         finally:
#             print("Spausdiname finally")
#
# enter_numbers()
# ------------------------------- pavyzdys 2 --------------------------

c = [1, 2, 3]
def do_something(a, b):
    print(a, b, c)
    c = 8
    print(c)

do_something(5, 10)
