import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# TASK 2:
conn = sqlite3.connect("../db/lesson.db")

sql_statement = """
    SELECT o.order_id, SUM(price * quantity) AS total_price
    from orders o 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
"""

df = pd.read_sql_query(sql_statement, conn)
print(df.head())
df['cumulative'] = df['total_price'].cumsum()
df.plot(x="order_id", y="cumulative", kind="line", color="slateblue", title="Cumulative Revenue by Order")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.show()

conn.close()
