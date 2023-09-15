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
        prices = [item[0] for item in data]
        df = pd.DataFrame(prices, columns=["price"])
        
        print("Count:", df['price'].sum())
        print("Mean:", df['price'].mean())
        print("Median:", df['price'].median())
        print("Min:", df['price'].min())
        print("Max:", df['price'].max())
        print("First Quartile (25%):", df['price'].quantile(0.25))
        print("Second Quartile (50%):", df['price'].quantile(0.5))
        print("Third Quartile (75%):", df['price'].quantile(0.75))
        
    except Exception as error:
        print(f"Error: {error}")
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()