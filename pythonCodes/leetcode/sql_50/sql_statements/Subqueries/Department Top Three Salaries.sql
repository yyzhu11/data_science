
select department_name, employee_name as Employee, salary from (

select DENSE_RANK() over ( partition by departmentId order by salary desc) as ranking, d.name as department_name, e.name as employee_name, salary  
from Employee6 e left join Department d on d.id = e.departmentId ) t1 where t1.ranking <= 3 order by department_name, salary desc
create table Employee6 (
	id	int,
	name varchar(255),
	salary int,
	departmentId int,
)

create table Department (
	id	int,
	name varchar(255),
)

insert into Employee6(id, name, salary, departmentId)
values
( 1  , 'Joe'   , 85000  , 1            ),
( 2  , 'Henry' , 80000  , 2            ),
( 3  , 'Sam'   , 60000  , 2            ),
( 4  , 'Max'   , 90000  , 1            ),
( 5  , 'Janet' , 69000  , 1            ),
( 6  , 'Randy' , 85000  , 1            ),
( 7  , 'Will'  , 70000  , 1            );


insert into Department(id, name)
values
( 1  , 'IT'    ),
( 2  , 'Sales' );


select t2.name, t1.name, t1.salary from 
(select  dense_rank() over (partition by departmentId order by salary desc) as ranking , salary, departmentId, name from Employee6) t1 left join Department t2
on t1.departmentId = t2.id 

where t1.ranking <=3