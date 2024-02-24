import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def extract_names_and_dates_from_json(json_file):
    # Read JSON data
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    # Initialize lists to store names and dates
    names = []
    dates = []

    # Extract names and dates from JSON data
    for experiencia in json_data['experiencias']:
        cargo = experiencia['cargo']
        periodo = experiencia['periodo']
        empresa = experiencia['empresa']
        
        # Extract version from the cargo field
        version = cargo.split()[-1]
        
        # Use the first year of the period as the date
        year = int(periodo.split()[0])
        date = f"{year}-01-01"
        
        # Append to lists
        names.append(empresa)
        dates.append(date)
    
    return names, dates

def plot_timeline(names, dates):
    # Convert date strings to datetime objects
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates)/6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.set(title="Experiences Timeline")

    # Plot the vertical stems
    ax.vlines(dates, 0, levels, color="tab:red")

    # Plot markers on the baseline
    ax.plot(dates, np.zeros_like(dates), "-o", color="k", markerfacecolor="w")

    # Annotate the lines
    for d, l, r in zip(dates, levels, names):
        ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="right", verticalalignment="bottom" if l > 0 else "top")

    # Format x-axis with 4 month intervals
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=12))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

    # Remove y-axis and spines
    ax.yaxis.set_visible(False)
    ax.spines[["left", "top", "right"]].set_visible(False)

    ax.margins(y=0.1)
    plt.show()

# Hardcoded data
names_hardcoded = ['Corrente','DSOP Educação Financeira', 'LexisNexis Risk Solutions', 'DSOP Educação Financeira', 'DXC Technology', 'Accesstage S/A', 'Interfloat HZ CCTVM', 'Tata Consultancy Services', 'EDS - Electronic Data Systems do Brasil', 'Hospital do Sepaco', 'Hast Sistemas Empresariais']
dates_hardcoded = ['2024-01-01','2023-01-01', '2021-01-01', '2021-01-01', '2011-01-01', '2010-01-01', '2008-01-01', '2006-01-01', '2003-01-01', '1999-01-01', '1996-01-01']

# Extract names and dates from JSON file
names_json, dates_json = extract_names_and_dates_from_json('dados.json')

# Plot timelines
# plot_timeline(names_hardcoded, dates_hardcoded)
plot_timeline(names_json, dates_json)
