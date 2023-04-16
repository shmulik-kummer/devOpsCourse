# Testing agify API - Create a program in python that generates 3 random names and
# checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
# between 0 - 120

import requests
from faker import Faker

# initialize faker
fake = Faker()

# Generate three random names
names = [fake.unique.first_name() for _ in range(3)]

# query Agify API for each name and check age
for name in names:
    response = requests.get(f"https://api.agify.io/?name={name}")
    if response.status_code == 200:
        age = response.json().get("age")
        if age is not None and 0 <= age <= 120:
            print(f"{name.capitalize()} is {age} years old.")
        else:
            print(f"Error: {name.capitalize()}'s age must be between 1-120.")
    else:
        print(f"Error: Could not get age for {name.capitalize()} from Agify API.")
