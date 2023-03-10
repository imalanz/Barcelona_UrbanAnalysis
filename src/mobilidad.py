import pandas as pd

def bici_ (df):
    # merge columns to create address.
    df["address"] = df["streetName"] + " " + df["streetNumber"].astype(str)
    df.drop(columns=["id", "type", "altitude", "slots", "nearbyStations", "status", "updateTime", "streetName", "streetNumber"], inplace=True)
    # apply function to address to separate the ZC.
    df["bikes"] = df["bikes"].astype(str)
    # make clumn category with same value.
    df["category"] = "bicing"
    # cleaning.
    df["bikes"] = df["bikes"].apply(lambda x: x.split(".")[0])
    df = df[["address", "bikes", "category", "latitude", "longitude"]]
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
        puertos["latitude"] = i[1]
        puertos["longitude"] = i[0]
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
    puertos = puertos[["address", "district_id", "district", "barri_id", "barri", "category", "latitude", "longitude"]]
    puertos.drop_duplicates(inplace=True)
    return puertos
