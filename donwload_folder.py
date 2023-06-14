import gdown

folder_id = 'FOLDER_ID'
#url = f'https://drive.google.com/drive/folders/{folder_id}?usp=sharing'
#gdown.download_folder(url, quiet=True, use_cookies=False)
gdown.download_folder(id=folder_id, quiet=False, use_cookies=False)