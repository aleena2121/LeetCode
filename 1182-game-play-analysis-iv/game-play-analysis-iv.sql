-- Write your PostgreSQL query statement below
with first_Login as (
    select player_id, min(event_date) as event_date from Activity
    group by player_id
),
consecutive_login as (
    select a.player_id, min(a.event_date) from Activity a
    join first_login f on a.player_id = f.player_id 
    and a.event_date = f.event_date + INTERVAL '1 Day'
    group by a.player_id
)
select round(count(*)::numeric / (select count(distinct player_id) from Activity), 2) as fraction
from consecutive_login;