import pandas as pd

df = pd.read_csv('Leaked.txt',low_memory=False)
df.to_csv('Leaked.csv.gz',sep=',',compression='gzip')
