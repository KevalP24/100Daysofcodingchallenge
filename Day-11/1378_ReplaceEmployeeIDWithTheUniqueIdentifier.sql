# Write your MySQL query statement below
select e.unique_id,m.name from Employees m left join EmployeeUNI e on e.id=m.id;
