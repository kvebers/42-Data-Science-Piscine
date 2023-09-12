import psycopg2


def main():
    try:
        with open("script_to_execute.sql", "r") as sql_file:
            sqlExecute = sql_file.read()
        conn = psycopg2.connect(dbname="piscineds", user="kvebers",
                                password="mysecretpassword",
                                host="localhost", port="5432")
        conExecute = conn.cursor()
        conExecute.execute(sqlExecute)
        conn.commit
        conExecute.close()
        conn.close()
    except Exception as error:
        print(f"Error {error} accured")


if __name__ == "__main__":
    main()
