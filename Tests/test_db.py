import pyodbc

# Define the connection string parameters
server_name = "your_server_name"  # Replace with your SQL Server's hostname
database_name = "your_database_name"  # Replace with your database name
username = "your_username"  # Replace with your SQL Server username
password = "your_password"  # Replace with your SQL Server password

# Create a connection string
connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server_name};Database={database_name};Uid={username};Pwd={password}"

try:
    # Establish a connection to the SQL Server database
    conn = pyodbc.connect(connection_string)

    # Create a cursor object for executing SQL queries
    cursor = conn.cursor()

    # Example: Execute a simple query
    cursor.execute("SELECT * FROM YourTable")

    # Fetch and print the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection when done
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("Error connecting to the database:", e)
