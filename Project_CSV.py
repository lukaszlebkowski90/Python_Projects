import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Pobranie dat oraz najwyższych oraz najniższych temperatur pliku
    dates, highs, lows = [], [] ,[]
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"brak danych dla {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


#Wygenerowanie wykresu najniższych i najwyższych temperatur
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(8,5), dpi=128)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Formatowanie wykresu
ax.set_title("Najwyższa i najniższa temperatura dnia - 2018\nDolina Śmierci, Kalifornia", fontsize=18)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)

plt.show()

