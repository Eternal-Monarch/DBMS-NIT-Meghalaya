import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find courses with no student enrollments
select_query = '''
SELECT CourseName
FROM Course
LEFT JOIN Enrollment ON Course.CourseID = Enrollment.CourseID
WHERE Enrollment.StudentID IS NULL;
'''

# Execute the SQL query
mycursor.execute(select_query)

# Fetch and print the results
results = mycursor.fetchall()
if len(results) == 0:
    print("No courses found with no student enrollments.")
else:
    print("Courses with no student enrollments:")
    for result in results:
        print(result[0])

# Close the connection
conn.close()
