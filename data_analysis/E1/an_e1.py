import pandas as pd
import os

script_path = os.getcwd()
# making data frame from csv file  
print(script_path + '/Movie_Movies.csv')
data = pd.read_csv(script_path + '/Movie_Movies.csv')

print(data.head(10))
#
