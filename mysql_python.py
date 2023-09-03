# Examples of using MySQL with Python

# Import the required libraries
from sqlalchemy import create_engine, text
import pandas as pd

# Define the connection parameters
host = "localhost"
user = "root"
password = "my-secret-pw"
database = "test"

# Create a connection object
connection = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# Create a cursor object
cursor = connection.connect()

# Create a table
cursor.execute(text("CREATE TABLE IF NOT EXISTS test_table (id INT, name VARCHAR(255))"))
cursor.commit()

# Insert a row
cursor.execute(text("INSERT INTO test_table VALUES (1, 'John')"))
cursor.commit()

# Select all rows
result = cursor.execute(text("SELECT * FROM test_table"))
print(result.fetchall())

# Update a row
cursor.execute(text("UPDATE test_table SET name='Jane' WHERE id=1"))
cursor.commit()

# Select all rows
result = cursor.execute(text("SELECT * FROM test_table"))
print(result.fetchall())

# Delete a row
# cursor.execute(text("DELETE FROM test_table WHERE id=1"))

df = pd.read_sql("SELECT * FROM test_table;", connection)
cursor.rollback()

print(df)

# add a new row to the dataframe
df.loc[0] = [1, 'Jill']

# write the dataframe to the database
df.to_sql("test_table", con=connection, if_exists="replace", index=False)
