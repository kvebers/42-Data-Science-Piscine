import os
import pandas as pd
from sqlalchemy import create_engine, inspect
from table import load

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
        engine = create_engine("postgresql://kvebers:mysecretpassword@localhost:5432/piscineds")
        inspector = inspect(engine)
        if inspector.has_table(tableName):
            engine.execute(f"DROP TABLE IF EXISTS {tableName}")
        engine.dispose()
        for item in TablesToAdd:
            full_path = os.path.join(path, item)
            load(full_path, tableName)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
