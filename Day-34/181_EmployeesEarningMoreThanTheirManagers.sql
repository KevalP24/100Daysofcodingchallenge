# Write your MySQL query statement below
select e.name as Employee from Employee as e, Employee as s where e.managerId = s.id and e.salary > s.salary
