import os
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy


def readData(path):
    data = pd.read_csv(path)
    return (data)


def extractTableNames(item):
    return [name[0:-4] for name in item]


def checkCSV(item):
    if (len(item) < 4):
        return False
    if (item[-4:] != ".csv"):
        return False
    return True


def main():
    path = "/goinfre/kvebers/subject/customer/"
    tableName = "customers"
    try:
        Files = os.listdir(path)
        TablesToAdd = [item for item in Files if checkCSV(item) is True]
        data = pd.DataFrame()
        for item in TablesToAdd:
            full_path = os.path.join(path, item)
            data = pd.concat([data, readData(full_path)], ignore_index=True)

        data_types = {
            "event_time": sqlalchemy.DateTime(),
            "event_type":  sqlalchemy.types.String(length=255),
            "product_id": sqlalchemy.types.Integer(),
            "price": sqlalchemy.types.Float(),
            "user_id": sqlalchemy.types.BigInteger(),
            "user_session": sqlalchemy.types.Uuid()
        }
        engine = create_engine("postgresql://kvebers:mysecretpassword@localhost:5432/piscineds")
        data.to_sql(tableName, engine, index=False, dtype=data_types)
        engine.dispose()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
