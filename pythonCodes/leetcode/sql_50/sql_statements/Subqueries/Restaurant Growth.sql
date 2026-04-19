select visited_on, amount, average_amount from (
select visited_on, sum(sum_amount) over (order by visited_on ROWS BETWEEN 
 6 PRECEDING  AND CURRENT ROW ) as amount, round(sum(sum_amount) over (order by visited_on ROWS BETWEEN 
 6 PRECEDING  AND CURRENT ROW )*1.0/7,2)  as average_amount from 
(select sum(amount) as sum_amount, visited_on from Customer2 group by visited_on) t1) t2 

where visited_on >= (select dateadd(day, 6, min(visited_on)) from Customer2)



create table Customer2 (
	customer_id	int,
	name	varchar(255),
	visited_on date,
	amount int
)

insert into Customer2(customer_id, name, visited_on, amount)
values
(1,		'Jhon',	'2019-01-01',	100),
(2, 	'Daniel',	'2019-01-02',	110),
(3, 	'Jade',	'2019-01-03',	120),
(4, 	'Khaled',	'2019-01-04',	130),
(5, 	'Winston',	'2019-01-05',	110),
(6, 	'Elvis',	'2019-01-06',	140),
(7, 	'Anna',	'2019-01-07',	150),
(8, 	'Maria',	'2019-01-08',	80),
(9, 	'Jaze',	'2019-01-09',	110),
(1, 	'Jhon',	'2019-01-10',	130),
(3, 	'Jade',	'2019-01-10',	150);
-- visited_on	amount	average_amount
--2019-01-07	860	122.86
--2019-01-08	840	120
--2019-01-09	840	120
--2019-01-10	1000	142.86



 select sum(sum_amount) over (order by visited_on rows between 6 PRECEDING and current row ) as amount, 
 round(sum(sum_amount*1.0) over (order by visited_on rows between 6 PRECEDING and current row )/7, 2) as average_amount,
 visited_on from 
 
(select sum(amount) as sum_amount, visited_on from Customer2 group by visited_on) t1 

where datediff(day, (select min(visited_on) from Customer2), visited_on) >= 6


select  from Customer2 t1 left join Customer2 t2 on datediff(day, t2.visited_on, t1.visited_on)





SELECT 
    a.visited_on, 
    SUM(b.amount) AS amount, 
    ROUND(SUM(b.amount*1.0)/7, 2) AS average_amount 

FROM 
    (SELECT DISTINCT visited_on FROM Customer2) a 
    JOIN Customer2 b ON DATEDIFF(day,b.visited_on, a.visited_on) BETWEEN 0 AND 6

GROUP BY a.visited_on
HAVING a.visited_on >= (select dateadd(day, 6, min(visited_on)) from Customer2)