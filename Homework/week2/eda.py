# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
import json

filename = r"D:\Meike\Documenten\Universiteit\Master\DataProcessing\Data-processing-2019\Homework\week2\input.csv"

# Read data from filename using Pandas
data = pd.read_csv(filename)

# drop unnessecary columns
to_drop = ['Population','Area (sq. mi.)', 'Coastline (coast/area ratio)','Net migration',
            'Literacy (%)', 'Phones (per 1000)', 'Arable (%)', 'Crops (%)','Other (%)',
            'Climate', 'Birthrate', 'Deathrate', 'Agriculture', 'Industry', 'Service']

data.drop(to_drop, inplace=True, axis=1)

# Drop rows with any empty cells or cells with the value unknown
data = data.dropna()
data = data[data['GDP ($ per capita) dollars'] != 'unknown']
data = data[data['Country'] != 'unknown']
data = data[data['Region'] != 'unknown']
data = data[data['Pop. Density (per sq. mi.)'] != 'unknown']
data = data[data['Infant mortality (per 1000 births)'] != 'unknown']

# Delete blankspaces
data["Country"]= data["Country"].str.strip()
data["Region"]= data["Region"].str.rstrip()

# Replace comma's with dots
data = data.stack().str.replace(',','.').unstack()

#Remove non numeric characters from GDP
data['GDP ($ per capita) dollars'] = data['GDP ($ per capita) dollars'].str.extract('(\d+)', expand=False)

# Change dtype of infant mortality, Pop. Density and GDP
data.loc[:,'Pop. Density (per sq. mi.)'] = np.asarray(data.loc[:,'Pop. Density (per sq. mi.)'], dtype='float64')
data.loc[:,'Infant mortality (per 1000 births)'] = np.asarray(data.loc[:,'Infant mortality (per 1000 births)'], dtype='float64')
data.loc[:,'GDP ($ per capita) dollars'] = np.asarray(data.loc[:,'GDP ($ per capita) dollars'], dtype='int64')

# Use the country as index
data = data.set_index(data['Country'])

# Delete country as colums
data.drop('Country', inplace=True, axis=1)


"""
Central Tendency
"""

# calculate and print mean, median and mode for GDP
GDP = data.loc[:,"GDP ($ per capita) dollars"]
mean_GDP = GDP.mean()
print("Mean GDP ($ per capita) dollar:", mean_GDP)
median_GDP = GDP.median()
print("Median GDP ($ per capita) dollar:", median_GDP)
mode_GDP = GDP.mode()
print("Mode GDP ($ per capita) dollar:", mode_GDP)

# Calculate standard deviation
std_GDP = GDP.std()
print("Standard Deviation of GDP ($ per capita) dollar:", std_GDP)

# Make a histogram of the std_GDP
n_bins = 75
plt.hist(GDP, bins = n_bins)
plt.xlabel("GDP ($ per capita) dollar")
plt.ylabel('Amount of countries')
plt.xlim(0, 425000)
plt.show()

"""
Five Number Summary
"""

infant_mortality = data.loc[:,'Infant mortality (per 1000 births)']

# Calculating quantiles of Infant mortality
quartiles = np.quantile(infant_mortality, [.25, .5, .75])
print("First quartile of infant mortality (per 1000 births):", quartiles[0])
print("Median of infant mortality (per 1000 births):", quartiles[1])
print("Third quartile of infant mortality (per 1000 births):", quartiles[2])

# Calculating the minimum Infant mortality
min_infant= infant_mortality.min()
print("Minimum infant mortality (per 1000 births):", min_infant)

# Calculating the maximum Infant mortality
max_infant= infant_mortality.max()
print("Maximum infant mortality (per 1000 births):", max_infant)

# Plot a boxplot of the infant mortality
data.boxplot(column = 'Infant mortality (per 1000 births)', grid = False)
plt.ylim(0, 200)
plt.show()


"""
Converting
"""

# Set path for JSON file
path = r"D:\Meike\Documenten\Universiteit\Master\DataProcessing\Data-processing-2019\Homework\week2\input.json"

# Create JSON file
data.to_json(path_or_buf = path, orient = 'index' )
