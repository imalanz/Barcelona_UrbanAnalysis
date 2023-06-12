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
    # Create new columns with clean info.
    df["barri"] = df[0].apply(lambda x: x.split(".")[1])
    df["district_id"] = df[0].apply(lambda x: x.split(".")[0])
    # Separate mixed nummbers to district numb.
    df["district_id"] = df["district_id"].apply(nums)
    # Clean DF and re organize it.
    df.drop(columns=[0, 4, 5, 6, 7, 8], inplace=True)
    df = df[["district_id", "barri", 1, 2, 3]]
    df.rename(columns={1:"1er trimestre", 2:"2do trimestre", 3:"3er trimestre"}, inplace=True)
    return df  

# function to get the number of the district.
def nums (i):  
    if len(str(i)) == 2:
        return i[0]
    else:
        return i[:2]
    

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
    # Create new columns with clean info.
    df["barri"] = df[0].apply(lambda x: x.split(".")[1])
    df["district_id"] = df[0].apply(lambda x: x.split(".")[0])
    # Separate mixed nummbers to district numb.
    df["district_id"] = df["district_id"].apply(nums)
    # clean first column names, change the names of columns.
    df.drop(columns=[0], inplace=True)
    df = df[["district_id", "barri", 1, 2, 3, 4, 5]]    
    df.rename(columns={0:"barri", 1:"2015", 2:"2016", 3:"2017", 4:"2018", 5:"2019"}, inplace=True)
    return df  

# web scraping for seguridad page per district.
def seguridad (url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    x = rows[9:-6]
    colum = rows[4]
    # tansform to df.
    df = pd.DataFrame(x, columns= colum)
    # Clean without number district column.
    df.columns = df.columns.str.lower()
    df["district_id"] = df["distrito"].apply(lambda x: x.split(".")[0])
    df["district"] = df["distrito"].apply(lambda x: x.split(".")[1])
    df.drop(columns=["distrito"], inplace=True)
    df.dropna(inplace=True)
    df = df[["district_id", "district", "denuncias por infracción de la ordenanza de convivencia ciudadana (% habitantes)", 
            "incidentes pordegradación del espacio público (‰ habitantes)", "incidentes en laconvivenciavecinal (‰ habitantes)",
            "incidentes por actividadesmolestas en el espaciopúblico (‰ habitantes)", "incidentes por actividadesindebidas en el espaciopúblico (‰ habitantes)"]]
    return df

# web scraping for ayuda of guardia urbana.
def pol_urbana_ayuda (url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    x = rows[9:-6]
    df = pd.DataFrame(x)
    # Clean and rename columns.
    df.drop(columns=[12], inplace=True) # distrito desconocido.   
    df.rename(columns={0: "Incidencias", 1:"Barcelona", 2:"1.Ciutat Vella", 3:"2.L'Eixample", 4:"3.Sants-Monjuïc",
                        5:"4.Les Corts", 6:"5.Sarrià-Sant Gervasi", 7:"6.Gràcia", 8:"7.Horta-Guiardó",
                        9: "8.Nou Barris", 10:"9.Sant Andreu", 11:"10.Sant Martí"}, inplace=True)
    return df

# web scraping for circulacion incidents.
def circulacion (url):  
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    x = rows[9:-6]
    df = pd.DataFrame(x)
    # clean and rename.
    df.drop(columns=[12, 13], inplace=True)
    df.rename(columns={0: "Incidencias", 1:"Barcelona", 2:"1.Ciutat Vella", 3:"2.L'Eixample", 4:"3.Sants-Monjuïc",
                            5:"4.Les Corts", 6:"5.Sarrià-Sant Gervasi", 7:"6.Gràcia", 8:"7.Horta-Guiardó",
                            9: "8.Nou Barris", 10:"9.Sant Andreu", 11:"10.Sant Martí"}, inplace=True)
    return df

# scraping for incidents with mossos by district.
def mossos_inc (url):   
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    x = rows[9:-6]
    df = pd.DataFrame(x)
    # clean and rename.
    df.drop(columns=[12], inplace=True)
    df.rename(columns={0: "Incidencias", 1:"Barcelona", 2:"1.Ciutat Vella", 3:"2.L'Eixample", 4:"3.Sants-Monjuïc",
                                5:"4.Les Corts", 6:"5.Sarrià-Sant Gervasi", 7:"6.Gràcia", 8:"7.Horta-Guiardó",
                                9: "8.Nou Barris", 10:"9.Sant Andreu", 11:"10.Sant Martí"}, inplace=True)
    return df 

# poblation census per years old.
def poblation (url): 
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find_all("table")[0]
    tags = table.find_all("tr")
    # select only texts and clean it.
    rows = [i.text.strip().replace("\xa0", "").split("\n") for i in tags]
    x = rows[9:-6]
    colum = rows[4]
    # transform to df.
    df = pd.DataFrame(x, columns=colum)
    # Create new columns with clean info.
    df["Barrio"] = df["Dto.Barrios"].apply(lambda x: x.split(".")[1])
    df["Dto."] = df["Dto.Barrios"].apply(lambda x: x.split(".")[0])
    # Separate mixed nummbers to district numb.
    df["Dto."] = df["Dto."].apply(nums)
    # clean first column names, change the names of columns.
    df.drop(columns=["Dto.Barrios"], inplace=True)
    df = df[["Dto.", "Barrio", "TOTAL", "0-14 años", "15-24 años", "25-64 años", "65 años y más"]]
    return df