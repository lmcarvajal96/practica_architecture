from bs4 import BeautifulSoup
import requests
import re
import pandas as pd 
url = 'https://www.marca.com/futbol/sevilla.html?intcmp=MENUESCU&s_kw=sevilla'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data_noticias = pd.DataFrame()
lista_noticias = []
for eq in soup.find_all('h3', class_="mod-title"):
    eq = str(eq)
    m = re.search('title=(.+?)>', eq)
    noticias = m.group(1)
    lista_noticias.append(noticias)
    
df = pd.DataFrame(lista_noticias)

project_id = 'news_MARCA'

from google.colab import auth
auth.authenticate_user()

from googleapiclient.discovery import build
gcs_service = build('storage', 'v1')
bucket_name = 'segmento_noticias'

file_name = 'noticias.csv'

from googleapiclient.http import MediaFileUpload

media = MediaFileUpload(df, 
                        mimetype='text/plain',
                        resumable=True)

request = gcs_service.objects().insert(bucket=bucket_name, 
                                       name=file_name,
                                       media_body=media)

response = None
while response is None:
 
  _, response = request.next_chunk()

print('Upload completo')
