Python Reference
================

## Print ##

The `print()` function is very flexible. There are many options not shown here.

| Code                   | Output
|:-----------------------|:------------------------------------
| `print('hello')`       | "hello" followed by a newline
| `print(a, b)`          | values a and b, separated by a space
| `print(a, b, sep=',')` | values a and b, separated by a comma
| `print(a, end='')`     | value of a, no newline at end
| `print(f'{a + b})`     | value of a + b
| `print(f'{a/b:.3f}')`  | value of a / b with 3 digits after .
| `print(f'{a/b:.3g}')`  | value of a / b in scientific notation

## Variables ##

The `type()` function returns the type of a variable.

| Type                | Meaning
|:--------------------|:----------------
| `int`               | integers
| `float`             | decimal numbers
| `str`               | string (text)
| `None`              | a non-value useful for debugging
| `bool`              | Boolean (True or False)
| `tuple`             | a collection of immutable values
| `list`              | a collection of mutable values
| `dict`              | a collection of key/value pairs
| `_io.textIOWrapper` | file handle

The `int()`, `float()`, and `str()` functions are useful to convert values from
one type to another.






## Math Operators ##

| Operator | Function          | Example
|:---------|:------------------|:---------
| `=`      | assignment        | a = 2
| `+`      | addition          | a = a + 1
| `-`      | subtraction       | a = 3 - 2
| `*`      | multiplication    | a = b * c
| `/`      | division          |
| `**`     | exponentiation    | c = (a**2 + b**2)**0.5
| `//`     | integer divide    |
| `%`      | remainder         |
| `()`     | precedence        |
| `+=`     | increment         |
| `-=`     | decrement         |
| `*=`     | multiply & assign |
| `/=`     | divide & assign   |


## Math Functions ##

|
| `min()`
| `max()`
| `sum()`
| `math.sqrt()`
| `math.`

| Function
|:------
| `int()`
| `float()`
| `str()`

## String Operators ##

## String Functions/Methods ##

| Functions

Examples

| Code                  |
|:----------------------|:---------------------------------------
| `a = 2`               | assigns the value of 2 to variable `a`
| `a = a + 1`           | increases `a` by 1
| `a += 1`              | increases `a` by 1


## Comparison Operators and Conditional Statements ##

| `==`
| `!=`
| `>=`
| `<=`

## Loops ##

+ Variables
	+ Assignment
	+ Comparison
	+ Conversion
+ Functions
+ Conditionals
+ Loops
+ Lists
+ File I/O

+ variables
+ math
+ random
+ functions

+ conditionals
+ loops
+ strings
+ files
+ tuples, lists

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

The better way to retrieve values from the command line is `argparse`.

```
import argparse
example code here
```




| `len()`
| `range()`



## Reading Files ##

To read in a file of numbers into a list, you must convert each number to a
`float` and then append it to a list.

```
values = [] # empty list
with open(filename) as fp:
	for line in fp:
		values.append(float(line))
```

To read a FASTA file into a string, remove the newlines and concatenate the
lines together.

```
seq = '' # empty string
with open(filename) as fp:
	header = fp.readline()
	for line in fp:
		seq += line.rstrip()
```

To read a multi-FASTA file, you can read all of the sequences into a list and
then return the list. However, this can be wasteful of CPU and memory for long
sequences. The function below has several interesting features.

+ It can read from compressed files or stdin
+ It uses `join` to reduce reallocations
+ It uses `yield` to reduce memory footprint

```
import gzip
def read_fasta(filename):
	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)
	name = None
	seqs = []
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()
```
