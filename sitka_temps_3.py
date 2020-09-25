import matplotlib.pyplot as plt
import csv
from datetime import datetime


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

highs = []
lows = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.title("Daily High and Low Temps, 2018", fontsize=16)
plt.xlabel("", fontsize=12)

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
