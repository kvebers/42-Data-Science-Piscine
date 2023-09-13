import psycopg2
import matplotlib.pyplot as plt
import numpy as np


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
        labels = []
        numbers = []
        for i in data:
            labels.append(i[0])
            numbers.append(float(i[1]))
        plt.pie(numbers, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()