from python_1.transport_task.vehicles.vehicle import Vehicle


class Car(Vehicle):
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
