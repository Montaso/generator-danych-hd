try:
    from .parameters import parameters
except ImportError:
    from parameters import parameters

import random
import csv


class StationsGenerator:
    def __init__(self, num_stations=500, start_index=1):
        self.num_stations = num_stations
        self.latitude_range = parameters.STATION_LATITUDE_RANGE
        self.longitude_range = parameters.STATION_LONGITUDE_RANGE
        self.capacity_range = parameters.STATION_CAPACITY_RANGE
        self.column_names = parameters.STATION_COLUMN_NAMES
        self.start_index = start_index

    def generate_name(self, capacity, id):
        return f's{capacity}x{id}'
        
    def _generate_station_data(self):
        stations = []

        for i in range(self.num_stations):
            id = i + self.start_index
            latitude = round(random.uniform(*self.latitude_range), 6)
            longitude = round(random.uniform(*self.longitude_range), 6)
            capacity = random.randint(*self.capacity_range)
            in_use = random.choices([1, 0], weights=[90, 10])[0]
            name = self.generate_name(capacity, id)

            stations.append((id, longitude, latitude, in_use, capacity, name))

        return stations

    def _write_to_csv(self, stations, filename='../generated_data/stations_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=parameters.CSV_DELIMETER)
            writer.writerow(self.column_names)
            writer.writerows(stations)

    def generate_and_save(self, filename='../generated_data/stations_data.csv'):
        stations = self._generate_station_data()
        self._write_to_csv(stations, filename)
        print(f"Generated {self.num_stations} stations and wrote to '{filename}'")


if __name__ == "__main__":
    StationsGenerator().generate_and_save()
