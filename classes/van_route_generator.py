try:
    from .parameters import parameters
except ImportError:
    from parameters import parameters

import csv
import random

try:
    from .date_generator import DateGenerator
except ImportError:
    from date_generator import DateGenerator


class VanRoutesGenerator:
    def __init__(self, drivers_filename='../generated_data/drivers.csv',
                 vans_filename='../generated_data/vans_data.csv',
                 num_routes=100, start_index=1):
        self.num_routes = num_routes
        self.date_generator = DateGenerator()
        self.start_index = start_index

        self.drivers = self.load_csv_ids(drivers_filename, 'id')
        self.vans = self.load_csv_ids(vans_filename, 'License_Plate')

        self.route_date_start = parameters.VAN_ROUTE_DATE_START
        self.route_date_end = parameters.VAN_ROUTE_DATE_END
        self.column_names = parameters.VAN_ROUTE_COLUMN_NAMES

    def load_csv_ids(self, filename, id_column):
        ids = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                ids = [row[id_column] for row in reader]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        return ids

    def generate_route_id(self, index):
        return index + self.start_index

    def generate_driver_fk(self):
        return random.choice(self.drivers)

    def generate_van_fk(self):
        return random.choice(self.vans)

    def generate_date_of_route(self):
        return self.date_generator.generate(1, self.route_date_start, self.route_date_end)

    def generate_van_routes_data(self):
        routes = []

        for i in range(self.num_routes):
            route_id = self.generate_route_id(i)
            driver_fk = self.generate_driver_fk()
            van_fk = self.generate_van_fk()
            date_of_route = self.generate_date_of_route()

            routes.append((route_id, driver_fk, van_fk, date_of_route))

        return routes

    def write_to_csv(self, routes, filename='../generated_data/van_routes_data.csv'):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=parameters.CSV_DELIMETER)
            writer.writerow(self.column_names)
            writer.writerows(routes)

    def generate_and_save(self, filename='../generated_data/van_routes_data.csv'):
        routes = self.generate_van_routes_data()
        self.write_to_csv(routes, filename)
        print(f"Generated {self.num_routes} van routes and wrote to '{filename}'")


if __name__ == "__main__":
    VanRoutesGenerator(num_routes=100).generate_and_save('../generated_data/van_routes_data.csv')
