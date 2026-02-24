create table Logs(

id	int,
num	varchar(255)
)

insert into Logs (id, num)
values
( 1 , '1'   ),
( 2  , '1'   ),
( 3  , '1'   ),
( 4  , '2'   ),
( 5  , '1'   ),
( 6  , '2'   ),
( 7  , '2'   );

select l1.num from Logs l1 join Logs l2 on  l2.id = l1.id + 1 join Logs l3 on l3.id = l2.id+1
where l1.num = l2.num  and l2.num = l3.num