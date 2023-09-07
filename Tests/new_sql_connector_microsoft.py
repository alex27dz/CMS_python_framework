import pyodbc  # Open Database Connectivity


def sql_microsoft_connector():
    # Define the connection string parameters
    server_name = "ltc-ist-08-cc-0019-sat-sql-ewc3a.database.windows.net,1433"  # Replace with your SQL Server's hostname
    database_name = "CMS_QA"  # Replace with your database name
    username = "CMSIstUser"  # Replace with your SQL Server username
    password = "j22WaVeDPUM4S3K9"  # Replace with your SQL Server password

    # Create a connection string
    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server_name};Database={database_name};Uid={username};Pwd={password}"

    # Establish a connection to the database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()  # Create a cursor to interact with the database
    cursor.execute("SELECT * FROM TrainingProviderApplicantBusinesses")  # Execute SQL queries
    rows = cursor.fetchall()
    for row in rows:  # Iterate through the results
        print(row)
    cursor.close()  # Close the cursor and connection when done
    connection.close()
# sql_microsoft_connector()



