import os
import pandas as pd
from sqlalchemy import create_engine, inspect
from table import load

def main():
    path = "/goinfre/kvebers/subject/customer/"
    tableName = "customers"
    try:
        print("I did something")
        Files = os.listdir(path)
        TablesToAdd = [item for item in Files]
        print(TablesToAdd)
        for item in TablesToAdd:
            full_path = os.path.join(path, item)
            load(full_path, tableName)
            print(full_path)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())