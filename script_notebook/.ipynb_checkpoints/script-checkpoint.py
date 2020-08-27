#test script functions vs jupiter cells
import pandas as pd
import sys
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("PS_20174392719_1491204439457_log.csv", nrows=200)

class desciptives:

    def summarize():
        return print(df.head())

    def types():
        print(df.dtypes)
    
    def describe():
        print(df.describe())

class plotting:
    
    def plot():
        plt = sns.violinplot(x="type", y="newbalanceOrig", 
                             hue="isFraud",
               split=True, inner="quart",
               data=df)
        plt.figure.savefig('plt.png')
    
    def plot_2():
        plt = sns.scatterplot(x="oldbalanceOrg", y="newbalanceOrig", 
                              data=df)
        plt.figure.savefig('plt.png')