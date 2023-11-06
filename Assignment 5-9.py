import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find students who have not registered for any exams
select_query = """
SELECT Student.Name
FROM Student
WHERE Student.StudentID NOT IN (SELECT DISTINCT StudentID FROM ExamRegistration)
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the students who have not registered for any exams
if results:
    for row in results:
        student_name = row[0]
        print("Student: {}".format(student_name))
else:
    print("No students found who have not registered for any exams.")

# Close the connection
conn.close()
