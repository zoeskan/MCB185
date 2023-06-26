Python Reference
================

## Naming Convenentions ##

Variable and function names are generally all lowercase. If a variable consists
of two words, you can merge them together or put an underscore between them.
The Python community does not use mixedCase or CamelCase.

+ `myvar` yes
+ `my_var` yes
+ `myVar` no
+ `MYVAR` yes, for constant value that never changes

Variables sometimes have very short names that describe their type.

+ `n` is an integer, as are `i`, `j`, and `k`
+ `f` is a float, as are `x`, `y`, `x1`, `x2`, `y1`, and `y2`
+ `p` is a probability, as is `q`
+ `a`, `b`, and `c` are often numbers: ax^2 + bx + c or a^2 + b^2 = c^2
+ `c` by itself is a character
+ `s` is a string, as are `s1`, `s2`
+ `nt` and `aa` are single nucleotides or amino acids
+ `seq` is often used for a biological sequence along with `dna` and `pep`
+ lists are usually plural: `seqs` is a list of sequences
+ `it` is an iterable, as are `it1` and `it2`
+ `d` is a dictionary
+ `fp` is a file pointer (variable)

## Print ##

The `print()` function is very flexible. There are many options not shown here.

| Code                   | Output
|:-----------------------|:-----------------------------------------
| `print('hello')`       | "hello" followed by a newline
| `print(a, b)`          | values a and b, separated by a space
| `print(a, b, sep=',')` | values a and b, separated by a comma
| `print(a, end='')`     | value of a, no newline at end
| `print(f'{a + b})`     | value of a + b interpolated in f-string
| `print(f'{a/b:.3f}')`  | value of a / b with 3 digits after .
| `print(f'{a/b:.3g}')`  | value of a / b in scientific notation

## Variables ##

The `type()` function returns the type of a variable.

| Type                | Meaning
|:--------------------|:---------------------------------
| `int`               | integer
| `float`             | number with a decimal point
| `str`               | string (text)
| `None`              | a non-value useful for debugging
| `bool`              | Boolean (True or False)
| `tuple`             | a collection of fixed values
| `list`              | a collection of mutable values
| `dict`              | a collection of key/value pairs
| `_io.textIOWrapper` | file handle

The `int()`, `float()`, and `str()` functions are useful to convert values from
one type to another.

## Numbers ##

Math operators work as you expect. There are some you may not be familiar with,
such as modulo `%`, which is the remainder after integer division `//`.
Absolute value is provided as the function `abs()`.

| Operator | Purpose           | Example
|:---------|:------------------|:--------------------------
| `=`      | assignment        | `a = 2`
| `+`      | addition          | `a = b + c`
| `-`      | subtraction       | `a = b - c`
| `*`      | multiplication    | `a = b * c`
| `/`      | division          | `a = b / c`
| `**`     | exponentiation    | `a = b ** c`
| `//`     | integer divide    | `a = 5 // 2 # 2`
| `%`      | remainder         | `a = 5 % 2  # 1`
| `()`     | precedence        | `c = (a**2 + b**2)**0.5`
| `+=`     | increment         | `a += 1`
| `-=`     | decrement         | `a -= 1`
| `*=`     | multiply & assign | `a *= 2`
| `/=`     | divide & assign   | `a /= 2`

Comparison operators are unsurprising.

| Operator | Purpose           | Example
|:---------|:------------------|:----------------------
| `==`     | equality          | `if a == b:`
| `!=`     | inequality        | `if a != b:`
| `<`      | less than         | `if a < b:`
| `>`      | greater than      | `if a > b:`
| `<=`     | less or equal     | `if a <= b:`
| `>=`     | greater or equal  | `if a >= b:`

Constants from the `math` library include:

| Constant      | Meaning
|:--------------|:---------------------------
| `math.pi`     | 3.14159...
| `math.e`      | 2.71828...
| `math.inf`    | infinity
| `math.nan`    | not a number (e.g. log(0))

Functions from the `math` library include:

