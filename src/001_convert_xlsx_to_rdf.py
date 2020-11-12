import pandas as pd
import numpy as np
import math
import sys
import argparse
import json
import urllib.parse

path = "data/year_jw.xlsx"

df = pd.read_excel(path, sheet_name=0, header=None, index_col=None)

r_count = len(df.index)
c_count = len(df.columns)

map = {}

for j in range(321, 600):

    year = df.iloc[j,0]

    if pd.isnull(year):
        year = df.iloc[j-1, 0]

    wareki = df.iloc[j,1]

    yomi = str(df.iloc[j,2]).replace("(", "",).replace(")", "")

    uru = df.iloc[j,4]

    print(year, uru)

    if year not in map:
        map[year] = {
            "wareki" : []
        }

    if not pd.isnull(uru):
        map[year]["uru"] = uru

    map[year]["wareki"].append(wareki)

with open("../assets/json/year_jw.json", 'w') as outfile:
    json.dump(map, outfile, ensure_ascii=False,
                indent=4, sort_keys=True, separators=(',', ': '))
