# Connecting MySQL with Python
# !pip install sqlalchemy
# !pip install pymysql

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
query = "CREATE TABLE IF NOT EXISTS test_table_2 (id INT, name VARCHAR(255))"
cursor.execute(text(query))

# Insert a row
insert_query = "INSERT INTO test_table_2 VALUES (1, 'John')"
cursor.execute(text(insert_query))
cursor.commit()


# Update a row
update_query = "UPDATE test_table_2 SET name='Jane' WHERE id=1"
cursor.execute(text(update_query))
cursor.commit()

# Select all rows
result = cursor.execute(text("SELECT * FROM test_table_2"))
#print(result.fetchall())

# Delete a row
# delete_query = "DELETE FROM test_table_2 WHERE id=1"
# cursor.execute(text(delete_query))
# cursor.commit()


# Retrieve data from the table into a dataframe
df = pd.read_sql("SELECT * FROM test_table_2;", connection)

# Add a new row to the dataframe
df.loc[0] = [2, 'Jill']

cursor.commit()

# Write the dataframe to the database
df.to_sql("test_table_2", con=connection, if_exists="append", index=False)



