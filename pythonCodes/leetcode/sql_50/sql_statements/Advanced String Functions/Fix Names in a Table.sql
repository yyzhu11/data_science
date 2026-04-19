select user_id, UPPER(substring(name, 1,1)) + lower(substring(name, 2,len(name))) as name from Users_8

CREATE TABLE Users_8(
	[user_id] [int] NOT NULL,
	name [varchar](255) NULL,
	PRIMARY KEY (user_id)
	
);

insert into Users_8 (user_id, name)
values
(1, 'aLice'),
(2,	'bOB');

select user_id, Upper(substring(name, 1, 1)) + LOWER(substring(name, 2, len(name)-1)) as name from Users_8