try:
    from .name_generator import NameGenerator
    from .date_generator import DateGenerator
    from .parameters import parameters
except ImportError:
    from name_generator import NameGenerator
    from date_generator import DateGenerator
    from parameters import parameters

import random
from datetime import datetime
import csv


class DriverGenerator:
    def __init__(self, n=100):
        self.n = n

        self.name_generator = NameGenerator()
        self.date_generator = DateGenerator()

        self.pesel_date_start = parameters.DRIVER_PESEL_DATE_START
        self.pesel_date_end = parameters.DRIVER_PESEL_DATE_END

        self.employment_date_start = parameters.DRIVER_EMPLOYMENT_DATE_START
        self.employment_date_end = parameters.DRIVER_EMPLOYMENT_DATE_END

        self.date_format = parameters.DATE_FORMAT

        self.csv_delimeter = parameters.CSV_DELIMETER

        self.still_working_ratio = parameters.DRIVER_STILL_WORKING_RATIO
        self.column_names = parameters.DRIVER_COLUMN_NAMES


    def generate_pesel(self):
        random_date = self.date_generator.generate(n=1, start_date=self.pesel_date_start, end_date=self.pesel_date_end)
        date_part = datetime.strptime(random_date, self.date_format).strftime('%y%m%d')
        
        
        sequence_number = f"{random.randint(0, 9999):04d}"
        
        pesel_without_checksum = date_part + sequence_number

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(pesel_without_checksum[i]) * weights[i] for i in range(10)) % 10
        checksum = (10 - checksum) % 10
        
        pesel = pesel_without_checksum + str(checksum)
        
        return pesel


    def generate(self):
        drivers = []
        unique_pesels = set()

        names = self.name_generator.generate(quantity=self.n)
        employment_dates = self.date_generator.generate(n=self.n, start_date=self.employment_date_start, end_date=self.employment_date_end)

        for i in range(self.n):
            # nie powtarzajace sie pesele
            pesel = self.generate_pesel()
            while pesel in unique_pesels:
                pesel = self.generate_pesel()

            unique_pesels.add(pesel)

            driver = {
                "pesel": pesel,
                "name": names[i][0],
                "surname": names[i][1],
                "employment_date": employment_dates[i],
                "still_working": 1 if random.random() < self.still_working_ratio else 0
            }

            drivers.append(driver)
        
        return drivers


    def _write_to_csv(self, drivers, filename='../generated_data/users.csv'):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=self.csv_delimeter)
            writer.writerow(self.column_names)

            for driver in drivers:
                writer.writerow([
                driver['pesel'],
                driver['name'],
                driver['surname'],
                driver['still_working'],
                driver['employment_date']
            ])
                

    def generate_and_save(self, filename='../generated_data/drivers.csv'):
        drivers = self.generate()
        self._write_to_csv(drivers, filename)
        print("generated drivers")


if __name__ == "__main__":
    DriverGenerator(n=1000).generate_and_save()