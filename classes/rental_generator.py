try:
    from .date_generator import DateGenerator
    from .parameters import parameters
except ImportError:
    from date_generator import DateGenerator
    from parameters import parameters
import csv
import random


class RentalGenerator:
    def __init__(self, stations_filename, vehicles_filename, users_filename,
                 num_rentals=100, start_index=1):
        self.num_rentals = num_rentals
        self.date_generator = DateGenerator()
        self.start_index = start_index

        self.stations = self.load_csv_ids(stations_filename, 'Id')
        self.vehicles = self.load_csv_ids(vehicles_filename, 'vehicle_id')
        self.users = self.load_csv_ids(users_filename, 'Id')

        self.base_rate_per_minute = parameters.RENTAL_BASE_RATE_PER_MINUTE
        self.base_rate_per_meter = parameters.RENTAL_BASE_RATE_PER_METER

        self.rent_time_min = parameters.RENTAL_TIME_MIN
        self.rent_time_max = parameters.RENTAL_TIME_MAX

        self.distance_min = parameters.RENTAL_DISTANCE_MIN
        self.distance_max = parameters.RENTAL_DISTANCE_MAX

        self.correct_putting_weights = parameters.RENTAL_CORRECT_PUTTING_WEIGHTS

        self.date_of_start_min = parameters.RENTAL_DATE_OF_START_MIN
        self.date_of_start_max = parameters.RENTAL_DATE_OF_START_MAX
        self.column_names = parameters.RENTAL_COLUMN_NAMES

        
    def load_csv_ids(self, filename, id_column):
        ids = []
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=parameters.CSV_DELIMETER)
                ids = [int(row[id_column]) for row in reader]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        return ids

    def generate_rental_id(self, index):
        return index

    def generate_station_fk(self):
        return random.choice(self.stations)

    def generate_vehicle_fk(self):
        return random.choice(self.vehicles)

    def generate_user_fk(self):
        return random.choice(self.users)

    def generate_cost(self, distance, rent_time):
        return round(distance * self.base_rate_per_meter + rent_time * self.base_rate_per_minute, 2)

    def generate_rent_time(self):
        return random.randint(self.rent_time_min, self.rent_time_max)

    def generate_distance(self):
        return random.randint(self.distance_min, self.distance_max)

    def generate_correct_putting(self):
        return random.choices([1, 0], weights=self.correct_putting_weights)[0]

    def generate_date_of_start(self):
        random_date = DateGenerator().generate(1, self.date_of_start_min, self.date_of_start_max)
        return random_date

    def generate_time_of_start(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return f"{hour:02}:{minute:02}"

    def generate_rental_data(self):
        rentals = []

        for i in range(self.num_rentals):
            rental_id = self.generate_rental_id(i + self.start_index)
            start_station_fk = self.generate_station_fk()
            end_station_fk = self.generate_station_fk()
            vehicle_fk = self.generate_vehicle_fk()
            user_fk = self.generate_user_fk()
            rent_time = self.generate_rent_time()
            distance = self.generate_distance()
            cost = self.generate_cost(distance, rent_time)
            correct_putting = self.generate_correct_putting()
            date_of_start = self.generate_date_of_start()
            time_of_start = self.generate_time_of_start()

            rentals.append((rental_id, start_station_fk, end_station_fk, cost, rent_time, distance, vehicle_fk, user_fk,
                            correct_putting, date_of_start, time_of_start))

        return rentals

    def write_to_csv(self, rentals, filename='../generated_data/rentals_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(self.column_names)
            writer.writerows(rentals)

    def generate_and_save(self, filename='../generated_data/rentals_data.csv'):
        rentals = self.generate_rental_data()
        self.write_to_csv(rentals, filename)
        print(f"Generated {self.num_rentals} rentals and wrote to '{filename}'")


if __name__ == "__main__":
    (RentalGenerator(stations_filename='../generated_data/stations_data.csv',
                     vehicles_filename='../generated_data/vehicles_data.csv',
                     users_filename='../generated_data/users.csv',
                     num_rentals=100)
                     .generate_and_save('../generated_data/rentals_data.csv'))