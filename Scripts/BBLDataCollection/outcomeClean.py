import pandas as pd

# To load the datasheet
df = pd.read_csv(r"D:\UniWork\SP52025\MathCom\2025-BBL-Championship-Predictor\Data\ProcessedData\BBLDataCollection.csv")

df = df.dropna(subset=["match_winner"]) # To drop all the rows which is missing the winner
print("After dropping:", df.shape) # Remaining number of rows and columns

# To remove all the unnecessary leading & trailing characters
df["team1"] = df["team1"].str.strip()
df["team2"] = df["team2"].str.strip()
df["toss_winner"] = df["toss_winner"].str.strip()
df["match_winner"] = df["match_winner"].str.strip()

# To convert all the Team names into one format. (First letter capital)
df["team1"] = df["team1"].str.title()
df["team2"] = df["team2"].str.title()
df["toss_winner"] = df["toss_winner"].str.title()
df["match_winner"] = df["match_winner"].str.title()

# To check the above conversions
""" 
print(df["team1"].unique())
print(df["team2"].unique())
print(df["toss_winner"].unique())
print(df["match_winner"].unique())
"""

#  print(df["toss_decision"].unique())
# -- Just to clarify the toss decisions incase if it written bowl it needs to be converted into field

# To convert the dates into actual date Objects
df["date"] = pd.to_datetime(df["date"], dayfirst =True, errors="coerce")

# To create a new CSV file
df.to_csv("BBLDataCollection_Clean.csv", index=False)



