import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve exams and their locations scheduled for November 2023
select_query = """
SELECT ExamDate, ExamTime, Location
FROM Exam
WHERE ExamDate >= '2023-11-01' AND ExamDate <= '2023-11-30'
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the exams and their locations for November 2023
for row in results:
    exam_date, exam_time, location = row
    print("Exam Date: {}, Exam Time: {}, Location: {}".format(exam_date, exam_time, location))

# Close the connection
conn.close()
