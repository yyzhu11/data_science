-- 1. Write a SQL query to fetch "FIRST_NAME" from the Student table in upper case 
-- and use ALIAS name as STUDENT_NAME.

SELECT upper("FIRST_NAME") as STUDENT_NAME from Student;

-- 2. Write a SQL query to fetch unique values of MAJOR Subjects from Student table

SELECT distinct MAJOR from Student;

-- 3. Write a SQL query to print the first 3 characters of FIRST_NAME from Student table

SELECT substring(FIRST_NAME,0,4) from Student;

-- 4. Write a SQL query to find the position of alphabet ('a') 
-- int the first name column 'Shivansh' from Student table

SELECT CHARINDEX('a',FIRST_NAME) from Student where FIRST_NAME='Shivansh'

-- 5. Write a SQL query that fetches the unique values of 
-- MAJOR Subjects from Student table and print its length

SELECT DISTINCT MAJOR, len(MAJOR) from Student

--6. Write a SQL query to print FIRST_NAME from the Student 
-- table after replacing 'a' with 'A'

SELECT replace(FIRST_NAME, 'a', 'A') as first_name from Student

--7. Write a SQL query to print the FIRST_NAME and LAST_NAME 
-- from Student table into single column COMPLETE_NAME

SELECT FIRST_NAME+' '+LAST_NAME AS COMPLETE_NAME FROM Student

--8. Write a SQL query to print all Student details from Student table 
--order by FIRST_NAME Ascending and MAJOR Subject descending

SELECT * FROM Student order by FIRST_NAME asc , MAJOR desc

--9. Write a SQL query to print details of the Students with 
-- the FIRST_NAME as 'Prem' and 'Shivansh' from Student table.

SELECT * FROM Student where FIRST_NAME in ('Prem', 'Shivansh')

--10. Write a SQL query to print details of the Students 
-- excluding FIRST_NAME as 'Prem' and 'Shivansh' from Student table.

SELECT * FROM Student where FIRST_NAME not in ('Prem', 'Shivansh')

--11. Write a SQL query to print details of the Students whose 
-- FIRST_NAME ends with 'a'

SELECT * FROM Student where FIRST_NAME like '%a'

--12. Write an SQL query to print details of the Students whose 
--FIRST_NAME ends with ‘a’ and contains five alphabets

SELECT * FROM Student where FIRST_NAME like '____a' 

--13. Write an SQL query to print details of the Students 
--whose GPA lies between 9.00 and 9.99

SELECT * FROM Student where GPA between 9.00 and 9.99

--14. Write an SQL query to fetch the count of Students 
--having Major Subject ‘Computer Science’.

SELECT COUNT(*) from Student where MAJOR ='Computer Science'

--15.Write an SQL query to fetch Students full names with GPA >= 8.5 and <= 9.5.

SELECT FIRST_NAME+' '+LAST_NAME AS Full_name from Student where GPA >=8.5 AND GPA <=9.5

--16. Write an SQL query to fetch the no. of Students for 
--each MAJOR subject in the descending order.

select count(*) as Count_Major, MAJOR from Student group by MAJOR order by Count_Major desc

--17.Display the details of students who have received scholarships, 
--including their names, scholarship amounts, and scholarship dates

select t.FIRST_NAME, t.LAST_NAME, s.SCHOLARSHIP_AMOUNT, s.SCHOLARSHIP_DATE from Student t
left join Scholarship s on s.STUDENT_REF_ID = t.STUDENT_ID where SCHOLARSHIP_AMOUNT is not null


--18.Write an SQL query to show only odd rows from Student table

select * from Student where STUDENT_ID %2 =1

--19. Write an SQL query to show only even rows from Student table

select * from Student where STUDENT_ID %2 =0

--20. List all students and their scholarship amounts 
-- if they have received any. If a student has not received a scholarship, 
-- display NULL for the scholarship details.

select s.FIRST_NAME, s.LAST_NAME, t.SCHOLARSHIP_AMOUNT 
from Student s 
left join Scholarship t on s.STUDENT_ID = t.STUDENT_REF_ID


--21. Write an SQL query to show the top n (say 5) records of 
-- Student table order by descending GPA

select top 5 * from Student order by GPA desc

--22. Write an SQL query to determine the nth (say n=5) highest GPA from a table

select top 1 * from (select top 6 *  from Student order by GPA desc) t  order by GPA 

select * from Student order by GPA desc OFFSET 5 ROWS FETCH NEXT 1 ROWS ONLY

