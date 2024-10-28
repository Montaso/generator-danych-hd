import threading
from classes.battery_replacement_generator import BatteryReplacementGenerator
from classes.driver_generator import DriverGenerator
from classes.rental_generator import RentalGenerator
from classes.station_generator import StationsGenerator
from classes.user_generator import UserGenerator
from classes.van_generator import VansGenerator
from classes.van_route_generator import VanRoutesGenerator
from classes.vehicle_generator import VehiclesGenerator

def generate_drivers():
    DriverGenerator(100).generate_and_save('generated_data/drivers.csv')

def generate_stations():
    StationsGenerator(100).generate_and_save('generated_data/stations_data.csv')

def generate_users():
    UserGenerator(100).generate_and_save('generated_data/users.csv')

def generate_vans():
    VansGenerator(100).generate_and_save('generated_data/vans_data.csv')

def generate_vehicles():
    VehiclesGenerator(100).generate_and_save('generated_data/vehicles_data.csv')

def generate_rentals():
    RentalGenerator(stations_filename='generated_data/stations_data.csv',
                    vehicles_filename='generated_data/vehicles_data.csv',
                    users_filename='generated_data/users.csv',
                    num_rentals=1000).generate_and_save('generated_data/rentals_data.csv')

def generate_van_routes():
    VanRoutesGenerator(drivers_filename='generated_data/drivers.csv',
                       vans_filename='generated_data/vans_data.csv',
                       num_routes=1000).generate_and_save('generated_data/van_routes_data.csv')

def generate_battery_replacements():
    BatteryReplacementGenerator(van_routes_csv='generated_data/van_routes_data.csv',
                                vehicles_csv='generated_data/vehicles_data.csv',
                                num_replacements=1000).generate_and_save('generated_data/battery_replacements_data.csv')


if __name__ == "__main__":
    # First wave
    first_wave_threads = [
        threading.Thread(target=generate_drivers),
        threading.Thread(target=generate_stations),
        threading.Thread(target=generate_users),
        threading.Thread(target=generate_vans),
        threading.Thread(target=generate_vehicles)
    ]

    for thread in first_wave_threads:
        thread.start()

    for thread in first_wave_threads:
        thread.join()

    # Second wave
    second_wave_threads = [
        threading.Thread(target=generate_rentals),
        threading.Thread(target=generate_van_routes)
    ]

    for thread in second_wave_threads:
        thread.start()

    for thread in second_wave_threads:
        thread.join()

    # Third wave
    third_wave_threads = [
        threading.Thread(target=generate_battery_replacements)
    ]

    for thread in third_wave_threads:
        thread.start()

    for thread in third_wave_threads:
        thread.join()
