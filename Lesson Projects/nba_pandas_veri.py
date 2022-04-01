import pandas as pd
import numpy as np

file = pd.read_csv("Players.csv")

result = file.head(10)

result = len(file)

result = file["height"].mean()

result = file["height"].max()

result = file.iloc[file["height"].argmax()]["Player"]
print(result)

result = file.query("height >= 190 & height <= 195")[["Player","collage"]]

file = file.fillna("")
result = file[file["Player"].str.contains("Cliff Barker")]["collage"]
print(result)

result = file.groupby("height").mean()["height"]

result = len(file["collage"])
# result = file["collage"].nunique() # üstteki satırın alternatifi

result = file["collage"].value_counts()


result = file["Player"].str.contains("and")
print(file[result]["Player"])