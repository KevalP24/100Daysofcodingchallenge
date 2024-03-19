# Write your MySQL query statement below
select if (
    (select count(*) from Employee)=1,null,
    (select distinct salary from(
        select salary ,dense_rank() over (order by salary desc) as ranking from employee) as n 
        where ranking=2)) as SecondHighestSalary;
