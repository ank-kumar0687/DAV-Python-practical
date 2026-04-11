import pandas as pd


data = {
    'col1': [1,2,3,4,5,6,7,8,9,10],
    'col2': [11,12,13,14,15,16,17,18,19,20]
}


df = pd.DataFrame(data, index=['a','b','c','d','e','f','g','h','i','j'])

print(df)
