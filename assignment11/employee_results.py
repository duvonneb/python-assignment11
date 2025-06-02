import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Task 1

# Connect to the database
conn = sqlite3.connect('./db/lesson.db')

# SQL query to calculate revenue by employee
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

# Load results into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Plotting
employee_results.plot(
    kind='bar',
    x='last_name',
    y='revenue',
    color='skyblue',
    figsize=(10, 6)
)

# Title and labels
plt.title('Employee Revenue', fontsize=16)
plt.xlabel('Employee Last Name', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)

# Show the plot
plt.show()