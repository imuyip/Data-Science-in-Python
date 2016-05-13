import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Funded.By.Investors')

plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()
