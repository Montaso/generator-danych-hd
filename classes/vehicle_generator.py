import random
import csv

try:
    from .date_generator import DateGenerator
except ImportError:
    from date_generator import DateGenerator


class VehiclesGenerator:
    def __init__(self, num_vehicles=100, start_date="01-01-2018", end_date="31-12-2022"):
        self.num_vehicles = num_vehicles
        self.start_date = start_date
        self.end_date = end_date

    def generate_id(self, index):
        return index + 1

    def generate_vehicle_type(self):
        return random.choice(["bicycle", "scooter"])

    def generate_electrical(self, vehicle_type):
        if vehicle_type == "bicycle":
            return random.choices([True, False], weights=[80, 20])[0]
        return random.choices([True, False], weights=[90, 10])[0]

    def generate_purchase_date(self):
        random_date = DateGenerator().generate(1, self.start_date, self.end_date)[0]
        return random_date

    def generate_engine_power(self, electrical):
        return random.randint(250, 1500) if electrical else 0

    def generate_battery_capacity(self, electrical):
        return random.randint(500, 1000) if electrical else 0

    def generate_in_use(self):
        return random.choices([True, False], weights=[95, 5])[0]

    def generate_vehicle_data(self):
        vehicles = []

        for i in range(self.num_vehicles):
            vehicle_id = self.generate_id(i)
            vehicle_type = self.generate_vehicle_type()
            electrical = self.generate_electrical(vehicle_type)
            purchase_date = self.generate_purchase_date()
            engine_power = self.generate_engine_power(electrical)
            battery_capacity = self.generate_battery_capacity(electrical)
            in_use = self.generate_in_use()
            vehicles.append(
                (vehicle_id, vehicle_type, electrical, purchase_date, engine_power, battery_capacity, in_use))

        return vehicles

    def write_to_csv(self, vehicles, filename='../generated_data/vehicles_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['vehicle_id', 'type', 'electrical', 'purchase_date', 'engine_power', 'battery_capacity',
                             'in_use'])
            writer.writerows(vehicles)

    def generate_and_save(self, filename='../generated_data/vehicles_data.csv'):
        vehicles = self.generate_vehicle_data()
        self.write_to_csv(vehicles, filename)
        print(f"Generated {self.num_vehicles} vehicles and wrote to '{filename}'")


if __name__ == "__main__":
    VehiclesGenerator(num_vehicles=100, start_date="01-01-2018", end_date="31-12-2022").generate_and_save('../generated_data/vehicles_data.csv')
