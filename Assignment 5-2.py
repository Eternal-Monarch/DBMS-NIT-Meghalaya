import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find courses with more than three credits
select_query = "SELECT CourseName FROM Course WHERE Credits > 3"

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the courses with more than three credits
for row in results:
    course_name = row[0]
    print("Course with more than three credits: {}".format(course_name))

# Close the connection
conn.close()
