create table Employee2 (
	id	int,
	salary	int,
	primary key (id)
)

insert into Employee2(id, salary)
values
(1,100);


select t1.salary as SecondHighestSalary 
from (select id, salary, rank() over ( order by salary desc) as ranking from Employee2) t1
where t1.ranking = 2

