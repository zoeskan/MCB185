Python Reference
================

This Python Reference contains a subset of the Python language used
specifically for MCB185. MCB185 students are not allowed to use any Python
construct that isn't in this reference. See the end of this document for some
common constructs that are not allowed.

Table of Contents
-----------------

+ [MCB185 Style Guide](#mcb185-style-guide)


## MCB185 Style Guide ##

Spacing Rules:

(1) Use a maximum line length of 79 characters (most of the time).

(2) Use 1 space around/after most operators, just like in English. But don't be
robotic about it, as sometimes it's clearer not to use spaces.

+ Yes: "Hello, my name is Ian. What's your name?"
+ No: "Hello,my name is Ian.What's your name?"
+ No: "Hello, my name is  Ian .  What's your name?"
+ Yes: `if a > b: a, b = b, a`
+ No: `if a>b:a,b=b,a`
+ Yes: `print('hello', end='')` there is no space around keyword `=`
+ Yes: `c = (a**2 + b**2) ** 0.5` the interior looks better without spaces

(3) Use vertical spacing (blank lines) to separate logic, just as you would use
paragraph structure in English.

(4) Use tabs for left side indentation, but spaces to pad elsewhere.

Naming Rules:

+ Variable and function names are generally all lowercase
+ Multi-word variables may use snake case, but not mixedCase

```
speedlimit  = 65  # yes
speed_limit = 65  # yes
speedLimit  = 65  # no
```

Variables sometimes have very short names that implicitly describe their type.
It's okay for loop variables to have such short names, but for longer-lived
variables, you should use more descriptive names.

+ `n` is an integer, as are `i`, `j`, and `k`
+ `f` is a float, as are `x`, `y`, `x1`, `x2`, `y1`, and `y2`
+ `p` and `q` are probabilities
+ `a`, `b`, and `c` are often numbers: ax^2 + bx + c or a^2 + b^2 = c^2
+ `c` by itself is a character
+ `s` is a string, as are `s1`, `s2`
+ `fp` is a file pointer (variable)

For biological sequences it's common to use these shorthands:

+ `nt` and `aa` are single characters of nucleotides or amino acids
+ `seq` is often used for a biological sequence
+ `dna`, `rna`, `tx` are nucleotide strings
+ `pro` and `pep` are protein strings

Lists are often plural version of descriptive names. If the word is very long,
use an abbreviation.

+ `probs` is a list of probabilities
+ `params` is a list of parameters
+ `seqs` is a list of sequences


Writing Output
--------------

In MCB185, we write to stdout only. We don't create named files. We use
f-strings only, and not the printf-style or str.format() constructions found in
older Python.

| Code                        | Output
|:----------------------------|:-----------------------------------------
| `print('hello')`            | "hello" followed by a newline to stdout
| `print(a, b)`               | values a and b, separated by a space
| `print(a, b, sep=',')`      | values a and b, separated by a comma
| `print(a, end='')`          | value of a, no newline at end
| `print(f'{a + b})`          | value of a + b interpolated in f-string
| `print(f'{a/b:.3f}')`       | value of a / b with 3 digits after .
| `print(f'{a/b:.3g}')`       | value of a / b in scientific notation
| `print(a, file=sys.stderr)` | print `a` to stderr rather than stdout


Variables
---------

Variables are given a type as they are created.

```
n = 1               # integer
f = 1.0             # floating point number
s = '1'             # string
v = None            # None
b = True            # Boolean
t = (1, 2)          # tuple
a = [1, 2]          # list (array)
fp = open(filename) # file pointer
```

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
| `_io.textIOWrapper` | file handle

The `int()`, `float()`, and `str()` functions are useful to convert values from
one type to another.


Numbers and Math
----------------

Math operators work as you expect, except `=` is used for assignment not
equality. Unfamiliar operators include `//` for integer division and `%`
(modulo) for the remainder after integer division. Absolute value is provided
as the function `abs()`.

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

Comparison operators are unsurprising except that `==` is used for equality
(because `=` is used for assignment).

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

Functions from the `math` library include:

| Function            | Purpose
|:--------------------|:---------------------------------------------
| `math.ceil(x)`      | round `x` up
| `math.floor(x)`     | round `x` down
| `math.log2(x)`      | `x` in log base 2
| `math.log10(x)`     | `x` in log base 10
| `math.sqrt(x)`      | square root of `x`
| `math.pow(x, y)`    | `x` to the power of `y`
| `math.factorial(n)` | factorial of integer n
| `math.isclose(a, b)`| returns True if `a` is nearly identical to `b`


Strings
-------

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
+ 'B' is less than 'a' (all capital letters are less than lowercase)
+ '1' is less than '10' (as 'a' is less than 'ace')
+ '2' is greater than '1000' (as 'b' is greater than 'ant')

A few useful character and string operations use function syntax:

| Function  | Purpose
|:----------|:---------------------------------------------
| `len(s)`  | get the length of a string
| `chr(n)`  | get the character whose ASCII value is `n`
| `ord(c)`  | get the ASCII value of the character `c`

Most string operations use method syntax `s.method()`.

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


Lists and Tuples
----------------

Tuples are created with parentheses. Lists are created with square brackets.
Tuples cannot be changed, but lists can. Both lists and tuples are indexed with
square brackets.

```
tup = (1, 2, 'cat', 'dog')
lis = [1, 2, 'cat', 'dog']
print(tup[2]) # cat
print(lis[3]) # dog
```

Some useful list/tuple operations use function syntax:

| Function            | Purpose
|:--------------------|:--------------------------------------------------
| `len(list)`         | get the length of a list
| `min(list)`         | return the minimum value from an iterable
| `max(list)`         | return the maximum value from an iterable
| `sum(list)`         | return the sum of an iterable
| `sorted(list)`      | return a copy of the sorted list (or tuple)
| `enumerate(list)`   | creates tuples of index and item
| `zip(list1, list2)` | simultaneously iterate through multiple lists

Most list operations use method syntax `list.method()`.

| Method              | Purpose
|:--------------------|:------------------------------------------------
| `list.append(a)`    | add `a` to the end of a list
| `list.pop()`        | remove and return the last item
| `list.count(a)`     | count the number of times `a` occurs in list
| `list.sort()`       | sort the list in place
| `list.reverse()`    | reverse the list in place


Slices
------

Slice syntax is a succinct way to access individual elements or segments of a
string, list, or tuple.

| Example      | Value    | Explanation
|:-------------|:---------|:----------------------------------------------
| `s = abcdef` |          | example string
| `s[0]`       | 'a'      | first element
| `s[1]`       | 'b'      | second element
| `s[0:1]`     | 'a'      | slice from first, ending *before* second
| `s[0:2]`     | 'ab'     | slice from first, ending *before* third
| `s[:2]`      | 'ab'     | from implicit begin, ending before element 2
| `s[3:]`      | 'def'    | from position 3 to implicit end
| `s[:]`       | 'abcdef' | from implicit begin to implicit end
| `s[::-1]`    | 'fedcba' | from begin to end, backwards
| `s[::2]`     | 'ace'    | from begin to end by twos


Loops
-----

| Statement                    | Meaning
|:-----------------------------|:--------------------------------------------
| `for i in range(3):`         | iterate 0, 1, 2
| `for i in range(0, 3):`      | iterate 0, 1, 2
| `for i in range(1, 3):`      | iterate 1, 2
| `for i in range(0, 7, 3):`   | iterate 0, 3, 6
| `for i in range(3, -1, -1):` | iterate 3, 2, 1, 0
| `for nt in dna:`             | for each nucleotide letter in a dna sequence
| `for n in numbers:`          | for each number in a list of numbers
| `for s in sys.argv[1:]`      | for each parameter on the command line
| `while True:`                | infinite loop
| `break`                      | exit the loop now
| `continue`                   | restart the loop now
| `for i, v in enumerate(t):`  | provide index and value for every item in `t`
| `for a, b in zip(t1, t2):`   | step through containers `t1` and `t2`

For `enumerate()`, `zip()` and related iterators, always unpack the tuple into
named variables.

```
pets = ('cat', 'dot', 'rat')
for i, pet in enumerate((pets): # yes, unpack the tuple
	print(i, pet)
for thing in enumerate(pets):   # no, don't index it numerically
	print(thing[0], thing[1]) 
```

Functions
---------

A function is created with the `def` keyword. Functions usually have
_positional_ arguments, meaning the arguments are in a specific order.
Functions may return multiple values. Here is a function with 3 positional
arguments that returns a tuple of 2 values.

```
def quadratic(a, b, c):
	x1 = -b - sqrt(b**2 - 4*a*c) / 2*a
	x2 = -b + sqrt(b**2 - 4*a*c) / 2*a
	return x1, x2
```

Functions can have named parameters, which are placed after positional
arguments and may occur in any order. For example, a `translate()` function
might translate coding sequence in frame 0 by default, but can also translate
in other reading frames using an optional `frame` parameter.

```
def translate(seq, frame=0):
	cds = ''
	for i in range(frame, len(seq) -2, 3):
		cds += seq[i:i+3]
	return cds
translate('ATGACG')    # implicitly use frame 0
translate('ATGACG', 1) # use frame 1
```

Functions may call themselves. This is called _recursion_.
**Recursion is not allowed in MCB185.**


Random
------

The random library is used to create random(-ish) numbers. If you want to
reproduce the same random numbers over and over (useful for debugging), set the
random see to any integer value.

| Statement                | Meaning
|:-------------------------|:----------------------------------------
| `random.random()`        | a random variable from 0 almost 1
| `random.seed(i)`         | set the random seed
| `random.randint(a, b)`   | a random integer from a to b, inclusive
| `random.choice('ACGT')`  | a random letter: A, C, G, or T
| `random.shuffle('ACGT')` | randomize positions, works on lists too


Reading Files
-------------

Files are opened and closed as follows:

```
fp = open(filename)
fp.close()
```

Files are automatically closed when using a `with open` construction. Here's
the preferred code to open a file, read it line-by-line, and automataically
close it:

```
with open(filename) as fp:
	for line in fp:
		# do something with each line
```

To open a compressed file, use `gzip.open()` and include an additional argument
`rt` to read as text, as shown below.

```
with gzip.open(filename, 'rt') as fp:
```


Regular Expressions
-------------------

This section not finished...

```
import re
re.match(pattern, string)
```


Commandline Interface
---------------------

Values on the command line are in the `sys.argv` list. While you _can_ read
values directly from here, it's not recommended.

```
filename = sys.argv[1]
k = int(sys.argv[2])
h = float(sys.argv[3])
```

The better way to retrieve values from the command line is with `argparse`.
This allows you to control input type, provide optional arguments, and display
a standard usage statement.

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


MCB185 Illegal
--------------

The following common and useful features of Python are not introduced in
MCB185, and are considered illegal for homework purposes.

+ Recursion - functions that call themselves
+ Dictionaries - maps, hashes, associative arrays
+ Sets - valueless dictionaries
+ The `match` and `case` conditional statement
+ Comprehensions (list, generator, dictionary, set)
+ Exceptions: `try` and `raise`
+ Classes - object-oriented programming
+ Decorators - function wrappers
+ Function annotations - function hints
+ Writing files - we use stdout and redirection instead
+ Dunders - for example, `if __name__ == '__main__':`

Only 6 libraries are allowed in MCB185:

+ argparse
+ gzip
+ math
+ random
+ re
+ sys

To be clear, no other libraries are allowed, including the following common,
and very useful libraries:

+ array
+ csv
+ fileinput
+ io
+ itertools
+ keras
+ matplotlib
+ numpy
+ pandas
+ os
+ seaborn
+ scipy
+ sklearn
+ statistics
+ torch
