import pandas as pd


Second_sheet = pd.read_excel("movies.xlsx", sheet_name="2000s")


Second_sheet['Avg Reviews'] = (Second_sheet['Reviews by Users'] + Second_sheet['Reviews by Critics']) / 2


print(Second_sheet.head())
