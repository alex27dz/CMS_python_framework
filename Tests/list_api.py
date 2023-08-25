import requests
import api
import pytest


def add_Learning_Record_API_98393():
    print('Add Learning Record API')
    url = "https://private-anon-78376c118a-bluedrop360apiv2network.apiary-mock.com/api-v2/learning-records"
    headers = {"Content-Type": "application/json"}
    body = {
      "learningRecordId": "4108123e-7f35-4097-928a-5bccd5fe4111",
      "trainingStandardKey": "WAH-E-B",
      "completionDate": "2018-11-21T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "external-class-111",
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-121",
        "firstname": "Peter",
        "lastname": "Johnson",
        "personalEmail": "perter.johnson@example.com",
        "birthYear": 1995,
        "address": {
          "street-address": "1230 Main Street",
          "extended-address": "PO Box 1234",
          "locality": "Toronto",
          "region": "ON",
          "postal-code": "M7A 1T7",
          "country-name": "Canada"
        },
        "mobilePhone": "6047771234",
        "homePhone": "7782225678"
      }
    }

    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    # print(response.json())
    # print(response.text)

add_Learning_Record_API_98393()

# build SQL connection and check the records was created


'''

import mysql.connector
db_name = 'users'
query_create_new_table_with_items = """CREATE TABLE {} (
                            full_name VARCHAR(255),
                            email VARCHAR(255),
                            phone_number VARCHAR(255),
                            id VARCHAR(255),
                            notes VARCHAR(255)
                        )""".format(db_name)

query_select_from = "SELECT * FROM users"

db = mysql.connector.connect(
    host='localhost',  # ip
    user='root',
    passwd='NV27vnmc',
    database='alex_db'  # name of the db
)

# cursor = db.cursor(query_create_new_table_with_items)
# cursor.execute()
# db.commit()
# db.close()


class alex_sql_modules(object):
    def __init__(self, db, query_create_new_table_with_items, query_select_from):
        self.db = db
        self.query_create_new_table_with_items = query_create_new_table_with_items
        self.query_select_from = query_select_from

    def mysql_check_db_connection(self):
        print(type(self.db))
        return self.db

    def mysql_create_new_table_with_items(self):
        mycursor = self.db.cursor()  # create cursor object
        mycursor.execute(self.query_create_new_table_with_items)  # creating a new table with columns - execute the query
        db.commit()
        print('new table and items created')

    def mysql_insert_items(self):
        mycursor = self.db.cursor()  # create cursor object
        sql = "INSERT INTO users (full_name, email, phone_number, id, notes) VALUES (%s, %s, %s, %s, %s)"  # inserting into columns
        val = ("alex dezho", "alex27dz@gmail.com", "4372392986", '123456789', 'new profile')  # inserted values
        mycursor.execute(sql, val)  # execute the query
        self.db.commit()

    def mysql_print_table_and_items(self):
        mycursor = self.db.cursor()  # create cursor object
        mycursor.execute(self.query_select_from)  # execute the query - define SQL query to select all items from a table
        results = mycursor.fetchall()  # fetch all the results
        print(results)
        for row in results:  # print the results
            print(row)
        return results
        # print(results[0])
        # print(type(results))
        # print(type(str(results)))
        # print(str(results).find('alex 2dezho'))

    def mysql_delete_table(self):
        mycursor = self.db.cursor()  # create cursor object
        delete_query = "DROP TABLE users"   # define SQL query to delete a table
        mycursor.execute(delete_query)  # execute the query
        print('table deleted')

    def mysql_close(self):
        self.db.close()


# sql = alex_sql_modules(db, query_create_new_table_with_items, query_select_from)

import mysql.connector
db_name = 'users'
query_create_new_table_with_items = """CREATE TABLE {} (
                            full_name VARCHAR(255),
                            email VARCHAR(255),
                            phone_number VARCHAR(255),
                            id VARCHAR(255),
                            notes VARCHAR(255)
                        )""".format(db_name)

query_select_from = "SELECT * FROM users"

db = mysql.connector.connect(
    host='localhost',  # ip
    user='root',
    passwd='NV27vnmc',
    database='alex_db'  # name of the db
)

# cursor = db.cursor(query_create_new_table_with_items)
# cursor.execute()
# db.commit()
# db.close()


class alex_sql_modules(object):
    def __init__(self, db, query_create_new_table_with_items, query_select_from):
        self.db = db
        self.query_create_new_table_with_items = query_create_new_table_with_items
        self.query_select_from = query_select_from

    def mysql_check_db_connection(self):
        print(type(self.db))
        return self.db

    def mysql_create_new_table_with_items(self):
        mycursor = self.db.cursor()  # create cursor object
        mycursor.execute(self.query_create_new_table_with_items)  # creating a new table with columns - execute the query
        db.commit()
        print('new table and items created')

    def mysql_insert_items(self):
        mycursor = self.db.cursor()  # create cursor object
        sql = "INSERT INTO users (full_name, email, phone_number, id, notes) VALUES (%s, %s, %s, %s, %s)"  # inserting into columns
        val = ("alex dezho", "alex27dz@gmail.com", "4372392986", '123456789', 'new profile')  # inserted values
        mycursor.execute(sql, val)  # execute the query
        self.db.commit()

    def mysql_print_table_and_items(self):
        mycursor = self.db.cursor()  # create cursor object
        mycursor.execute(self.query_select_from)  # execute the query - define SQL query to select all items from a table
        results = mycursor.fetchall()  # fetch all the results
        print(results)
        for row in results:  # print the results
            print(row)
        return results
        # print(results[0])
        # print(type(results))
        # print(type(str(results)))
        # print(str(results).find('alex 2dezho'))

    def mysql_delete_table(self):
        mycursor = self.db.cursor()  # create cursor object
        delete_query = "DROP TABLE users"   # define SQL query to delete a table
        mycursor.execute(delete_query)  # execute the query
        print('table deleted')

    def mysql_close(self):
        self.db.close()


# sql = alex_sql_modules(db, query_create_new_table_with_items, query_select_from)

'''



