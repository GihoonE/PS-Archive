# Write your MySQL query statement below
Select max(M.num) as num
from MyNumbers as M
where 1 = (Select count(N.num)
            from MyNumbers as N
            where M.num = N.num
            group by N.num)