import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve students who scored the highest in each exam
select_query = """
SELECT E.ExamID, E.ExamDate, S.Name, ER.StudentID, MAX(EResults.score) AS Max_Score
FROM Exam E
INNER JOIN ExamRegistration ER ON E.ExamID = ER.ExamID
INNER JOIN Student S ON ER.StudentID = S.StudentID
INNER JOIN ExamResults EResults ON ER.ExamID = EResults.ExamID AND ER.StudentID = EResults.StudentID
GROUP BY E.ExamID, E.ExamDate, S.Name, ER.StudentID
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the students who scored the highest in each exam
for row in results:
    exam_id, exam_date, student_name, student_id, max_score = row
    print("Exam ID: {}, Exam Date: {}, Student Name: {}, Student ID: {}, Max Score: {}".format(exam_id, exam_date, student_name, student_id, max_score))

# Close the connection
conn.close()
