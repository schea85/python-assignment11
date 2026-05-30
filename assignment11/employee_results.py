import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# TASK 1:
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()
    
sql_statement = """
    SELECT last_name, SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY e.employee_id;
"""
    
df = pd.read_sql_query(sql_statement, conn)
print(df)
df.plot(x="last_name", y="revenue", kind="bar", color="royalblue", title="Employee Revenue")
plt.xlabel("Employee's Last Name")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

conn.close()
    