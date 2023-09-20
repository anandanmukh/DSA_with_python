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

## Names, Values and Types
- Values have types 
- Determine what operations are allowed 
- Names inherit type from currently assigned value 
- Can assign values of different types to a name 
- int, float, bool
- +,-,*,/,..  and,or,..  ==,!=,>,..

## Manipulating Text
- Computation is a lot more than number crunching 
- Text processing is increasingly important  
- Document preparation 
- Importing/exporting spreadsheet data 
- Matching search queries to content

## Strings —type str
- Type string, str, a sequence of characters 
- A single character is a string of length 1 
- No separate type char 
- Enclose in quotes—single, double, even triple! 
-  city = 'Chennai'  
-  title = "Hitchhiker's Guide to the Galaxy" 
-   dialogue = '''He said his favourite book is 
"Hitchhiker's Guide to the Galaxy”'''

## Strings as sequences
- String: sequence or list of characters 
- Positions 0,1,2,...,n-1 for a string of length n 
> s = "hello"
- Positions -1,-2,... count backwards from end 
> s[1] == "e", s[-2] = "l"
-  h e l l o
-  0 1 2 3 4
- -5 -4 -3 -2 -1

## Operations on strings
- Combine two strings: concatenation, operator +
> s = "hello" 
>
> t = s + ", there" 
- t is now "hello, there" 
- len(s) returns length of s 
- The strings operations are done [here](02_strings.ipynb)

## Extracting substrings
- A slice is a “segment” of a string 
- s = "hello" 
- s[1:4] is “ell" 
- s[i:j] starts at s[i] and ends at s[j-1] 
- s[:j] starts at s[0], so s[0:j] 
- s[i:] ends at s[len(s)-1], so s[i:len(s)]

## Modifying strings
- Cannot update a string “in place” 
- s = "hello", want to change to "help!" 
- s[3] = "p" — error! 
- Instead, use slices and concatenation 
- s = s[0:3] + "p!" 

## Lists
- Sequences of values 
- Type need not be uniform 
- Extract values by position, slice, like str
- Length is given by len()
- The lists operations can be found [here](03_lists.ipynb)

## Lists and strings
- For str, both a single position and a slice return 
strings 
>h = "hello"
>
> h[0] == h[0:1] == "h"
- For lists, a single position returns a value, a slice 
returns a list 
> factors = [1,2,5,10]
>
> factors[0] == 1, factors[0:1] == [1]

## Nested lists
- Lists can contain other lists 

>nested = [[2,[37]],4,["hello"]]
>
>nested[0] is [2,[37]]
>
>nested[1] is 4
>
>nested[2][0][3] is "l"
>
>nested[0][1:2] is [[37]]

## Updating lists
- Unlike strings, lists can be updated in place 
> nested = [[2,[37]],4,["hello"]]
>
> nested[1] = 7
>
> nested is now [[2,[37]],7,["hello"]]
>
> nested[0][1][0] = 19
>
> nested is now [[2,[19]],7,["hello"]]
- Lists are mutable, unlike strings

## Mutable vs immutable
- What happens when we assign names? 

> x = 5 
>
> y = x 
>
> x = 7
- Has the value of y changed? 
- No, why should it? 
- Does assignment copy the value or make both 
names point to the same value?
- Does assignment copy the value or make both 
names point to the same value? 
- For immutable values, we can assume that 
assignment makes a fresh copy of a value 
- Values of type int, float, bool, str are 
immutable 
- Updating one value does not affect the copy
- For mutable values, assignment does not make a 
fresh copy 

> list1 = [1,3,5,7] 
>
> list2 = list1 
>
> list1[2] = 4
What is list2[2] now? 
list2[2] is also 4 
list1 and list2 are two names for the same list





