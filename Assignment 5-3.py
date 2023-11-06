import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to list exams scheduled after November 15, 2023
select_query = "SELECT * FROM Exam WHERE ExamDate > '2023-11-15'"

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the exams scheduled after November 15, 2023
for row in results:
    exam_id, exam_date, exam_time, location = row
    print("Exam ID: {}, Date: {}, Time: {}, Location: {}".format(exam_id, exam_date, exam_time, location))

# Close the connection
conn.close()
