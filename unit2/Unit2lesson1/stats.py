from scipy import stats
import pandas as pd
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = [i.split(', ') for i in data.splitlines()]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

#print df

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


alcmean = df['Alcohol'].mean() # 5.4436363636363634
alcmed = df['Alcohol'].median() # 5.63
# If all numbers occur equally often, stats.mode() will return the smallest number
alcmod = stats.mode(df['Alcohol'])[0][0] # 4.02
alcrang =  max(df['Alcohol']) - min(df['Alcohol']) # 2.4500000000000002
alcstd = df['Alcohol'].std() # 0.79776278087252406
alcvar = df['Alcohol'].var() # 0.63642545454546284


tobmean = df['Tobacco'].mean() # 3.6181818181818186
tobmed = df['Tobacco'].median() # 3.53
tobmod = stats.mode(df['Tobacco'])[0][0] # 2.71
tobrang = max(df['Tobacco']) - min(df['Tobacco']) # 1.8499999999999996
tobstd = df['Tobacco'].std() # 0.59070835751355388
tobvar = df['Tobacco'].var() # 0.3489363636363606

# Challenge:
# Print the mean, median, mode, range, variance, and standard deviation for
# the Alcohol and Tobacco dataset with full text:
# (ex. "The range for the Alcohol and Tobacco dataset is ...").

import numpy as np
table = np.zeros((6,0))

index = np.array(['mean', 'median', 'mode', 'range', 'standard deviation', 'variance'])
index[:, np.newaxis]

alcohols = np.array([alcmean, alcmed, alcmod, alcrang, alcstd, alcvar])
alcohols[:,np.newaxis]

tobaccos = np.array([tobmean, tobmed, tobmod, tobrang, tobstd, tobvar])
tobaccos[:, np.newaxis]

newtable = np.c_[index, alcohols, tobaccos, table]

for (x,y,z) in newtable:
    print ('The {0} for the alcohol dataset is {1}.'.format(x,y))
    print ('The {0} for the tobacco dataset is {1}.'.format(x,z))
