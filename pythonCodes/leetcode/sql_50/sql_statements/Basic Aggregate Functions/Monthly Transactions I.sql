select FORMAT(trans_date, 'yyyy-MM') as month, country,  count(distinct id) as trans_count, 
sum(case when state ='approved' then 1 else 0 end) as approved_count , sum(amount) as trans_total_amount , 
sum(case when state ='approved' then amount else 0 end) as approved_total_amount 
from Transactions group by FORMAT(trans_date, 'yyyy-MM'), country

create table Transactions (
	id int,
	country varchar(255),
	state varchar(255),
	amount int,
	trans_date date
	);

insert into Transactions ( id  , country,state , amount ,trans_date)
values
(121 , 'US' , 'approved' ,1000 ,'2018-12-18' ),
(122 , 'US' , 'declined' ,2000 ,'2018-12-19' ),
(123 , 'US' , 'approved' ,2000 ,'2019-01-01' ),
(124 , 'DE' , 'approved' ,2000 ,'2019-01-07' );




-- Write an SQL query to find for each month and country, the number of transactions and their total amount, 
-- the number of approved transactions and their total amount

select format(trans_date, 'yyyy-MM') as month, country, count(*) as trans_count, sum(case when state ='approved' then 1 else 0 end) as approved_count,

sum(amount) as trans_total_amount, sum(case when state ='approved' then amount else 0 end) as	approved_total_amount
from Transactions group by format(trans_date, 'yyyy-MM'), country 



select FORMAT(trans_date, 'yyyy-MM') AS month from Transactions group by month, country, 

SELECT DATEPART(MONTH, '2025-01-19') AS MonthNumber