import sqlite3

# 1. Connection with database
connection = sqlite3.connect("sqlite.db")

# Cursor to execute queries and fetch data
cursor = connection.cursor()


# 2. Create a table with coloumns
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment(
    id INTEGER PRIMARY KEY,
    content TEXT,
    weight REAL,
    status TEXT
    )
""")

# 3. Add shipment data - Insert values in the table
cursor.execute("""
    INSERT INTO shipment 
    VALUES (12703, "Gold", 123242, "placed")
""")

# # Commit the change to the database - without commitment nothing is valid in this world
# connection.commit()

# 4. Read a shipment by id
cursor.execute("""
    SELECT * FROM shipment 
    WHERE content = "metal gears"
""")

result = cursor.fetchall()
print(result)

# 5. Update a shipment
cursor.execute("""
    UPDATE shipment SET 
    status = 'in_transit'
    WHERE id = 12701
""")
connection.commit()

# # Delete a shipment by id
# cursor.execute("""
#     DELETE FROM shipment 
#     where id = 12701
# """)
# connection.commit()

# Delete table if needed
# cursor.execute(" DROP TABLE shipment ")

connection.close()

