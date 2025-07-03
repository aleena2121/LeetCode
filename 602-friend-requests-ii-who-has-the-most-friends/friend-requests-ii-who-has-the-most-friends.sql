-- Write your PostgreSQL query statement below
with friends as(
    select requester_id as id from RequestAccepted 
    union all
    select accepter_id as id from RequestAccepted 
),
friends_count as(
    select id, count(*)
    from friends
    group by id
)
select id, count as num from friends_count
order by count desc
limit 1;