import pandas as pd


Second_sheet = pd.read_excel("movies.xlsx", sheet_name="2000s")



USA50 = Second_sheet[(Second_sheet['Country'] == 'USA') & (Second_sheet['Duration'] < 50)]


print(USA50)
