import mysql.connector

conn = mysql.connector.connect(host='localhost', password='shuvo634', user='root', database='shuvodb')
mycursor = conn.cursor()

# Create Student Table
Table_1 = """
CREATE TABLE IF NOT EXISTS Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Address TEXT
);
"""

# Create Course Table
Table_2 = """
CREATE TABLE IF NOT EXISTS Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(255),
    Credits INT
);
"""

# Create Exam Table
Table_3 = """
CREATE TABLE IF NOT EXISTS Exam (
    ExamID INT PRIMARY KEY,
    ExamDate DATE,
    ExamTime TIME,
    Location VARCHAR(255)
);
"""

# Create Faculty Table
Table_4 = """
CREATE TABLE IF NOT EXISTS Faculty (
    FacultyID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Department VARCHAR(255)
);
"""

# Create Enrollment Table
Table_5 = """
CREATE TABLE IF NOT EXISTS Enrollment (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
);
"""

# Create Teaching Table
Table_6 = """
CREATE TABLE IF NOT EXISTS Teaching (
    TeachingID INT PRIMARY KEY,
    FacultyID INT,
    CourseID INT,
    FOREIGN KEY (FacultyID) REFERENCES Faculty (FacultyID),
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
);
"""

# Create ExamRegistration Table
Table_7 = """
CREATE TABLE IF NOT EXISTS ExamRegistration (
    RegistrationID INT PRIMARY KEY,
    StudentID INT,
    ExamID INT,
    RegistrationDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID),
    FOREIGN KEY (ExamID) REFERENCES Exam (ExamID)
);
"""

# Create ExamResults Table
Table_8 = """
CREATE TABLE IF NOT EXISTS ExamResults (
    ResultID INT PRIMARY KEY,
    StudentID INT,
    ExamID INT,
    Score DECIMAL(5, 2),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID),
    FOREIGN KEY (ExamID) REFERENCES Exam (ExamID)
);
"""

# Execute the SQL queries to create tables
mycursor.execute(Table_1)
mycursor.execute(Table_2)
mycursor.execute(Table_3)
mycursor.execute(Table_4)
mycursor.execute(Table_5)
mycursor.execute(Table_6)
mycursor.execute(Table_7)
mycursor.execute(Table_8)

# Data insertion queries
# Insert data into the tables


data_insert = """
INSERT INTO ExamResults (ResultID, StudentID, ExamID, Score)
VALUES
    (501, 1, 201, 92.5),
    (502, 2, 201, 88.0),
    (503, 3, 202, 95.5),
    (504, 4, 203, 89.0),
    (505, 5, 204, 94.5),
    (506, 6, 205, 91.0),
    (507, 7, 201, 87.5);"""

# Execute the SQL queries
mycursor.execute(data_insert)





# Commit the changes and close the connection
conn.commit()
conn.close()
