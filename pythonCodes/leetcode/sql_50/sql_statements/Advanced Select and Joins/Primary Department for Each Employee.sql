create table Employee4 (
 employee_id   int    ,
  department_id  int     ,
  primary_flag   varchar(255)
  )

  insert into Employee4 (employee_id, department_id, primary_flag)
  values
 ( 1 , 1, 'N'  ),
 ( 2 , 1 , 'Y' ),
 ( 2 , 2, 'N'  ),
 ( 3, 3, 'N' ),
 ( 4, 2, 'N' ),
 ( 4, 3 , 'Y' ),
 ( 4, 4 , 'N' );


 (select employee_id, department_id from Employee4 where primary_flag = 'Y')

 union 

 (select employee_id, department_id from Employee4 where employee_id in (
	select employee_id from Employee4 group by employee_id having count(department_id) = 1
	))
