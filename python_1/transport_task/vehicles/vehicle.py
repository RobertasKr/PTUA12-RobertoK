from datetime import datetime
from python_1.transport_task.driver.driver import Driver


class Vehicle:
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

        time_now = datetime.now()
        inspection_date = self.technical_inspection
        get_insurance = self.get_need_insurance_next_month()

        if (
            time_now.month == inspection_date.month - 1
            and time_now.year == inspection_date.year
            or time_now.month == inspection_date.month + 11
            and time_now.year == inspection_date.year - 1
        ):
            return True, get_insurance
        return False, get_insurance

    def get_expenses_for_a_distance(self, kilometres: int):
        return self.consumption + (self.expenses / 365) * kilometres

    def get_need_insurance_next_month(self):

        time_now = datetime.now()
        insurance_date = self.insurance_date

        if (
            time_now.month == insurance_date.month - 1
            and time_now.year == insurance_date.year
            or time_now.month == insurance_date.month + 11
            and time_now.year == insurance_date.year - 1
        ):
            return True
        return False

    def get_driver_on_vacation(self, driver: Driver):
        return driver.get_vacation()
