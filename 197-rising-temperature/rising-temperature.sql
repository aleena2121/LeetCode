-- Write your PostgreSQL query statement below
select w1.id
from weather w1
join weather w2
ON w1.recordDate = w2.recordDate + INTERVAL '1 day'
where w1.temperature > w2.temperature;