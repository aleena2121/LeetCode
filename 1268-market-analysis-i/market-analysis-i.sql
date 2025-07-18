-- Write your PostgreSQL query statement below
select u.user_id as buyer_id, u.join_date, count(distinct o.order_id) as orders_in_2019
from users u left join
orders o on u.user_id = o.buyer_id 
and o.order_date::date >= '2019-01-01'
and o.order_date::date < '2020-01-01'
group by u.user_id, u.join_date;