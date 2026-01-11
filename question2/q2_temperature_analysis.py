import os
import pandas as pd
import numpy as np

folder_path = "temperatures"

# Australian seasons mapping
season_map = {
    "December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"
}

all_data = []

# Read all CSV files
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)

        # Keep only station name + months
        months = list(season_map.keys())
        df_months = df[["STATION_NAME"] + months]
        df_months["SourceFile"] = file  # optional, track file
        all_data.append(df_months)

# Combine all CSVs
data = pd.concat(all_data, ignore_index=True)

# Melt the months into rows
data_melted = data.melt(id_vars=["STATION_NAME"], value_vars=list(season_map.keys()),
                        var_name="Month", value_name="Temperature")

data_melted = data_melted.dropna(subset=["Temperature"])

# Map month to season
data_melted["Season"] = data_melted["Month"].map(season_map)

# -------- Seasonal Average --------
season_avg = data_melted.groupby("Season")["Temperature"].mean()
with open("average_temp.txt", "w") as f:
    for season, temp in season_avg.items():
        f.write(f"{season}: {temp:.1f}°C\n")

# -------- Temperature Range per Station --------
ranges = data_melted.groupby("STATION_NAME")["Temperature"].agg(["max", "min"])
ranges["range"] = ranges["max"] - ranges["min"]
max_range = ranges["range"].max()

with open("largest_temp_range_station.txt", "w") as f:
    for station, row in ranges[ranges["range"] == max_range].iterrows():
        f.write(
            f"Station {station}: Range {row['range']:.1f}°C "
            f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
        )

# -------- Temperature Stability --------
std_dev = data_melted.groupby("STATION_NAME")["Temperature"].std()
min_std = std_dev.min()
max_std = std_dev.max()

with open("temperature_stability_stations.txt", "w") as f:
    for station in std_dev[std_dev == min_std].index:
        f.write(f"Most Stable: Station {station}: StdDev {min_std:.1f}°C\n")
    for station in std_dev[std_dev == max_std].index:
        f.write(f"Most Variable: Station {station}: StdDev {max_std:.1f}°C\n")

print("Question 2 analysis completed successfully.")
