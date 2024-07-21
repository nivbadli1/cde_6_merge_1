# transformations.py
import pandas as pd

def clean_column_names(df):
    return df.rename(columns=lambda x: x.lower().replace(' ', '_'))

def convert_date_columns(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    return df

def aggregate_data(df, group_by_cols, agg_dict):
    return df.groupby(group_by_cols).agg(agg_dict).reset_index()
