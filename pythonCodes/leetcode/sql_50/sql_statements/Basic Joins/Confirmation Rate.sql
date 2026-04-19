create table Signups (
user_id	int,
time_stamp	datetime

)

create table Confirmations(
user_id	int,
time_stamp	datetime,
action	varchar(255)
)

insert into Signups(user_id, time_stamp)
values
(3,	'2020-03-21 10:16:13'),
(7,	'2020-01-04 13:57:59'),
(2,	'2020-07-29 23:09:44'),
(6,	'2020-12-09 10:39:37');


insert into Confirmations(user_id, time_stamp, action)
values

(3,	'2021-01-06 03:30:46','timeout'),
(3,	'2021-07-14 14:00:00','timeout'),
(7,	'2021-06-12 11:57:29','confirmed'),
(7,	'2021-06-13 12:58:28','confirmed'),
(7,	'2021-06-14 13:59:27','confirmed'),
(2,	'2021-01-22 00:00:00','confirmed'),
(2,	'2021-02-28 23:59:59','timeout');


select s.user_id,  round((case when sum(case when c.action = 'confirmed' then 1 else 0 end) =0 then 0 
else sum(case when c.action = 'confirmed' then 1 else 0 end)*1.0/count(*) end), 2) as confirmation_rate

from Signups s left join Confirmations c on s.user_id = c.user_id group by s.user_id order by s.user_id

-----------------------------------------------------------------------

SELECT s.user_id,
       ROUND(ISNULL(AVG(case when c.action = 'confirmed' then 1.0 else 0 end), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
  ON s.user_id = c.user_id
GROUP BY s.user_id;
