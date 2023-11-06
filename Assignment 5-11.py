import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find the students enrolled in the "History" course
select_query = """
SELECT Student.Name
FROM Student
JOIN Enrollment ON Student.StudentID = Enrollment.StudentID
JOIN Course ON Enrollment.CourseID = Course.CourseID
WHERE Course.CourseName = 'History'
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the students enrolled in the "History" course
if results:
    for row in results:
        student_name = row[0]
        print("Student enrolled in History: {}".format(student_name))
else:
    print("No students found who are enrolled in History.")

# Close the connection
conn.close()
