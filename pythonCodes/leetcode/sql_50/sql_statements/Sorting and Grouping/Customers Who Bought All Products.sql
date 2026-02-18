create table Customer (
	customer_id  int, 
	product_key  int,
	FOREIGN KEY (product_key) REFERENCES Product(product_key)
);

create table Product (
	product_key  int,
	PRIMARY KEY (product_key)
);
insert into Product (product_key)
values
(5),
(6);

insert into Customer (customer_id, product_key)
values 
(1,  5 ),
(2,  6 ),
(3 , 5 ),  
(3,  6 ),
(1,  6 );

select distinct customer_id 

from 

(select customer_id, count(distinct product_key) as num_product from Customer group by customer_id ) t1

where t1.num_product = (select count(distinct product_key) from Product)


