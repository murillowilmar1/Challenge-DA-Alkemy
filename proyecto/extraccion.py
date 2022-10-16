# -*- coding: utf-8 -*-


import pandas as pd 
import requests
import os

# Extracción de datos museos 

data_museos= requests.get("https://datos.cultura.gob.ar/dataset/espacios-culturales-argentina-sinca/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv", allow_redirects=True)
os.makedirs("museos/2022-octubre")
open('museos/2022-octubre/museos-13-10-2022.csv', 'wb').write(data_museos.content)
data_museos.url

#Extracción de datos cine 

data_cine= requests.get("https://datos.cultura.gob.ar/dataset/espacios-culturales-argentina-sinca/resource/f7a8edb8-9208-41b0-8f19-d72811dcea97/download/cine.csv", allow_redirects=True)
os.makedirs("cine/2022-octubre")
open('cine/2022-octubre/cine-13-10-2022.csv', 'wb').write(data_cine.content)
data_cine.url

# Extracción de datos bibliotecas populares 

data_biblio= requests.get("https://datos.cultura.gob.ar/dataset/espacios-culturales-argentina-sinca/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/bibliotecas.csv", allow_redirects=True)
os.makedirs("bibliotecas/2022-octubre")
open('bibliotecas/2022-octubre/bibliotecas-13-10-2022.csv', 'wb').write(data_biblio.content)

data_biblio.url

# metodo para verificar que los datos cargaron exitosamente
print(data_museos.status_code)
print(data_cine.status_code)
print(data_biblio.status_code)