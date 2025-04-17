Select p.product_id, p.product_name
from Product as p
where p.product_id in (Select product_id
from Sales
group by product_id
having max(sale_date) between '2019-01-01' and '2019-03-31' and min(sale_date) between '2019-01-01' and '2019-03-31')