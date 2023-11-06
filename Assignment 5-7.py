import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to list students who scored above 90 on any exam
select_query = """
SELECT DISTINCT Student.Name, ExamResults.score
FROM Student
JOIN ExamResults ON Student.StudentID = ExamResults.StudentID
WHERE ExamResults.score > 90
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the students who scored above 90 on any exam
for row in results:
    student_name, score = row
    print("Student: {}, Score: {}".format(student_name, score))

# Close the connection
conn.close()
