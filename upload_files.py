from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Caminho para a pasta local
pasta_local = 'LOCAL_FOLDER'

# ID da pasta de destino no Google Drive
id_pasta_destino = 'FOLDER_ID'

# Autenticação e criação do objeto drive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Função para enviar um arquivo para o Google Drive
def enviar_arquivo(nome_arquivo, caminho_local, id_pasta_destino):
    arquivo = drive.CreateFile({'title': nome_arquivo, 'parents': [{'id': id_pasta_destino}]})
    arquivo.SetContentFile(caminho_local)
    arquivo.Upload()

# Itera sobre os arquivos na pasta local e envia para o Google Drive
for nome_arquivo in os.listdir(pasta_local):
    caminho_local = os.path.join(pasta_local, nome_arquivo)
    enviar_arquivo(nome_arquivo, caminho_local, id_pasta_destino)

print("Arquivos enviados com sucesso para o Google Drive.")
