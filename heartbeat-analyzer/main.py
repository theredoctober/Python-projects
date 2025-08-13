# Main Code

from heartbeat_utils import read_heartbeat_csv
from heartbeat_utils import plot_heartbeat


# Capture ECG data from sheet and convert to dataframe

df = read_heartbeat_csv("data/sample_heartbeat.csv")


if df is not None:
    # Print starting rows of the ECG data
    print(df.head())

    # Plot the dataframe ECG data as voltage vs time graph
    plot_heartbeat(df)






