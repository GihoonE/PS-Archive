# Write your MySQL query statement below
Select project_id, round(avg(experience_years),2) as average_years
from Project as P, Employee as E
where P.employee_id = E.employee_id
group by project_id