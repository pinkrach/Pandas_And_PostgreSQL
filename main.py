# Rachel Pinkney, Karlie Ward, Sabrina Wong, Spencer Bigelow, Mason Zarges, Gavin Smith
# GROUP PROJECT WOHOOOO!! :)

import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plot

#optional to use
import openpyxl
from sqlalchemy import text
import psycopg2

df = pd.read_excel('Retail_Sales_Data.xlsx')

print("If you want to import data, enter 1." "If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: ")