select (id +1) AS id, student from Seat where id % 2 =1 and (id +1) in (select id from Seat)

union 

select (id -1) AS id, student from Seat where id % 2 =0 and (id -1) in (select id from Seat)

union

select (id) AS id, student from Seat where id % 2 =1 and id = (select max(id) from Seat)

create table Seat (

	id	int,
	student	varchar(255),

)


insert into Seat(id, student)
values

( 1  , 'Abbot'  ),
( 2  , 'Doris'   ),
( 3  , 'Emerson' ),
( 4  , 'Green'   ),
( 5  , 'Jeames'  )


select (case when id % 2 = 0  then (id -1)
 when id % 2 =1 and id+1 < (select max(id) from Seat) then id +1 
when id = (select max(id) from Seat) and id % 2 =1 then id end) as id, student from Seat order by id