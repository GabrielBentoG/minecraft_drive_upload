import gdown

url = 'https://drive.google.com/drive/folders/1SeyuIZKbNnEe1jx4ItB9SGPqHsklNqj9?usp=sharing'
gdown.download_folder(url, quiet=True, use_cookies=False)
