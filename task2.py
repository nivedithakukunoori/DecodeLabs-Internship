import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")

print(data.isnull().sum())

data = data.drop_duplicates()

print("Duplicates Removed")

print(data.shape)