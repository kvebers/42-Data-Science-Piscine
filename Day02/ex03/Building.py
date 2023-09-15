import psycopg2
import matplotlib.pyplot as plt


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
        frquencyMap = {}
        monetaryMap = {}
        for item in data:
            if item[0] not in frquencyMap:
                frquencyMap[item[0]] = 1
            else:
                frquencyMap[item[0]] += 1
            if item[0] not in monetaryMap:
                monetaryMap[item[0]] = item[1]
            else:
                monetaryMap[item[0]] += item[1]
        freq_categories = {'0-10': 0, '10-20': 0, '20-30': 0, '30-40': 0, '40+': 0}
        monetary_categories = {'0-50': 0, '50-100': 0, '100-150': 0, '150-200': 0, '200+': 0}

        for k, v in frquencyMap.items():
            if v <= 10:
                freq_categories['0-10'] += 1
            elif v <= 20:
                freq_categories['10-20'] += 1
            elif v <= 30:
                freq_categories['20-30'] += 1
            elif v <= 40:
                freq_categories['30-40'] += 1
            else:
                freq_categories['40+'] += 1

        for k, v in monetaryMap.items():
            if v <= 50:
                monetary_categories['0-50'] += 1
            elif v <= 100:
                monetary_categories['50-100'] += 1
            elif v <= 150:
                monetary_categories['100-150'] += 1
            elif v <= 200:
                monetary_categories['150-200'] += 1
            else:
                monetary_categories['200+'] += 1
        fig, ax = plt.subplots(1, 2, figsize=(10, 8))
        ax[0].bar(freq_categories.keys(), freq_categories.values(), color='b')
        ax[0].set_ylabel('Count')
        ax[0].set_title('Frequency Distribution')
        ax[0].set_xticklabels(freq_categories.keys(), rotation=45)
        ax[1].bar(monetary_categories.keys(), monetary_categories.values(), color='r')
        ax[1].set_xlabel('Category')
        ax[1].set_ylabel('Count')
        ax[1].set_title('Monetary Distribution')
        ax[1].set_xticklabels(monetary_categories.keys(), rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as error:
        print(f"Error: {error}")
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()