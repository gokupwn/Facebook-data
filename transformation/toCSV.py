import pandas as pd

df = pd.read_csv('Lebanon.txt',low_memory=False)
df.to_csv('Lebanon.csv.gz',sep=',',compression='gzip')