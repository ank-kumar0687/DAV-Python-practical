import pandas as pd


Second_sheet = pd.read_excel("movies.xlsx", sheet_name="2000s")  



print(len(Second_sheet))

