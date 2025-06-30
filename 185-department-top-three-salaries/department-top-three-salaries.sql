-- Write your PostgreSQL query statement below
select Department, Employee, Salary from
(
    select d.name as Department,
    e.name as Employee, 
    e.salary as Salary, 
    dense_rank() over (
        partition by e.departmentId 
        order by e.salary desc
        ) 
    as rank from department d
    inner join employee e 
    on e.departmentId = d.id
) where rank < 4;