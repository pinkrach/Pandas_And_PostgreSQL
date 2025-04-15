# Rachel Pinkney, Karlie Ward, Sabrina Wong, Spencer Bigelow, Mason Zarges, Gavin Smith
# GROUP PROJECT WOHOOOO!! :)

# Assume you are given a sample of sale data from an online retailer in the form of an excel file. 
# The retailer wants your team to test how they could transfer their data into a postgres database and 
# read data programmatically back from the database. You’ll use Pandas to read the data in, to transfer it to postgres, 
# and to read it back from postgres to display a summary of different product categories.

# import libraries
import pandas as pd
import matplotlib.pyplot as plot

#optional to use
import openpyxl
from sqlalchemy import create_engine, text
import psycopg2

# connect to postgres/pgadmin
username = 'postgres'
password = "Soccer360"
host = 'localhost'
port = '5432'
database = 'is303'

# create engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

condition = True
while condition == True:
    # ask for input either 1 or 2 anything else exit
    userNum = int(input("\nIf you want to import data, enter 1.\nIf you want to see summaries of stored data, enter 2. \nEnter any other value to exit the program: "))
    
    # option 1
    if userNum == 1:
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

        df.to_sql("sale", engine, if_exists = 'replace', index = False)

        # Step 5: Confirmation message
        print("You've imported the excel file into your postgres database.")

    # option 2
    elif userNum == 2:
        
        # create a database from the sale table
        dfImported = pd.read_sql_query("select * from sale;", engine)
        # create a table from the sale table with distinct categories
        dfCategories = pd.read_sql_query("select distinct category from sale;", engine)
        
        # create a dictionary and assign each category a number that will be the key
        category_dict = {}
        category_dict = {i: category for i, category in enumerate(dfCategories['category'])}

        # print and ask for input
        print("The following are all the categories that have been sold:")
        print(dfCategories)
        userNumber = int(input("Please enter the number of the category you want to see summarized: "))
        
        # get the information about the category the user wants
        dfQuery = dfImported.query(f'category =="{category_dict[userNumber]}"')

        # find the sum, mean, and quantity sum form asked for category
        iColumnSum = format(dfQuery["total_price"].sum(),'.2f')
        iColumnAvg = round(dfQuery["total_price"].mean(), 2)
        iColumnQuantity = dfQuery["quantity_sold"].sum()

        # print out summary
        print(f"Total Sales for {category_dict[userNumber]}: {iColumnSum}")
        print(f"Average sale amount for {category_dict[userNumber]}: {iColumnAvg}")
        print(f"Total units sold for {category_dict[userNumber]}: {iColumnQuantity}")

        # Using group by on the product to get one row for each product,
        # and then calculating the sum of total prices for each of those products
        dfProductSales = dfQuery.groupby ('product') ['total_price'].sum()

        # creating the chart
        dfProductSales.plot(kind='bar') # creates the chart
        plot.title(f"Total Sales in {category_dict[userNumber]}") #adds title to the top of the chart 
        plot.xlabel("Product") # label for the x-axis 
        plot.ylabel("Total Sales") # label for the y-axis 
        plot.show() # makes the chart pop up on the screen

    # end the program if user inputs anything but 1 or 2
    else:
        print("Exiting Program")
        condition = False
