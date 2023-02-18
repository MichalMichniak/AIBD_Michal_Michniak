import pandas as pd
import numpy as np

def clean():
    df = pd.read_csv("../Orginal Data/14_WIELKOPOLSKIE.csv",index_col=0)
    df["Wiek kupującego"].fillna(df["Wiek kupującego"].median(), inplace=True)
    df.to_csv("../Analysis Data/wielkopolskie.csv")

if __name__ == '__main__':
    df = pd.read_csv("./Orginal Data/14_WIELKOPOLSKIE.csv",index_col=0)
    df["Wiek kupującego"].fillna(df["Wiek kupującego"].median(), inplace=True)
    df.to_csv("./Analysis Data/wielkopolskie.csv")