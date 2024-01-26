import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def preprocess_data(filepath):
  
  file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\googleplaystore.csv"


  df = pd.read_csv(filepath)
  df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
  df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
  df['Category'] = df['Category'].str.upper().str.strip()
  return df

def create_line_plot(df):
  """
  Create a line plot of average app ratings over time.

  Args:
    df: DataFrame - the preprocessed Google Play Store DataFrame
  """
  df['Year'] = df['Last Updated'].dt.year
  average_rating_per_year = df.groupby('Year')['Rating'].mean().dropna()
  plt.figure(figsize=(12, 6))
  plt.plot(average_rating_per_year.index, average_rating_per_year, marker='o', color='b', label='Average Rating')
  plt.title('Trend of Average App Ratings Over Time')
  plt.xlabel('Year')
  plt.ylabel('Average Rating')
  # Add legend for line plot
  plt.legend()  
  plt.grid(True)
  plt.show()

def create_pie_chart(df):
  """
  Create a pie chart of the distribution of apps across top categories.

  Args:
    df: DataFrame - the preprocessed Google Play Store DataFrame
  """
  category_counts = df['Category'].value_counts().head(10)
  plt.figure(figsize=(14, 14))
  plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, explode=[0.1] * len(category_counts), shadow=True, colors=plt.cm.Paired(np.arange(len(category_counts))))
  plt.title('Distribution of Apps Across Top 10 Categories')
  plt.legend(category_counts.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))  # Add legend for pie chart
  plt.show()

def create_histogram(df):
  """
  Create a histogram of the distribution of app ratings.

  Args:
    df: DataFrame - the preprocessed Google Play Store DataFrame
  """
  plt.figure(figsize=(12, 6))
  plt.hist(df['Rating'].dropna(), bins=25, range=(0, 5), color='purple', edgecolor='black', label='App Ratings')
  plt.title('Distribution of App Ratings')
  plt.xlabel('Rating')
  plt.ylabel('Frequency')
  plt.xticks(np.arange(0, 5.1, 0.5))
  # Add legend for histogram
  plt.legend() 
  plt.grid(axis='y')
  plt.show()

# Path to the dataset 
dataset_path = 'googleplaystore.csv'

# Preprocess the data
google_play_store_df = preprocess_data(dataset_path)

# Create visualizations
create_line_plot(google_play_store_df)
create_pie_chart(google_play_store_df)
create_histogram(google_play_store_df)