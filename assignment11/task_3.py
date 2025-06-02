import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Task 3

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print the first 10 and last 10 rows
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# Clean the 'strength' column
# Convert values like "0-1" and "2-3" to midpoints like 0.5 and 2.5 for simplicity
# Alternatively, remove non-numeric characters and cast to float, depending on goal

# Here's a robust way to convert range strings to midpoints:
def range_to_float(value):
    if isinstance(value, str) and '-' in value:
        parts = value.split('-')
        return (float(parts[0]) + float(parts[1])) / 2
    try:
        return float(value)
    except:
        return None

df['strength'] = df['strength'].apply(range_to_float)

# Create an interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs. Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
)

# Save the plot as HTML
fig.write_html('wind.html')