create table Employee11 (
	id	int,
	salary	int,
	primary key (id)
)

insert into Employee11(id, salary)
values
(1,100),
(2,100),
(3,100);

select  distinct salary from Employee11 order by salary desc


SELECT distinct salary FROM Employee11
ORDER BY salary desc  -- Mandatory clause
OFFSET 1 ROWS            -- Skips the first row
FETCH NEXT 1 ROWS ONLY