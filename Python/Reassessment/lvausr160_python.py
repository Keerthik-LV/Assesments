# -*- coding: utf-8 -*-
"""LVAUSR160_Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17B4q6yaGs92U46UV5aeGQJd0vcnZdPVs

**1. Load and Examining Dataset**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Cuisine_rating.csv')

print(df.columns)

# convert specific columns
df['Location'] = pd.to_numeric(df['Location'], errors='coerce')
df['Gender'] = pd.to_numeric(df['Gender'], errors='coerce')
df['Marital Status'] = pd.to_numeric(df['Marital Status'], errors='coerce')
df['Activity'] = pd.to_numeric(df['Activity'], errors='coerce')
df['Cuisines'] = pd.to_numeric(df['Cuisines'], errors='coerce')
df['Alcohol '] = pd.to_numeric(df['Alcohol '], errors='coerce')
df['Smoker'] = pd.to_numeric(df['Smoker'], errors='coerce')
df['Often A S'] = pd.to_numeric(df['Often A S'], errors='coerce')

# Get the number of rows and columns
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

# Check the data types of the columns
print("\nData types:")
print(df.dtypes)

# Select only numeric columns for quartile calculation
numeric_columns = df.select_dtypes(include=['int', 'float'])

# Calculate quartiles for numeric columns
quartiles = numeric_columns.quantile([0.25, 0.5, 0.75])
print("\nQuartiles:")
print(quartiles)

# Count the number of missing values per column
print("\nMissing values:")
print(df.isnull().sum())

"""**2. Data Cleaning**"""

import pandas as pd
import numpy as np
# Create a sample DataFrame with missing values
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, np.nan, 5],
        'D': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull())

# Drop rows with missing values
df.dropna(inplace=True)

# Drop columns with missing values
df.dropna(axis=1, inplace=True)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Fill missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Forward fill missing values
df.fillna(method='ffill', inplace=True)

# Backward fill missing values
df.fillna(method='bfill', inplace=True)

"""**3. Descriptive Statistics**"""

# Convert non-numeric columns to numeric where possible
for col in df.columns:
    if df[col].dtype == 'object':  # Check if the column is of type object (non-numeric)
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, setting errors to NaN
        except ValueError:
            pass

# Calculate mean
mean_values = df.mean()

print("Mean values:")
print(mean_values)

# Calculate median
median_values = df.median()

print("\nMedian values:")
print(median_values)

# Calculate variance
variance_values = df.var()

print("\nVariance values:")
print(variance_values)

# Calculate standard deviation
std_deviation_values = df.std()

print("\nStandard Deviation values:")
print(std_deviation_values)

# Calculate range
range_values = df.max() - df.min()

print("\nRange values:")
print(range_values)

"""**4. Data Visualization**"""

# Inspect the first few rows to understand the column names
print(df.head())

# Convert non-numeric columns to numeric where possible
for col in df.columns:
    if df[col].dtype == 'object':  # Check if the column is of type object (non-numeric)
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, setting errors to NaN
        except ValueError:
            pass

# Histograms
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

plt.figure(figsize=(20, 15))
df.hist(bins=50, figsize=(20, 15))
plt.suptitle('Histograms of Numeric Columns')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Bar Charts
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

plt.figure(figsize=(7, 4))
if 'Gender' in df.columns:
    df['Gender'].value_counts().plot(kind='bar', color=['Green', 'Lightgreen'])
    plt.title('Bar Chart of Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.xticks(rotation=0)  # Rotate x-axis labels to horizontal
    plt.show()
else:
    print("The column 'Gender' is not present in the dataset.")

"""**5. Identifying Relationships**"""

# convert specific columns
df['Location'] = pd.to_numeric(df['Location'], errors='coerce')
df['Gender'] = pd.to_numeric(df['Gender'], errors='coerce')
df['Marital Status'] = pd.to_numeric(df['Marital Status'], errors='coerce')
df['Activity'] = pd.to_numeric(df['Activity'], errors='coerce')
df['Cuisines'] = pd.to_numeric(df['Cuisines'], errors='coerce')
df['Alcohol '] = pd.to_numeric(df['Alcohol '], errors='coerce')
df['Smoker'] = pd.to_numeric(df['Smoker'], errors='coerce')
df['Often A S'] = pd.to_numeric(df['Often A S'], errors='coerce')

corr_matrix = df.corr()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 15))
sns.heatmap(corr_matrix, annot=True, cmap='Greens', square=True)
plt.title('Correlation Matrix')
plt.show()

#Outliers Detection
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

# Convert non-numeric columns to numeric where possible
for col in df.columns:
    if df[col].dtype == 'object':  # Check if the column is of type object (non-numeric)
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, setting errors to NaN
        except ValueError:
            pass

# Visualize potential outliers using box plots
plt.figure(figsize=(7, 8))
df.boxplot()
plt.xticks(rotation=45)
plt.title('Box Plot of Numeric Columns')
plt.show()

# Detect outliers using z-score method
z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number)))
outliers = (z_scores > 3).any(axis=1)

# Display rows with outliers
outliers_df = df[outliers]
print("Rows with outliers:")
print(outliers_df)

"""**6. Comprehensive Analysis - Ratings consistency in Locations**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

# Ensure columns are correctly typed
numeric_columns = ['Location', 'Gender', 'Marital Status', 'Activity', 'Cuisines', 'Alcohol ', 'Smoker', 'Often A S', 'Overall Rating', 'Food Rating', 'Service Rating']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows where 'Overall Rating' is NaN
df = df.dropna(subset=['Overall Rating'])

