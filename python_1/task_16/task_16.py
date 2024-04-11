"""
Sukurkite Calculator klasę su pagrindinėmis funkcijomis: sudėti, dalyti, dauginti, atimti ir t. t.. Inicijuokite klasę ir parodykite keletą skaičiavimų.
"""
print("-------------------------------1------------------------------")

class Calculator:

    def __init__(self):
        self.x = 69
        self.y = 3

    def numbers_sum(self):
        print(self.x + self.y)

    def numbers_subtract(self):
        print(self.x - self.y)

    def numbers_multiply(self):
        print(self.x * self.y)

    def numbers_divide(self):
        print(self.x / self.y)


calculator = Calculator()

calculator.numbers_sum()
calculator.numbers_divide()
calculator.numbers_subtract()
calculator.numbers_multiply()

"""
Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas). Turint asmens vardą ir pavardę:

Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.

Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį . Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
"""
print("-------------------------------2------------------------------")
class Worker:

    def __init__(self):
        self.fullname = "Robertas", "Krašauskas"
        self.email = "email@email.com"

    def fullname_join(self):
        print(" ".join(self.fullname))

    def generate_email(self):
        print((".".join(self.fullname) + "@company.com").lower())


worker = Worker()

print(worker.fullname)
worker.fullname_join()
worker.generate_email()

"""
Sukurkite knygos klasę Book, kuri turi du atributus:

name

author

ir du metodus:

Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.

Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.

ir instancuokite šią klasę sukurdami 3 naujas knygas:


- Pride and Prejudice - Jane Austen (PP)
- Hamletas - Viljamas Šekspyras (H)
- Karas ir taika - Levas Tolstojus (WP)
Naujų egzempliorių pavadinimai turėtų būti atitinkamai PP, H ir WP. Pavyzdžiui, jei, naudodamas šią knygų klasę, instancuočiau šią knygą:


- Haris Poteris - J. K. Rowling (HP)
Gaučiau šiuos atributus ir metodus:


HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Pavadinimas: Haris Poteris"
HP.get_author() ➞ "Autorius: Rowling"
"""
print("-------------------------------3------------------------------")
class Book:

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def get_title(self):
        print("Pavadinimas: " + self.name)
    def get_author(self):
        print("Autorius: " + self.author)

PP = Book(name="Pride and Prejudice", author="Jane Austen")
H = Book(name="Hamletas", author="Viljamas Šekspyras")
WP = Book(name="Karas ir taika", author="Levas Tolstojus")

PP.get_title(), PP.get_author()
H.get_title(), H.get_author()
WP.get_title(), WP.get_author()

"""
Apie šalį galima sakyti, kad ji yra didelė, jei ji yra:
Didelė gyventojų skaičiumi.
Didelė pagal plotą.
Šalies klasę papildykite taip, kad joje būtų atributas is_big. Nustatykite jį į True, jei tenkinamas kuris nors iš šių kriterijų:
Gyventojų skaičius yra didesnis nei 20 mln.
Plotas didesnis nei 3 mln. km².
Taip pat sukurkite metodą, kuris palygintų šalies gyventojų tankį su kitos šalies objektu. Grąžinkite tokio formato eilutę:

{country} has a {smaller / larger} population density than {other_country}
Pavyzdys:

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
"""

class Country:

    def __init__(self, country: str, population: int,  area: int):
        self.country = country
        self.area = area
        self.population = population
        self.is_big = population > 20000000 or self.area > 3000000

    def is_big(self):
        self.is_big = self.population > 20000000 or self.area > 3000000

    def compare_pd(self, country_name):
        if self.population / self.area > country_name.population / country_name.area:
            print(f"{self.country} has a larger population density than ")
        else:
            print(f"{self.country} has a smaller population density than ")
        return country_name.population

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)
print(andorra.is_big)
andorra.compare_pd(australia) #➞ "Andorra has a larger population density than Australia"
print(andorra.compare_pd(australia))
