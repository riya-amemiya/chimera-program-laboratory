import pandas as pd
df = pd.read_csv('./score.csv')
x = df[["name", "count"]]
t = df[["averageTime", "totalTime"]]
