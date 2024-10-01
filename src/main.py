from aws_utils import handle_s3
import os
import pandas as pd

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

partition_date = pd.Timestamp.now().date()

#s3_key = f'particao_data={partition_date}/ibov_atual.parquet'

# handle_s3(file_name, bucket, access_key, secret_key, action, object_name=None, prefix=None)

# Exemplo de uso para upload:
handle_s3(r"C:\Users\Victor_1\Documents\VSCode\fiap_tech_challenge_03\src\data\raw\healthcare-dataset-stroke-data.csv",  # Corrigido
          'victor-mlet-tech-challenge-03', # Apenas o nome do bucket
          aws_access_key_id,
          aws_secret_access_key,
          'upload',
          'healthcare-dataset-stroke-data.csv', # Caminho no S3 onde o arquivo será salvo
          f'raw/{partition_date}')

# Instrução para salvar arquivo em parquet
# https://stackoverflow.com/questions/41066582/python-save-pandas-data-frame-to-parquet-file