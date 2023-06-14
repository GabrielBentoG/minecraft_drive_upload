import gdown

# Donwload a complete folder
folder_id = ''
#url = f'https://drive.google.com/drive/folders/{folder_id}?usp=sharing'
#gdown.download_folder(url, quiet=True, use_cookies=False)
gdown.download_folder(id=folder_id, quiet=False, use_cookies=False)

