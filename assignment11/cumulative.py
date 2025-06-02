import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Task 2

# Connect to the SQLite database
conn = sqlite3.connect('./db/lesson.db')

# SQL query to get total price per order
query = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id;
"""

# Load data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Calculate cumulative revenue using cumsum
df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs. order_id
df.plot(
    x='order_id',
    y='cumulative',
    kind='line',
    figsize=(10, 6),
    color='green',
)

# Add plot titles and labels
plt.title('Cumulative Revenue vs. Orders', fontsize=16)
plt.xlabel('Order ID', fontsize=12)
plt.ylabel('Cumulative Revenue ($)', fontsize=12)

# Show the plot
plt.show()