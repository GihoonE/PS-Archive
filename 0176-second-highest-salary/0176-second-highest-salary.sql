# Write your MySQL query statement below
Select Coalesce(max(salary),NULL) as SecondHighestSalary
from Employee
where salary not in (
Select max(salary)
from Employee
)