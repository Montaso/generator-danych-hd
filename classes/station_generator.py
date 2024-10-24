import random
import csv


class StationsGenerator:

    LATITUDE_RANGE = (49.0, 54.8)
    LONGITUDE_RANGE = (14.1, 24.1)
    CAPACITY_RANGE = (5, 30)

    def __init__(self, num_stations=500):
        self.num_stations = num_stations

    def _generate_station_data(self):
        stations = []

        for i in range(self.num_stations):
            id = i + 1
            latitude = round(random.uniform(*self.LATITUDE_RANGE), 6)
            longitude = round(random.uniform(*self.LONGITUDE_RANGE), 6)
            capacity = random.randint(*self.CAPACITY_RANGE)
            in_use = random.choices([True, False], weights=[90, 10])[0]

            stations.append((id, longitude, latitude, capacity, in_use))

        return stations

    def _write_to_csv(self, stations, filename='../generated_data/stations_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Id', 'Longitude', 'Latitude', 'Capacity', 'In_Use'])
            writer.writerows(stations)

    def generate_and_save(self, filename='../generated_data/stations_data.csv'):
        stations = self._generate_station_data()
        self._write_to_csv(stations, filename)
        print(f"Generated {self.num_stations} stations and wrote to '{filename}'")


if __name__ == "__main__":
    StationsGenerator().generate_and_save()
