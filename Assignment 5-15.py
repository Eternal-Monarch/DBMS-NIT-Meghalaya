import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve exams with no registered students
select_query = """
SELECT Exam.ExamID, Exam.ExamDate, Exam.ExamTime, Exam.Location
FROM Exam
WHERE Exam.ExamID NOT IN (SELECT DISTINCT ExamID FROM ExamRegistration)
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the exams with no registered students
if results:
    for row in results:
        exam_id, exam_date, exam_time, location = row
        print("Exam ID: {}, Exam Date: {}, Exam Time: {}, Location: {}".format(exam_id, exam_date, exam_time, location))
else:
    print("No exams found with no registered students.")

# Close the connection
conn.close()
