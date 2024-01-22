Unit 2: Calculations
====================

## Contents ##

+ [Hello, again](#hello-again)
+ [Comments and Whitespace](#comments-and-whitespace)
    + [Comments](#comments)
    + [Whitespace](#whitespace)
+ [Math](#math)
    + [Numbers](#numbers)
    + [Math Operators](#math-operators)
    + [Math Functions](#math-functions)
    + [Numbers Aren't Real](#numbers-arent-real)
+ [Variables](#variables)
    + [Assignment](#assignment)
    + [Type](#type)
+ [Functions](#functions)
    + [Block Structure](#block-structure)
    + [Example](#example)
    + [assert() and sys.exit()](#assert-and-sysexit)
    + [Practice](#practice)
+ [Strings](#strings)
+ [Conditionals](#conditionals)
    + [if](#if)
    + [Boolean](#boolean)
    + [Chaining](#chaining)
    + [Floating Point Warning](#floating-point-warning)
    + [Sting Comparison](#string-comparison)
    + [Mismatched Type Error](#mismatched-type-error)
    + [More Practice](#more-practice)
+ [Style](#style)
	+ [Spacing](#spacing)
	+ [Naming](#naming)
+ [Homework](#homework)
    + [20demo.py](#20demopy)
    + [21quadratic.py](#21quadraticpy)
    + [22oligotemp.py](#22oligotemppy)
    + [23hydropathy.py](#23hydropathypy)
    + [24accuracy.py](#24accuracypy)
    + [25entropy.py](#25entropypy)

------------------------------------------------------------------------------

## Hello, again ##

Create a new file called `20demo.py` and save it in your `mcb185_homework`
repo. `touch` the file into existence and then open it in your text editor
(e.g. FeatherPad, Notepad++, BBedit, etc.).

```
cd ~/Code/mcb185_homework
touch 20demo.py
```

We used the `print()` function in Unit 0 to output "hello world". Edit
`20demo.py` so that it prints out "hello, again". Save your work, then go to
your terminal and run the program.

```
python3 20demo.py
```

If you don't see the output "hello, again", stop now and get help.

------------------------------------------------------------------------------

## Comments and Whitespace ##

### Comments ###

The line you wrote with the `print()` function is called a _statement_.
Programs are made up of many statements, but not everything in a program is a
statement. Another important type of line is a "comment". Any line that begins
with `#` (pound, hash) symbol is a comment. Comments may also be used at the
end of a line, at which point, the rest of the line is a comment.

Modify your program with comments as shown below. It's a good idea to put a
comment in your programs with your name.

```
# 20demo.py by your_name
print('hello, again') # greeting
```

Python also has multi-line comments. These begin and end with triple quotes.
Note that we generally use single quotes, like in `hello, again`, but for
multi-line comments we use double quotes.

```
"""
This is a
multi-line
comment
"""
```

### Whitespace ###

Another important type of line is a blank line. Use blank lines to separate
different "thoughts" much as you would use paragraphs to separate different
thoughts.

The comment with your program name and author name is like a header. It's very
different from the code that follows, and should have vertical spacing between
the code that follows. We call this vertical spacing "whitespace".

```
# 20demo.py by your_name

print('hello, again') # greeting
```

Whitespace is also used to separate different tokens (words, symbols) in
statements to provide clarity. This is much like using spaces as part of
punctuation. Note how the lack of horizontal whitespace below impedes
readability.

```
#20demo.py by your_name
print('hello,again')#greeting,formatted badly
```

Clarity is much more important than saving keystrokes. Use vertical and
horizontal whitespace to improve clarity.

------------------------------------------------------------------------------

## Math ##

### Numbers ###

The values 1, 1.0, and '1' are all different in Python. 1 is an integer. 1.0 is
a floating point number, which means that it has a decimal, and '1' is text
with the numeral "1". You can do math with 1 and 1.0, but not '1'. Python
understands scientific notation. 1.5e-2 means 1.5 times 10 to the -2 power
(0.015).

```
print(1.5e-2)
```

### Math Operators ##

Python has the typical mathematical operators you're familiar with and uses
parentheses to force precedence. There are also some operators that you may not
have seen before. The `//` operator performs an integer division. That is, it
throws away the remainder. The `%` operator is called "modulo". It provides the
remainder after performing an integer division. Modulo will be very useful to
us later, as it is used to assign reading frame to DNA.

Try adding some `print()` statements to your demo program and observe the
output.

| Operator | Purpose           | Example             | Output
|:---------|:------------------|:--------------------|:------
| `+`      | addition          | `print(1 + 1)`      | 2
| `-`      | subtraction       | `print(1 - 1)`      | 0
| `*`      | multiplication    | `print(2 * 2)`      | 4
| `/`      | division          | `print(1 / 2)`      | 0.5
| `**`     | exponentiation    | `print(2 ** 3)`     | 8
| `//`     | integer divide    | `print(5 // 2)`     | 2
| `%`      | remainder         | `print(5 % 2)`      | 1
| `()`     | precedence        | `print(5 * (2 + 1))`| 15

### Math Functions ###

Some typical mathematical transformations are not provided with operators. You
might expect `|-1|` to produce the absolute value of -1, but it does not.
Absolute value is a function called `abs()`. There is also `pow()` and
`round()`.

| Function              | Purpose
|:----------------------|:---------------------------
| `abs(x)`              | absolute value of `x`
| `pow(x, y)`           | `x` to the power of `y`
| `round(x, ndigits=3)` | round off `x` to 3 digits

What about logarithms and such? Those are in the math library. In order to use
those functions you must `import math` in your code. Import statements usually
go at the top of your program. Try out some of the functions below.

| Function            | Purpose
|:--------------------|:-----------------------------
| `math.ceil(x)`      | round `x` up
| `math.floor(x)`     | round `x` down
| `math.log(x)`       | `x` in log base e
| `math.log2(x)`      | `x` in log base 2
| `math.log10(x)`     | `x` in log base 10
| `math.sqrt(x)`      | square root of `x`
| `math.pow(x, y)`    | `x` to the power of `y`
| `math.factorial(n)` | factorial of integer n

The math library also defines some useful constants.

+ `math.e`:  2.71828...
+ `math.pi`: 3.14159...
+ `math.inf`: infinity
+ `math.nan`: not a number (e.g. 0/0)

Here's what my demo program looks like. Notice that there are multiple ways to
do powers and roots.

```
# 20demo.py by Ian Korf

import math

print('hello, again')
print(1.5e-2)
print(1 + 1)
print(2 ** 3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2 ** 0.5)
print(math.sqrt(2))
print(math.log(2))
```

### Numbers Aren't Real ###

Numbers inside your computer aren't exactly what you think they are. While
integers (ints) have exact values, floating point numbers (floats) are
approximations with finite precision. For example, the value 0.1 isn't exactly
equal to 0.1.

```
print(0.1 * 1)
print(0.1 * 3)
```

Why is `0.1 * 3` equal to 0.30000000000000004? Because the number 0.1 can't be
represented exactly by the IEEE754 standard for storing 8-byte floats. Python
sometimes hides the imprecision from you and shows you 0.1 instead of its
actual value: 0.100000001490116119384765625.

------------------------------------------------------------------------------

## Variables ##

### Assignment ###

We don't usually do math inside `print()` statements. We usually store numbers
inside variables and do math with the variables. The `=` sign is used to assign
numbers (and other types of things).

The code below computes the hypotenuse `c` given sides `a` and `b`.

```
a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)
```

Note the use of comments to explain the intent of the variables. This is
generally not necessary if you use more descriptive variable names. Take note
of how neat the code looks with all of the comments aligned vertically. Also
note the use of `a**2` rather than `a ** 2`. There are some cases where not
using spaces is neater than using spaces.

### Type ###

When variables are created, they always have a type. In the code above, `a` and
`b` are both ints because their numerical values don't have decimals. The
`math.sqrt()` function creates floats. Consequently, `c` is a float. To see the
type of a variable, use the `type()` function.

```
print(type(a), type(b), type(c))
```

This is the first place we have used the `print()` function with multiple
arguments. When given multiple things to display, the function puts spaces
between the values. You can change the separator from a space to anything else.
For example, let's change the separator to a comma followed by a space using
the optional `sep=` syntax (this is very similar to Linux commands with
optional parameters).

```
print(type(a), type(b), type(c), sep=', ')
```

------------------------------------------------------------------------------

## Functions ##

Functions are reusable code constructs that form the backbone of computer
programs. Functions are created with the `def` keyword, followed by the unique
name of the function, followed by parentheses and a colon. The next line, and
all lines that are part of the function, must be indented.

Here's a function that simply prints a greeting.

```
def greeting():
    print('hello yourself')
```

In general, functions like these are useless. Functions should do some _work_
or solve a problem. Also, it's generally a bad idea to put `print()` statements
in functions.

### Block Structure ###

Functions, and other structures we will use later in the class, use "block
structure". Blocks show hierarchy. The `print()` statement _belongs_ to the
`greeting()` function. It is indented to show its membership. Block structure
is very much like a hierarchical outline.

In this class, we ALWAYS use tabs to indent. If you indent with spaces, your
code will be flagged for potential cheating and you will get zero credit.
Unfortunately, some text editors automatically convert tabs to spaces.

Notepad++ users, make sure you uncheck the "Replace by space" in: Settings ->
Preferences -> Language -> Tab Settings -> python

Check right now if your editor has inserted spaces instead of a tab. If you
have spaces, change your editor preferences. If you can't figure out how to do
that, ask for help.

### Example ###

Suppose we want to turn the Pythagorean formula above into something we could
re-use again and again. We would like to write `x = pythagoras(3, 4)`. That is,
values `3`, and `4` are passed into the function, the function does the work,
and hands back the value `5`, which is stored in variable `x`. Here's how that
looks in code.

```
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
```

We can run it like this:

```
x = pythagoras(3, 4)
print(x)
```

We don't really need the variables `c` or `x`.

```
def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

print(pythagoras(3, 4))
print(pythagoras(1, 1))
```

### assert() and sys.exit() ###

What happens if you send the wrong value to a function? For example, the
pythagorean formula only works for positive numbers. Triangles can't have
negative or zero length sides.

To ensure that your functions only receive correct values, use `assert()`. If
the assertion isn't true, the program ends with an error.

```
def pythagoras(a, b):
    assert(a > 0)
    assert(b > 0)
    return math.sqrt(a**2 + b**2)

print(pythagoras(-1, 1))
```

An alternative is to call `sys.exit()` and provide your own error message.

```
def pythagoras(a, b):
    if a <= 0: sys.exit('error: a must be greater than 0')
    if b <= 0: sys.exit('error: b must be greater than 0')
    return math.sqrt(a**2 + b**2)
```

### Practice ###

Write a function that turns negative numbers into positive numbers and vice
versa. Give your function a name that is simultaneously simple and descriptive.

Write functions that compute the areas, circumferences, or volumes of simple
shapes like squares, rectangles, circles, spheres, etc.

Write functions that convert temperature (whichever scales you prefer).

Write functions that convert speeds (mph, kph, fps, mps, etc).

Write a function that computes DNA concentration from OD260.

Write a function that computes the distance between two points in a graph.

Write a function that computes the midpoint between two points. Note that this
function must return values for x and y. Your `return` statement will have two
values separated by a comma. Your function will look something like this.

```
def midpoint(x1, y1, x2, y2):
	# insert stuff here
	return mx, my
```

Call your function like this: `x, y = midpoint(x1, y1, x2, y2)`.

------------------------------------------------------------------------------

## Strings ##

So far, all of the variables we have seen have been numbers of some kind. But
you can also store letters in variables. A collection of zero or more letters
inside quotes is known as a string. In your first program, 'hello world' was a
string. Note that both 'hello world' and "hello world" are exactly the same
thing. In Python, we use single quotes because it's one less keypress compared
to double quotes. The exception to that is multi-line comments, which are
triple-double-quotes (see above).

```
s = 'hello world'
print(s, type(s))
```

Since this is a class that features bioinformatics programming, we will be
working with biological sequences as strings quite a bit. But not so much in
this unit.

------------------------------------------------------------------------------

## Conditionals ##

### if ###

A "conditional statement" makes choices about what to do next. The simplest
form of a conditional is the `if` construction. In the code below, the
`print()` statement only runs if `a` has the same value as `b`. Note that
equality uses a double equals sign `==`. That's because a single equals sign is
used for assignment. Try changing `b` so that they are unequal and observe the
behavior.

```
a = 2
b = 2
if a == b:
    print('a equals b')
```

Did you notice that the `print()` statement was indented? That's because it has
block structure. In the following block, the values of `a` and `b` are only
reported if they are equal.

```
if a == b:
    print('a equals b')
    print(a, b)
```

If you want the program to report the values always, put the second statement
outside the conditional (either before or after).

```
if a == b:
    print('a equals b')
print(a, b)
```

The numeric comparison operators are shown below.

| Operator | Purpose           | Example
|:---------|:------------------|:----------------------
| `==`     | equality          | `if a == b:`
| `!=`     | inequality        | `if a != b:`
| `<`      | less than         | `if a < b:`
| `>`      | greater than      | `if a > b:`
| `<=`     | less or equal     | `if a <= b:`
| `>=`     | greater or equal  | `if a >= b:`


### Boolean ###

This may seem weird, but the expression `a == b` has a value and type. We can
explore this by assigning it to a variable.

```
c = a == b
print(c)
print(type(c))
```

Expressions like `a == b` are Boolean expressions of type "bool" that can have
a value of either `True` or `False`. Try changing the values of `a` and `b` and
observe the value of `c`.

### if-elif-else ###

Much of the time we write conditional statements, there are multiple branches.
In these cases, we use the `if-elif-else` construct. There is only one `if` and
only one `else`, but there can be any number of `elif`.

```
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')
```

When you have a stack of really simple if-elif-else conditions, it's tidy to
format as one-liners and align them horizontally. You can't do this if each
block has multiple statements.

```
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
```

### Chaining ###

Boolean expressions can be chained with `and` and `or` and inverted with `not`.

```
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)
```

### Floating Point Warning ###

If you recall that floating point numbers have finite precision you may not be
surprised that the following code reports that a < b.

```
a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
```

NEVER expect equality with floating point numbers. Instead, examine their
difference and if that's less than some acceptable precision, consider them to
be the same. Here's how you do that manually.

```
print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')
```

Python has a math function `math.isclose()` that compares two values and
returns `True` if their values are close and `False` otherwise.

```
if math.isclose(a, b): print('close enough')
```

### String Comparison ###

Strings are compared alphabetically, sort of. They are actually compared by
their ASCII values. This is why "A" is less than "B" but "B" is less than "a".

```
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')
```

### Mismatched Type Error ###

If two variables have different types, it usually doesn't make sense to compare
them. That's why the following code results in a "Type Error".

```
a = 1
s = 'G'
if a < s: print('a < s')
```

### More Practice ###

Write a function that determines if a number is an integer. A good name for
such a function would be `is_integer()` or `isinteger()`. Functions with
Boolean return values often have `is` in their prefix.

Write a function that determines if a number is odd.

Write a function that determines if a number is a valid probability.

Write a function that returns the molecular weight of a DNA letter.

Write a function that returns the complement of a DNA letter.

------------------------------------------------------------------------------

## Style ##

Your code is graded on two criteria:

1. Correctness - does the code solve the problem
2. Style - does the code have good "style"

Correctness is easier to grade than style, but style is at least as important.
Incorrect code can usually be fixed quickly. Code with poor style is confusing
and difficult to maintain/extend. Here's a typical scenario in a biology lab. A
postdoc writes some code and then leaves. The PI asks the graduate student to
continue working on the project. However, the code has poor style and the
graduate student can't work with it. Instead, she reinvents the whole project
from the beginning. Unfortunately, when she leaves, the next student has the
same problem.

### Spacing ###

(1) Use a maximum line length of 79 characters (most of the time).

(2) Use 1 space around/after most operators, just like in English. But don't be
robotic about it, as sometimes it's clearer not to use spaces.

+ Yes: "Hello, my name is Ian. What's your name?"
+ No: "Hello,my name is Ian.What's your name?"
+ No: "Hello, my name is  Ian .  What's your name?"
+ Yes: `print(a, b, c)`
+ No: `print(a,b,c)`
+ Yes: `if a > b: a = 1`
+ No: `if a>b:a=1`
+ Yes: `print('hello', end='')` there is no space around keyword `=`
+ Yes: `c = (a**2 + b**2) ** 0.5` the interior looks better without spaces

(3) Use vertical spacing (blank lines) to separate logic, just as you would use
paragraph structure in English.

(4) Use tabs for left side indentation. The use of spaces for indentation flags
your code as potential **cheating**.

(5) Use spaces for lining up simple `if-elif-else` type constructs.

```
if   nt == 'A': comp = 'T'
elif nt == 'C': comp = 'G'
elif nt == 'G': comp = 'C'
elif nt == 'T': comp = 'A'
else:           sys.exit('unknown nucleotide', nt)
```

(6) There is no space between a function and its opening parentheses. Note that
`return` is a keyword, not a function.

+ Yes: `print('hello')`
+ No: `print ('hello')`
+ Yes: `return a, b`
+ No: `return(a, b)`
+ No: `return (a, b)`

### Naming ###

+ Variable and function names are generally all lowercase
+ Multi-word variables may use snake case, but not mixedCase

```
widowsize   = 60  # yes
window_size = 60  # yes
windowSize  = 60  # no
```

Variables sometimes have very short names that implicitly describe their type.
It's okay for loop variables to have such short names, but for longer-lived
variables, you should use more descriptive names.

+ `i`, `j`, `k`, and `n` are integers
+ `f`, `x`, and `y`, are floating point numbers
+ `p` and `q` are probabilities
+ `a`, `b`, and `c` are often numbers: ax^2 + bx + c or a^2 + b^2 = c^2
+ `c` by itself is a character
+ `s` is a string
+ `fp` is a file pointer

For biological sequences it's common to use these shorthands:

+ `nt` and `aa` are single characters of nucleotides or amino acids
+ `seq` is often used for a biological sequence
+ `dna`, `rna`, `tx` are nucleotide strings
+ `pro` and `pep` are protein/peptide strings

------------------------------------------------------------------------------

## Homework ##

Check the following programs into your homework repo. They are described in
more detail below.

+ `20demo.py`
+ `21quadratic.py`
+ `22oligotemp.py`
+ `23hydropathy.py`
+ `24accuracy.py`
+ `25entropy.py`

### 20.demo.py ###

It doesn't matter what state your demo program is in. Just check it into your
repo.

### 21quadratic.py ###

Write a function that solves the quadratic formula (ax^2 + bx + c), returning
the two X-intercepts. Demonstrate that it works by using the formula multiple
times within the program.

### 22oligotemp.py ###

Write a program that computes oligo melting temperature given the number of As,
Cs, Gs, and Ts in the oligo. Use these two methods.

1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)

Demonstrate that your program works by computing the Tm of several oligos of
different sizes.

### 23hydropathy.py ##

Write a function that returns the Kyte-Doolittle hydrophobicity value for an
amino acid letter. Demonstrate that the function works by calling it multiple
times with different letters.

### 24accuracy.py ###

Given values for true positives, false positives, true negatives, and false
negatives, write a function that reports the accuracy and F1 score. Demonstrate
your function works by using it several times in the program.

### 25entropy.py ##

Write a function that calculates Shannon entropy for nucleotide counts a, c, g,
t. Demonstrate it works using multiple calls.
