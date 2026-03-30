import pandas as pd

data = {
    'Name': ['Ankit', 'Rahul', 'Priya'],
    'Course1': [85, 78, 92],
    'Course2': [88, 74, 90],
    'Course3': [90, 80, 95]
}

df = pd.DataFrame(data)

df['Mean'] = df[['Course1', 'Course2', 'Course3']].mean(axis=1)

print(df)