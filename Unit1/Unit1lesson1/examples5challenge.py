# Challenge
# The data world is now your oyster. Play with some of the other population data
# and see what you come up with. Try and calculate the population change
# between 2010 and 2100. Remember the lesson about doing integer divison.
# Convert one of the numbers to floating point decimal by using the float()
# function. Which continent is estimated to grow the most in the next 90 years?
#
# Try and calculate the population density (total national population divided by
# the total land area and remember to convert at least one number to float).
# Which continent was most densely populated in 2010?

import pandas as pd

data = pd.read_csv('lecz-urban-rural-population-land-area-estimates_country-1km-90m.csv')

populations = data[data['ElevationZone']=='Total National Population'][['Country', 'Population2010', 'Population2100']].groupby('Country').sum()

populations['PopulationChange'] = populations['Population2100'] - populations['Population2010']
print populations[['PopulationChange']]

# with open('national_population.csv', 'w') as outputFile:
#     outputFile.write('continent,2010_population\n')
#     for k,v in population_dict.iteritems():
#         outputFile.write(k + ',' + str(v) + '\n')
