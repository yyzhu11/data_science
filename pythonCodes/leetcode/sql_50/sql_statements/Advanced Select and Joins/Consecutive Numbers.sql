select l1.num from Logs l1 join Logs l2 on  l2.id = l1.id + 1 join Logs l3 on l3.id = l2.id+1
where l1.num = l2.num  and l2.num = l3.num

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

select t4.num1 as ConsecutiveNums from (
select t1.num as num1, t2.num as num2, t3.num as num3 from Logs t1 left join Logs t2  on t2.id = (t1.id +1) left join Logs t3 on t3.id = (t2.id+1)) t4 
where num1 = num2 and num2 = num3

select num as ConsecutiveNums from (
select num, LEAD(num, 1, null) OVER (ORDER BY id ) as num1, LEAD(num, 2, null) OVER (ORDER BY id ) as num2 from Logs) t1
where num = num1 and num1 = num2