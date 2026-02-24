create table Products2(

product_id	int,
new_price	int,
change_date	date
)


insert into Products2(product_id, new_price, change_date)
values
(1,20,	'2019-08-14'),
(2,50,	'2019-08-14'),
(1,	30,	'2019-08-15'),
(1,	35,	'2019-08-16'),
(2,	65,	'2019-08-17'),
(3,	20,	'2019-08-18');



select p4.product_id, (case when max_date > '2019-08-16' and min_price is not null then min_price 
when max_date = '2019-08-16' and max_price is not null then max_price else 10 end) as price from 

(select p1.product_id, max_date, p2.new_price as max_price, min_date, p3.new_price as min_price from 
( select product_id, min(case when change_date >= '2019-08-16' then change_date else null end) as max_date,
max(case when change_date < '2019-08-16' then change_date else null end) as min_date from Products2 
group by product_id ) p1 left join Products2 p2 on p1.product_id = p2.product_id and p1.max_date =  p2.change_date
left join Products2 p3 on p1.product_id = p3.product_id and p1.min_date =  p3.change_date ) p4