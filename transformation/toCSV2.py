import pandas as pd

df = pd.read_csv('Lebanon.csv',low_memory=False,skiprows=1)
df.to_csv('Lebanon.csv')
