from python_1.transport_task.vehicles.vehicle import Vehicle
import math


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

    def print_driver_can_drive(self, driver_license: str):
        if driver_license == self.driver_license:
            return True
        return False

    def get_transporting_plan(self, transporting_mass: int):

        truck = self.transporting_weight
        trailer = self.trailer_transporting_weight

        max_trips = math.ceil(transporting_mass / self.get_transporting_weight_with_trailer())

        if max_trips * truck <= transporting_mass:
            trips_with_trailer = math.ceil((transporting_mass - truck * max_trips) / trailer)
        else:
            trips_with_trailer = 0
        return max_trips, trips_with_trailer
