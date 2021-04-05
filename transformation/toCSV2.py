import pandas as pd

df = pd.read_csv('Leaked.csv',low_memory=False,skiprows=1)
df.to_csv('Leaked.csv')
