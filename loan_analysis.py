# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Import data from a JSON file using Google Colab's file upload feature
from google.colab import files
uploaded = files.upload()

# Import the data from the uploaded JSON file
import json
with open('loan_data_json.json') as f:
    data = json.load(f)

# Print the loaded data to verify
print(data)

# Create a DataFrame from the loaded JSON data
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
df.head()

# Display the last few rows of the DataFrame
df.tail()

# Get information about the DataFrame, such as column data types and missing values
df.info()

# Define a function to categorize FICO scores
def fico_use_case(score):
    if score < 400:
        return 'Very Poor'
    elif score >= 400 and score < 600:
        return 'Poor'
    elif score >= 601 and score < 660:
        return 'Fair'
    elif score >= 660 and score < 700:
        return 'Good'
    else:
        return 'Excellent'

# Apply the FICO categorization function to create a new 'Fico_category' column
df['Fico_category'] = df['fico'].apply(fico_use_case)

# Display the first few rows of the DataFrame with the new 'Fico_category' column
df.head()

# Define a function to categorize interest rates
def interest(i):
    if i > 0.12:
        return 'High'
    else:
        return 'Low'

# Apply the interest rate categorization function to create a new 'int.rate.type' column
df['int.rate.type'] = df['int.rate'].apply(interest)

# Display the 'int.rate.type' column
df['int.rate.type']

# Create a new 'annual_income' column by applying a lambda function
# This column calculates the annual income using the natural logarithm
df['annual_income'] = df['log.annual.inc'].apply(lambda x: round(math.e**x, 2))

# Display the 'annual_income' column
df['annual_income']

# Create a bar plot to visualize the distribution of FICO categories
catplot = df.groupby(['Fico_category']).size()
catplot.plot.bar()

# Create a bar plot to visualize the distribution of loan purposes
purpose_plot = df.groupby(['purpose']).size()
purpose_plot.plot.bar()

# Save the cleaned DataFrame to a CSV file without the index column
df.to_csv('loandata_cleaned.csv', index=False)

# Add an 'id' column with unique identifiers for each row
df['id'] = range(1, len(df) + 1)

# Display the first few rows of the DataFrame with the 'id' column
df.head()

# Drop the 'count' column from the DataFrame
df = df.drop('count', axis=1)

# Display the first few rows of the DataFrame after dropping the 'count' column
df.head()

# Save the cleaned DataFrame again to a CSV file without the index column
df.to_csv('loandata_cleaned.csv', index=False)
