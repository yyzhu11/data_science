select results from 
(select top 1 u2.name as results from MovieRating u1 left join Users_9 u2 on u1.user_id = u2.user_id group by u1.user_id, u2.name 
order by count(distinct movie_id) desc, u2.name ) t2

UNION   

select results from 
(select top 1 m2.title as results from MovieRating m1 left join Movies m2 on m1.movie_id = m2.movie_id

where m1.created_at between '2020-02-01' and '2020-02-29' group by m1.movie_id, m2.title order by avg(rating*1.0) desc, m2.title) t1


create table Users_9 (
	user_id	int,
	name	varchar(255),
)

insert into Users_9(user_id, name)
values
(1	,'Daniel'),
(2	,'Monica'),
(3	,'Maria'),
(4	,'James');


create table Movies (
	movie_id int,
	title varchar(255),
)

insert into Movies(movie_id, title)
values
(1	,'Avengers'),
(2	,'Frozen 2'),
(3	,'Joker');

create table MovieRating (
	movie_id	int,
	user_id	 int,
	rating	int,
	created_at	date,
)


insert into MovieRating(movie_id, user_id, rating, created_at)
values
( 1, 1, 3, '2020-01-12'  ),
( 1,  2,  4 ,'2020-02-11'  ),
( 1,  3 ,2 , '2020-02-12'  ),
( 1, 4, 1, '2020-01-01'  ),
( 2, 1, 5, '2020-02-17'  ), 
( 2, 2, 2, '2020-02-01'  ), 
( 2, 3,2, '2020-03-01'  ),
( 3, 1, 3, '2020-02-22'  ), 
( 3, 2, 4, '2020-02-25' );


select results from 
(
select top 1 t2.name as results from MovieRating t1 left join Users_9 t2 on t1.user_id = t2.user_id

group by t1.user_id, t2.name order by count(t1.movie_id) desc, t2.name 

) t3

union

select results from 
(
select top 1 t6.title as results from MovieRating t5 left join Movies t6 on t5.movie_id = t6.movie_id where 
created_at between '2020-02-01' and '2020-02-29' 

group by t5.movie_id, t6.title order by avg(t5.rating*1.0) desc, t6.title 

) t7