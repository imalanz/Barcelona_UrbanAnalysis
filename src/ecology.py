import pandas as pd


# clean df of stations and its districts.
def limpia_estacions_aire(df):
    # pequeña limpia de columnas.
    df.drop(columns=["Clas_2", "Clas_1", "codi_dtes", "zqa", "codi_eoi", "ubicacio", "nom_cabina"], inplace=True)
    # crear df de solo los datos que necesito para el merge por mes.
    distr = df[["Estacio", "Codi_districte", "Nom_districte"]]
    distr.columns = distr.columns.str.lower()
    return distr

# df of contaminants.
def limpia_contaminants (df):
    # make it lower case.
    df.columns = df.columns.str.lower()
    return df

# Get the monthly air quality.
def aire_monthly (maindf, contami_df, distr_df, name):
    x = maindf.drop(columns=["PROVINCIA", "CODI_PROVINCIA", "CODI_MUNICIPI", "MUNICIPI" ])
    # sum all values for contaminant per hour in a total column.
    x["total_mean"] = x.fillna(0)["H01"] + x.fillna(0)["H02"] + x.fillna(0)["H03"] + x.fillna(0)["H04"] + x.fillna(0)["H05"] + x.fillna(0)["H06"] + x.fillna(0)["H07"] + x.fillna(0)["H08"] + x.fillna(0)["H09"] + x.fillna(0)["H10"] + x.fillna(0)["H11"] + x.fillna(0)["H12"] + x.fillna(0)["H13"] + x.fillna(0)["H14"] + x.fillna(0)["H15"] + x.fillna(0)["H16"] + x.fillna(0)["H17"] + x.fillna(0)["H18"] + x.fillna(0)["H19"] + x.fillna(0)["H20"] + x.fillna(0)["H21"] + x.fillna(0)["H22"] + x.fillna(0)["H23"] + x.fillna(0)["H24"]
    x["total_mean"] = x["total_mean"] / 24
    # drop columns with values per hour.
    x.drop(columns=["H01", "V01", "H02", "V02", "H03", "V03", "H04", "V04", "H05", "V05", "H06", "V06", "H07", "V07", "H08", "V08", "H09", "V09",
                    "H10", "V10", "H11", "V11", "H12", "V12", "H13", "V13", "H14", "V14", "H15", "V15", "H16", "V16", "H17", "V17", "H18", "V18", 
                    "H19", "V19", "H20", "V20", "H21", "V21", "H22", "V22", "H23", "V23", "H24", "V24"], inplace=True)
    # make columns name equal.
    x.columns = x.columns.str.lower()

    # Merge 2df contaminants code with station.
    aire = pd.merge(x, contami_df, on= "codi_contaminant", how="left")
    total = pd.merge(aire, distr_df, on= "estacio", how="left")
    total.rename(columns={"nom_districte":"district", "desc_contaminant": "contaminant", "total_mean": "total"}, inplace=True)
    # groupby district and name of contaminant.
    group = total[["contaminant", "district", "total"]].groupby(by=["district","contaminant"]).agg({"total":"mean"})
    x = group.reset_index().rename(columns={"index":"district"})
    x.rename(columns={"total": name}, inplace=True)
    return x

# mini function to apply.
def returning (x):
    if "DEN" in x:
        return x
    else:
        return "NAN"

# function for df of sound, returns a df with only barri, district and porcentage of different types of desiveles.
def soroll_barris(df):
    df.columns = df.columns.str.lower()
    df.rename(columns={"nom_barri":"barri", "concepte":"time", "rang_soroll":"sound", "Nom_Districte":"district"}, inplace=True)
    df["valor"] = df["valor"].apply(lambda x: x.replace("%", ""))
    df["time"] = df["time"].apply(returning)
    # selecting only the "total_den" because is the avarege for all day. 
    x = df[df["time"] == "TOTAL_DEN"]
    x.drop(columns=["codi_districte", "codi_barri", "time"], inplace=True)
    return x

# Clean from csv df all columns and organized it for interior gardens.
def jardin_interior (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding", "addresses_type",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitude", "geo_epgs_4326_y":"longitude" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    # make clumn category with same value.
    df["category"] = "jardin_interior"
    df.dropna(inplace=True)
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0])
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df   

# Clean from csv df all columns and organized it for refugis.
def refugi (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding", "addresses_type",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitude", "geo_epgs_4326_y":"longitude" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    # make clumn category with same value.
    df["category"] = "refugis"
    df.dropna(inplace=True)
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0])
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df   

# df clean for arvriari. 
def arbolado(df):
    df.drop(columns=["codi", "x_etrs89", "y_etrs89", "cat_especie_id", "categoria_arbrat", "data_plantacio", "nom_catala", "espai_verd", "tipus_reg",
                    "tipus_aigua", "geom", "catalogacio"], inplace=True)
    df.rename(columns={"tipus_element":"category", "adreca":"address", "nom_cientific":"taxon_name", "nom_castella":"common_name", "nom_barri":"barri", "nom_districte":"district",
                      "codi_barri":"barri_id", "codi_districte":"district_id"}, inplace=True)
    # rearange names of columns.
    viari = df[["taxon_name", "common_name", "barri_id", "barri", "district_id", "district", "category", "address", "latitud", "longitud"]]
    # Clean.
    viari.dropna(inplace=True)
    viari["barri_id"] = viari["barri_id"].astype(str)
    viari["barri_id"] = viari["barri_id"].apply(lambda x: x.split('.')[0])
    viari["address"] = viari["address"].apply(lambda x: x.replace('C\ ', ""))
    viari["barri"] = viari["barri"].str.lower()
    viari["district"] = viari["district"].str.lower()
    return viari