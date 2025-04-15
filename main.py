# Rachel Pinkney, Karlie Ward, Sabrina Wong, Spencer Bigelow, Mason Zarges, Gavin Smith
# GROUP PROJECT WOHOOOO!! :)

import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plot

#optional to use
import openpyxl
from sqlalchemy sql import text
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

