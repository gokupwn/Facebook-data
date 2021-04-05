import pandas as pd

df = pdf.read_csv('Leaked.csv',low_memory=False)
df.to_json('Leaked.json.gz',compression='gzip')

