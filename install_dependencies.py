import subprocess

# Lê o arquivo requirements.txt e obtém a lista de pacotes
with open('requirements.txt', 'r') as file:
    requirements = file.read().splitlines()

# Instala cada pacote usando o pip
for package in requirements:
    subprocess.call(['pip', 'install', package])

print("Pacotes instalados com sucesso.")
