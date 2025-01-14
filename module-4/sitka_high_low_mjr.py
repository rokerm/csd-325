import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
from matplotlib import pyplot as plt

#File Location
filename = 'sitka_weather_2018_simple.csv'

#Made this into a function to read file and extract data. 
def read_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file. Note modified code so it also extracts data for low temps
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


# Plot the temperatures.
def plot_temperatures(dates, temps, title, color):
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot. Title is 
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Main menu loop
def main_menu():
    dates, highs, lows = read_weather_data(filename)

    while True:
        print("\nWeather Data Menu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("Thank you for using the Weather Data Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main_menu()
