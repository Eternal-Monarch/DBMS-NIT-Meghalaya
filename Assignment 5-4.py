import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to get faculty members in the "Mathematics" department
select_query = "SELECT Name, Email FROM Faculty WHERE Department = 'Mathematics'"

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the faculty members in the "Mathematics" department
for row in results:
    name, email = row
    print("Name: {}, Email: {}".format(name, email))

# Close the connection
conn.close()
