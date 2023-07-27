import numpy as np
import tensorly as tl
import pandas as pd
import csv

link2data = "/Users/sebastian/Downloads/archive/CCA/test.csv"

df = pd.read_csv(link2data).dropna()
df.head()

dimension = input("what dimension do you want to use?")
dimension = int(dimension)

minT = df['#Time'].min()
minLon = int(df['Lon'].min() * 1000)
minLat = int(df['Lat'].min() * 1000)


maxT = df['#Time'].max()
maxLon = int(df['Lon'].max() * 1000)
maxLat = int(df['Lat'].max() * 1000)


RangeT = (maxT - minT)/dimension
RangeLon = (maxLon - minLon)/dimension
RangeLat = (maxLat - minLat)/dimension
#(Time,weekday,lat,long)
shape = (dimension + 1, 7, dimension + 1, dimension + 1)
# Initialize a numpy array with zeros
arr = np.zeros(shape)
X = tl.tensor(arr)

# Open the CSV file
i = 0
with open(link2data, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate over each row
    for row in csv_reader:
        # Process each row
        if i == 0:
            i = i + 1
            continue

        index = (int((int(row[6]) - minT)/RangeT), int(row[7]), int((int(1000 * float(row[1])) - minLat)/RangeLat), int((int(1000 * float(row[2])) - minLon)/RangeLon) )
        X[index] =+ 1
        # Access individual values using row[index]

    X_numpy = tl.to_numpy(X)
    count = 0
    # Loop through the array
    for i in range(X_numpy.shape[0]):
        for j in range(X_numpy.shape[1]):
            for k in range(X_numpy.shape[2]):
                for l in range(X_numpy.shape[3]):
                    # Access and process each element
                    element = X_numpy[i, j, k, l]
                    if element == 0:
                        count += 1
                    else:
                        print(element)
                        print([i, j, k, l])





