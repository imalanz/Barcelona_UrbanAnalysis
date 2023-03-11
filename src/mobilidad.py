import pandas as pd

def bici_ (df):
    # merge columns to create address.
    df["address"] = df["streetName"] + " " + df["streetNumber"].astype(str)
    df.drop(columns=["id", "type", "altitude", "slots", "nearbyStations", "status", "updateTime", "streetName", "streetNumber"], inplace=True)
    # apply function to address to separate the ZC.
    df["bikes"] = df["bikes"].astype(str)
    # make clumn category with same value.
    df["category"] = "bicing"
    df["division"] = "mobilidad"
    # cleaning.
    df.rename(columns={"latitude":"latitud", "longitude":"longitud"}, inplace=True)
    df["bikes"] = df["bikes"].apply(lambda x: x.split(".")[0])
    df = df[["address", "bikes", "category", "division", "latitud", "longitud"]]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df

# get the json transform into readable, and transform it to clean df.
def bicipuertos (json):
    # transform to df
    puertos = pd.json_normalize(json, record_path =["features"])
    # clean.
    puertos.drop(columns=["type", "geometry.type", "properties.ID_SIT", "properties.X_ETRS89", "properties.Y_ETRS89", 
                             "properties.TIPUS", "properties.NUM_PLACES"], inplace=True)
    puertos.rename(columns={"geometry.coordinates":"coordinates", "properties.DISTRICTE":"district", "properties.BARRI":"Barrio",
                               	"properties.NOM_CARRER":"direccion", "properties.NUM_CARRER":"num"},inplace=True)
    # iterate coordinates to make new separate columns.
    for i in puertos.coordinates:
        puertos["latitud"] = i[1]
        puertos["longitud"] = i[0]
    # split by and separate into 2 columns.
    puertos["district_id"] = puertos["district"].apply(lambda x: x.split(".")[0])
    puertos["district"] = puertos["district"].apply(lambda x: x.split(".")[1])
    puertos["barri_id"] = puertos["Barrio"].apply(lambda x: x.split(".")[0])
    puertos["barri"] = puertos["Barrio"].apply(lambda x: x.split(".")[1])
    # merge columns to create address.
    puertos["address"] = puertos["direccion"] + " " + puertos["num"].astype(str)
    puertos.drop(columns=["coordinates", "Barrio", "direccion", "num"], inplace=True)
    # make clumn category with same value.
    puertos["category"] = "puerto_bici"
    puertos["division"] = "mobilidad"
    puertos = puertos[["address", "district_id", "district", "barri_id", "barri", "category", "division", "latitud", "longitud"]]
    puertos.drop_duplicates(inplace=True)
    return puertos

# clean df of buses stops.
def buses (df):
    df.drop(columns=["CODI_CAPA", "CAPA_GENERICA", "ED50_COORD_X", "ED50_COORD_Y", "ETRS89_COORD_X", "ETRS89_COORD_Y", "ADRECA", "TELEFON"],inplace=True)
    df.columns = df.columns.str.lower()
    df.rename(columns={"nom_capa":"category", "equipament":"name", "districte":"district_id", "barri":"barri_id", "nom_districte":"district", "nom_barri":"barri"}, inplace=True)
    df["division"] = "mobilidad"
    df = df[["name", "district_id", "district", "barri_id", "barri", "category", "division", "latitud", "longitud"]]
    df.dropna(inplace=True)
    return df

# clean df de transportes publicos en barcelona. 
def clean_transportes (df):
    df.drop(columns=["CODI_CAPA", "CAPA_GENERICA", "ED50_COORD_X", "ED50_COORD_Y", "ETRS89_COORD_X", "ETRS89_COORD_Y", "ADRECA", "TELEFON"],inplace=True)
    df.columns = df.columns.str.lower()
    df.rename(columns={"nom_capa":"category", "equipament":"name", "districte":"district_id", "barri":"barri_id", "nom_districte":"district", "nom_barri":"barri"}, inplace=True)
    # clean float to only select integer.
    df["district_id"] = df["district_id"].astype(str)
    df["district_id"] = df["district_id"].apply(lambda x: x.split(".")[0])
    df["barri_id"] = df["barri_id"].astype(str)
    df["barri_id"] = df["barri_id"].apply(lambda x: x.split(".")[0])
    df["division"] = "mobilidad"
    df = df[["name", "district_id", "district", "barri_id", "barri", "category", "division", "latitud", "longitud"]]
    df.dropna(inplace=True)
    return df