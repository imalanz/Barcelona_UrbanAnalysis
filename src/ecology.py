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
def aire_monthly (maindf, contami_df, distr_df):
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
    group = total[["district", "contaminant", "total"]].groupby(by=["district", "contaminant"]).agg({"total":"mean"})
    return group