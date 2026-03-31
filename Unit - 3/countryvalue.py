import pandas as pd


Second_sheet = pd.read_excel('movies.xlsx', sheet_name='2000s')


Second_sheet['Avg Reviews'] = (Second_sheet['Reviews by Users'] + Second_sheet['Reviews by Critics']) / 2


sorted_data = Second_sheet.sort_values(by=['Country', 'Avg Reviews'], ascending=[True, False])


print(sorted_data.head())
