import pandas as pd

def normalize_data(data_src,data_destynation):
    df = pd.read_csv(data_src)
    # col correction
    col_names = ["country","beer","spirit","wine","pure_alcohol"]
    df.columns = col_names
    ## del every zero record
    df = df[(df["pure_alcohol"]!=0)]
    ## normalization by total alcohol
    df["wine_norm"] = df["wine"] / df["pure_alcohol"]
    df["beer_norm"] = df["beer"] / df["pure_alcohol"]
    df["spirit_norm"] = df["spirit"] / df["pure_alcohol"]
    df.to_csv(data_destynation)


normalize_data("./OrginalData/drinks.csv","./AnalysisData/norm.csv")