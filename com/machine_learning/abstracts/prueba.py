import pandas as pd
import numpy as np

df = pd.DataFrame([{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}])

print(df)

for index, row in df.iterrows():
    print(row['c1'], row['c2'])
