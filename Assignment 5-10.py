import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve the total number of enrollments for each course
select_query = """
SELECT Course.CourseName, COUNT(Enrollment.CourseID) AS TotalEnrollments
FROM Course
LEFT JOIN Enrollment ON Course.CourseID = Enrollment.CourseID
GROUP BY Course.CourseName
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the total number of enrollments for each course
for row in results:
    course_name, total_enrollments = row
    print("Course: {}, Total Enrollments: {}".format(course_name, total_enrollments))

# Close the connection
conn.close()
