#test script functions vs jupiter cells
import pandas as pd
import sys
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("../author_algo/data/df.csv", nrows=200)

class desciptives:

    def summarize():
        return print(df.head())

    def types():
        print(df.dtypes)
    
    def describe():
        print(df.describe())

class plotting:
    
    def plot():
        plt = sns.violinplot(x="type", y="id", 
                             hue="age",
               split=True, inner="quart",
               data=df)
        plt.figure.savefig('plt1.png')
    
    def plot_2():
        plt = sns.scatterplot(x="id", y="age", 
                              data=df)
        plt.figure.savefig('data/plt2.png')