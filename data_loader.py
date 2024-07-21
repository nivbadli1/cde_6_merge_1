# data_loader.py
import pandas as pd
from sqlalchemy import create_engine

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_from_database(connection_string, query):
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

def save_to_database(df, table_name, connection_string):
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
