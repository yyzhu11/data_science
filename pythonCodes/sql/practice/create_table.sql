USE interview;

create table Student (
    STUDENT_ID int,
    FIRST_NAME varchar(255),
    LAST_NAME varchar(255),
    GPA float,
    ENROLLMENT_DATE DATETIME,
	MAJOR varchar(255),
	PRIMARY KEY (STUDENT_ID)

);


INSERT INTO Student (STUDENT_ID, FIRST_NAME, LAST_NAME, GPA, ENROLLMENT_DATE, MAJOR)
VALUES 
(201, 'Shivansh', 'Mahajan',  8.79, '2021-09-01 09:30', 'Computer Science'),
(202, 'Umesh', 'Sharma',  8.44, '2021-09-01 08:30', 'Mathematics'),
(203, 'Rakesh', 'Kumar',  5.6, '2021-09-01 10:00', 'Biology'),
(204, 'Radha', 'Sharma',  9.2, '2021-09-01 12:45', 'Chemistry'),
(205, 'Kush', 'Kumar',  7.85, '2021-09-01 08:30', 'Physics'),
(206, 'Prem', 'Chopra',  9.56, '2021-09-01 09:24', 'History'),
(207, 'Pankaj', 'Vats',  9.78, '2021-09-01 02:30', 'English'),
(208, 'Navleen', 'Kaur',  7, '2021-09-01 06:30', 'Mathematics');

create table Program (
    STUDENT_REF_ID int,
    "PROGRAM_NAME" varchar(255),
    PROGRAM_START_DATE DATETIME,    
	FOREIGN KEY (STUDENT_REF_ID) REFERENCES Student(STUDENT_ID)
);

INSERT INTO Program (STUDENT_REF_ID, "PROGRAM_NAME", PROGRAM_START_DATE)
VALUES 
(201, 'Computer Science',  '2021-09-01 00:00'),
(202, 'Mathematics',  '2021-09-01 00:00'),
(208, 'Mathematics',  '2021-09-01 00:00'),
(205, 'Physics',  '2021-09-01 00:00'),
(204, 'Chemistry',  '2021-09-01 00:00'),
(207, 'Psychology',  '2021-09-01 00:00'),
(206, 'History',  '2021-09-01 00:00'),
(203, 'Biology',  '2021-09-01 00:00');

create table Scholarship (
    STUDENT_REF_ID int,
    SCHOLARSHIP_AMOUNT int,
    SCHOLARSHIP_DATE DATETIME,    
	FOREIGN KEY (STUDENT_REF_ID) REFERENCES Student(STUDENT_ID)
);

INSERT INTO Scholarship (STUDENT_REF_ID, SCHOLARSHIP_AMOUNT, SCHOLARSHIP_DATE)
VALUES 
(201, 5000,  '2021-10-15 00:00'),
(202, 4500,  '2022-08-18 00:00'),
(208, 3000,  '2022-01-25 00:00'),
(205, 4000,  '2021-10-15 00:00');
