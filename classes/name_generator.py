import pandas as pd
import requests
from io import StringIO
import numpy as np


class NameGenerator:
    def __init__(self):
        self.male_name_api = "https://api.dane.gov.pl/resources/54109,lista-imion-meskich-w-rejestrze-pesel-stan-na-19012023-imie-pierwsze/csv"
        self.female_name_api = "https://api.dane.gov.pl/resources/54110,lista-imion-zenskich-w-rejestrze-pesel-stan-na-19012024-imie-pierwsze/csv"
        self.name_number_threshold = 10000

        self.male_surname_api = "https://api.dane.gov.pl/resources/54097,nazwiska-meskie-stan-na-2024-01-19/csv"
        self.female_surname_api = "https://api.dane.gov.pl/resources/54098,nazwiska-zenskie-stan-na-2024-01-19/csv"
        self.surname_number_threshold = 500
    

    def get_names(self):

        response_male = requests.get(self.male_name_api)
        csv_data_male = StringIO(response_male.text)
        data_male = pd.read_csv(csv_data_male)

        response_female = requests.get(self.female_name_api)
        csv_data_female = StringIO(response_female.text)
        data_female = pd.read_csv(csv_data_female)

        # obciecie malo popularnych imion
        data_female = data_female[data_female.iloc[:, 2] > self.name_number_threshold]
        data_male = data_male[data_male.iloc[:, 2] > self.name_number_threshold]
        
        # usuniecie reszty kolumn
        data_male = data_male["IMIĘ_PIERWSZE"]
        data_female = data_female["IMIĘ_PIERWSZE"]
        
        return [data_male, data_female]
    

    def get_surnames(self):
        response_male = requests.get(self.male_surname_api)
        csv_data_male = StringIO(response_male.text)
        data_male = pd.read_csv(csv_data_male)

        response_female = requests.get(self.female_surname_api)
        csv_data_female = StringIO(response_female.text)
        data_female = pd.read_csv(csv_data_female)

        # obciecie malo popularnych nazwisk
        data_female = data_female[data_female.iloc[:, 1] > self.surname_number_threshold]
        data_male = data_male[data_male.iloc[:, 1] > self.surname_number_threshold]
        
        # usuniecie reszty kolumn
        data_male = data_male["Nazwisko aktualne"]
        data_female = data_female["Nazwisko aktualne"]
        
        return [data_male, data_female]


    def generate(self, quantity=100):
        names = self.get_names()
        surnames = self.get_surnames()

        male_names = np.array(names[0])
        female_names = np.array(names[1])

        male_surnames = np.array(surnames[0])
        female_surnames = np.array(surnames[1])

        male_nmb = np.random.randint(int(quantity * 0.4), int(quantity * 0.6 + 1))

        random_names_male = np.random.choice(male_names, size=male_nmb, replace=True)
        random_surnames_male = np.random.choice(male_surnames, size=male_nmb, replace=True)
        random_males = np.array([random_names_male, random_surnames_male])

        random_names_female = np.random.choice(female_names, size=quantity-male_nmb, replace=True)
        random_surnames_female = np.random.choice(female_surnames, size=quantity-male_nmb, replace=True)
        random_females = np.array([random_names_female, random_surnames_female])

        randoms = np.concatenate((random_males, random_females), axis=1)

        tuples = list(zip(randoms[0], randoms[1]))
        np.random.shuffle(tuples)

        # randoms = randoms.astype(str)
        # combined = np.char.add(np.char.add(randoms[0, :], ' '), randoms[1, :])

        return tuples



if __name__ == "__main__":
    a = NameGenerator().generate(quantity=50)
    print(a)
