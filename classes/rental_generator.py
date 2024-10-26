from classes.date_generator import DateGenerator
import csv
import random


class RentalGenerator:
    def __init__(self, stations_filename, vehicles_filename, users_filename, num_rentals=100):
        self.num_rentals = num_rentals
        self.date_generator = DateGenerator()

        self.stations = self.load_csv_ids(stations_filename, 'Id')
        self.vehicles = self.load_csv_ids(vehicles_filename, 'vehicle_id')
        self.users = self.load_csv_ids(users_filename, 'Id')

    def load_csv_ids(self, filename, id_column):
        ids = []
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                ids = [int(row[id_column]) for row in reader]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        return ids

    def generate_rental_id(self, index):
        return index + 1

    def generate_station_fk(self):
        return random.choice(self.stations)

    def generate_vehicle_fk(self):
        return random.choice(self.vehicles)

    def generate_user_fk(self):
        return random.choice(self.users)

    def generate_cost(self, distance, rent_time):
        base_rate_per_minute = 0.10
        base_rate_per_meter = 0.05
        return round(distance * base_rate_per_meter + rent_time * base_rate_per_minute, 2)

    def generate_rent_time(self):
        return random.randint(5, 180)

    def generate_distance(self):
        return random.randint(200, 15000)

    def generate_correct_putting(self):
        return random.choices([True, False], weights=[95, 5])[0]

    def generate_date_of_start(self):
        random_date = DateGenerator().generate(1, "01-01-2022", "31-12-2023")
        return random_date

    def generate_time_of_start(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return f"{hour:02}:{minute:02}"

    def generate_rental_data(self):
        rentals = []

        for i in range(self.num_rentals):
            rental_id = self.generate_rental_id(i)
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
            writer.writerow(
                ['rental_id', 'start_station_fk', 'end_station_fk', 'cost', 'rent_time', 'distance', 'vehicle_fk',
                 'user_fk', 'correct_putting', 'date_of_start', 'time_of_start'])
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