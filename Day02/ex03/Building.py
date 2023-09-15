import psycopg2
import pandas as pd



def main():
    try:
        with open("script_to_execute.sql", "r") as sql_file:
            sqlToExecute = sql_file.read()
        connection = psycopg2.connect(dbname="piscineds", user="kvebers",
                                      password="mysecretpassword",
                                      host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute(sqlToExecute)
        data = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        print(data)
    except Exception as error:
        print(f"Error: {error}")
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()