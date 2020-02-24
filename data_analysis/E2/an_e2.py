import pandas as pd
import os


script_path = os.getcwd()
resolved_path = os.path.join(script_path, '../E1/Movie_Movies.csv')

df = pd.read_csv(resolved_path, low_memory=False)
print(df.groupby('Director').Director.count().sort_values(ascending=False).head(10))

