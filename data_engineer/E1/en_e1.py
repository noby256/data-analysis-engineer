import pandas as pd
from sql_handler import SqlHandler
import os


script_path = os.getcwd()
data = pd.read_csv(script_path + '/eurofxref-hist.csv')

columns = [col + ' numeric' for col in data.columns[1:4]]
columns = ',\n'.join(columns)

print(columns)
# data = pd.read_csv(script_path + '/eurofxref-hist.csv')
# print(data.head(5))

sql = SqlHandler()
# sql.drop_table()
# sql.create_table(columns)
sql.copy_csv_into_table(data)

