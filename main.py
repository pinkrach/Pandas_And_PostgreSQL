
# Rachel Pinkney, Karlie Ward, Sabrina Wong, Spencer Bigelow, Mason Zarges, Gavin Smith
# GROUP PROJECT WOHOOOO!! :)

import sqlalchemy 
import pandas as pd
import matplotlib.pyplot as plot

#optional to use
import openpyxl
from sqlalchemy import create_engine, text
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


userNumber = input("If you want to import data, enter 1." "If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: ")

if userNumber == 1:
    #do this
    print("Hi")

elif userNumber == 2:
    print("The following are all the categories that have been sold:")

#  conn = psycopg2.connect(username = 'postgres',
#     password = 'Soccer360',
#     host = 'localhost',
#     port = '5432',
#     database = 'is303')

#     engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

#     import psycopg2

# cur_food_essentials = conn.cursor()

# cur_food_essentials.execute("select * from candy;")

# print(cur_food_essentials.fetchone())

dfImported = pd.re_sql("select * from sales;", conn)


shopping_categories = {
    1: "Groceries",
    2: "Clothing",
    3: "Electronics",
    4: "Home & Kitchen",
    5: "Books",
    6: "Toys & Games",
    7: "Beauty & Personal Care",
    8: "Sports & Outdoors",
    9: "Automotive",
    10: "Health"
}

print("The following are all the categories that have been sold:")
print(shopping_categories)
userNumber = input("Please enter the number of the category you want to see summarized: ")

# query based on input

# calculate sums

# print sums
dfImported.query()
iColumnSum = dfImported[shopping_categories(userNumber)].sum()
iColumnAvg = dfImported[shopping_categories(userNumber)].mean()
iColumnQuantity = dfImported[shopping_categories(userNumber)].quantity()

