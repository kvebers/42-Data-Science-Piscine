import pandas as pd
from sqlalchemy import create_engine, types
import sqlalchemy


def load(path, tableName):
    try:
        data = pd.read_csv(path)
        data_types = {
            "product_id": sqlalchemy.types.Integer(),
            "category_id": sqlalchemy.types.BigInteger(),
            "category_code": sqlalchemy.types.String(length=255),
            "brand": sqlalchemy.types.String(length=255)
        }
        engine = create_engine("postgresql://kvebers:mysecretpassword@localhost:5432/piscineds")
        data.to_sql(tableName, engine, index=False, dtype=data_types)
        engine.dispose()
    except Exception as e:
        print(f"An error occurred: {e}")