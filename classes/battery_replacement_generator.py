import csv
import random
import os


class BatteryReplacementGenerator:
    def __init__(self, van_routes_csv='../generated_data/van_routes_data.csv',
                 vehicles_csv='../generated_data/vehicles_data.csv',
                 num_replacements=100,
                 start_index=1):
        self.num_replacements = num_replacements

        self.van_routes = self.load_csv_ids(van_routes_csv, 'route_id')
        self.vehicles = self.load_csv_ids(vehicles_csv, 'vehicle_id')
        self.start_index = start_index

    def load_csv_ids(self, filename, id_column):
        ids = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                ids = [row[id_column] for row in reader]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        return ids

    def generate_replacement_id(self, index):
        return index + self.start_index

    def generate_van_route_fk(self):
        return random.choice(self.van_routes)

    def generate_vehicle_fk(self):
        return random.choice(self.vehicles)

    def generate_battery_replacements_data(self):
        replacements = []

        for i in range(self.num_replacements):
            replacement_id = self.generate_replacement_id(i)
            van_route_fk = self.generate_van_route_fk()
            vehicle_fk = self.generate_vehicle_fk()

            replacements.append((replacement_id, van_route_fk, vehicle_fk))

        return replacements

    def write_to_csv(self, replacements, filename='../generated_data/battery_replacements_data.csv'):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['replacement_id', 'van_route_fk', 'vehicle_fk'])
            writer.writerows(replacements)

    def generate_and_save(self, filename='../generated_data/battery_replacements_data.csv'):
        replacements = self.generate_battery_replacements_data()
        self.write_to_csv(replacements, filename)
        print(f"Generated {self.num_replacements} battery replacements and wrote to '{filename}'")


if __name__ == "__main__":
    (BatteryReplacementGenerator(num_replacements=100)
     .generate_and_save('../generated_data/battery_replacements_data.csv'))
