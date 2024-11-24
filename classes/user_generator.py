try:
    from .name_generator import NameGenerator
    from .date_generator import DateGenerator
    from .parameters import parameters
except ImportError:
    from date_generator import DateGenerator
    from name_generator import NameGenerator
    from parameters import parameters
import csv
from datetime import datetime
import time
import random

class UserGenerator:
    def __init__(self, n=100, start_index=1):
        self.n = n

        self.name_generator = NameGenerator()
        self.date_generator = DateGenerator()
        self.start_index = start_index
        
        self.birthdate_start = parameters.USER_BIRTHDATE_START
        self.birthdate_end = parameters.USER_BIRTHDATE_END
        self.date_format = parameters.DATE_FORMAT

        self.registration_date_start = parameters.USER_REGISTRATION_DATE_START
        self.registration_date_end = parameters.USER_REGISTRATION_DATE_END

        self.csv_delimeter = parameters.CSV_DELIMETER
        self.column_names = parameters.USER_COLUMN_NAMES

    def _generate_pesel(self):
        random_date = self.date_generator.generate(n=1, start_date=self.birthdate_start, end_date=self.birthdate_end)
        date_part = datetime.strptime(random_date, self.date_format).strftime('%y%m%d')

        sequence_number = f"{random.randint(0, 9999):04d}"

        pesel_without_checksum = date_part + sequence_number

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(pesel_without_checksum[i]) * weights[i] for i in range(10)) % 10
        checksum = (10 - checksum) % 10

        pesel = pesel_without_checksum + str(checksum)

        return pesel

    def generate(self):
        users = []

        ids = [i + self.start_index for i in range(self.n)]
        names = self.name_generator.generate(quantity=self.n)
        birthdates = self.date_generator.generate(n=self.n, start_date=self.birthdate_start, end_date=self.birthdate_end)
        unique_pesels = set()
        
        registration_dates = []
        for i, date in enumerate(birthdates):
            date1 = datetime.strptime(date, self.date_generator.date_format)
            date2 = datetime.strptime(self.registration_date_start, self.date_generator.date_format)
            registration_dates.append(self.date_generator.generate(n=1, start_date=date if date1 > date2 else self.registration_date_start, end_date=self.registration_date_end))

            pesel = self._generate_pesel()
            while pesel in unique_pesels:
                pesel = self._generate_pesel()
            unique_pesels.add(pesel)

            user = {
                "id": ids[i],
                "name": names[i][0],
                "surname": names[i][1],
                "birthdate": birthdates[i],
                "registration_date": registration_dates[i],
                "pesel": pesel
            }

            users.append(user)

        return users

    def _write_to_csv(self, users, filename='../generated_data/users.csv'):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=self.csv_delimeter)
            writer.writerow(self.column_names)

            for user in users:
                writer.writerow([
                    user['id'],
                    user['name'],
                    user['surname'],
                    user['birthdate'],
                    user['registration_date'],
                    user['pesel']
            ])

    def generate_and_save(self, filename='../generated_data/users.csv'):
        users = self.generate()
        self._write_to_csv(users, filename)
        print("generated users data")


if __name__ == "__main__":
    start_time = time.time()
    UserGenerator(n=100).generate_and_save()
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Executed script in: {elapsed_time:.6f} seconds")