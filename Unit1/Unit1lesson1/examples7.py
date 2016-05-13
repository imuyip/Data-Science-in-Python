import pandas as pd

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

print list(input_dataframe)
#list(input_dataframe.columns.values)
print input_dataframe[0:10]
