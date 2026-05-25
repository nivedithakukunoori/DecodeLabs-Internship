import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("StudentsPerformance.csv")

data["gender"].value_counts().plot(kind="bar")

plt.title("Gender Count")

plt.show()