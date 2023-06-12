import pandas as pd

# clean data frame of civic places.
def civic_ (df):
    # drop columns.
    civic = df.drop(columns=["Any", "Ambit", "Notes_Dades", "Notes_Equipament", "TipusEquipament", "TipusGeneral", "Titularitat"])
    #iterate throw columns to create separete columns values and make it df, 2 df
    total_usos_entitats = {index:[row[0], row[2]] for index, row in civic.iterrows() if row [1] == "TotalUsosEntitats"}
    total_usos_entitats = pd.DataFrame.from_dict(total_usos_entitats, orient="index")
    total_usos_entitats.rename(columns={0: "Equipament", 1:"total_usos_entitats"}, inplace=True)
    metres_quadrats = {index:[row[0], row[2]] for index, row in civic.iterrows() if row [1] == "Metres_quadrats"}
    metres_quadrats = pd.DataFrame.from_dict(metres_quadrats, orient="index")
    metres_quadrats.rename(columns={0: "Equipament", 1:"metres_quadrats"},inplace=True)
    # drop columns and duplicates.
    civic.drop(columns=["Indicador", "Valor"],inplace=True)
    civic.drop_duplicates(inplace=True)
    #merge the 2 df into the main.
    x = pd.merge(civic, total_usos_entitats, on= "Equipament", how="left")
    df = pd.merge(x, metres_quadrats, on= "Equipament", how="left")
    # rename columns names.
    df.columns = df.columns.str.lower()
    df["division"] = "equipamiento"
    df["category"] = "centro_civic"
    df["sub_category"] = "centro_civico"
    df.rename(columns={"equipament":"name", "codi_districte":"district_id", "nom_districte":"district", "codi_barri":"barri_id", 
                                  "nom_barri":"barri"}, inplace=True)   
    return df

# Clean from csv df all columns and organized it from equipamientos csv, applyes to must of the df of equipments.
def clean_equipamientos (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "secondary_filters_id", "secondary_filters_fullpath", "secondary_filters_tree", 
                    "secondary_filters_asia_id", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town", "addresses_type",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitud", "geo_epgs_4326_y":"longitud" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0])
    df["division"] = "equipamiento"
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df    

# Clean from csv df all columns and organized it from equipamientos csv, applyes to must of the df of cultura y ocio.
def clean_cult_ocio (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "secondary_filters_id", "secondary_filters_fullpath", "secondary_filters_tree", 
                    "secondary_filters_asia_id", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town", "addresses_type",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitud", "geo_epgs_4326_y":"longitud" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0])
    df["division"] = "cultura/ocio"
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df    

# Clean ids from boolean to strings no digits.
def clean_ids (df):
    df["barri_id"] = df["barri_id"].astype(str)
    df["district_id"] = df["district_id"].astype(str)
    df["barri_id"] = df["barri_id"].apply(lambda x: x.split(".")[0])
    df["district_id"] = df["district_id"].apply(lambda x: x.split(".")[0])
    return df

# Clean from csv df all columns and organized it from excersice.
def clean_excersice (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "secondary_filters_id", "secondary_filters_fullpath", "secondary_filters_tree", 
                    "secondary_filters_asia_id", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town", "addresses_type",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitud", "geo_epgs_4326_y":"longitud" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    # make clumn category with same value.
    df["category"] = "excersice"
    df["division"] = "excersice"
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0]) 
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df    

# Clean from csv df all columns and organized it from POOLs.
def clean_pool (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding", "addresses_type",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitud", "geo_epgs_4326_y":"longitud" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    # make clumn category with same value.
    df["category"] = "piscina"
    df["division"] = "excersice"
    df.dropna(inplace=True)
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0])
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df   

# Clean from csv df all columns and organized it from circuitos walk.
def clean_circuit (df):
    df.drop(columns=["register_id", "institution_id", "institution_name", "created", "modified", "addresses_roadtype_id", "addresses_roadtype_name",
                    "addresses_road_id", "values_description", "geo_epgs_25831_x", "geo_epgs_25831_y", "addresses_end_street_number", "addresses_town",
                    "values_id", "values_attribute_id", "values_category", "values_attribute_name", "values_value", "values_outstanding", "addresses_type",
                    "addresses_main_address"], inplace=True)
    df.rename(columns={"addresses_neighborhood_id":"barri_id", "addresses_neighborhood_name":"barri", "addresses_district_id":"district_id", 
                        "addresses_district_name":"district", "secondary_filters_name":"category", "geo_epgs_4326_x":"latitud", "geo_epgs_4326_y":"longitud" },inplace=True)
    # Merge the address columns into one.
    df["address"] = df["addresses_road_name"] + " " + df["addresses_start_street_number"].astype(str)
    # Drop duplicates and null.
    df.drop_duplicates(inplace=True)
    # make clumn category with same value.
    df["category"] = "walk_circuit"
    df["division"] = "excersice"
    df.dropna(inplace=True)
    # apply function to address to separate the ZC.
    df["address"] = df["address"].apply(lambda x: x.split(".")[0])
    # drop columns already in address column
    df.drop(columns=["addresses_road_name", "addresses_start_street_number", "addresses_zip_code"], inplace=True)
    return df   