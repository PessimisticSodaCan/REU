import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/sebastian/Downloads/archive/CCA/merged Uber Data.csv')

print(df.head())

# Split the datetime values by the space character and select the time component
df[['Date', 'Time']] = df['Date/Time'].str.split(' ', expand=True)

df[['Hours', 'Minutes','Sec']] = df['Time'].str.split(':',expand=True)
df[['Month', 'Day','Year']] = df['Date'].str.split('/',expand=True)



# Write the updated DataFrame to a new CSV file
df.to_csv('/Users/sebastian/Downloads/archive/CCA/test.csv', index=False)