#Add function to read heartbeat data

import pandas as pd
import matplotlib.pyplot as plt

def read_heartbeat_csv(filepath):
    """
    Reads heartbeat csv and returns a dataframe
    """
    try:

        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"file not found: {filepath}")
        return None


def plot_heartbeat(df):
    """
    Plots heartbeat signal from a DataFrame with 'Time (s)' and 'Voltage (mV)' columns.
    """
    try:
        # Getting the column names from data file
        x_col = df.columns[0]
        y_col = df.columns[1]

        plt.figure(figsize=(10,4))
        #plt.plot(df["Time (s)"],df["Voltage (mV)"],label='HeartBeat signal')
        plt.plot(df.iloc[:,0], df.iloc[:,1],label='HeartBeat signal')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        #plt.ylabel(""Voltage (mV)")
        plt.title("HeartBeat signal plot")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print("Data not in plottable format")