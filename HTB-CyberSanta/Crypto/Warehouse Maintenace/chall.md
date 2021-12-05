# Task

## Create signature

At the start, we have a session bound salt $s$ with byte length between 8 and 100

```
salt = os.urandom(randint(8,100))
```

Then, the raw bytes of $d$

```
USE xmas_warehouse;
#Make sure to delete Santa from users. Now Elves are in charge.
```

are concatenated, which are 83 in total. Therefore, we receive the value $h = H(s + d)$. In total, $H$ consumed between $91$ and $183$ bytes. $H$ operates on $64$ bytes, so we have either two or three calls to the underlying SHA512 function which will also add padding. Later, it will be checked if $h$ and our payload $p$ collides.

# Steps

## Use database

Therefore, we just receive one sample and send it such that we use the right data base

We want to have this payload later on:

```sql
SELECT table_name FROM information_schema.tables;
```

## Bruteforcing the salt

${256}^8$ possibilities per query if we are lucky and urandom is $8 \implies$ Bad idea.

## Length extension attack

For a $d'$, the algorithm computes $h' = H(s + d + d')$. We know $h = H(s + d)$.

We want to have the following query

```sql
USE xmas_warehouse;
#Make sure to delete Santa from users. Now Elves are in charge.
SELECT table_name FROM information_schema.tables;
```

See <https://www.rfc-editor.org/rfc/rfc4634#page-6>

First, we use $h$ as the internal state of our SHA-512 implementation. It is padded 
with $10000 \cdots 0000 || len(d+s)$. Therefore, $m = s||d||10000 \cdots 0000 || len(d+s)$

Because we want to append, we have know the byte length of $s+d$, such that we can 
compute the padding. The padding will be put into the comment of the SQL query.

After trying different values for $d'$, we end up with $m' = s||d||d'$ where $d'$ must start with $10000 \cdots 0000 || len(d+s)||$ which goes into the padding. Now, $H(s||d) = H'(s||d||d')$ where $H'$ is unpadded. For $d'$ we can put the sql-query in we want. After we have the query, we send $d'$ and $H'(s||d||d')$.


Sadly, not enough time to solve the task.