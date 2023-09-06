# Algorithms, programming
* Algorithms: how to systematically perform a task
* Write down as a sequence of steps ("Recipe" or program)
* Programming language describes the steps
* What is a step? Degrees of detail
- "Arrage the chairs" vs "Make 8 rows with 10 chairs in each row".
- Program is a sequence of steps
- Some steps are repeated
- Some steps are conditional

## Our Focus 
Algorithms that manipulate information
1. Compute numerical functions
2. Reorganize data - eg. arrange in ascending order
3. Optimization - find the shortest route

## GCD
- gcd(m,n)
- list out the factors of m
- list out the factors of n
- report the largest number that appears on both lists
- the [python programme](01_gcd.py) is for gcd

## Some important takeaways
- Use names to remember intermediate values (m,n,fm,fn,i,j,f)
- Values can be single items or collections
- Assign values to names

## Can we do better?
- why compare two lists and then compare them to compute the gcd?
- For each i in 1 to max(m,n), if i divides m and i also divides n, then add i to cf
- Actually any common factor must be less than min(m,n)
- For each i in 1 to min(m,n), if i divides m and i also divides n, then add i to cf
- The [short python programme](02_gcd.py) is for the enhanced gcd

## An implementation of gcd with [no lists](03_gcd.py)

## An implementation of gcd with no lists and by [scanning backwards](04_gcd.py) 