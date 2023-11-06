import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve faculty members who teach multiple courses
select_query = """
SELECT Faculty.Name, COUNT(Teaching.CourseID) as CourseCount
FROM Faculty
JOIN Teaching ON Faculty.FacultyID = Teaching.FacultyID
GROUP BY Faculty.Name
HAVING CourseCount > 1
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the faculty members who teach multiple courses
for row in results:
    faculty_name, course_count = row
    print("Faculty: {}, Number of Courses Taught: {}".format(faculty_name, course_count))

# Close the connection
conn.close()
