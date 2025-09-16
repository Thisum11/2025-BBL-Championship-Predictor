import json
import pandas as pd
import glob

files = glob.glob(r"D:\UniWork\SP52025\MathCom\2025-BBL-Championship-Predictor\Data\RawData\21-22\*.json")

records = []

for file in files:
    with open(file, "r") as f:
        data = json.load(f) # Load the JSON file
        info = data["info"]

        record = {
            "date":info["dates"][0],                    # Date
            "venue":info.get("venue"),                  # Venue
            "team1": info["teams"][0],                  # Home Team
            "team2": info["teams"][1],                  # Away Team
            "toss_winner": info["toss"]["winner"],      # Toss winner
            "toss_decision": info["toss"]["decision"],  # Toss Decision
            "match_winner": info["outcome"].get("winner", None) # Match Winner
        }

        records.append(record)

df = pd.DataFrame(records)
df.to_csv("BBLDataCollection.csv", index=False)
print(df.head())
