import numpy as np
import pandas as pd
import glob
import time

files = glob.glob('caged*.csv')
# Usando map:
df_total = pd.concat(map(lambda file: pd.read_csv(file, skiprows=5), files), ignore_index=True)
print(df_total)

df_total.to_csv("geral_caged.csv", index=False)
print("junção dos arquivos Concluída!")

