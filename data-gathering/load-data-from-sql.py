
import sqlite3
import pandas as pd

DB_FILE = "data/sample.db"

### Connect to SQLite database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

#Droping and creating Creating employees table
cursor.execute("DROP TABLE IF EXISTS employees")
    
cursor.execute("""
            CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary float NOT NULL
        )
    """)

## Insert records
employees = [
        (1, "Navneet", "IT", 45000),
        (2, "Priya", "HR", 38000),
        (3, "Rajann", "Finance", 42000),
        (4, "Neha", "IT", 50000),
        (5, "Sapna", "Marketing", 40000)
    ]

cursor.executemany("""
        INSERT INTO employees
        (id, name, department, salary)
        VALUES (?, ?, ?, ?)
    """, employees)

conn.commit()

query = """
        SELECT id, name, department, salary
        FROM employees
        ORDER BY id
    """

df = pd.read_sql_query(query, conn)
# Displaying DataFrame
print("========== DATAFRAME ==========")
print(df)

conn.close()

print("\n SQLite database saved as sample.db under data folder.")

##done