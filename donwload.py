import gdown
import os
from dotenv import load_dotenv
load_dotenv()
folder_id = os.getenv('FOLDER_ID')
# Donwload a complete folder
gdown.download_folder(id=folder_id, quiet=False, use_cookies=False)

