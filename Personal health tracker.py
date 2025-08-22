import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

FILE = "health_data.csv"

def add_entry(steps, calories, water, sleep, pulse, heart_rate):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), steps, calories, water, sleep, pulse, heart_rate])
    print("Entry added successfully!")

def view_progress():
    dates, steps, calories, pulse_rates, heart_rates = [], [], [], [], []
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader, None) 
        for row in reader:
            dates.append(row[0])
            steps.append(int(row[1]))
            calories.append(int(row[2]))
            pulse_rates.append(int(row[5]))
            heart_rates.append(int(row[6]))

    x = np.arange(len(dates))  
    width = 0.18  


    plt.bar(x - 2*width, steps, width, label="Steps")
    plt.bar(x - width, calories, width, label="Calories Burned")
    plt.bar(x, pulse_rates, width, label="Pulse Rate (bpm)")
    plt.bar(x + width, heart_rates, width, label="Heart Rate (bpm)")

    plt.xticks(x, dates, rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.legend()
    plt.title("Health Progress Tracker (Bar Graph)")
    plt.tight_layout()
    plt.show()

try:
    with open(FILE, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Steps", "Calories", "Water(L)", "Sleep(Hrs)", "Pulse Rate", "Heart Rate"])
except FileExistsError:
    pass

add_entry(5000, 200, 2, 7, 72, 78)
add_entry(7000, 350, 2.5, 6, 75, 80)
view_progress()
