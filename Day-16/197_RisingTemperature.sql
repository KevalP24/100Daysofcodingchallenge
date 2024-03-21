# Write your MySQL query statement below
select s.id from Weather s join Weather w on s.temperature>w.temperature and DATEDIFF(s.recordDate,w.recordDate) = 1
