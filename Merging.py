# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
import os


# Get a list of all CSV files in the folder
csv_files = glob.glob('/Users/sebastian/Downloads/archive/CCA/*.csv')

# Create an empty list to store DataFrames
dfs = []

# Read each CSV file into a DataFrame and append to the list
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('/Users/sebastian/Downloads/archive/CCA/merged Uber Data.csv', index=False)



# Press the green button in the gutter to run the script.
