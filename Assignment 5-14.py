import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find the average score for each student
select_query = """
SELECT Student.Name, AVG(ExamResults.score) AS AverageScore
FROM Student
LEFT JOIN ExamResults ON Student.StudentID = ExamResults.StudentID
GROUP BY Student.Name
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the average score for each student
for row in results:
    student_name, average_score = row
    print("Student: {}, Average Score: {}".format(student_name, average_score))

# Close the connection
conn.close()
