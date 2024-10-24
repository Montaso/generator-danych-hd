import pandas as pd
import requests
from io import StringIO


class NameDownloader:
    def __init__(self):
        self.male_name_link = "https://api.dane.gov.pl/resources/54109,lista-imion-meskich-w-rejestrze-pesel-stan-na-19012023-imie-pierwsze/csv"
        self.female_name_link = "https://api.dane.gov.pl/resources/54110,lista-imion-zenskich-w-rejestrze-pesel-stan-na-19012024-imie-pierwsze/csv"
        self.name_number_threshold = 50
    
    def get_names(self):

        response_male = requests.get(self.male_name_link, verify=False)
        csv_data_male = StringIO(response_male.text)
        data_male = pd.read_csv(csv_data_male)

        # obciecie malo popularnych imion
        data_male = data_male[data_male.iloc[:, 2] > self.name_number_threshold]
        data_male = data_male["IMIĘ_PIERWSZE"]


        response_female = requests.get(self.female_name_link, verify=False)
        csv_data_female = StringIO(response_female.text)
        data_female = pd.read_csv(csv_data_female)

        # obciecie malo popularnych imion
        data_female = data_female[data_female.iloc[:, 2] > self.name_number_threshold]
        data_female = data_female["IMIĘ_PIERWSZE"]
        


        data_all = pd.concat([data_male, data_female], ignore_index=True)
        return data_all
    

a = NameDownloader()
a.get_names()

b = 1