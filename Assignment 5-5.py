import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634', database='shuvodb')
mycursor = conn.cursor()

# Define the SQL query to retrieve the courses that each student is enrolled in
select_query = """
SELECT Student.Name, Course.CourseName
FROM Student
JOIN Enrollment ON Student.StudentID = Enrollment.StudentID
JOIN Course ON Enrollment.CourseID = Course.CourseID
"""

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the results
results = mycursor.fetchall()

# Create a dictionary to store courses for each student
student_courses = {}

# Populate the dictionary with student-course information
for row in results:
    student_name, course_name = row
    if student_name not in student_courses:
        student_courses[student_name] = []
    student_courses[student_name].append(course_name)

# Print the courses for each student
for student, courses in student_courses.items():
    print("Student: {}".format(student))
    for course in courses:
        print(" - Course: {}".format(course))

# Close the connection
conn.close()
