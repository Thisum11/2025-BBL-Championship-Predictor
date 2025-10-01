import pandas as pd

df = pd.read_csv(r"D:\UniWork\SP52025\MathCom\2025-BBL-Championship-Predictor\Data\ProcessedData\BBLDataCollection_Clean.csv")

#Listing out all the teams
teams = sorted(set(df["team1"]).union(df["team2"]).union(df["match_winner"]))

# Mapping out all the teams in Team1 column
team_map = {team: index for index, team in enumerate(teams)}

# Applying the mapping to other columns with team names and adding the encoded columns to the csv
for col in ["team1", "team2", "toss_winner", "match_winner"]:
    df[col + "_Encoded"] = df[col].map(team_map)

toss_result = df["toss_decision"]
toss_decision_map = {'bat':1, 'field': 0} # Binary mapping the toss results
# Adding the encoded toss decision column
df[col + "_Encoded"] = df["toss_decision"].map(toss_decision_map)

print(team_map)   # To check the team mapping
print(toss_decision_map)
print(df.head()) # To check new encoded columns





