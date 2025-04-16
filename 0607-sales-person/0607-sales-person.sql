# Write your MySQL query statement below
Select SA.name
from SalesPerson as SA
except(
                    Select S.name
                    from SalesPerson as S, Orders as O, Company as C
                    where S.sales_id = O.sales_id and O.com_id = C.com_id and C.name = "RED")