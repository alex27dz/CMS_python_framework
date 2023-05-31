Makefile, YML pipeline - By using a Makefile, developers can automate the build process and ensure that the project is built correctly and consistently across different platforms and environments. This can save time and reduce errors, particularly in larger projects with many dependencies and configurations.

Setup and teardown @classmethod - functions - are special functions that can be used to set up and tear down the test environment before and after each test case is executed. These functions are often used to create or initialize objects, open and close database connections, or perform other tasks that are required to run the test cases. One common use case for @classmethod in pytest is to define a setup method that needs to be run before any tests in the class are run. By defining a class method with the @classmethod decorator and naming it setup_class, pytest will automatically run this method before any tests in the class are run.

Fixtures - fixtures @pytest.fixture - functions define functions that we can pass and can be used only in test_ scenarios to verify processes , verify connection, or to pass configuration parameters usually its the fist steps of the testing cycle. or open a session or hold on processes like sql and requests 

Files and paths - OS - operating systems library
import os
os.name: Returns the name of the operating system.
os.getcwd(): Returns the current working directory.
os.chdir(path): Changes the current working directory to the specified path.
os.listdir(path='.'): Returns a list of all files and directories in the specified path.
os.mkdir(path): Creates a new directory with the specified path.
os.makedirs(path): Creates a new directory and all necessary parent directories with the specified path.
os.remove(path): Deletes the file with the specified path.
os.rmdir(path): Deletes the directory with the specified path (directory must be empty).
os.removedirs(path): Deletes the directory and all parent directories with the specified path (directories must be empty).
os.rename(src, dst): Renames the file or directory with the specified source path to the specified destination path.
os.path.exists(path): Returns True if the file or directory with the specified path exists, otherwise False.
os.path.isdir(path): Returns True if the specified path is a directory, otherwise False.
os.path.isfile(path): Returns True if the specified path is a file, otherwise False.
os.path.join(path1, path2, ...): Joins two or more path components together, using the appropriate separator for the operating system.
os.path.abspath(path): Returns the absolute path of the specified path.
os.path.basename(path): Returns the base name of the specified path (i.e. the file or directory name).
os.path.commonpath(paths): Returns the longest common sub-path of the specified paths.
os.path.commonprefix(paths): Returns the longest common prefix of the specified paths.
os.path.dirname(path): Returns the directory name of the specified path.
os.path.exists(path): Returns True if the specified path exists, otherwise False.
os.path.expanduser(path): Expands the initial component of the path to the user's home directory.
os.path.expandvars(path): Expands environment variables in the specified path.
os.path.getatime(path): Returns the last access time of the specified path as a floating-point number of seconds since the epoch.
os.path.getctime(path): Returns the creation time of the specified path as a floating-point number of seconds since the epoch.
os.path.getmtime(path): Returns the last modification time of the specified path as a floating-point number of seconds since the epoch.
os.path.getsize(path): Returns the size of the specified file in bytes.
os.path.isabs(path): Returns True if the specified path is an absolute path, otherwise False.
os.path.isdir(path): Returns True if the specified path is a directory, otherwise False.
os.path.isfile(path): Returns True if the specified path is a file, otherwise False.
os.path.islink(path): Returns True if the specified path is a symbolic link, otherwise False.
os.path.ismount(path): Returns True if the specified path is a mount point, otherwise False.
os.path.join(path1, path2, ...): Joins two or more path components together, using the appropriate separator for the operating system.
os.path.normcase(path): Normalizes the case of the specified path.
os.path.normpath(path): Normalizes the specified path by removing redundant separators and up-level references.
os.path.realpath(path): Returns the absolute path of the specified path, resolving any symbolic links.
os.path.relpath(path, start='.'): Returns a relative path from start to the specified path.
os.path.samefile(path1, path2): Returns True if the two specified paths refer to the same file, otherwise False.
os.path.sameopenfile(fp1, fp2): Returns True if the two specified open files refer to the same file, otherwise False.
os.path.amestat(stat1, stat2): Returns True if the two specified file stat structures refer to the same file, otherwise False.
os.path.split(path): Splits the specified path into a directory and file name.
os.path.splitdrive(path): Splits the specified path into a drive letter and the rest of the path.
os.path.splitext(path): Splits the specified path into a base name and extension


