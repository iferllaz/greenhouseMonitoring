import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

# Load dataset
df = pd.read_csv('../data/agent_data.csv')

# Add headers
df.columns = ['Temp', 'Hum', 'sMois', 'Lum','phWater', 'phSoil']

# Show top 5 lines and some properties
print("\n> Collected data")
print("\n>",df.head())

## TEMPERATURE
# Histogram
plt.figure(figsize=(3, 3))
plt.title("Histogram")
plt.hist(df['Temp'], color = 'blue')
plt.show()

# Scatterplot
plt.figure(figsize=(3, 3))
plt.title("Scatterplot")
plt.scatter(df['Temp'], df['Hum'])
plt.show()

#Boxplots
plt.figure(figsize=(3, 3))
plt.title("Boxplots")
sns.boxplot(x=df['Temp'])
plt.show()

# Calculate the mean
mean_temp = df['Temp'].mean()
print("\n> Mean: ", mean_temp)

# Calculate the median
median_temp = df['Temp'].median()
print("\n> Median: ", median_temp)

# Calculate the mode
mode_temp = df['Temp'].mode()
print("\n> Mode: ",mode_temp)

# Get a statistical summary of the 'Temp' column
temp_summary = df['Temp'].describe()
print("\n\nSumary\n ", temp_summary)

## HUMIDITY
# Histogram
plt.figure(figsize=(3, 3))
plt.title("Histogram")
plt.hist(df['Hum'], color = 'green')
plt.show()

# Scatterplot
plt.figure(figsize=(3, 3))
plt.title("Scatterplot")
plt.scatter(df['Hum'], df['sMois'], color = 'green' )
plt.show()

#Boxplots
plt.figure(figsize=(3, 3))
plt.title("Boxplots")
sns.boxplot(x=df['Hum'], color = 'green')
plt.show()

# Calculate the mean
mean_Hum = df['Hum'].mean()
print("\n> Mean: ", mean_Hum)

# Calculate the median
median_Hum = df['Hum'].median()
print("\n> Median: ", median_Hum)

# Calculate the mode
mode_Hum = df['Hum'].mode()
print("\n> Mode: ", mode_Hum)

# Get a statistical summary of the 'Hum' column
Hum_summary = df['Hum'].describe()
print("\n\nSumary\n ", Hum_summary)


# LUMINOSITY
# Histogram
plt.figure(figsize=(3, 3))
plt.title("Histogram")
plt.hist(df['Lum'], color = 'yellow')
plt.show()

# Scatterplot
plt.figure(figsize=(3, 3))
plt.title("Scatterplot")
plt.scatter(df['Lum'], df['Temp'], color = 'yellow' )
plt.show()

#Boxplots
plt.figure(figsize=(3, 3))
plt.title("Boxplots")
sns.boxplot(x=df['Lum'], color = 'yellow')
plt.show()

# Calculate the mean
mean_Lum = df['Lum'].mean()
print("\n> Mean: ", mean_Lum)

# Calculate the median
median_Lum = df['Lum'].median()
print("\n> Median: ", median_Lum)

# Calculate the mode
mode_Lum = df['Lum'].mode()
print("\n> Mode: ", mode_Lum)

# Get a statistical summary of the 'Lum' column
Lum_summary = df['Lum'].describe()
print("\n\nSumary\n ", Lum_summary)


## SOIL MOISTURE
# Histogram
plt.figure(figsize=(3, 3))
plt.title("Histogram")
plt.hist(df['sMois'], color = 'brown')
plt.show()

# Scatterplot
plt.figure(figsize=(3, 3))
plt.title("Scatterplot")
plt.scatter(df['sMois'], df['Hum'], color = 'brown' )
plt.show()


#Boxplots
plt.figure(figsize=(3, 3))
plt.title("Boxplots")
sns.boxplot(x=df['sMois'], color = 'brown')
plt.show()

# Calculate the mean
mean_sMois = df['sMois'].mean()
print("\n> Mean: ", mean_sMois)

# Calculate the median
median_sMois = df['sMois'].median()
print("\n> Median: ", median_sMois)

# Calculate the mode
mode_sMois = df['sMois'].mode()
print("\n> Mode: ", mode_sMois)

# Get a statistical summary of the 'sMois' column
sMois_summary = df['sMois'].describe()
print("\n\nSumary\n ", sMois_summary)


## WATER PH
# Histogram
plt.figure(figsize=(3, 3))
plt.title("Histogram")
plt.hist(df['phWater'], color = 'aqua')
plt.show()

# Scatterplot
plt.figure(figsize=(3, 3))
plt.title("Scatterplot")
plt.scatter(df['phWater'], df['Hum'], color = 'aqua' )
plt.show()

#Boxplots
plt.figure(figsize=(3, 3))
plt.title("Boxplots")
sns.boxplot(x=df['phWater'], color = 'aqua')
plt.show()

# Calculate the mean
mean_phWater = df['phWater'].mean()
print("\n> Mean: ", mean_phWater)

# Calculate the median
median_phWater = df['phWater'].median()
print("\n> Median: ", median_phWater)

# Calculate the mode
mode_phWater = df['phWater'].mode()
print("\n> Mode: ", mode_phWater)

# Get a statistical summary of the 'phWater' column
phWater_summary = df['phWater'].describe()
print("\n\nSumary\n ", phWater_summary)

## SOIL PH
# Histogram
plt.figure(figsize=(3, 3))
plt.title("Histogram")
plt.hist(df['phSoil'], color = 'orange')
plt.show()

# Scatterplot
plt.figure(figsize=(3, 3))
plt.title("Scatterplot")
plt.scatter(df['phSoil'], df['Temp'], color = 'orange' )
plt.show()

#Boxplots
plt.figure(figsize=(3, 3))
plt.title("Boxplots")
sns.boxplot(x=df['phSoil'], color = 'orange')
plt.show()

# Calculate the mean
mean_phSoil = df['phSoil'].mean()
print("\n> Mean: ", mean_phSoil)

# Calculate the median
median_phSoil = df['phSoil'].median()
print("\n> Median: ", median_phSoil)

# Calculate the mode
mode_phSoil = df['phSoil'].mode()
print("\n> Mode: ", mode_phSoil)

# Get a statistical summary of the 'phSoil' column
phSoil_summary = df['phSoil'].describe()
print("\n\nSumary\n ", phSoil_summary)

