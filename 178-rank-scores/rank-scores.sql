-- Write your PostgreSQL query statement below
select score, dense_rank() over (ORDER BY score DESC) as rank from Scores;