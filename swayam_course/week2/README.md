## Assignment Statement
- Assign a value to a name
- eg i = 5
- Left hand side is a name
- Right hand side is an expression
- Operations in expression depend on type of value

## Numeric Values
- Numbers come in two flavours
- int: integers
- float: fractional numbers
- 178, -3, 2344532 are examples of integers
- 13.2, 0.4, -9.3 are examples of type float

## int vs float
- Why are these different types?
- Internally, a value is stored as a finite sequence of 0's and 1's(binary digits or bits)
- For an int, this sequence is read off as a binary number
- for a float, this sequence breaks up into a mantissa and exponent
- Like 6.022 * 10**24

## Operations on Numbers 
- Normal arithmetic operations: +, -, *, /
- / always produces a float
- Quotient is // and remainder is %
- Exponentiation is **
- the "math" library is required for log(), sqrt(), sin()...

## Names, values and types
- Values have types
- Type determines what operations are legal
- Names inherit their type from their current value Type of a name is not fixed
- Unlike languages like C, C++, Java where each name is “declared” in advance with its type

## Names, Values and Types
- Names can be assigned values of different types as the program evolves
eg. 
i=5 #i is int
i=7*1 #i is still int
j = i/3 # j is float, / creates float ...
i=2*j #i is now float
- type(e) returns type of expression e
- Not a good style to assign values of mixed types to same name!

## Boolean values: bool
- True, False
- Logical operators: not, and, or
- not True is False, not False is True
- x and y is True if both of x,y are True
- x or y is True if at least one of x,y is True

## Comparisons
- x == y, a != b, 
- z < 17*5, n > m, 
- i <= j+k, 19 >= 44*d
- Combine using logical operators
- n > 0 and m%n == 0
- Assign a boolean expression to a name
- divisor = (m%n == 0)