# Rachel Pinkney, Karlie Ward, Sabrina Wong, Spencer Bigelow, Mason Zarges, Gavin Smith
# GROUP PROJECT WOHOOOO!! :)

import sqlalchemy 
import pandas as pd
import matplotlib.pyplot as plot


#optional to use
import openpyxl
from sqlalchemy import create_engine, text
import psycopg2

df = pd.read_excel('Retail_Sales_Data.xlsx')

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





