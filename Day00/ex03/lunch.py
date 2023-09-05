import pandas as pd
from sqlalchemy import create_engine


def load(path, tableName):

    try:
        data = pd.read_csv(path)
        engine = create_engine("postgresql://kvebers:mysecretpassword@localhost:5432/piscineds")
        data.to_sql(tableName, engine, if_exists='replace', index=False)
        engine.dispose()
    except Exception as e:
        print(f"An error occurred: {e}")
