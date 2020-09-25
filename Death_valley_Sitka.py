import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_sitka_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
sitka_csv_file = csv.reader(open_sitka_file, delimiter=",")

header_row = next(csv_file)
sitka_header = next(sitka_csv_file)

highs = []
lows = []
dates = []
sitka_high = []
sitka_low = []
sitka_dates = []

for row in sitka_csv_file:
    try:
        s_highs = int(row[sitka_header.index('TMAX')])
        s_lows = int(row[sitka_header.index('TMIN')])
        the_date = datetime.strptime(
            row[sitka_header.index('DATE')], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        sitka_high.append(s_highs)
        sitka_low.append(s_lows)
        sitka_dates.append(the_date)

for row in csv_file:
    try:
        high = int(row[header_row.index('TMAX')])
        low = int(row[header_row.index('TMIN')])
        current_date = datetime.strptime(
            row[header_row.index('DATE')], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

fig, ax = plt.subplots(2)

# plt.plot(dates, highs, c="red", alpha=0.5)
# plt.plot(dates, lows, c="blue", alpha=0.5)

ax[0].plot(sitka_dates, sitka_high, c="red", alpha=0.5)
ax[0].plot(sitka_dates, sitka_low, c="blue", alpha=0.5)

ax[1].plot(dates, highs, c="red", alpha=0.5)
ax[1].plot(dates, lows, c="blue", alpha=0.5)

plt.xlabel("", fontsize=2)

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax[0].fill_between(sitka_dates, sitka_high, sitka_low,
                   facecolor="blue", alpha=0.1)

ax[0].set_title('SITKA AIRPORT, AK US')
ax[1].set_title('DEATH VALLEY, CA US')

fig.suptitle(
    'Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US')

ax[1].tick_params(axis="both", labelsize=6)
ax[0].tick_params(axis="both", labelsize=6)


fig.autofmt_xdate()

plt.show()
