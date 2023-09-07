
import mysql.connector


def mysql_connector():
    # Define the connection parameters
    host = "ltc-ist-08-cc-0019-sat-sql-ewc3a.database.windows.net"
    port = 1433      #  3306  # MySQL default port
    database = "CMS_QA"
    user = "CMSIstUser"
    password = "j22WaVeDPUM4S3K9"

    # Create the MySQL connection
    conn = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # if conn.is_connected():
    print("Connected to the MySQL database")
    cursor = conn.cursor()  # Create a cursor object to interact with the database
    cursor.execute("SELECT * FROM TrainingProviderApplicantBusinesses")  # Execute a query to fetch data from a table
    rows = cursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)
    cursor.close()  # Close the cursor and connection when done
    conn.close()
# mysql_connector()



