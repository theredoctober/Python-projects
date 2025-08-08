# Main Code

from heartbeat_utils import read_heartbeat_csv


# Capture ECG data from sheet and convert to dataframe

df = read_heartbeat_csv("data/sample_heartbeat.csv")
if df is not None:
    print(df.head())