Strings
len(string): Returns the length of the string.
string.lower(): Returns the lowercase version of the string.
string.upper(): Returns the uppercase version of the string.
string.strip(): Removes leading and trailing whitespace from the string.
string.replace(old, new): Replaces all occurrences of old in the string with new.
string.split(separator): Splits the string into a list of substrings based on the separator.
string.startswith(substring): Returns True if the string starts with the specified substring.
string.endswith(substring): Returns True if the string ends with the specified substring.
string.count(substring): Returns the number of times substring appears in the string.
string.find(substring): Returns the index of the first occurrence of substring in the string.
string.isnumeric(): Returns True if the string consists of only numeric characters.
string.isalpha(): Returns True if the string consists of only alphabetic characters.
string.isalnum(): Returns True if the string consists of only alphanumeric characters.


Lists
len(list): Returns the number of elements in the list.
list.append(item): Adds an element to the end of the list.
list.insert(index, item): Inserts an element at a specific index in the list.
list.remove(item): Removes the first occurrence of an element from the list.
list.pop(index): Removes and returns the element at a specific index in the list.
list.sort(): Sorts the elements of the list in ascending order.
list.reverse(): Reverses the order of the elements in the list.
list.index(item): Returns the index of the first occurrence of an element in the list.
list.count(item): Returns the number of times an element appears in the list.
list.copy(): Returns a shallow copy of the list.
list.clear(): Removes all elements from the list.
list.extend(iterable): Appends the elements of an iterable to the end of the list.
len(): Returns the number of elements in the list.
append(): Adds an element to the end of the list.
extend(): Adds the elements of another list (or any iterable) to the end of the list.
insert(): Inserts an element at a specified position in the list.
remove(): Removes the first occurrence of an element from the list.
pop(): Removes and returns the element at a specified index in the list.
index(): Returns the index of the first occurrence of an element in the list.
count(): Returns the number of times an element appears in the list.
sort(): Sorts the elements of the list in ascending order.
reverse(): Reverses the order of the elements in the list.
copy() : make a copy of the list into a new list


Dictionary
len(dictionary): Returns the number of key-value pairs in the dictionary.
dictionary[key]: Returns the value associated with a given key in the dictionary.
dictionary[key] = value: Associates a value with a given key in the dictionary.
dictionary.get(key, default): Returns the value associated with a given key in the dictionary, or a default value if the key is not present.
dictionary.pop(key): Removes a key-value pair from the dictionary and returns the corresponding value.
dictionary.keys(): Returns a list of all keys in the dictionary.
dictionary.values(): Returns a list of all values in the dictionary.
dictionary.items(): Returns a list of all key-value pairs in the dictionary as tuples.
dictionary.update(other_dictionary): Adds all key-value pairs from another dictionary to the current dictionary.
dictionary.clear(): Removes all key-value pairs from the dictionary.
len(): Returns the number of key-value pairs in the dictionary.
keys(): Returns a list of all the keys in the dictionary.
values(): Returns a list of all the values in the dictionary.
items(): Returns a list of tuples, where each tuple contains a key-value pair.
get(key, default): Returns the value associated with the given key, or the default value if the key is not present in the dictionary.
pop(key, default): Removes and returns the value associated with the given key, or the default value if the key is not present in the dictionary.
popitem(): Removes and returns a key-value pair from the dictionary in arbitrary order.
update(dict2): Adds the key-value pairs from dict2 to the dictionary.
clear(): Removes all the key-value pairs from the dictionary.


