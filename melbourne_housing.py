import pandas as pd
# This code reads a dataset containing Melbourne housing data and prints a summary of the data.
from datetime import datetime


iowa_file_path = './datasets/train_housing.csv'
# read the data and store data in DataFrame titled home_data
home_data = pd.read_csv(iowa_file_path)
# print a summary of the data in home_data
print(home_data.describe())



# What is the average lot size (rounded to nearest integer)?
avg_lot_size = home_data['LotArea'].mean().round()
print(f"Average Lot Size: {avg_lot_size} square feet")
# As of today, how old is the newest home (current year - the date in which it was built)

newest_home_age = home_data['YearBuilt'].max()
current_year = datetime.now().year
print(f"Newest Home Age: {current_year - newest_home_age} years")




# save filepath to variable for easier access
melbourne_file_path = './datasets/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
#print(melbourne_data.describe())
# Print the columns of the Melbourne data
print(melbourne_data.columns)

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
