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
    
for noticia in lista_noticias:
    data_noticias['noticias'] = noticia
    data_noticias.append(data_noticias)

print(data_noticias)