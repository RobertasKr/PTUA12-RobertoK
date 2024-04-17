import random
from datetime import datetime, timedelta
from vehicles.vehicle import Vehicle
from vehicles.car import Car
from vehicles.bus import Bus
from vehicles.truck import Truck
from driver.driver import Driver


def get_vacation():
    vacation_start = datetime.today() + timedelta(days=random.randint(1, 365))
    vacation_end = vacation_start + timedelta(days=random.randint(1, 30))
    return [vacation_start.strftime("%Y-%m-%d"), vacation_end.strftime("%Y-%m-%d")]

# Cia sukuriamos visos reikiamos reiksmes Vehicle klasei
range_per_year = random.randint(8000, 25000)
fuel_type = random.choice(["Gasoline", "Diesel", "Electric", "Hybrid"])
plate_number = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
expenses = round(random.uniform(200, 1000), 2)
# technical_inspection = datetime.today() + timedelta(days=270)
technical_inspection = datetime.today() + timedelta(days=random.randint(1, 365))
driver_license = "".join(random.choices("ABCDT", k=1))
consumption = round(random.uniform(5, 15), 2)  # Assuming liters/100km
insurance_date = datetime.today() + timedelta(days=random.randint(1, 365))

# Cia testavau, kokias reiksmes gaunu jas sukuriant
# print("range_per_year:", range_per_year)
# print("fuel_type:", fuel_type)
# print("plate_number:", plate_number)
# print("expenses:", expenses)
# print("technical_inspection:", technical_inspection.strftime("%Y-%m-%d"))
# print("driver_license:", driver_license)
# print("consumption:", consumption)
# print("insurance_date:", insurance_date.strftime("%Y-%m-%d"))

vehicle1 = Vehicle(
    range_per_year,
    fuel_type,
    plate_number,
    expenses,
    technical_inspection,
    driver_license,
    consumption,
    insurance_date,
)
print(vehicle1.get_need_inspection_next_month())
print(vehicle1.get_expenses_for_a_distance(random.randint(10, 500)))
car1 = Car(
    range_per_year,
    fuel_type,
    plate_number,
    expenses,
    technical_inspection,
    driver_license,
    consumption,
    insurance_date,
)
print(car1.get_expenses_for_a_distance(random.randint(10, 500)))
bus1 = Bus(
    range_per_year,
    fuel_type,
    plate_number,
    expenses,
    technical_inspection,
    driver_license,
    consumption,
    insurance_date,
    passengers=50,
)
print(bus1.get_buses_needed_for_passengers(201))
truck1 = Truck(
    range_per_year,
    fuel_type,
    plate_number,
    expenses,
    technical_inspection,
    "T",
    consumption,
    insurance_date,
    transporting_weight=12,
    trailer=True,
    trailer_transporting_weight=5,
)


vacation = get_vacation()
salary = random.randint(3000, 8000)
driver = Driver(vacation, "A", salary)

print(vacation)

truck1.get_transporting_plan(36)
truck1.print_driver_can_drive(driver.driver_license)

print(driver.vacation)
driver.get_vacation()
