-- Write your PostgreSQL query statement below
select * from users
where email ~* '^[A-Za-z\d_]+@[A-Za-z]+.com'