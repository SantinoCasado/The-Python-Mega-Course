import psycopg2

def create_table():
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=data_base1 user=postgres password=46184393 host=localhost port=5432")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Create a table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS store (
            item TEXT,
            quantity INTEGER,
            price REAL
        )
    """)
    print("Table created successfully.")
    # Commit the changes
    conn.commit()
    # Close the cursor and connection
    cur.close()
    conn.close()

def instert(item, quantity, price):
    conn = psycopg2.connect("dbname=data_base1 user=postgres password=46184393 host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO store (item, quantity, price) VALUES (%s, %s, %s)", (item, quantity, price))
    print("Data inserted successfully.")
    conn.commit()
    cur.close()
    conn.close()

def view():
    conn = psycopg2.connect("dbname=data_base1 user=postgres password=46184393 host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname=data_base1 user=postgres password=46184393 host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    print("Data deleted successfully.")
    conn.commit()
    cur.close()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname=data_base1 user=postgres password=46184393 host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    print("Data updated successfully.")
    conn.commit()
    cur.close()
    conn.close()

#create_table()
#instert("Apple", 10, 0.25)
#instert("Banana", 5, 0.30)
#delete("Apple")
update(15, 0.20, "Banana")
print(view())
