select p.product_name, num_order from 
(select product_id,  
sum(unit) as num_order from Orders where FORMAT(order_date, 'yyyy-MM')='2020-02'

group by product_id, FORMAT(order_date, 'yyyy-MM') having sum(unit) >= 100) t1 
left join Products p on t1.product_id = p.product_id

select product_name, sum(unit) as unit from Orders o left join Products p on o.product_id = p.product_id 
where order_date between '2020-02-01' and '2020-02-29' group by product_name having sum(unit) >= 100

create table Products (

	product_id	int,
	product_name	varchar(255),
	product_category	varchar(255)
	primary key (product_id)
);

create table Orders (
	product_id	int,
	order_date	date,
	unit	int,
	FOREIGN KEY (product_id) REFERENCES Products(product_id)
	);


insert into Products(product_id,product_name,product_category)
values
(1, 'Leetcode Solutions',	'Book'),
(2,	'Jewels of Stringology',	'Book'),
(3,	'HP',	'Laptop'),
(4,	'Lenovo',	'Laptop'),
(5,	'Leetcode Kit',	'T-shirt');


insert into Orders (product_id, order_date, unit)
values

(1,	'2020-02-05',	60),
(1,	'2020-02-10',	70),
(2,	'2020-01-18',	30),
(2,	'2020-02-11',	80),
(3,	'2020-02-17',	2),
(3,	'2020-02-24',	3),
(4,	'2020-03-01',	20),
(4,	'2020-03-04',	30),
(4,	'2020-03-04',	60),
(5,	'2020-02-25',	50),
(5,	'2020-02-27',	50),
(5,	'2020-03-01',	50);





