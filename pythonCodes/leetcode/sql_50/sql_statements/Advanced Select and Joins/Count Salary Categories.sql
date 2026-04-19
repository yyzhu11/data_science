select 'Low Salary' as category, sum(case when income < 20000 then 1 else 0 end ) as accounts_count 
from Accounts 
union 
select 'Average Salary' as category, sum(case when income >= 20000 and income <= 50000 then 1 else 0 end ) as accounts_count  from Accounts
union
select 'High Salary' as category, sum(case when income > 50000 then 1 else 0 end ) as accounts_count  from Accounts


select 'Low Salary' as category, sum(case when income < 20000 then 1 else 0 end) as accounts_count from Accounts
union 

select 'Average Salary' as category, sum(case when income >= 20000 and income <= 50000 then 1 else 0 end) as accounts_count from Accounts
union
select 'High Salary' as category, sum(case when income > 50000 then 1 else 0 end) as accounts_count from Accounts


create table Accounts (

account_id	int,
income	int
);

insert into Accounts(account_id, income)
values
(3,	108939),
(2,	12747),
(8,	87709),
(6,	91796); 


select 'Low Salary' as category, 
sum(case when income < 20000 then 1 else 0 end) as accounts_count from Accounts

union 

select 'Average Salary' as category, 
sum(case when income >= 20000 and income >= 50000 then 1 else 0 end) as accounts_count from Accounts

union

select 'High Salary' as category, 
sum(case when income > 50000 then 1 else 0 end) as accounts_count from Accounts




