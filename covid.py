import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('covid_19_india(in).csv')
print(df.to_string())
x=df['Confirmed']
y=df['Deaths']
plt.plot(x,y)
plt.title("Covid-19 cases analysis")
plt.xlabel("No. of totalcases")
plt.ylabel("Total population")
plt.show()