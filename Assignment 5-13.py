import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to list the courses with the highest number of enrollments
select_query = """
SELECT Course.CourseName, COUNT(Enrollment.CourseID) AS TotalEnrollments
FROM Course
LEFT JOIN Enrollment ON Course.CourseID = Enrollment.CourseID
GROUP BY Course.CourseName
ORDER BY TotalEnrollments DESC
LIMIT 1
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch the result
result = mycursor.fetchone()

# Print the course with the highest number of enrollments
if result:
    course_name, total_enrollments = result
    print("Course with the highest enrollments: {}, Total Enrollments: {}".format(course_name, total_enrollments))
else:
    print("No courses found with enrollments.")

# Close the connection
conn.close()
