import pandas as pd
import os

# Caminho para o arquivo .txt
txt_file_path = "data\\measurements.txt"

# Caminho para salvar o arquivo .parquet
parquet_file_path = "data\\measurements.parquet"

# Leia o arquivo .txt em um DataFrame, especificando os nomes das colunas
column_names = ['station', 'temperature']
df = pd.read_csv(txt_file_path, delimiter=';', names=column_names)

# Salve o DataFrame em formato Parquet
df.to_parquet(parquet_file_path, engine='pyarrow')