Unix/Linux
* Create files from the terminal: Terminal > touch “File name” -> touch filename.txt
* ls: List the contents of a directory
* cd: Change the current working directory
* pwd: Print the current working directory
* mkdir: Create a new directory
* rm: Remove a file or directory
* cp: Copy a file or directory
* mv: Move or rename a file or directory
* cat: Print the contents of a file to the screen
* grep: Search for a pattern in a file or output
* sed: Stream editor for modifying text
* awk: Text processing tool for extracting and manipulating data
* chmod: Change the permissions of a file or directory
* chown: Change the owner of a file or directory
* sudo: Run a command with elevated privileges
* ssh: Secure Shell client for remote login and execution of commands on a remote machine
* scp: Secure Copy for transferring files between machines over a secure network
* tar: Archive utility for creating and manipulating tar archives
* gzip: Compression utility for compressing files
* curl: Command-line tool for transferring data from or to a server
* wget: Command-line tool for retrieving files from the web
* ps: Display information about running processes
* top: Display a real-time view of system performance and process activity
* ps aux - checks what are the running apps


Flags in Pytest execution:
* -v: Increase verbosity of test output.
* -q: Decrease verbosity of test output.
* -k EXPRESSION: Only run tests whose names match the given substring expression.
* -m MARKEXPR: Only run tests that are marked with the given marker expression.
* -x: Stop the test run after the first failure.
* --maxfail=num: Stop the test run after num failures.
* --lf: Run only the tests that failed in the previous test run.
* --ff: Run all tests, but run the failures from the previous test run first.
* --tb=style: Set the traceback style. Valid styles are "auto", "long", "short", "line", and "native".
* --pdb: Drop into the Python debugger on test failures or errors.
* --capture: Set the mode for capturing stdout/stderr. Valid modes are "no", "sys", "fd", and "tee-sys".


Pytest APIs
* Approx
def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)
def test_approx_with_tolerance():
    assert 0.1 + 0.2 == pytest.approx(0.3, rel=1e-6, abs=1e-12)


Python with SQL databases:
1. Connecting to a database: To connect to a SQL database from Python, you'll typically use a library such as sqlite3, mysql-connector-python, or psycopg2. You'll need to provide the connection details such as the hostname, port, username, password, and database name.
2. Querying the database: Once you've established a connection to the database, you can execute SQL queries using the execute() method on a cursor object. You can use placeholders such as ? or %s in the SQL query to specify values that will be substituted at runtime.
3. Fetching results: After executing a query, you can fetch the results using the fetchone(), fetchall(), or fetchmany() methods on the cursor object, depending on whether you expect one, all, or some of the results to be returned.
4. Updating the database: To update the data in a SQL database, you can execute INSERT, UPDATE, or DELETE statements using the execute() method on a cursor object. You'll typically need to commit the changes using the commit() method on the database connection object.
5. Creating tables: To create a table in a SQL database, you can execute a CREATE TABLE statement using the execute() method on a cursor object. You can specify the column names, data types, and constraints in the statement.
6. Dropping tables: To delete a table from a SQL database, you can execute a DROP TABLE statement using the execute() method on a cursor object.
7. Handling errors: When working with a SQL database from Python, it's important to handle errors that may occur during connection, query execution, or other operations. You can use try-except blocks to catch exceptions and handle them appropriately.

SQL commands:
1. SELECT - used to retrieve data from one or more tables
2. INSERT INTO - used to insert data into a table
3. UPDATE - used to update existing data in a table
4. DELETE - used to delete data from a table
5. CREATE TABLE - used to create a new table in the database
6. ALTER TABLE - used to modify an existing table in the database
7. DROP TABLE - used to delete an entire table and all of its data
8. CREATE INDEX - used to create an index on a table for faster data retrieval
9. GRANT - used to grant permissions to a user or group to perform specific actions in the database
10. REVOKE - used to revoke permissions previously granted to a user or group


Terminal only:
Install Python 
Install Pip
Install Virtual environment
Activating virtual environment
Install packages and work with python

Virtual Machine as an Agent:
Download the Azure agent 
Navigate to the agent folder via terminal 
./run.sh - to start the agent - listening to jobs
Control + C - to stop the agent

Flask
Flask is a popular micro web framework written in Python. It is designed to be lightweight, flexible, and easy to use, making it a great choice for building small to medium-sized web applications.
Flask provides a simple and intuitive API for building web applications, which includes features such as routing, template rendering, and request handling. It also allows developers to easily integrate with various third-party libraries and tools.









