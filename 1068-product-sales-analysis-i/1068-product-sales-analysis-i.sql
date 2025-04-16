# Write your MySQL query statement below
Select product_name,year,price
from Sales as S, Product as P
where S.product_id = P.product_id