--23. Write an SQL query to determine the 5th highest GPA without 
--using LIMIT keyword

select * from (select ROW_NUMBER() OVER (ORDER BY GPA desc) as row_num, * from Student) t where row_num = 6

--24. Write an SQL query to fetch the list of Students with the same GPA

select s.FIRST_NAME, s.LAST_NAME, t.FIRST_NAME, t.LAST_NAME from Student s 
left join  Student t on s.GPA = t.GPA where s.STUDENT_ID!= t.STUDENT_ID


--25. Write an SQL query to show the second highest GPA from a Student 
-- table using sub-query

select top 1 * from (select top 2 * from Student order by GPA desc) t order by GPA 

--26. Write an SQL query to show one row twice in results from a table.
--UNION vs UNION ALL
select * from Student s
UNION ALL select * from Student t order by STUDENT_ID

--27. Write an SQL query to list STUDENT_ID who does not get Scholarship

select t.STUDENT_ID from Student t 
left join Scholarship s on t.STUDENT_ID = s.STUDENT_REF_ID where s.SCHOLARSHIP_AMOUNT is null

SELECT STUDENT_ID FROM Student 
WHERE STUDENT_ID NOT IN (SELECT STUDENT_REF_ID FROM Scholarship);

--28. Write an SQL query to fetch the first 50% records from a table

select select count(*) as num from Student  

--29.Write an SQL query to fetch the MAJOR subject that have less than 
-- 4 people in it

select count(MAJOR), MAJOR from Student group by MAJOR having count(MAJOR) < 4

--30. Write an SQL query to show all MAJOR subject along with 
-- the number of people in there

select count(MAJOR), MAJOR from Student group by MAJOR

--31. Write an SQL query to show the last record from a table

select * from (select ROW_NUMBER() over(order by (select 1)) as row_num, * from Student) t 
where row_num=(select count(*) from Student)

--32. Write an SQL query to fetch the first row of a table

select * from (select ROW_NUMBER() over(order by (select 1)) as row_num, * from Student) t where row_num = 1

--33. Write an SQL query to fetch the last five records from a table

select * from Student where STUDENT_ID in (select top 5 STUDENT_ID from Student  order by STUDENT_ID desc) order by STUDENT_ID


--34. Write an SQL query to fetch three max GPA from a table 
--using co-related subquery.

select GPA from (select row_number() over(order by GPA desc) as row_num, GPA from Student )t where row_num <4
 

--35. Write an SQL query to fetch three min GPA from a 
--table using Correlated subquery

select GPA from (select row_number() over(order by GPA) as row_num, GPA from Student )t where row_num <4

--36. Write an SQL query to fetch nth max GPA from a table

select GPA from (select distinct GPA, ROW_NUMBER() over(order by GPA desc)  as row_num from Student) t where row_num = 2

SELECT DISTINCT GPA FROM Student S1 
WHERE 2 = (SELECT COUNT(DISTINCT GPA) FROM Student S2 WHERE S1.GPA <= S2.GPA) 
ORDER BY S1.GPA DESC;

--37. Write an SQL query to fetch MAJOR subjects along with the max 
--GPA in each of these MAJOR subjects.

select select max(GPA) as max_GPA, MAJOR from Student group by MAJOR

--38. Write an SQL query to fetch the names of Students who has highest GPA

select top 1 FIRST_NAME, LAST_NAME FROM Student order by GPA

--39. Write an SQL query to show the current date and time.

select SYSDATETIME() 

--40. Write a query to create a new table which consists of data and 
--structure copied from the other table (say Student) or clone the table 
--named Students
use interview
SELECT * INTO newtable FROM Student


--41. Write an SQL query to update the GPA of all the students 
--in 'Computer Science' MAJOR subject to 7.5

update Student set MAJOR=7.5 where MAJOR='Computer Science'

--42. Write an SQL query to find the average GPA for each major

SELECT AVG(GPA), MAJOR from Student group by MAJOR

--43. Write an SQL query to show the top 3 students with the highest GPA

SELECT TOP 3 * FROM Student order by GPA desc

--44. Write an SQL query to find the number of students in each major 
--who have a GPA greater than 3.5

SELECT COUNT(*) from (Select * from Student where GPA > 3.5) t group by MAJOR 


--45. Write an SQL query to find the students who have the same 
--GPA as 'Shivansh Mahajan'

SELECT * FROM Student where GPA =  
(SELECT GPA FROM Student where FIRST_NAME+' '+LAST_NAME = 'Shivansh Mahajan') 


