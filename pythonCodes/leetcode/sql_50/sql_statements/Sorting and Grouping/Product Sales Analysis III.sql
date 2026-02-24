create table Sales (
	sale_id	int,
	product_id	int,
	year	int,
	quantity	int,
	price	int
	PRIMARY KEY (sale_id, year)
);

insert into Sales (sale_id, product_id, year, quantity, price)
values
(1, 100, 2008, 	10, 5000),
(2,	100,	2009,	12,	5000),
(7,	200,	2011,	15,	9000);


select t.product_id, t.first_year, s.quantity, s.price from  

(select product_id, min(year) as first_year from Sales group by product_id) t left join 

Sales s on  t.product_id = s.product_id and t.first_year = s.year 