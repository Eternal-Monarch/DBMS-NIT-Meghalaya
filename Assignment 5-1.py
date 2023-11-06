import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve names and email addresses of all students
select_query = "SELECT Name, Email FROM Student"

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the names and email addresses of all students
for row in results:
    name, email = row
    print("Name: {}, Email: {}".format(name, email))

# Close the connection
conn.close()
