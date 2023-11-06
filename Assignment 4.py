
import mysql.connector
# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='shuvo634',
database='shuvodb')
mycursor = conn.cursor()
# Define the SQL query to create the table
Insert_1 = '''
INSERT INTO Student(StudentID,Name,Email,Phone,Address)
VALUES (1,"John Doe", "john.doe@example.com", "123-456-7890", "123 Main St"),
(2, "Jane Smith", "jane.smith@example.com", "987-654-3210", "456 Elm St"),
(3, "Robert Johnson", "robert.j@example.com", "555-123-4567", "789 Oak Ave"),
(4, "Emily White", "emily.white@example.com", "111-222-3333", "567 Pine St"),
(5, "Michael Lee", "michael.lee@example.com", "333-444-5555", "789 Cedar Dr"),
(6, "Sarah Brown", "sarah.brown@example.com", "555-666-7777", "890 Willow Ln"),
(7, "David Clark", "david clark@example.com", "777-888-9999", "123 Birch Ave"),
(8, "Melissa Turner", "melissa.turner@example.com", "888-999-0000", "456 Redwood
Rd");
'''
Insert_2 = '''
INSERT INTO Course (CourseID, CourseName, Credits)
VALUES (101, "Mathematics" ,3),
(102, "History", 4),
(103, "Computer science",3),
(104, "Literature",3),
(105, "Chemistry", 4),
(106, "Physics", 4),
(107, "Economics",3),
(108, "Biology", 4);
'''
Insert_3 = '''
INSERT INTO Exam(ExamID, ExamDate, ExamTime, Location)
VALUES (201, "2023-11-10", "09:00:00", "Exam Hall A"),
(202, "2023-11-12", "14:00:00", "Exam Hall B"),
(203, "2023-11-15", "10:30:00", "Exam Hall C"),
(204, "2023-11-18", "15:15:00", "Exam Hall D"),
(205, "2023-11-20", "13:00:00", "Exam Hall E");
'''
Insert_4 = '''
INSERT INTO Faculty(FacultyID, Name, Email, Phone, Department)
VALUES (301, "Dr. Smith", "smith@example.com", "111-222-3333", "Mathematics"),
(302, "Prof. Johnson" ,"johnson@example.com", "444-555-6666", "History"),
(303, "Prof. Brown", "brown@example.com", "777-888-9999", "Computer Science"),
(304, "Dr. Parker", "parker@example.com", "888-777-6666", "Chemistry"),
(305, "Prof. Adams", "adams@example.com", "999-888-7777", "Physics"),
(306, "Dr. Wilson", "wilson@example.com", "555-444-3333", "Economics"),
(307, "Prof. Davis", "davis@example.com", "333-222-1111", "Biology"),
(308, "Dr. Turner", "turner@example.com", "222-333-4444", "Literature");
'''
Insert_5 = '''
INSERT INTO Enrollment (EnrollmentID, StudentID, CourseID, EnrollmentDate)
VALUES (1, 1, 101, "2023-09-01"),
(2, 1, 102, "2023-09-10"),
(3, 2, 101, "2023-09-02"),
(4, 3, 103, "2023-09-03"),
(5, 4, 104, "2023-09-04"),
(6, 5, 105, "2023-09-05"),
(7, 6, 106, "2023-09-06"),
(8, 7, 107, "2023-09-07"),
(9, 8, 108, "2023-09-08");
'''
Insert_6 = """
INSERT INTO Teaching (TeachingID, FacultyID, CourseID)
VALUES (1, 301, 101),
(2, 302, 102),
(3, 303, 103),
(4, 304, 104),
(5, 305, 105),
(6, 306, 106),
(7, 307, 107),
(8, 308, 108);
"""
Insert_7 = '''
INSERT INTO ExamRegistration (RegistrationID, StudentID, ExamID, RegistrationDate)
VALUES (101, 1, 201, "2023-10-15"),
(102, 2, 201, "2023-10-16"),
(103, 3, 202, "2023-10-17"),
(104, 4, 203, "2023-10-18"),
(105, 5, 204, "2023-10-19"),
(106, 6, 205, "2023-10-20"),
(107, 7, 201, "2023-10-21"),
(108, 8, 202, "2023-10-22");
'''
Insert_8 = """
INSERT INTO ExamResults (ResultID, StudentID, ExamID, score)
VALUES (501, 1, 201, 92.5),
(502, 2, 201, 88.0),
(503, 3, 202, 95.5),
(504, 4, 203, 89.0),
(505, 5, 204, 94.5),
(506, 6, 205, 91.0),
(507, 7, 201, 87.5);
"""
# Execute the SQL query
mycursor.execute(Insert_1)
mycursor.execute(Insert_2)
mycursor.execute(Insert_3)
mycursor.execute(Insert_4)
mycursor.execute(Insert_5)
mycursor.execute(Insert_6)
mycursor.execute(Insert_7)
mycursor.execute(Insert_8)
# Commit the changes
conn.commit()
# Close the connection
conn.close()


