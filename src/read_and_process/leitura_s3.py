import boto3
import pandas as pd
from io import BytesIO, StringIO

# Nome do bucket e chave do arquivo Parquet no S3
bucket_name = 'victor-mlet-tech-challenge-03'
file_key = 'raw/2024-09-29/healthcare-dataset-stroke-data.csv'
#file_key = 's3://victor-mlet-tech-challenge-02/refined/Data_pregao=2024-07-24/*'

# Cliente S3
s3 = boto3.client('s3')

# Obtém o arquivo CSV/Parquet do S3
response = s3.get_object(Bucket=bucket_name, Key=file_key)
csv_content = response['Body'].read().decode('utf-8')
#parquet_content = response['Body'].read()

# Usa o Pandas para ler o CSV/Parquet diretamente da string/memória
df = pd.read_csv(StringIO(csv_content))
#df = pd.read_parquet(BytesIO(parquet_content))

# Exibe as primeiras linhas do DataFrame
print(df.head())
