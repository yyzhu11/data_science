create table Activity (
	player_id	int,
	device_id	int,
	event_date	date,
	games_played	int
);

insert into Activity (player_id, device_id, event_date,games_played)
values 
(1,	2,	'2016-03-01',	5),
(1,	2,	'2016-03-02',	6),
(2,	3,	'2017-06-25',	1),
(3,	1,	'2016-03-02',	0),
(3,	4,	'2018-07-03',	5); 


select round( sum(case when event_date is not null then 1 else 0 end)*1.0/count(distinct table1.player_id),2) 

as fraction from (
select t2.player_id,  t2.login_date, t1.event_date from 

(select player_id, min(event_date) as login_date from Activity group by player_id 
) t2 left join Activity t1 
on t2.login_date = dateadd(day, -1, t1.event_date) and t1.player_id = t2.player_id ) table1

