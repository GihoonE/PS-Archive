Delete
from Person as p
where p.id not in (
    Select min(temp.id)
    from (Select * from Person) as temp
    group by temp.email
)

