import csv
import random
from datetime import timedelta


class ReportGenerator:
    def __init__(self, n, van_route_filename='../generated_data/van_routes_data2.csv'):
        self.n = n
        self.routes_ids = self.load_csv_ids(van_route_filename, 'route_id')
        self.routes_dates = self.load_csv_ids(van_route_filename, 'date_of_route')

        self.route_length_min = 50.0
        self.route_length_max = 150.0

        self.avg_fuel_consumption_min = 10.0
        self.avg_fuel_consumption_max = 15.0

        self.avg_speed = 50


    def load_csv_ids(self, filename, id_column):
        ids = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                ids = [row[id_column] for row in reader]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        return ids
    

    def generate_random_route_length(self):
        return round(random.uniform(self.route_length_min, self.route_length_max), 2)


    def generate_random_fuel_consumption(self):
        return round(random.uniform(self.avg_fuel_consumption_min, self.avg_fuel_consumption_max), 2)
    

    def generate_route_time(self, route_length = 0, is_random = False):
        time_hours = route_length / self.avg_speed
        total_seconds = int(time_hours * 3600)
        return str(timedelta(seconds=total_seconds))


    def generate_random_hhmmss(self, hhmmss = [0, 23, 0, 59, 0, 59]):
        time_hours = random.randint(hhmmss[0], hhmmss[1])
        time_minutes = random.randint(hhmmss[2], hhmmss[3])
        time_seconds = random.randint(hhmmss[4], hhmmss[5])

        return str(str(time_hours) + ':' + str(time_minutes) + ':' + str(time_seconds))

    def generate(self):
        reports = []

        for i in range(self.n):
            # random_idx = random.randint(0, len(self.routes_ids)-1)

            route_id = self.routes_ids[i]
            route_length = self.generate_random_route_length()
            route_time = self.generate_route_time(route_length=route_length)
            avg_fuel_consumption = self.generate_random_fuel_consumption()
            route_date = self.routes_dates[i]
            route_hr = self.generate_random_hhmmss([6, 12, 0, 59, 0, 59])
            moved_bikes = random.randint(0, 10)
            moved_scooters = random.randint(0, 10)


            reports.append((route_id, route_length, route_time, avg_fuel_consumption, route_date, route_hr, moved_bikes, moved_scooters))

        return reports


    def write_to_csv(self, reports, filename='../generated_data/reports.csv'):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['route_id', 'route_length', 'route_time', 'average_fuel_consumption', 'route_date', 'finish_time', 'moved_bikes', 'moved_scooters'])
            writer.writerows(reports)


    def generate_and_save(self, filename='../generated_data/reports.csv'):
        routes = self.generate()
        self.write_to_csv(routes, filename)
        print(f"Generated {self.n} reports and wrote to '{filename}'")


if __name__ == "__main__":
    ReportGenerator(n=100).generate_and_save(filename='../generated_data/reports2.csv')
