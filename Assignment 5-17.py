import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find students who have registered for exams in both "Mathematics" and "Computer Science" departments
select_query = """
SELECT Student.Name
FROM Student
JOIN Enrollment ON Student.StudentID = Enrollment.StudentID
JOIN Course ON Enrollment.CourseID = Course.CourseID
JOIN Teaching ON Course.CourseID = Teaching.CourseID
JOIN Faculty ON Teaching.FacultyID = Faculty.FacultyID
WHERE Faculty.Department IN ('Mathematics', 'Computer Science')
GROUP BY Student.StudentID
HAVING COUNT(DISTINCT Faculty.Department) = 2;
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the students who have registered for exams in both "Mathematics" and "Computer Science" departments
if results:
    for row in results:
        student_name = row[0]
        print("Student registered for exams in both Mathematics and Computer Science: {}".format(student_name))
else:
    print("No students found who have registered for exams in both departments.")

# Close the connection
conn.close()
