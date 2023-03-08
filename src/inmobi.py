from bs4 import BeautifulSoup 
import pandas as pd
import requests


## INMOBILIARIAS.

# web scraping throw monthly price rent per barri in barcelona.
def scraping_prices (url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    rowse = rows[10:-6]
    # transform to df.
    df = pd.DataFrame(rowse)
    # clean first column names and drop not necesary columns, change the names of columns.
    df[0] = df[0].apply(lambda x: x.split(".")[1])
    df.drop(columns=[4, 5, 6, 7, 8], inplace=True)
    df.rename(columns={0:"barrio", 1:"1er trimestre", 2:"2do trimestre", 3:"3er trimestre"}, inplace=True)
    return df  

# web scraping socio-economic indice per barri.
def scraping_sociecon (url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    x = rows[9:-9]
    # transform to df.
    df = pd.DataFrame(x)
    # clean first column names, change the names of columns.
    df[0] = df[0].apply(lambda x: x.split(".")[1])
    df.rename(columns={0:"barrio", 1:"2015", 2:"2016", 3:"2017", 4:"2018", 5:"2019"}, inplace=True)
    return df  

