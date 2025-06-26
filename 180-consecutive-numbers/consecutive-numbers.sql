-- Write your PostgreSQL query statement below
    select distinct num as ConsecutiveNums from
    (
        select num,
        LAG(num, 1) OVER (ORDER BY id) as prev1,
        LAG(num, 2) OVER (ORDER BY id) as prev2
        from logs
    ) as temp
    where num = prev1 and num = prev2