import random
from datetime import datetime, timedelta


class DateGenerator:
    def __init__(self):
        self.date_format = str("%d-%m-%Y")


    def set_date_format(self, new_format: str):
        self.date_format = new_format


    def generate(self, n: int, start_date: str, end_date: str) -> str:

        start = datetime.strptime(start_date, self.date_format)
        end = datetime.strptime(end_date, self.date_format)

        date_range = (end - start).days

        random_dates = [
        (start + timedelta(days=random.randint(0, date_range))).strftime(self.date_format)
        for _ in range(n)
        ]

        return random_dates[0] if n==1 else random_dates


if __name__ == "__main__":
    start_date = "01-01-2000"
    end_date = "01-01-2022"
    a = DateGenerator().generate(n=1000, start_date=start_date, end_date=end_date)
    print(a)