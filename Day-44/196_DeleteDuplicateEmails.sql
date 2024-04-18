# Write your MySQL query statement below
delete p from Person p , person pp where p.Email=pp.Email and p.Id>pp.Id
