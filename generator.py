from classes.battery_replacement_generator import BatteryReplacementGenerator
from classes.driver_generator import DriverGenerator
from classes.rental_generator import RentalGenerator
from classes.station_generator import StationsGenerator
from classes.user_generator import UserGenerator
from classes.van_generator import VansGenerator
from classes.van_route_generator import VanRoutesGenerator
from classes.vehicle_generator import VehiclesGenerator


if __name__ == "__main__":
    # first wave
    DriverGenerator(100).generate_and_save('generated_data/drivers.csv')
    StationsGenerator(100).generate_and_save('generated_data/stations_data.csv')
    UserGenerator(100).generate_and_save('generated_data/users.csv')
    VansGenerator(100).generate_and_save('generated_data/vans_data.csv')
    VehiclesGenerator(100).generate_and_save('generated_data/vehicles_data.csv')

    #second wave
    RentalGenerator(stations_filename='generated_data/stations_data.csv',
                    vehicles_filename='generated_data/vehicles_data.csv',
                    users_filename='generated_data/users.csv',
                    num_rentals=1000).generate_and_save('generated_data/rentals_data.csv')
    (VanRoutesGenerator(drivers_filename='generated_data/drivers.csv',
                       vans_filename='generated_data/vans_data.csv',
                        num_routes=1000)
     .generate_and_save('generated_data/van_routes_data.csv'))

    #third wave
    (BatteryReplacementGenerator(van_routes_csv='generated_data/van_routes_data.csv',
                                vehicles_csv='generated_data/vehicles_data.csv',
                                 num_replacements=1000)
     .generate_and_save('generated_data/battery_replacements_data.csv'))




