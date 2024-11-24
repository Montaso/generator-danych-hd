import csv
import threading
import random

from classes.battery_replacement_generator import BatteryReplacementGenerator
from classes.driver_generator import DriverGenerator
from classes.rental_generator import RentalGenerator
from classes.station_generator import StationsGenerator
from classes.user_generator import UserGenerator
from classes.van_generator import VansGenerator
from classes.van_route_generator import VanRoutesGenerator
from classes.vehicle_generator import VehiclesGenerator
from classes.parameters import parameters
from merger import merge


def generate_drivers(start_index, rows, name_end):
    DriverGenerator(start_index=start_index, n=rows).generate_and_save(f'generated_data/drivers{name_end}.csv')


def generate_stations(start_index, rows, name_end):
    (StationsGenerator(num_stations=rows, start_index=start_index)
     .generate_and_save(f'generated_data/stations_data{name_end}.csv'))


def generate_users(start_index, rows, name_end):
    UserGenerator(n=rows, start_index=start_index).generate_and_save(f'generated_data/users{name_end}.csv')


def generate_vans(rows, name_end):
    VansGenerator(num_vans=rows).generate_and_save(f'generated_data/vans_data{name_end}.csv')


def generate_vehicles(start_index, rows, name_end):
    (VehiclesGenerator(num_vehicles=rows, start_index=start_index)
     .generate_and_save(f'generated_data/vehicles_data{name_end}.csv'))


def generate_rentals(start_index, rows, name_end, source_name_end):
    RentalGenerator(stations_filename=f'generated_data/stations_data{source_name_end}.csv',
                    vehicles_filename=f'generated_data/vehicles_data{source_name_end}.csv',
                    users_filename=f'generated_data/users{source_name_end}.csv',
                    num_rentals=rows,
                    start_index=start_index).generate_and_save(f'generated_data/rentals_data{name_end}.csv')


def generate_van_routes(start_index, rows, name_end, source_name_end):
    VanRoutesGenerator(drivers_filename=f'generated_data/drivers{source_name_end}.csv',
                       vans_filename=f'generated_data/vans_data{source_name_end}.csv',
                       num_routes=rows,
                       start_index=start_index).generate_and_save(f'generated_data/van_routes_data{name_end}.csv')


def generate_battery_replacements(start_index, rows, name_end, source_name_end):
    BatteryReplacementGenerator(van_routes_csv=f'generated_data/van_routes_data{source_name_end}.csv',
                                vehicles_csv=f'generated_data/vehicles_data{source_name_end}.csv',
                                num_replacements=rows,
                                start_index=start_index).generate_and_save(
        f'generated_data/battery_replacements_data{name_end}.csv')


def generate_SCD(num=1):
    still_working_drivers = []
    still_in_use_vehicles = []
    lines = 1

    with open('generated_data/drivers.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['Czy nadal pracuje'] == '1':
                still_working_drivers.append(row)

    if still_working_drivers:
        selected_drivers = random.sample(still_working_drivers, min(num, len(still_working_drivers)))
        with open('generated_data/drivers12.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for _ in reader:
                lines += 1
        with open('generated_data/drivers12.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=selected_drivers[0].keys(), delimiter=';')

            for random_driver in selected_drivers:
                random_driver['Czy nadal pracuje'] = 0
                random_driver['id'] = lines
                writer.writerow(random_driver)

    lines = 1
    with open('generated_data/vehicles_data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['in_use'] == '1':
                still_in_use_vehicles.append(row)

    if still_working_drivers:
        selected_vehicles = random.sample(still_in_use_vehicles, min(num, len(still_in_use_vehicles)))
        with open('generated_data/vehicles_data12.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for _ in reader:
                lines += 1
        with open('generated_data/vehicles_data12.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=selected_vehicles[0].keys(), delimiter=';')

            for random_vehicle in selected_vehicles:
                random_vehicle['in_use'] = 0
                random_vehicle['vehicle_id'] = lines
                writer.writerow(random_vehicle)


def generate_dimension_data(dim_index=1, dim_rows=100, name_end=''):
    threads = [
        threading.Thread(target=generate_drivers, args=(dim_index, dim_rows, name_end)),
        threading.Thread(target=generate_stations, args=(dim_index, dim_rows, name_end)),
        threading.Thread(target=generate_users, args=(dim_index, dim_rows, name_end)),
        threading.Thread(target=generate_vans, args=(dim_rows, name_end)),
        threading.Thread(target=generate_vehicles, args=(dim_index, dim_rows, name_end))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def generate_fact_data(fact_index=1, fact_rows=1000, name_end='', source_name_end=''):
    threads = [
        threading.Thread(target=generate_rentals, args=(fact_index, fact_rows, name_end, source_name_end)),
        threading.Thread(target=generate_van_routes, args=(fact_index, fact_rows, name_end, source_name_end))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def generate_missing_fact_data(fact_index=1, fact_rows=1000, name_end='', source_name_end=''):
    threads = [
        threading.Thread(target=generate_battery_replacements, args=(fact_index, fact_rows, name_end, source_name_end))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def set_parameters(ALL_START, ALL_END, USER_BIRTHDAY_END, DRIVER_PESEL_DATE_END):
    parameters.DRIVER_EMPLOYMENT_DATE_START = ALL_START
    parameters.DRIVER_EMPLOYMENT_DATE_END = ALL_END
    parameters.USER_BIRTHDATE_END = USER_BIRTHDAY_END
    parameters.DRIVER_PESEL_DATE_END = DRIVER_PESEL_DATE_END
    parameters.VAN_ROUTE_DATE_START = ALL_START
    parameters.VAN_ROUTE_DATE_END = ALL_END
    parameters.VEHICLE_END_DATE = ALL_START
    parameters.RENTAL_DATE_OF_START_MIN = ALL_START
    parameters.RENTAL_DATE_OF_START_MAX = ALL_END


dimensions = ['drivers', 'users', 'stations_data', 'vans_data', 'vehicles_data']
if __name__ == "__main__":
    set_parameters('01-01-2016', '01-01-2020', "01-01-2003",
                   '01-01-1998')
    generate_dimension_data(1, 100, '')
    generate_fact_data(1, 1000, '', '')
    generate_missing_fact_data(1, 1000, '', '')

    set_parameters('01-01-2020', '01-01-2024', '01-01-2007',
                    '01-01-2002')
    generate_dimension_data(101, 10, '2')
    for dim in dimensions:
        merge(dim)
    generate_SCD()

    generate_fact_data(1001, 100, '2', '12')
    merge('van_routes_data')
    merge('rentals_data')

    generate_missing_fact_data(1001, 100, '2', '12')
    merge('battery_replacements_data')





