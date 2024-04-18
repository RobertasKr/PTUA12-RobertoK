from python_1.transport_task.vehicles.vehicle import Vehicle
from math import ceil


class Bus(Vehicle):
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

    def get_buses_needed_for_passengers(self, passengers_needed: int):
        return ceil(passengers_needed / self.passengers)

    def get_sum_expenses_for_x_km(self, passengers_needed: int, x_km: int):
        expenses_per_x_km = self.get_expenses_for_a_distance(x_km)
        trips_count = self.get_buses_needed_for_passengers(passengers_needed)
        return trips_count * expenses_per_x_km
