# Rachel Pinkney, Karlie Ward, Sabrina Wong, Spencer Bigelow, Mason Zarges, Gavin Smith
# GROUP PROJECT WOHOOOO!! :)

import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plot

#optional to use
import openpyxl
from sqlalchemy import text, create_engine
import psycopg2

#Create the file_path variable
file_path = "Retail_Sales_Data.xlsx"

#use pandas to read the ecxel file
df = pd.read_excel(file_path)

# Step 2: Split the 'name' column into 'first_name' and 'last_name'
dfSeparatedNames = df["name"].str.split("_", expand=True)
df.insert(0, "first_name", dfSeparatedNames[0])
df.insert(1, "last_name", dfSeparatedNames[1])
del df["name"]

# Step 3: Fix the 'category' column using the provided dictionary
productCategoriesDict = {
    'Camera': 'Technology',
    'Laptop': 'Technology',
    'Gloves': 'Apparel',
    'Smartphone': 'Technology',
    'Watch': 'Accessories',
    'Backpack': 'Accessories',
    'Water Bottle': 'Household Items',
    'T-shirt': 'Apparel',
    'Notebook': 'Stationery',
    'Sneakers': 'Apparel',
    'Dress': 'Apparel',
    'Scarf': 'Apparel',
    'Pen': 'Stationery',
    'Jeans': 'Apparel',
    'Desk Lamp': 'Household Items',
    'Umbrella': 'Accessories',
    'Sunglasses': 'Accessories',
    'Hat': 'Apparel',
    'Headphones': 'Technology',
    'Charger': 'Technology'
}

df["category"] = df["product"].map(productCategoriesDict)

username = 'postgres'
password = ""
host = 'localhost'
port = '5432'
database = 'is303'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

df.to_sql("sale", engine, if_exists = 'replace', index = False)

# Step 5: Confirmation message
print("You've imported the excel file into your postgres database.")
