select query_name,	round(avg(rating*1.0/position),2) as quality, 
round(sum(case when rating <3 then 1 else 0 end)*1.0/count(*),2) as poor_query_percentage from Queries group by query_name

create table Queries (
	query_name varchar(255),
	result varchar(255),
	position int,
	rating int
);

INSERT INTO Queries (query_name, result, position, rating)
VALUES 
('Dog', 'Golden Retriever', 1, 5),
('Dog', 'German Shepherd', 2, 5),
('Dog', 'Mule', 200, 1),
('Cat', 'Shirazi', 5, 2),
('Cat', 'Siamese', 3, 3),
('Cat', 'Sphynx', 7, 4);



select query_name, round(AVG(rating*1.0/position),2) as quality, 
round(sum(case when rating <3 then 1 else 0 end)*100.0/count(*),2) as poor_query_percentage from Queries group by query_name

SELECT query_name,
    ROUND(sum(rating / position) / COUNT(*), 2) as quality,
    ROUND(100 * SUM(rating < 3) / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP by query_name


-- Write your MySQL query statement below
SELECT
    query_name,
    ROUND(SUM(rating / position) / COUNT(*), 2) AS quality,
    ROUND(100 * SUM(rating < 3) / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;