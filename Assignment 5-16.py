import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to list faculty members who have yet to teach any courses
select_query = """
SELECT Faculty.Name
FROM Faculty
WHERE Faculty.FacultyID NOT IN (SELECT DISTINCT FacultyID FROM Teaching)
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Print the faculty members who have yet to teach any courses
if results:
    for row in results:
        faculty_name = row[0]
        print("Faculty member who has yet to teach any courses: {}".format(faculty_name))
else:
    print("No faculty members found who have yet to teach any courses.")

# Close the connection
conn.close()
