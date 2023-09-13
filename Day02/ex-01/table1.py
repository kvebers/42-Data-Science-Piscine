import psycopg2


def main():
    try:
        with open("1_more_script_to_execute.sql", "r") as sql_file:
            sqlToExecute = sql_file.read()
        connection = psycopg2.connect(dbname="piscineds", user="kvebers",
                                      password="mysecretpassword",
                                      host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute(sqlToExecute)
        connection.commit()
    except Exception as error:
        print(f"Error: {error}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()