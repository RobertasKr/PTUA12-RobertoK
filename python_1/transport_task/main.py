import random
from datetime import datetime
from vehicles.vehicle import Vehicle
from vehicles.car import Car
from vehicles.bus import Bus
from vehicles.truck import Truck
from driver.driver import Driver

# Cia sukuriamos visos reikiamos reiksmes Vehicle klasei
range_per_year = random.randint(8000, 25000)
fuel_type = random.choice(["Gasoline", "Diesel", "Electric", "Hybrid"])
plate_number = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
expenses = random.randint(200, 1000)
# technical_inspection = datetime.today() + timedelta(days=270)
technical_inspection = datetime(year=2024, month=5, day=5)
driver_license = "".join(random.choices("ABCDT", k=1))
consumption = 12  # Assuming liters/100km
insurance_date = datetime(year=2024, month=5, day=5)

print("----------------TEST VARIABLES--------------------")
# Cia testavau, kokias reiksmes gaunu jas sukuriant
print("range_per_year:", range_per_year)
print("fuel_type:", fuel_type)
print("plate_number:", plate_number)
print("expenses:", expenses)
print("technical_inspection:", technical_inspection.strftime("%Y-%m-%d"))
print("driver_license:", driver_license)
print("consumption:", consumption)
print("insurance_date:", insurance_date.strftime("%Y-%m-%d"))
print("-----------------TEST VARIABLES--------------------\n\n")


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

truck1 = Truck(
    range_per_year,
    fuel_type,
    plate_number,
    expenses,
    technical_inspection,
    "T",
    consumption,
    insurance_date,
    transporting_weight=20,
    trailer=True,
    trailer_transporting_weight=12,
)

vacation_dates1 = [datetime(year=2024, month=4, day=18), datetime(year=2024, month=4, day=28)]
vacation_dates2 = [datetime(year=2024, month=8, day=18), datetime(year=2024, month=8, day=28)]
salary = 5000
driver1 = Driver(vacation_dates1, "T", salary)
driver2 = Driver(vacation_dates2, "A", salary)

print("-----------------Results--------------------\n")
inspection_needed = vehicle1.get_need_inspection_next_month()[0]
insurance_needed = vehicle1.get_need_inspection_next_month()[1]

print(f"Kita menesi technikine reikes atsinaujinti: {inspection_needed}"
      f"\nKita menesi draudima reikes atsinaujinti: {insurance_needed}\n")

x_kilometres = 50
expenses_per_x_km = vehicle1.get_expenses_for_a_distance(x_kilometres)
print(f"Islaidos {x_kilometres} kilometru kelione sudarys: "
      f"{round(expenses_per_x_km)} Eur\n")

passengers_needed = 201
x_kilometres = 120
busses_count = bus1.get_buses_needed_for_passengers(passengers_needed)
print(f"Pervezti {passengers_needed} keleivius, reikes {busses_count} autobusu")
bus_expenses_x_km = bus1.get_sum_expenses_for_x_km(passengers_needed, x_kilometres)
print(f"Pervezti {passengers_needed} keleivius {busses_count} kartus "
      f"sudarys tokias islaidas: {round(bus_expenses_x_km)} Eur\n")

print(f"Vairuotojo atostogu statusas: {truck1.get_driver_on_vacation(driver1)}\n")

truck_trips = truck1.get_transporting_plan(33)
print(f"Reikes {truck_trips[0]} reisu, kuriuose {truck_trips[1]} reisu su priekaba\n")

license_check = truck1.print_driver_can_drive(driver2.driver_license)
print(f"Ar vairuotojas gali vairuoti {truck1.driver_license} kategorijos auto: "
      f"{license_check}\n")

print("-----------------Results--------------------")