| Function            | Purpose
|:--------------------|:---------------------------------------------
| `math.ceil(x)`      | round `x` up
| `math.floor(x)`     | round `x` down
| `math.log(x)`       | `x` in log base e
| `math.log2(x)`      | `x` in log base 2
| `math.log10(x)`     | `x` in log base 10
| `math.sqrt(x)`      | square root of `x`
| `math.pow(x, y)`    | `x` to the power of `y`
| `math.comb(n, k)`   | n choose k
| `math.factorial(n)` | factorial of integer n
| `math.isclose(a, b)`| returns True if `a` is nearly identical to `b`
| `math.sin(x)`       | sine of `x` (there are many trig functions)
| `math.degrees(x)`   | convert to radians
| `math.radians(x)`   | convert to degrees

## Strings ##

Some of the familar mathematical operators are also used for text.

| Operator | Purpose           | Example
|:---------|:------------------|:------------------------
| `=`      | assignment        | `s = 'hello'`
| `+`      | concatenation     | `s = 'hello' + 'world'`
| `*`      | repetition        | `polyA = 'A' * 100`
| `\`      | special symbols   | `tab = '\t'`
| `in`     | membership        | `if 'GAATTC' in dna:`
| `[]`     | slice             | see Slices below

Comparison operators work just like their numeric counterparts except that
strings are compared by their ASCII values.

+ 'A' is less than 'B'
+ 'B' is less than 'a'
+ '1' is less than '10'
+ '2' is greater than '1000'

Some useful characater and string functions are in the global namespace.

| Function  | Purpose
|:----------|:---------------------------------------------
| `len(s)`  | get the length of a string
| `chr(n)`  | get the character whose ASCII value is `n`
| `ord(c)`  | get the ASCII value of the character `c`

Most string functions use method syntax `s.function()`.

| Method              | Purpose
|:--------------------|:------------------------------------------------
| `s.count(s1)`       | number of occurrences of `s1` in `s`
| `s.endswith(s1)`    | True if `s` ends with `s1`
| `s.startswith(s1)`  | True if `s` starts with `s1`
| `s.find(s1)`        | position of `s1` in `s` or -1 if not found
| `s.join(it)`        | join elements of `it` with s between
| `s.upper()`         | convert s to uppercase
| `s.lower()`         | convert s to lowercase
| `s.rstrip()`        | remove characters from the end, usually newline
| `s.split(s1)`       | split `s` into a list of strings at every `s1`

## Lists ##


sorted() - return a new sorted list
list.sort()

is
append
clear
count
extend
index
insert
pop
remove
reverse
sort
len

## Slices ##


## Looping ##


## Iterables ##

Iterables are objects that can return their contents one at a time.
Commonly-used iterable operations are defined for your convenience.

| Function        | Purpose
|:----------------|:--------------------------------------------------
| `next(it)`      | gets the next item in the iterable
| `min(it)`       | return the minimum value from an iterable
| `max(it)`       | return the maximum value from an iterable
| `sum(it)`       | return the sum of an iterable
| `enumerate(it)` | creates tuples of index and item
| `zip(it, it2)`  | simultaneously iterate through multiple iterables



## Functions ##

A function is created with the `def` keyword. Functions usually have
_positional_ arguments, meaning they must have a specific number of arguments,
and those arguments must be in the correct order. Functions may return multiple
values. Here is a function with 3 positional arguments that returns a tuple of
2 values.

```
def quadratic(a, b, c):
	x1 = -b - sqrt(b**2 - 4*a*c) / 2*a
	x2 = -b + sqrt(b**2 - 4*a*c) / 2*a
	return x1, x2
```

Functions can have named parameters, which are placed after positional
arguments and may occur in any order. For example, a `translate()` function
might translate coding sequence in frame 0 by default, but can also translate
in other reading frames using an optional `frame` named parameter.

```
def translate(seq, frame=0):
	cds = ''
	for i in range(frame, len(seq) -2, 3):
		cds += seq[i:i+3]
	return cds
```

## Commandline Parameters ##

Values on the command line are in the `sys.argv` list. While you _can_ read
values directly from here, it's not recommended.

```
filename = sys.argv[1]
k = int(sys.argv[2])
h = float(sys.argv[3])
```

The better way to retrieve values from the command line is with `argparse`.
This allows you to control input type, provide optional arguments, and display
a pretty usage statement.

```
import argparse
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('k', type=int, help='window size')
parser.add_argument('h', type=float, help='entropy threshold')
parser.add_argument('--lower', action='store_true', help='mask with lowercase')
arg = parser.parse_args()
do_something(arg.file, arg.k, arg.h, arg.lower)
```

## Reading Files ##

fp = open()
fp.close()
with open() as fp