Python - Concepts
- [ ] Python - Full pytest documentation https://docs.pytest.org/en/7.1.x/contents.html 
- [ ] Python - Pytest API reference https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest%20approx 
- [ ] Python - Flask documentation https://flask.palletsprojects.com/en/2.2.x/ 
- [ ] Python - Flask, Django
- [ ] Python - running tests in parallel
- [ ] Python - fixtures @pytest.fixture functions
- [ ] Setup and teardown @classmethod functions 
- [ ] How to add more functions for inherited class and for father class
- [ ] Python - simple math % // * **2
- [ ] Python - Classes inheritance how to create new function in a parent class using child class
- [ ] Python - Linux / unix commands
- [ ] Python - HTTP/REST, WebSockets, SOAP
- [ ] Python - Rest API - RESTful APIs provide a simple and standardized way for clients to communicate with servers, using standard HTTP methods and formats, sending HTTP requests (like GET, POST, PUT, DELETE) to the server. The server then returns an HTTP response with the data, which is typically in a standardized format such as JSON or XML
- [ ] Python - SOAP UI, sending xml data to soap client, getting data back with requests.post
- [ ] Python - global variable	
- [ ] Python - object oriented
- [ ] Python - Classes inheritance
- [ ] Python - Data types list
- [ ] Python - Data types dict
- [ ] Python - Strings
- [ ] Python - keywords
- [ ] Python - files + os
- [ ] Python - Asserts - must use in purest test_ scenarios for testing - checking a True statement , if it fails it stops the code with assert msg , not like if statement that not stopping the code
- [ ] Python - map - combining a function and a list of parameters generating the list 
- [ ] Python - lambda - creates a small function using parameters
- [ ] Python - mysql: Connect to DB, execute creation of table query , execute insert into query, commit, execute select from query, fetch all ,close connection
- [ ] Python - API, using requests, getting back JSON format a dictionary or list of dictionaries
- [ ] Python - Logs, import logging, basic config, logging.info (‘add info msg to logging’)
- [ ] Python - Requests
- [ ] Python - JSON
- [ ] Python - selenium
- [ ] Python - BDD with pytest
- [ ] Python - Pytest APIs
- [ ] Python - Review all topics from IKM assessment
- [ ] Python - Django (Tutorial + home analyzer as example)
- [ ] Python - Appium mobile automation create regression
- [ ] Python - Review Dov links and the tutorial video 
- [ ] Python - Python book - fluent python, python for everyone, python cookbook
- [ ] Python - Leet code - python, discover all topics
- [ ] Networking concepts
- [ ] SQL - concepts




# Environment setup:
# Local
- Download latest python version
- Download latest Pycharm version
- Configure project test runner to be pytest
- Download required packages (pip install)


# Create folders inside the project:
### functions:
- Imoprt packeges
- General functions
- General Classes
- BDD tagging
- parameters
- Dictionaries
- Lists
- Links
- Environments
- APIs
- SoapUI
- Requests
- APP scenarios

### tests:
- from functions import *
- test_ senario01()
- test_scenario02()

### YAML:
- Yaml-pipeline-file.yml , Create YAML pipeline and execute the jobs by steps via Azure devops
  setting up the branch the pool of the VM and the steps for execution downloading pythong then installing the packages then executing the scenarios with pytest
- Requirments.txt - list of all required packages and their versions to use in automation

- Execute scenarios locally and review all works

# Cloud
- Upload the code to github repo
- Create and configure Agent in Azure pools and the VM (windows, MAC, linux)
- Create the pipeline run and debug make sure all working
- Execute jobs and review the results in Azure pipelines logs or HTML report

### Extra:
- BDD add bdd folder and the bdd scenarios.sql file
- tag the functions with the BDD steps "Given When And Then And"

# Projects:
1) Python Automation framework - python + pytest + Azure pipelines integration
2) Python Mobile Automation framework - python + pytest + appium + Android emulator


