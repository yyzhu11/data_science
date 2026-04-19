 (select employee_id, department_id from Employee4 where primary_flag = 'Y')

 union 

 (select employee_id, department_id from Employee4 where employee_id in (
	select employee_id from Employee4 group by employee_id having count(department_id) = 1
	))


	 select t1.employee_id, t2. department_id from 

(select employee_id, count(department_id) as count_dep from Employee4 group by employee_id) t1 
left join Employee4 t2 on t1.employee_id = t2.employee_id

where (count_dep = 1 and primary_flag = 'N') or (count_dep > 1 and primary_flag = 'Y')
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

 select t1.employee_id, t1.department_id from Employee4 t1 left join (
 
 select employee_id, count(distinct department_id) as dep_count from Employee4 group by employee_id ) t2 on t1.employee_id = t2.employee_id

 where (t2.dep_count = 1 and t1.primary_flag = 'N') or (t2.dep_count > 1 and t1.primary_flag = 'Y')

