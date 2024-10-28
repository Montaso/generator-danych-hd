# Set parameters for all tables

class parameters:
    START_DATE_T1 = '01-01-2016'
    END_DATE_T1 = '01-01-2020'
    START_DATE_T2 = '02-01-2020'
    END_DATE_T2 = '01-01-2024'
    START_DATE_ALL = START_DATE_T2
    END_DATE_ALL = END_DATE_T2

    CSV_DELIMETER = ';'
    DATE_FORMAT = '%d-%m-%Y'

    # Uzytkownicy
    USER_COLUMN_NAMES = ['Id', 'Imię', 'Nazwisko', 'Data Urodzenia', 'Data Rejestracji']
    USER_BIRTHDATE_START = "01-01-1950"
    USER_BIRTHDATE_END = "01-01-2008"

    USER_REGISTRATION_DATE_START = START_DATE_ALL
    USER_REGISTRATION_DATE_END = END_DATE_ALL


    # Stacje
    STATION_COLUMN_NAMES = ['Id', 'Longitude', 'Latitude', 'In_Use', 'Capacity']
    STATION_LATITUDE_RANGE = (49.0, 54.8)
    STATION_LONGITUDE_RANGE = (14.1, 24.1)
    STATION_CAPACITY_RANGE = (5, 30)

    # Kierowcy
    DRIVER_COLUMN_NAMES = ['PESEL', 'Imię', 'Nazwisko', 'Czy nadal pracuje', 'Data Zatrudnienia']
    DRIVER_PESEL_DATE_START = '01-01-1950'
    DRIVER_PESEL_DATE_END = '01-01-1998'

    DRIVER_EMPLOYMENT_DATE_START = START_DATE_ALL
    DRIVER_EMPLOYMENT_DATE_END = END_DATE_ALL

    DRIVER_STILL_WORKING_RATIO = 0.5


    # Vany
    VANS_COLUMN_NAMES = ['License_Plate', 'In_Use', 'Capacity']
    VANS_LICENSE_PLATE_PREFIXES = ["GD", "KR", "WA", "PO", "LU", "BI", "CZ", "TK"]
    VANS_CAPACITY_RANGE_CM3 = (5_000_000, 20_000_000)

    # Trasy Vanow
    VAN_ROUTE_COLUMN_NAMES = ['route_id', 'driver_fk', 'van_fk', 'date_of_route']
    VAN_ROUTE_DATE_START = START_DATE_ALL
    VAN_ROUTE_DATE_END = END_DATE_ALL

    # Pojazdy
    VEHICLE_COLUMN_NAMES = ['vehicle_id', 'type', 'electrical', 'purchase_date', 'engine_power', 'in_use',
                            'battery_capacity']
    VEHICLE_START_DATE = "01-01-2015"
    VEHICLE_END_DATE = START_DATE_T2
    VEHICLE_ENGINE_POWER_MIN = 250
    VEHICLE_ENGINE_POWER_MAX = 1500
    VEHICLE_BATTERY_CAPACITY_MIN = 500
    VEHICLE_BATTERY_CAPACITY_MAX = 1000
    VEHICLE_TYPES = ["bicycle", "scooter"]
    VEHICLE_IN_USE_WEIGHTS = [95, 5]
            
    # Wypozyczenia
    RENTAL_COLUMN_NAMES = ['rental_id', 'start_station_fk', 'end_station_fk', 'cost', 'rent_time', 'distance', 'vehicle_fk',
                 'user_fk', 'correct_putting', 'date_of_start', 'time_of_start']
    RENTAL_BASE_RATE_PER_MINUTE = 0.10
    RENTAL_BASE_RATE_PER_METER = 0.05
    RENTAL_TIME_MIN = 5
    RENTAL_TIME_MAX = 180
    RENTAL_DISTANCE_MIN = 200
    RENTAL_DISTANCE_MAX = 15000
    RENTAL_CORRECT_PUTTING_WEIGHTS = [95, 5]
    RENTAL_DATE_OF_START_MIN = START_DATE_ALL
    RENTAL_DATE_OF_START_MAX = END_DATE_ALL

