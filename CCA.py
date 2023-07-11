
import pandas as pd
from sklearn.cross_decomposition import CCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

link2data = "/Users/sebastian/Downloads/archive/CCA/test.csv"
df = pd.read_csv(link2data)
df =df.dropna()
df.head()

X = df[['Lon','Lat']]
print(X.head())
lonMean = X['Lon'].mean()
lonStd = X['Lon'].std()

latMean = X['Lat'].mean()
latStd = X['Lat'].std()

X.loc[:, 'Lon'] = (X.loc[:, 'Lon'] - lonMean) / lonStd
X.loc[:, 'Lat'] = (X.loc[:, 'Lat'] - latMean) / latStd



print(X.head())

Y = df[['#Time', '#Date']]
print(Y.head())

ca = CCA(n_components=2)
ca.fit(X, Y)
X_c, Y_c = ca.transform(X, Y)
print(X_c.shape)
print(Y_c.shape)

print("end of CCA")

cc_res = pd.DataFrame({"CCX_1":X_c[:, 0],
                       "CCY_1":Y_c[:, 0],
                       "CCX_2":X_c[:, 1],
                       "CCY_2":Y_c[:, 1]})

print(cc_res.head())

first = np.corrcoef(X_c[:, 0], Y_c[:, 0])
print(first)

second = np.corrcoef(X_c[:, 1], Y_c[:, 1])
print(second)

sns.set_context("talk", font_scale=1.2)
plt.figure(figsize=(10,8))
sns.scatterplot(x="CCX_1",
                y="CCY_1",
                data=cc_res)
plt.title('Comp. 1, corr = %.2f' %
         np.corrcoef(X_c[:, 0], Y_c[:, 0])[0, 1])
plt.show()

plt.figure(figsize=(10,8))
sns.boxplot(x="Species",
            y="CCX_1",
            data=cc_res)
sns.stripplot(x="Species",
              y="CCX_1",
              data=cc_res)
plt.show()