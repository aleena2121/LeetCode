-- Write your PostgreSQL query statement below
select sd.student_id, sd.student_name, sub.subject_name, 
count(e.subject_name) as attended_exams from students sd 
cross join subjects sub
left join examinations e on sd.student_id = e.student_id and sub.subject_name = e.subject_name
group by sd.student_id, sd.student_name, sub.subject_name
order by sd.student_id, sub.subject_name;