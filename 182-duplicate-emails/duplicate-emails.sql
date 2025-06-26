-- Write your PostgreSQL query statement below
select email from 
(
    select email, count(email) as count
    from Person
    group by email
) where count > 1;