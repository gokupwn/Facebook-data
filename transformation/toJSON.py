import pandas as pd

df = pdf.read_csv('Lebanon.csv',low_memory=False)
df.to_json('Lebanon.json.gz',compression='gzip')

