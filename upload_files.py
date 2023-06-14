from dotenv import load_dotenv
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tqdm import tqdm  # Importa a biblioteca tqdm
import os

# Caminho para a pasta local
pasta_local = 'mundos'

# ID da pasta de destino no Google Drive
id_pasta_destino = 'FOLDER_ID'

# Autenticação e criação do objeto drive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Itera sobre os arquivos na pasta local e envia para o Google Drive
arquivos = os.listdir(pasta_local)

# Função para enviar um arquivo para o Google Drive
def enviar_arquivo(nome_arquivo, caminho_local, id_pasta_destino):
    arquivo = drive.CreateFile({'title': nome_arquivo, 'parents': [{'id': id_pasta_destino}]})
    arquivo.SetContentFile(caminho_local)
    arquivo.Upload()

# Autentica e, em seguida, mostra a barra de progresso
gauth.LocalWebserverAuth()
for nome_arquivo in tqdm(arquivos, desc='Enviando arquivos'):
    caminho_local = os.path.join(pasta_local, nome_arquivo)
    enviar_arquivo(nome_arquivo, caminho_local, id_pasta_destino)

print("Arquivos enviados com sucesso para o Google Drive.")
