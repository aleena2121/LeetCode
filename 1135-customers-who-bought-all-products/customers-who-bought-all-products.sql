-- Write your PostgreSQL query statement below
select customer_id from
(
    select customer_id, count(distinct product_key) as count
    from customer
    group by customer_id
)
where count = (select count(*) from product);