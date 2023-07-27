import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/sebastian/Downloads/archive/CCA/merged Uber Data.csv')

print(df.head())


# Split the datetime values by the space character and select the time component
df[['Date', 'Time']] = df['Date/Time'].str.split(' ', expand=True)

#df[['Hours', 'Minutes','Sec']] = df['Time'].str.split(':',expand=True)
#df[['Month', 'Day','Year']] = df['Date'].str.split('/',expand=True)


print(df.head())

# Extract the hour and minute portion from the datetime values
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

df['#Time'] = df['Time'].dt.strftime('%H%M')

# Convert the 'Time' column to integer dtype
df['#Time'] = df['#Time'].astype(int)

print(df.head())

temp = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Weekday'] = temp.dt.weekday.astype(int)

df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time

print(df.head())
# Write the updated DataFrame to a new CSV file
df.to_csv('/Users/sebastian/Downloads/archive/CCA/test.csv', index=False)