create table Users (
	user_id int,
	user_name varchar(255),
	PRIMARY KEY (user_id)
);

INSERT INTO Users (user_id, user_name)
VALUES 
(6, 'Alice'),
(2, 'Bob'),
(7, 'Alex');

create table Register (
	contest_id int,
	user_id int,
	FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Register (contest_id, user_id)
VALUES 
(215, 6),
(209, 2),
(208, 2),
(210, 6),
(208, 6),
(209, 7),
(209, 6),
(215, 7),
(208, 7),
(210, 2),
(207, 2),
(210, 7);


select contest_id, round (count(distinct user_id)*1.0/(select count(user_id) from Users) *100, 2) from Register  group by contest_id


select contest_id, round(count(distinct user_id) *100.0/(select count(*) from Users), 2) as percentage from Register group by contest_id 
order by percentage desc, contest_id 