import random
import csv
import string


class VansGenerator:
    LICENSE_PLATE_PREFIXES = ["GD", "KR", "WA", "PO", "LU", "BI", "CZ", "TK"]
    CAPACITY_RANGE_CM3 = (5_000_000, 20_000_000)

    def __init__(self, num_vans=100):
        self.num_vans = num_vans
        self.generated_plates = set()

    def generate_license_plate(self):
        while True:
            prefix = random.choice(self.LICENSE_PLATE_PREFIXES)
            first_part = ''.join(random.choices(string.digits, k=2))
            second_part = ''.join(random.choices(string.digits + string.ascii_uppercase, k=3))  # Three characters mix
            plate_number = f"{prefix}{first_part}{second_part}"
            if plate_number not in self.generated_plates:
                self.generated_plates.add(plate_number)
                return plate_number

    def generate_van_data(self):
        vans = []

        for _ in range(self.num_vans):
            license_plate = self.generate_license_plate()
            capacity_cm3 = random.randint(*self.CAPACITY_RANGE_CM3)

            in_use = random.choices([True, False], weights=[90, 10])[0]

            vans.append((license_plate, capacity_cm3, in_use))

        return vans

    def write_to_csv(self, vans, filename='../generated_data/vans_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['License_Plate', 'Capacity', 'In_Use'])
            writer.writerows(vans)

    def generate_and_save(self, filename='../generated_data/vans_data.csv'):
        vans = self.generate_van_data()
        self.write_to_csv(vans, filename)
        print(f"Generated {self.num_vans} vans and wrote to '{filename}'")


if __name__ == "__main__":
    VansGenerator().generate_and_save()