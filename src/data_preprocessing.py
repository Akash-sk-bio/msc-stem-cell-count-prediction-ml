import pandas as pd

def load_data(path):
    return pd.read_excel(path)

def clean_missing(df):
    return df.fillna(df.median(numeric_only=True))
