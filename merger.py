import pandas as pd

def merge(name):
    original_csv = pd.read_csv(f'generated_data/{name}.csv')
    append_csv = pd.read_csv(f'generated_data/{name}2.csv')

    combined_csv = pd.concat([original_csv, append_csv], ignore_index=True)
    combined_csv.to_csv(f'generated_data/{name}12.csv', index=False)

mode = "facts"

if mode != "facts":
    merge('drivers')
    merge('users')
    merge('stations_data')
    merge('vans_data')
    merge('vehicles_data')

else:
    merge('van_routes_data')
    merge('rentals_data')
    merge('battery_replacements_data')
