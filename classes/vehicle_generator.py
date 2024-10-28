import random
import csv

try:
    from .date_generator import DateGenerator
    from .parameters import parameters
except ImportError:
    from date_generator import DateGenerator
    from parameters import parameters


class VehiclesGenerator:
    def __init__(self, num_vehicles=100,
                 start_date=parameters.VEHICLE_START_DATE, 
                 end_date=parameters.VEHICLE_END_DATE,
                 start_index=1):
        
        self.num_vehicles = num_vehicles
        self.start_date = start_date
        self.end_date = end_date
        self.vehicle_types = parameters.VEHICLE_TYPES
        self.engine_power_min = parameters.VEHICLE_ENGINE_POWER_MIN
        self.engine_power_max = parameters.VEHICLE_ENGINE_POWER_MAX
        self.battery_capacity_min = parameters.VEHICLE_BATTERY_CAPACITY_MIN
        self.battery_capacity_max = parameters.VEHICLE_BATTERY_CAPACITY_MAX
        self.in_use_weights = parameters.VEHICLE_IN_USE_WEIGHTS
        self.column_names = parameters.VEHICLE_COLUMN_NAMES
        self.start_index = start_index


    def generate_id(self, index):
        return index + self.start_index

    def generate_vehicle_type(self):
        return random.choice(self.vehicle_types)

    def generate_electrical(self, vehicle_type):
        if vehicle_type == "bicycle":
            return random.choices([1, 0], weights=[80, 20])[0]
        return random.choices([1, 0], weights=[90, 10])[0]

    def generate_purchase_date(self):
        random_date = DateGenerator().generate(1, self.start_date, self.end_date)
        return random_date

    def generate_engine_power(self, electrical):
        return random.randint(self.engine_power_min, self.engine_power_max) if electrical else 0

    def generate_battery_capacity(self, electrical):
        return random.randint(self.battery_capacity_min, self.battery_capacity_max) if electrical else 0

    def generate_in_use(self):
        return random.choices([1, 0], weights=self.in_use_weights)[0]

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
                (vehicle_id, vehicle_type, electrical, purchase_date, engine_power, in_use, battery_capacity))

        return vehicles

    def write_to_csv(self, vehicles, filename='../generated_data/vehicles_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=parameters.CSV_DELIMETER)
            writer.writerow(self.column_names)
            writer.writerows(vehicles)

    def generate_and_save(self, filename='../generated_data/vehicles_data.csv'):
        vehicles = self.generate_vehicle_data()
        self.write_to_csv(vehicles, filename)
        print(f"Generated {self.num_vehicles} vehicles and wrote to '{filename}'")


if __name__ == "__main__":
    VehiclesGenerator(num_vehicles=100, start_date="01-01-2018", end_date="31-12-2022").generate_and_save('../generated_data/vehicles_data.csv')
