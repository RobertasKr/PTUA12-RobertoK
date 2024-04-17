"""
Automobilių parkas. Susideda iš:
-	Lengvųjų automobilių;
-	Keleivių pervežimo automobiliai;
-	Krovinių pervežimo automobiliai.

"""

import random
from datetime import datetime, timedelta

"""
-	Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo;
-	Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą;

"""


class Vehicles:
    def __init__(
        self,
        range_per_year: int,
        fuel_type: str,
        plate_number: str,
        expenses: int,
        technical_inspection: str,
        driver_license: str,
        consumption: int,
        insurance_date: str,
    ):
        self.range_per_year = range_per_year
        self.fuel_type = fuel_type
        self.plate_number = plate_number
        self.expenses = expenses
        self.technical_inspection = technical_inspection
        self.driver_license = driver_license
        self.consumption = consumption
        self.insurance_date = insurance_date

    def get_need_inspection_next_month(self):
        pass

    def get_expenses_for_a_distance(self):
        pass


class Buses(Vehicles):
    def __init__(
        self,
        range_per_year: int,
        fuel_type: str,
        plate_number: str,
        expenses: int,
        technical_inspection: str,
        driver_license: str,
        consumption: int,
        insurance_date: str,
        passengers: int,
    ):
        super().__init__(
            range_per_year,
            fuel_type,
            plate_number,
            expenses,
            technical_inspection,
            driver_license,
            consumption,
            insurance_date,
        )
        self.passengers = passengers


class Cars(Vehicles):
    def __init__(
        self,
        range_per_year: int,
        fuel_type: str,
        plate_number: str,
        expenses: int,
        technical_inspection: str,
        driver_license: str,
        consumption: int,
        insurance_date: str,
    ):
        super().__init__(
            range_per_year,
            fuel_type,
            plate_number,
            expenses,
            technical_inspection,
            driver_license,
            consumption,
            insurance_date,
        )


class Trucks(Vehicles):
    def __init__(
        self,
        range_per_year: int,
        fuel_type: str,
        plate_number: str,
        expenses: int,
        technical_inspection: str,
        driver_license: str,
        consumption: int,
        insurance_date: str,
        transporting_weight: int,
        trailer: bool,
        trailer_transporting_weight: int,
    ):
        super().__init__(
            range_per_year,
            fuel_type,
            plate_number,
            expenses,
            technical_inspection,
            driver_license,
            consumption,
            insurance_date,
        )
        self.trailer_transporting_weight = trailer_transporting_weight
        self.trailer = trailer
        self.transporting_weight = transporting_weight


range_per_year = random.randint(8000, 25000)  # Assuming kilometers
fuel_type = random.choice(["Gasoline", "Diesel", "Electric", "Hybrid"])
plate_number = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=7))
expenses = round(random.uniform(200, 1000), 2)  # Assuming currency
technical_inspection = datetime.today() + timedelta(days=random.randint(1, 365))
driver_license = "".join(random.choices("0123456789", k=10))
consumption = round(random.uniform(5, 15), 2)  # Assuming liters/100km
insurance_date = datetime.today() + timedelta(days=random.randint(1, 365))
passangers = random.randint(4, 50)

print("range_per_year:", range_per_year)
print("fuel_type:", fuel_type)
print("plate_number:", plate_number)
print("expenses:", expenses)
print("technical_inspection:", technical_inspection.strftime("%Y-%m-%d"))
print("driver_license:", driver_license)
print("consumption:", consumption)
print("insurance_date:", insurance_date.strftime("%Y-%m-%d"))
