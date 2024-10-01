#import subprocess
#import os
import kaggle

from pathlib import Path

# Configurando os Path
new_folder_kaggle = r'C:\Users\Victor_1\Documents\VSCode\fiap_tech_challenge_03\src\data\raw'
download_path = r'C:\Users\Victor_1\Documents\VSCode\fiap_tech_challenge_03\src\data\raw'

# Nome do conjunto de dados
#dataset_name = 'goyaladi/flight-dataset'
dataset_name = 'fedesoriano/stroke-prediction-dataset'

file_name = f"{download_path}/{dataset_name.split('/')[1]}.zip"
file_name = Path(file_name)
print(f"Esse é o path montado {file_name}")

download_path = Path(download_path)
print(f"Esse é o path de download {download_path}")

kaggle.api.authenticate()

kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

# Link Dataset: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset