import pandas as pd
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt
loansData = pd.read_csv('loansData_clean.csv')

loansData['IR_TF'] = loansData['Interest.Rate'] < 12

# print loansData[loansData['Interest.Rate'] == 10].head() # should all be True
# print loansData[loansData['Interest.Rate'] == 13].head() # should all be False
loansData['intercept'] = 1

#print loansData

#ind_vars = loansData.columns.values
ind_vars = ['intercept', 'Amount.Requested', 'FICO.Score']
#print ind_vars

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])


result = logit.fit()
#print result

coeff = result.params
print coeff

def int_rate(coeff, amountreq, ficoscore):
    return - coeff['intercept'] - (coeff['FICO.Score']*ficoscore) - (coeff['Amount.Requested']*amountreq)

def logistic_function(coeff, amountreq, ficoscore):
    return 1/(1 + math.exp(int_rate(coeff, amountreq, ficoscore)))

res = logistic_function(coeff, 10000, 750)
print res

ficos, probs = [],[]

for ficoscore in range (550,950):
    ficos.append(ficoscore)
    probs.append(logistic_function(coeff,10000,ficoscore))

plt.plot(ficos,probs,'r-')
plt.title('Plot of Probability of getting a loan vs. FICO score')
plt.xlabel('FICO score')
plt.ylabel('Probability of getting loan')
plt.show()

def pred(coeff, amountreq, ficoscore):
    yesno = logistic_function(coeff, amountreq, ficoscore) > 0.7
    if yesno == 1:
        print "Loan granted"
    else:
        print "Loan not granted"

test = pred(coeff,10000,750)
print test
