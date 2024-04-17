from datetime import datetime, timedelta


class Driver:
    def __init__(self, vacation, driver_license: str, salary: int):
        self.salary = salary
        self.driver_license = driver_license
        self.vacation = vacation

    def get_vacation(self):
        if (
            self.vacation[0]
            < (datetime.now() + timedelta(days=77)).strftime("%Y-%m-%d")
            < self.vacation[1]
        ):
            return print(f"Vairuotojas atostogauja iki {self.vacation[1]}")
        else:
            return print(f"Vairuotojas atostogaus nuo {self.vacation[0]}")
