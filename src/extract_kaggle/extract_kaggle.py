import subprocess
import os
import kaggle

from pathlib import Path

# Configurando os Path
new_folder_kaggle = r'C:\Users\Victor_1\Documents\VSCode\fiap_tech_challenge_03\src\data\raw'
download_path = r'C:\Users\Victor_1\Documents\VSCode\fiap_tech_challenge_03\src\data\raw'

# Nome do conjunto de dados
dataset_name = 'goyaladi/flight-dataset'

file_name = f"{download_path}/{dataset_name.split('/')[1]}.zip"
file_name = Path(file_name)
print(f"Esse é o path montado {file_name}")

download_path = Path(download_path)
print(f"Esse é o path de download {download_path}")

kaggle.api.authenticate()

kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

'''
if not os.path.exists(file_name):
    # Criando nova pasta para arquivos kaggle
    subprocess.run(['mkdir', '-p', new_folder_kaggle])

    # Baixando arquivo zip do kaggle
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', download_path])

    # Descompactando os arquivos baixados com a opção -o para substituir sem prompt
    subprocess.run(['tar', '-o', file_name, '-d', download_path])

    # Deletar arquivo zip
    subprocess.run(['rm', '-r', file_name, '-d', download_path])

#command = ['tar', '-xf', zip_file, '-C', extract_to]
'''
# Executa o comando
#subprocess.run(command, check=True)