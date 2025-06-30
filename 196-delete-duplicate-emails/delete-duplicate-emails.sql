-- Write your PostgreSQL query statement below
delete from Person where id in(
select p1.id
FROM Person p1
JOIN Person p2
ON p1.email = p2.email AND p1.id > p2.id
);
