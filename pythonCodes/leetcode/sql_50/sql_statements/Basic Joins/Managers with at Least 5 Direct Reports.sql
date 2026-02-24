create table Employee0 (

id	int,
name	varchar(255),
department	varchar(255),
managerId	int,
primary key(id)
)


insert into Employee0(id,name,department,managerId)
values
(101,'John',	'A',	NULL),
(102,'Dan',	'A',	101),
(103,'James',	'A',	101),
(104,'Amy',	'A',	101),
(105,'Anne',	'A',	101),
(106,'Ron',	'B',	101);


select e2.name from Employee0 e1 join Employee0 e2 on e1.managerId = e2.id

group by e2.managerId, e2.name  having  count(distinct e1.id) >= 5





