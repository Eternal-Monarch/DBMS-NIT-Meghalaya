import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve faculty members with an average enrollment count above 10
select_query = '''
SELECT F.Name AS FacultyName, F.Department, AVG(EnrollmentCount) AS AverageEnrollment
FROM Faculty F
JOIN Teaching T ON F.FacultyID = T.FacultyID
JOIN Course C ON T.CourseID = C.CourseID
LEFT JOIN (
    SELECT CourseID, COUNT(StudentID) AS EnrollmentCount
    FROM Enrollment
    GROUP BY CourseID
) AS E ON C.CourseID = E.CourseID
GROUP BY F.FacultyID
HAVING AVG(EnrollmentCount) > 10;
'''

# Execute the SQL query
mycursor.execute(select_query)

# Fetch and print the results
results = mycursor.fetchall()
for result in results:
    faculty_name, department, average_enrollment = result
    print(f"Faculty Name: {faculty_name}, Department: {department}, Average Enrollment: {average_enrollment:.2f}")

# Close the connection
conn.close()
