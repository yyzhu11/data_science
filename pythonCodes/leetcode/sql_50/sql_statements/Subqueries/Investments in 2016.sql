select round(sum(tiv_2016),2) as tiv_2016 from Insurance

where tiv_2015 in (

select tiv_2015 from Insurance group by tiv_2015 having count(*) > 1 ) and CONCAT(lat,',', lon) in (


select CONCAT(lat,',', lon) from Insurance group by lat, lon having count(*) =1)

create table Insurance (
	pid	int,
	tiv_2015 float,
	tiv_2016 float,
	lat	float,
	lon	float,

)



insert into Insurance(pid, tiv_2015, tiv_2016, lat, lon)
values
( 1   , 10       , 5        , 10  , 10  ),
( 2   , 20       , 20       , 20  , 20  ),
( 3   , 10       , 30       , 20  , 20  ),
( 4   , 10       , 40       , 40  , 40  );


select round(CONVERT(FLOAT, sum(tiv_2016*1.00)), 2) as tiv_2016 from Insurance 
where tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(distinct pid) >= 2) 
and concat(lat,',', lon) in (select concat(lat,',', lon) from Insurance group by lat, lon having count(distinct pid)=1)








9
