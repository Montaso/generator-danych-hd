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
    DriverGenerator(10).generate_and_save('generated_data/drivers2.csv')

def generate_stations(start_index):
    StationsGenerator(10, start_index).generate_and_save('generated_data/stations_data2.csv')

def generate_users(start_index):
    UserGenerator(10, start_index).generate_and_save('generated_data/users2.csv')

def generate_vans():
    VansGenerator(10).generate_and_save('generated_data/vans_data2.csv')

def generate_vehicles(start_index):
    VehiclesGenerator(10, start_index=start_index).generate_and_save('generated_data/vehicles_data2.csv')

def generate_rentals(start_index):
    RentalGenerator(stations_filename='generated_data/stations_data12.csv',
                    vehicles_filename='generated_data/vehicles_data12.csv',
                    users_filename='generated_data/users12.csv',
                    num_rentals=100,
                    start_index=start_index).generate_and_save('generated_data/rentals_data2.csv')

def generate_van_routes(start_index):
    VanRoutesGenerator(drivers_filename='generated_data/drivers12.csv',
                       vans_filename='generated_data/vans_data12.csv',
                       num_routes=100,
                       start_index=start_index).generate_and_save('generated_data/van_routes_data2.csv')

def generate_battery_replacements(start_index):
    BatteryReplacementGenerator(van_routes_csv='generated_data/van_routes_data12.csv',
                                vehicles_csv='generated_data/vehicles_data12.csv',
                                num_replacements=100,
                                start_index=start_index).generate_and_save('generated_data/battery_replacements_data2.csv')

mode = "facts"
mode2 = "last"

if __name__ == "__main__":
    # First wave
    if mode != "facts":
        first_wave_threads = [
            threading.Thread(target=generate_drivers),
            threading.Thread(target=generate_stations, args=(101,)),
            threading.Thread(target=generate_users, args=(101,)),
            threading.Thread(target=generate_vans),
            threading.Thread(target=generate_vehicles, args=(101,))
        ]

        for thread in first_wave_threads:
            thread.start()

        for thread in first_wave_threads:
            thread.join()

    if mode2 != "last":
        # Second wave
        second_wave_threads = [
            threading.Thread(target=generate_rentals, args=(1001,)),
            threading.Thread(target=generate_van_routes, args=(1001,))
        ]

        for thread in second_wave_threads:
            thread.start()

        for thread in second_wave_threads:
            thread.join()

    # Third wave
    third_wave_threads = [
        threading.Thread(target=generate_battery_replacements, args=(1001,))
    ]

    for thread in third_wave_threads:
        thread.start()

    for thread in third_wave_threads:
        thread.join()
