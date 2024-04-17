from datetime import datetime


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
        print(f"Time now: {time_now.year}-{time_now.month}")
        print(
            f"Time inspection: {self.technical_inspection.year}-{self.technical_inspection.month}"
        )
        if (
            time_now.month == self.technical_inspection.month - 1
            and time_now.year == self.technical_inspection.year
            or time_now.month == self.technical_inspection.month + 11
            and time_now.year == self.technical_inspection.year - 1
        ):
            return (f"Kita menesi automobiliui su {self.plate_number} numeriais, YRA reikalinga technine apziura!"
                    f"\n{self.get_need_insurance_next_month()}")

        else:
            return (f"Kita menesi automobiliui su {self.plate_number} numeriais, NERA reikalinga technine apziura."
                    f"\n{self.get_need_insurance_next_month()}")

    def get_expenses_for_a_distance(self, kilometres: int):
        return f"Islaidos nuvaziavus {kilometres} kilometrus: {self.consumption + (self.expenses / 365) * kilometres}"

    def get_need_insurance_next_month(self):
        time_now = datetime.now()
        if (
            time_now.month == self.insurance_date.month - 1
            and time_now.year == self.insurance_date.year
            or time_now.month == self.insurance_date.month + 11
            and time_now.year == self.insurance_date.year - 1
        ):
            return f"Kita menesi automobiliui su {self.plate_number} numeriais, YRA reikalingas draudimo pratesimas!"
        else:
            return f"Kita menesi automobiliui su {self.plate_number} numeriais, NERA reikalingas draudimo pratesimas."
