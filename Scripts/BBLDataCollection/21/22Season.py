import json
import pandas as pd
import glob
import os

files = glob.glob(r"D:\UniWork\SP52025\MathCom\2025-BBL-Championship-Predictor\Data\RawData\bbl_json\*.json")

records = []

for idx, file in enumerate(files, start=1):
    with open(file, "r") as f:
        data = json.load(f) # Load the JSON file
        info = data["info"]

        record = {
            "id_num":idx,                               # To increment the id automatically
            "id_file": os.path.basename(file).replace(".json",""), # file-based id
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
print(df.head()) # To test the code
