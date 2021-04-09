import os
import requests
import shutil
from download_util import download_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')

url = 'https://cdn.britannica.com/s:400x225,c:crop/97/158797-050-ABECB32F/North-Cascades-National-Park-Lake-Ann-park.jpg'

r = requests.get(url, stream=True)

#for smallish item
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)


""" dl_filename = os.path.basename(url)
new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)

with requests.get(url, stream=True)as r:
    with open(new_dl_path, 'wb') as file_obj:
        shutil.copyfileobj(r.raw, file_obj) """

download_file(url, DOWNLOADS_DIR)