from datetime import datetime


class Driver:
    def __init__(self, vacation: list, driver_license: str, salary_per_month: int):
        self.salary_per_month = salary_per_month
        self.driver_license = driver_license
        self.vacation = vacation

    def get_vacation(self):
        return self.vacation[0] < datetime.now() < self.vacation[1]
