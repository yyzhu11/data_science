create table Delivery (
	delivery_id  int, 
	customer_id int,     
	order_date date,
	customer_pref_delivery_date date
);

insert into Delivery (delivery_id, customer_id, order_date,customer_pref_delivery_date)
values 
(1, 1 , '2019-08-01', '2019-08-02'),
(2, 2 ,  '2019-08-02' ,  '2019-08-02'),
(3, 1 ,  '2019-08-11' ,  '2019-08-12'),
(4 ,  3 ,  '2019-08-24' ,  '2019-08-24'),
(5 ,  3 ,  '2019-08-21' ,  '2019-08-22'),
(6 ,  2  ,  '2019-08-11',  '2019-08-13'),
(7 ,  4 ,  '2019-08-09',  '2019-08-09');   

select round(sum(if_immediate)*1.0/count(distinct customer_id),2) from 

(select customer_id, (case when min(order_date)=min(customer_pref_delivery_date) then 1 else 0 end) as if_immediate  
from Delivery group by customer_id) t


