import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
loansData = pd.read_csv('loansData.csv')

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(
    lambda x:float(x.rstrip('%'))
)

loansData['Loan.Length'] = loansData['Loan.Length'].map(
    lambda x:float(x.rstrip(' months'))
)


loansData['FICO.Range'] = loansData['FICO.Range'].map(
    lambda x:tuple(x.split('-'))
)

loansData['FICO.Score'] = loansData['FICO.Range'].map(
    lambda x:float(x[0])
)

print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Score'][0:5]

# plt.figure()
# p = loansData['FICO.Score'].hist()
# plt.show()
#
# plt.figure()
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10),diagonal='hist')
# plt.show()

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

# X = sm.add_constant(x)
# model = sm.OLS(y,X)
# f = model.fit()

#print f.summary()

loansData.to_csv('loansData_clean.csv', header=True, index=False)
