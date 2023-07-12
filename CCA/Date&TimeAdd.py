import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/sebastian/Downloads/archive/CCA/merged Uber Data.csv')

# Split the datetime values by the space character and select the time component
df['Time'] = df['Date/Time'].apply(lambda x: x.split(' ')[1])
df['Date'] = df['Date/Time'].apply(lambda x: x.split(' ')[0])
df['#Date'] = df['Date'].str.replace('/', '')
df['#Date'] = df['#Date'].astype('int')
df['#Time'] = df['Time'].str.replace(':', '')
df['#Tate'] = df['#Time'].astype('int')





# Write the updated DataFrame to a new CSV file
df.to_csv('/Users/sebastian/Downloads/archive/CCA/test.csv', index=False)
