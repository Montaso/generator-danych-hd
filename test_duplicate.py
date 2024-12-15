import csv


# Function to check for duplicates using a set
def check_duplicates(file_path):
    seen_pesels = set()  # Set to store unique PESEL values
    duplicates = []  # List to store rows with duplicates

    # Open the CSV file and read the data
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')

        for row in reader:
            pesel = row['Pesel']

            # If the PESEL is already in the set, it's a duplicate
            if pesel in seen_pesels:
                duplicates.append(row)  # Add the duplicate row to the list
            else:
                seen_pesels.add(pesel)  # Add PESEL to the set if it's not seen before

    return seen_pesels


# Main function to run the script
def main():
    # Path to your CSV file
    file_path = 'C:\\Users\\Adrian\\Desktop\\Studia\\sem 5\\HD\\generator-danych-hd\\generated_data\\users12.csv'  # Replace with the actual path of your CSV file

    # Check for duplicates
    duplicates = check_duplicates(file_path)

    # Print the results
    print(len(duplicates))


if __name__ == '__main__':
    main()


