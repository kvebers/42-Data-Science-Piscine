import psycopg2
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date


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
        # Declearing the subplots
        fig, axs = plt.subplots(1, 3, figsize=(16, 4))
        time = {}
        time1 = {}
        time2 = {}
        time3 = {}
        # Setting up the data to work with 1st table
        for item in data:
            month = item[0].month
            if month > 9 or month < 2:
                if (item[1] == "purchase"):
                    dateKey = item[0].date()
                    monthKey = item[0].month
                    if dateKey not in time:
                        time[dateKey] = 1
                    else:
                        time[dateKey] += 1
                    if monthKey not in time1:
                        time1[monthKey] = float(item[2])
                    else:
                        time1[monthKey] += float(item[2])
                    if dateKey not in time2:
                        time2[dateKey] = {"sum": 0, "users": set()}
                    time2[dateKey]["sum"] += float(item[2])
                    time2[dateKey]["users"].add(item[3])
        for Val, values in time2.items():
            time3[Val] = values["sum"] / len(values["users"])
        # First plot
        sortedTime = sorted(time.items())
        breakpointIdx = next(i for i, (d, _) in enumerate(sortedTime) if d.month == 1)
        sortedTime.insert(breakpointIdx, (date(sortedTime[breakpointIdx-1][0].year, 12, 31), float('nan')))
        sortedTime.insert(breakpointIdx+1, (date(sortedTime[breakpointIdx][0].year, 1, 1), float('nan')))
        dates, counts = zip(*sortedTime)
        axs[0].plot(dates, counts, color='b')
        months = mdates.MonthLocator(bymonth=[10, 11, 12, 1])
        month_fmt = mdates.DateFormatter('%b')
        axs[0].xaxis.set_major_locator(months)
        axs[0].xaxis.set_major_formatter(month_fmt)
        axs[0].set_ylabel('Number of customers')
        # 2nd plot
        months = ['Oct', 'Nov', 'Dec', 'Jan']
        mils = 1000000
        values = [time1.get(10, 0) / mils, time1.get(11, 0) / mils, time1.get(12, 0) / mils, time1.get(1, 0) / mils]
        axs[1].bar(months, values)
        axs[1].set_ylabel('Total sales in Millions of Hichiker currency')
        # 3d plot
        sortedTime = sorted(time3.items())
        breakpointIdx = next(i for i, (d, _) in enumerate(sortedTime) if d.month == 1)
        sortedTime.insert(breakpointIdx, (date(sortedTime[breakpointIdx-1][0].year, 12, 31), float('nan')))
        sortedTime.insert(breakpointIdx+1, (date(sortedTime[breakpointIdx][0].year, 1, 1), float('nan')))
        dates, counts = zip(*sortedTime)
        axs[2].set_ylim(0, 60)        # Set the y-axis limits
        axs[2].set_yticks(range(0, 61, 5)) 
        axs[2].plot(dates, counts, color='b')
        axs[2].fill_between(dates, counts, color='b', alpha=0.2)
        months = mdates.MonthLocator(bymonth=[10, 11, 12, 1])
        month_fmt = mdates.DateFormatter('%b')
        axs[2].xaxis.set_major_locator(months)
        axs[2].xaxis.set_major_formatter(month_fmt)
        axs[2].set_ylabel('Average value per customer')
        # Displaying all plots
        plt.tight_layout()
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()