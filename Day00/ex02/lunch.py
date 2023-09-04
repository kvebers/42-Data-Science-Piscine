import pandas as pd
from sqlalchemy import create_engine

try:
    data = pd.read_csv("/goinfre/kvebers/subject/customer/data_2022_dec.csv")
    engine = create_engine("postgresql://kvebers:mysecretpassword@localhost:5432/piscineds")
    data.to_sql("ex02", engine, if_exists='replace', index=False)
    engine.dispose()
except Exception as e:
    print(f"An error occurred: {e}")
