import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")

print(data.head())

print(data.columns)

print(data.shape)

print(data.info())