import csv
import random

# Define the headers for the CSV file
headers = ['name', 'age', 'sex', 'height']

# Generate random data for each row
data = []
for i in range(100):
    name = f'Person {i+1}'
    age = random.randint(18, 65)
    sex = random.choice(['Male', 'Female'])
    height = round(random.uniform(1.5, 2.0), 2)  # in meters
    row = [name, age, sex, height]
    data.append(row)

# Write the data to a CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)