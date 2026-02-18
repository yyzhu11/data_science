create table MyNumbers (
	num	int
)

insert into MyNumbers (num)
values
(8 ),
( 8 ),
( 3 ),
( 3 ),
( 1),
( 4),
( 5),
( 6 );


select max(num) as num from 

(select num, count(*) as cnt from MyNumbers group by num ) t1 where t1.cnt = 1