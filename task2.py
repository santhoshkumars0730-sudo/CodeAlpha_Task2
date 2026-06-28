# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset (file name correctா இருக்கணும்)
df = pd.read_csv("Unemployment in India.csv")

# Step 3: Show first rows
print(df.head())

# Step 4: Check null values
print(df.isnull().sum())

# Step 5: Rename columns (easy use)
df.columns = ['States', 'Date', 'Frequency', 'Estimated Unemployment Rate',
              'Estimated Employed', 'Estimated Labour Participation Rate', 'Region']

# Step 6: Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Step 7: Basic info
print(df.describe())

# Step 8: Plot unemployment rate
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate')
plt.title("Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.show()

# Step 9: State wise average unemployment
state_avg = df.groupby('States')['Estimated Unemployment Rate'].mean().sort_values()

plt.figure(figsize=(12,6))
state_avg.plot(kind='bar')
plt.title("State-wise Average Unemployment Rate")
plt.show()