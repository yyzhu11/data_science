select top 1 accepter_id as id, coalesce(friend_count1,0) + coalesce(friend_count2,0) as num  from 

(select count(distinct requester_id) as friend_count1, accepter_id from RequestAccepted group by accepter_id) t1

left join 

(select count(distinct accepter_id) as friend_count2, requester_id from RequestAccepted group by requester_id) t2 

on t1.accepter_id = t2.requester_id  order by num desc 

create table RequestAccepted (
	requester_id	int,
	accepter_id int,
	accept_date date,	
)



insert into RequestAccepted(requester_id, accepter_id, accept_date)
values
(1,	2, '2016/06/03'),
(1, 3,	'2016/06/08'),
(2, 3, '2016/06/08'),
(3, 4, '2016/06/09');


select top 1 accepter_id as id, (coalesce(t1.friend_count1,0) + coalesce(t2.friend_count2,0)) as num from 

(select count(distinct requester_id) as friend_count1, accepter_id from RequestAccepted group by accepter_id) t1

left join 

(select count(distinct accepter_id) as friend_count2, requester_id from RequestAccepted group by requester_id) t2 
on t1.accepter_id = t2.requester_id order by num desc 