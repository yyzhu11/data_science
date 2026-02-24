create table Activities (
	sell_date	date,
	product	varchar(255)
)

insert into Activities(sell_date, product)
values
('2020-05-30',	'Headphone'),
('2020-06-01',	'Pencil'),
('2020-06-02',	'Mask'),
('2020-05-30',	'Basketball'),
('2020-06-01',	'Bible'),
('2020-06-02',	'Mask'),
('2020-05-30',	'T-Shirt');

select sell_date, count(distinct product) as num_sold, STRING_AGG(distinct product, ',') from Activities 
group by sell_date