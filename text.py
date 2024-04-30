import pandas as pd

# Read the Excel file
df = pd.read_excel("interests.xlsx")


df.to_csv("interests.csv", index=False)