# Get the top 5 locations with the highest average "Overall Rating"
top_locations = df.groupby('Location')['Overall Rating'].mean().sort_values(ascending=False).head(5)
print("Top 5 Locations with the highest average 'Overall Rating':")
print(top_locations)

# Ensuring no NaN values for these locations
top_location_ids = top_locations.index.tolist()
filtered_df = df[df['Location'].isin(top_location_ids)]
filtered_df = filtered_df.dropna(subset=['Food Rating', 'Service Rating'])

# Assess the standard deviation of "Food Rating" and "Service Rating" for the top 5 locations
std_devs = filtered_df.groupby('Location')[['Food Rating', 'Service Rating']].std()
print("\nStandard deviation of 'Food Rating' and 'Service Rating' for the top 5 locations:")
print(std_devs)

# Visualize
fig, ax = plt.subplots(figsize=(10, 6))
std_devs.plot(kind='bar', ax=ax, rot=0, color=['skyblue', 'salmon'])
ax.set_title('Standard Deviation of Food Rating and Service Rating for Top 5 Locations')
ax.set_xlabel('Location')
ax.set_ylabel('Standard Deviation')
ax.legend(['Food Rating', 'Service Rating'])
ax.set_xticklabels([str(loc) for loc in std_devs.index], rotation=0)  # Ensure x-axis labels are set correctly
plt.tight_layout()
plt.show()

# Ensure x-axis labels are set correctly
ax.set_xticklabels([str(loc) for loc in std_devs.index], rotation=0)
plt.tight_layout()
plt.show()

"""**7. Differential Analysis of Budget Impact on ratings**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

# Display column names
print(df.columns)

# Ensure columns are correctly typed as numeric where appropriate
numeric_columns = ['Location', 'Gender', 'Marital Status', 'Activity', 'Cuisines', 'Alcohol ', 'Smoker', 'Often A S', 'Overall Rating', 'Food Rating', 'Service Rating', 'Budget']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows where 'Overall Rating', 'Food Rating', or 'Budget' is NaN to ensure grouping works correctly
df = df.dropna(subset=['Overall Rating', 'Food Rating', 'Budget'])

# Group by 'Budget' and calculate the mean of 'Overall Rating' and 'Food Rating'
average_ratings = df.groupby('Budget')[['Overall Rating', 'Food Rating']].mean()
print("\nAverage 'Overall Rating' and 'Food Rating' by Budget:")
print(average_ratings)

# Plot the results
fig, ax = plt.subplots(figsize=(10, 6))
average_ratings.plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])
ax.set_title('Average Overall Rating and Food Rating by Budget')
ax.set_xlabel('Budget')
ax.set_ylabel('Average Rating')
ax.legend(['Overall Rating', 'Food Rating'])
plt.tight_layout()
plt.show()

"""**8. Distribution of Ratings across different activities**"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

# Filter the dataset for Professional and Student activities
filtered_df = df[df['Activity'].isin(['Professional', 'Student'])]

# Calculate the average Overall Rating for each user activity category
average_ratings = filtered_df.groupby('Activity')['Overall Rating'].mean()

# Print the average ratings
print("Average Overall Rating for each user activity:")
print(average_ratings)

# Visualize the distribution of Overall Ratings for each user activity category
plt.figure(figsize=(10, 6))
filtered_df.boxplot(column='Overall Rating', by='Activity', grid=False)
plt.title('Distribution of Overall Rating by User Activity')
plt.xlabel('User Activity')
plt.ylabel('Overall Rating')
plt.suptitle('')  # Remove default title
plt.xticks([1, 2], ['Professional', 'Student'])  # Set x-axis labels
plt.show()

"""**9. Impact of location on alcohol consumption preferences**"""

import pandas as pd

# Load the dataset
df = pd.read_csv('/content/Cuisine_rating.csv')

# Group by Location and find the most common alcohol consumption status
location_alcohol = df.groupby('Location')['Alcohol '].agg(lambda x: x.value_counts().index[0])

# Print the most common alcohol consumption status per location
print("Most common alcohol consumption status per location:")
print(location_alcohol)

"""**10. Data Discovery**

Here's a summary of the analysis conducted in the provided code snippets:

**1.	Loading and Cleaning Data**

The dataset was loaded, and specific columns were converted to numeric data types.
o	Data cleaning steps such as handling missing values and converting object columns to numeric were performed.

**2.	Descriptive Statistics**

Mean, median, variance, standard deviation, and range were calculated for numeric columns to understand data distribution and variability.

**3.	Data Visualization**

Histograms were plotted to visualize the distribution of numeric columns.
o	Bar charts were used to visualize the distribution of gender in the dataset.

**4.	Identifying Relationships**
Correlation analysis was conducted to identify relationships between numeric variables using a heatmap.

**5.	Outliers Detection**
o	Outliers were detected using box plots and the z-score method to identify potential anomalies in the data.

**6.	Comprehensive Analysis - Ratings Consistency in Locations**

The top 5 locations with the highest average overall ratings were identified and the standard deviation of food and service ratings for these locations was calculated and visualized using bar charts.

**7. Differential Analysis of Budget Impact on Ratings**

The impact of budget on overall and food ratings was analysed by grouping data based on budget levels and calculating average ratings, which were then visualized using bar charts.

**8.	Distribution of Ratings across Different Activities:**

The distribution of overall ratings across professional and student activities was examined using box plots.

**9.	Impact of Location on Alcohol Consumption Preferences**

The most common alcohol consumption status per location was determined, providing insights into alcohol consumption preferences across different locations.

These analyses provide insights into various aspects of cuisine ratings, including factors influencing ratings, relationships between variables, and preferences based on demographics and activities.

Visualizations such as histograms, bar charts, box plots, and heatmaps were used to effectively communicate findings and aid in understanding the data.
"""