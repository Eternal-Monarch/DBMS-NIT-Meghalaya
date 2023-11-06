import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to find the average score for each exam
select_query = """
SELECT ExamID, AVG(score) as AverageScore
FROM ExamResults
GROUP BY ExamID
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the average score for each exam
for row in results:
    exam_id, average_score = row
    print("Exam ID: {}, Average Score: {}".format(exam_id, average_score))

# Close the connection
conn.close()
