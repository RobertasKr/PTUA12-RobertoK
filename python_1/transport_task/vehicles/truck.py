from python_1.transport_task.vehicles.vehicle import Vehicle
import random
from datetime import datetime, timedelta


class Truck(Vehicle):
    def __init__(
            self,
            range_per_year: int,
            fuel_type: str,
            plate_number: str,
            expenses: float,
            technical_inspection,
            driver_license: str,
            consumption: float,
            insurance_date,
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
        self.trailer = trailer  # ??????? nezinau ar panaudosiu
        self.transporting_weight = transporting_weight

    def get_transporting_weight_with_trailer(self):
        return self.trailer_transporting_weight + self.transporting_weight

    def get_transporting_plan(self, transporting_mass: int):
        mixed_transporting = self.get_transporting_mixed(
            transporting_mass=transporting_mass
        )
        with_trailer = self.get_transporting_with_trailer(
            transporting_mass=transporting_mass
        )
        without_trailer = self.get_transporting_without_trailer(
            transporting_mass=transporting_mass
        )
        if with_trailer == without_trailer and mixed_transporting is None:
            return print(
                f"Kroviniui pristatyti reikes {without_trailer} reisu, be priekabos"
            )
        elif with_trailer < without_trailer and mixed_transporting is None:
            return print(
                f"Kroviniui pristatyti reikes {with_trailer} reisu, su priekaba"
            )
        elif mixed_transporting is True:
            return print(
                f"Kroviniui pristatyti reikes {with_trailer - 1} reisu, su priekaba ir 1 reiso be priekabos"
            )

    def get_transporting_with_trailer(self, transporting_mass: int):
        transporting_with_trailer = 0
        temp_mass = transporting_mass
        while temp_mass > 0:
            if 0 < self.get_transporting_weight_with_trailer() < temp_mass:
                temp_mass -= self.get_transporting_weight_with_trailer()
                transporting_with_trailer += 1
            elif 0 < temp_mass < self.get_transporting_weight_with_trailer():
                transporting_with_trailer += 1
                break
            else:
                transporting_with_trailer += 1
                break
        return transporting_with_trailer

    def get_transporting_without_trailer(self, transporting_mass: int):
        transporting_without_trailer = 0
        temp_mass = transporting_mass
        while temp_mass > 0:
            if temp_mass > self.transporting_weight > 0:
                temp_mass -= int(self.transporting_weight)
                transporting_without_trailer += 1
            elif 0 < temp_mass < self.transporting_weight:
                transporting_without_trailer += 1
                break
            else:
                transporting_without_trailer += 1
                break
        return transporting_without_trailer

    def get_transporting_mixed(self, transporting_mass: int):
        with_trailer = self.get_transporting_with_trailer(
            transporting_mass=transporting_mass
        )
        without_trailer = self.get_transporting_without_trailer(
            transporting_mass=transporting_mass
        )
        mass_remaining = transporting_mass % self.get_transporting_weight_with_trailer()
        if with_trailer == without_trailer:
            return
        if transporting_mass >= 12:
            if mass_remaining > self.transporting_weight:
                return
            elif mass_remaining == 0:
                return
            elif mass_remaining < self.transporting_weight:
                return True
        else:
            return

    def print_driver_can_drive(self, driver_license: str):
        if driver_license == self.driver_license:
            return print(
                f"Vairuotojas turi {driver_license}, todel GALI vairuoti {plate_number} transporto priemone!"
            )
        else:
            return print(
                f"Vairuotojas turi {driver_license}, todel NEGALI vairuoti {plate_number} transporto priemones."
            )

range_per_year = random.randint(8000, 25000)
fuel_type = random.choice(["Gasoline", "Diesel", "Electric", "Hybrid"])
plate_number = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
expenses = round(random.uniform(200, 1000), 2)
technical_inspection = datetime.today() + timedelta(days=random.randint(1, 365))
driver_license = "".join(random.choices("ABCDT", k=1))
consumption = round(random.uniform(5, 15), 2)  # Assuming liters/100km
insurance_date = datetime.today() + timedelta(days=random.randint(1, 365))
passangers = random.randint(4, 50)
