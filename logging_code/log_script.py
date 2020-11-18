import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

print('>> process started')
print('-------------------------------')

# read and log data
df = pd.read_csv('df.csv')
df.describe().transpose().to_csv('log.csv', mode='a', header=False)
print('>> data loaded and logged')
print('-------------------------------')

# load log
df = pd.read_csv('log.csv')
df = df.reset_index()
print('>> log loaded')
print('-------------------------------')

# plot log
sns.lineplot(data=df, x="index", y="mean", hue="Unnamed: 0")
plt.savefig("plot.png")
print('>> log plotting done')
