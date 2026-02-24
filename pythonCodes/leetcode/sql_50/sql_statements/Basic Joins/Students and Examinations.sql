create table Students (

student_id	int,
student_name	varchar(255)

)

create table Subjects(
subject_name	varchar(255)
)

create table Examinations(
student_id	int,
subject_name	varchar(255)
)

insert into Students(student_id, student_name)
values
(1	,'Alice'),
(2	,'Bob'),
(13	,'John'),
(6	,'Alex');

insert into Subjects(subject_name)
values
('Math'),
('Physics'),
('Programming');

insert into Examinations(student_id, subject_name)
values
(1	,'Math'),
(1	,'Physics'),
(1	,'Programming'),
(2	,'Programming'),
(1	,'Physics'),
(1	,'Math'),
(13	,'Math'),
(13	,'Programming'),
(13	,'Physics'),
(2	,'Math'),
(1	,'Math');


select t1.student_id, t1.student_name, t1.subject_name, ISNULL(t2.attended_exams,0)  as attended_exams from 
(select s.student_id, student_name,	b.subject_name
from Students s join Subjects b on 1=1) t1  left join 
(select student_id, subject_name, count(*) as attended_exams from Examinations group by student_id, subject_name) t2 
on t1.student_id = t2.student_id and t1.subject_name = t2.subject_name order by t1.student_id, t1.subject_name


