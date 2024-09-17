import pandas as pd

data = [{'Apples': 35, 'Bananas': 21}, {'Apples': 41, 'Bananas': 34}]

df = pd.DataFrame(data, index =["2017 Sales", "2018 Sales"])

print(df)

df.to_csv('fruit.csv')