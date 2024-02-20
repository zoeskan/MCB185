Unit 5: Containers
==================

## Contents ##

+ [Indexes](#indexes)
+ [Slices](#slices)
+ [Tuples](#tuples)
+ [enumerate() and zip()](#enumerate-and-zip)
    + [enumerate()](#enumerate)
    + [zip()](#zip)
+ [Lists](#lists)
    + [list()](#list)
    + [split() and join()](#split-and-join)
+ [Searching](#searching)
+ [Practice Problems](#practice-problems)
+ [Practice Solutions](#practice-solutions)
    + [minimum()](#minimum)
    + [minmax()](#minmax)
    + [mean()](#mean)
    + [entropy()](#entropy)
    + [dkl()](#dkl)
+ [Files](#files)
    + [Compressed Files](#compressed-files)
    + [Converting Types](#converting-types)
    + [51cdslength.py](#51cdslengthpy)
+ [sys.argv](#sysargv)
	+ [52entropy.py](#52entropypy)
+ [Homework](#homework)
    + [53genomestats.py](#53genomestatspy)
    + [54genomestats.md](#54genomestatsmd)
    + [55colorname.py](#55colornamepy)
    + [56birthday.py](#56birthdaypy)
    + [57birthday.py](#57birthdaypy)

------------------------------------------------------------------------------

## Indexes  ##

As usual, create a demo file for the unit: `50demo.py`.

A string is a container that holds letters. Each character of a string has an
index, which is its position. `seq[0]` is the first letter of the sequence
(most computer languages start counting at 0 rather than 1). `seq[1]` is the
second character.

```python
seq = 'GAATTC'
print(seq[0], seq[1])
```

Indexes can be negative, in which case they count backwards from the right,
starting at -1. So `seq[-1]` is the last character of string.

```python
print(seq[-1])
```

Previously, we iterated through the characters in a string using a `for` loop.

```python
for nt in seq: print(nt, end='')
print()
```

We can also iterate through the letters by their indices using the `range()`
function to generate the indices and `len()` to set the limit.

```python
for i in range(len(seq)):
    print(i, seq[i])
```

------------------------------------------------------------------------------

## Slices ##

A _slice_ is a subset of a container. The slice operator is a pair of square
brackets. Slices work a little like the `range()` function in they take an
initial position and an end-before limit. Unlike the `range()` function, the
separator is a colon and not a comma. The following code prints the first 5
letters of the string. The `0` represents the initial position, while the `5`
is the end-before limit.

```python
s = 'ABCDEFGHIJ'
print(s[0:5])
```

Like the `range()` function, slices can also have a step size. When omitted,
the step size is assumed to be 1.

```python
print(s[0:8:2])
```

As a shortcut, you may omit either the initial value, which is replaced by 0,
or the final value, which is the length of the string.

```python
print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ
```

It may seem a little strange but `s[0]` is the same thing as `s[0:1]`. `s[0]`
indexes a single element. `s[0:1]` is a slice that starts at the zero-th
element and ends before the first.

`s` is also equivalent to `s[0:len(s)]` and `s[::]`, which explicitly or
implicitly set the bounds of the slice to the whole string. While it is not
very surprising that `s[::1]` is also the same thing, your should definitely
take a long look at `s[::-1]`.

```python
print(s, s[::], s[::1], s[::-1])
```

------------------------------------------------------------------------------

## Tuples ##

A tuple is container that holds multiple values. Tuples are generally
constructed with comma-separated values (usually in parentheses).

```python
tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax)                       # note the parentheses in the output
```

Tuples and strings are immutable. That means you cannot change their contents
by poking at their indices. These two lines generate errors.

```python
s[0] = 'C'
tax[0] = 'human'
```

Tuples are linear containers of values, just like strings, and can be indexed
and sliced using the exact same syntax.

```python
print(tax[0])      # index
print(tax[::-1])   # slice
```

You may not have realized it, but you already wrote a function that returned a
tuple. `quadratic()` returns two values separated by a comma. That was a tuple.

```python
def quadratic(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return x1, x2
```

When you call a function that returns a tuple, you can either _unpack_ the
tuple into separate named variables or capture the entire tuple as a single
value and access its contents by the interior indices. ALWAYS UNPACK THE TUPLE.

```python
x1, x2 = quadratic(5, 6, 1)          # unpacked tuple - yes
print(x1, x2)                        # pretty
intercepts = quadratic(5, 6, 1)      # packed tuple - no
print(intercepts[0], intercepts[1])  # ugly

```

------------------------------------------------------------------------------

## enumerate() and zip() ##

### enumerate() ###

When stepping through containers, it's often useful to have both indices and
values. One way to do this is with the `range()` function.

```python
nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
```

A tidier alternative is to have `enumerate()` provide you a tuple containing
the index and value in separate named variables.

```python
for i, nt in enumerate(nts):
    print(i, nt)
```

### zip() ###

When stepping through two containers in parallel, you can use `range()` to
simultaneously index separate containers.

```python
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
```

The tidier solution uses `zip()` to retrieve an element from each container and
return them to you in a tuple.

```python
for nt, name in zip(nts, names):
    print(nt, name)
```

You can even enumerate the zip as shown below. Here, you have to unpack the
tuples in series using additional parentheses.

```python
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)
```

------------------------------------------------------------------------------

## Lists ##

Lists are similar to tuples except they are constructed with square brackets
and their contents are mutable.

```python
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
```

Elements can be added to the end of a list with `list.append()`.

```python
nts.append('C')
print(nts)
```

**NOTE**: This is the first time we have seen "method syntax". All of the
functions we have used so far put a variable inside parentheses like `len(s)`.
The `len()` function can be used with strings, tuples, and lists. However, the
`list.append()` function _only_ works with lists. Functions that only work with
specific data types, and are closely bound to those data types are called
"methods".

Remove elements from the end of a list with `list.pop()`.

```python
last = nts.pop()
print(last)
```

Lists are sorted with `list.sort()`. Note that all of the elements in the list
must have similar types. You can sort a mixture of ints and floats, but you
cannot mix them with strings.

```python
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
```

If you make a new variable to an existing list, it is not a copy, but another
name for the same list. In the example below, `nucleotides` is modified and the
modifications also occur in `nts` because both variable names correspond to the
same underlying data.

```python
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
```

To make a copy, use `list.copy()`. This is a "shallow" copy, meaning that
multi-dimensional lists and other complex data structures are not fully copied.
We don't make deep copies in this class.

### list() ###

The `list()` function without arguments creates empty lists.

```python
items = list()
print(items)
items.append('eggs')
print(items)
```

You can also create empty lists with empty square brackets.

```python
stuff = []
stuff.append(3)
print(stuff)
```

The `list()` function coerces other "iterables" into lists. For example, it can
convert a string into a list of letters.

```python
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
```

### split() and join() ###

The `list.split()` method splits strings into lists of strings. This is useful
for segmenting words. By default, the delimiter is any number of spaces.

```python
text = 'good day   to you'
words = text.split()
print(words)
```

For TSV or CSV data, split on `\t` or comma (as shown below).

```python
line = '1.41,2.72,3.14'
print(line.split(','))
```

Lists can be turned into strings by joining them with a delimiter. The
delimiter can be nothing. Here, the list is an argument to a method owned by
the delimiter string (which can be empty).

```python
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
```

## Searching ##

To search for items in containers, you can use `in`, `find()`, and `index()`.

The keyword `in` reads particularly well in conditional statements.

```python
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
```

The `index()` method returns the index of the first element it finds. If it
can't find a matching item, the function throws an error.

```python
print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))
```


The `find()` method returns the index of the first element it finds or a -1 if
it can't be found. This very useful behavior only works for strings, and not
tuples or lists.

```python
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
```

If you are searching a list or tuple, and you don't know if the element is
in the list, first use `in`.

```python
if thing in list: idx = list.index(thing)
```

------------------------------------------------------------------------------


## Practice Problems ##

Write a function that returns the minimum value of a list.

Write a function that returns both the minimum and maximum values of a list.

Write a function that returns the mean of the values in a list.

Write a function that computes the entropy of a probability distribution.

Write a function that computes the Kullback-Leibler distance between two sets
of probability distributions.

## Practice Solutions ##

### minimum() ###

The initialization on line 1 sets the minimum to the first value. If the list
is only 1 item long, this is the minimum. For longer lists, the minimum is
compared to every other value after the first `vals[1:]`. Whenever a value is
less than the current minimum (line 4) the minimum is reset `mini = val`. There
is no finalization step here.

```python
1   def minimum(vals):
2       mini = vals[0]
3       for val in vals[1:]:
4           if val < mini: mini = val
5       return mini
```

Note that python has built-in functions `min()`, `max()` and `sum()`. Sorry,
but you're not allowed to use them in this class.

### minmax() ###

This function is very similar to `minimum()` except that it has 2
initializations (lines 2-3) and 2 return values (line 7). The conditionals on
lines 5-6 could be formed as an `elif`.

```python
1   def minmax(vals):
2       mini = vals[0]
3       maxi = vals[0]
4       for val in vals:
5           if val < mini: mini = val
6           if val > maxi: maxi = val
7       return mini, maxi
```

An alternative way to write this function is to sort the values and then return
the first and last element. The sort method is more computationally expensive
and has a side-effect of re-ordering the list, which the caller might not want.

### mean() ###

Unlike the previous two functions, this one has a finalization step on line 4.
It is possible to write this without finalizing, with `total += val/len(vals)`,
but that increases the number of division calculations.

```python
1   def mean(vals):
2       total = 0
3       for val in vals: total += val
4       return total / len(vals)
```

### entropy() ###

This function should checks that the probability distribution in `probs` sums
up to something close to 1.0. It will also run into numerical errors if any of
the values are 0. Can you write it better?

```python
1   def entropy(probs):
2       h = 0
3       for p in probs:
4           h -= p * math.log2(p)
5       return h
6   print(entropy([0.2, 0.3, 0.5]))
```

### dkl() ###

In this function, capital `P` and `Q` stand for probability distributions while
`p` and `q` represent individual values. This example follows more of a math
convention for naming variable (single letters) than software engineering
(descriptive names). Given the K-L is so commonly described by P and Q, this
seems fitting.

Note the use of `zip()` on line 3 that simultaneously retrieves probabilities
from `P` and `Q`. It is assumed that `P` and `Q` are containers with the same
length (and also that they sum up to 1 and don't have zeros or negative
numbers). Again, maybe you can improve the function?

Lines 6 and 7 create containers to hold the probability distributions. `p1` is
defined as a list while `p2` is defined as a tuple. That's okay because both
can be zipped in parallel.

```python
1   def dkl(P, Q):
2       d = 0
3       for p, q in zip(P, Q):
4           d += p * math.log2(p/q)
5       return d
6   p1 = [0.4, 0.3, 0.2, 0.1]
7   p2 = (0.1, 0.3, 0.4, 0.2)
8   print(dkl(p1, p2))
```

------------------------------------------------------------------------------

## Files ##

Text files can contain lots of data, but they are not containers in the same
way that strings, tuples, and lists are. Files cannot be sliced. Files must be
"opened" to get access to them. Later, they must be "closed". Here's the
canonical structure for reading a file line-by-line.

```python
with open(path) as fp:
    for line in fp:
        do_something_with(line)
```

The `open()` function creates a new type of variable which is commonly called a
"file pointer" which is why the variable is abbreviated `fp`. If you use the
`type()` function you will see it has a much longer name: `_io.TextIOWrapper`.
The `open()` function takes a "path" argument, which is a relative or absolute
path to a file.

The `for` loop iterates through the file until there are no more lines to read.

The `do_something_with(line)` is a stand-in for whatever is going to happen
next.

Note that there is no close operation. Files are automatically closed when
program execution goes beyond the `with` block. Here's the alternative, not
recommended way to write the equivalent code.

```python
fp = open(path)
for line in fp:
    do_something_with(line)
fp.close()
```

### Compressed Files ###

Reading compressed files is really simple. We only need to make 2 changes to
the typical structure.

1. `import gzip`
2. change `open(path)` to `gzip.open(path, 'rt')`

This code snippet reads a compressed file and reports its contents to stdout.
This is effectively the same thing as `gunzip -c path`.

```python
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')
```

### Converting Types ###

Text files contain strings. Even though numbers like 1, 3.14, or 1e-5 all look
like numbers. they are actually strings. If you want to do math with
string-like numbers, you must first convert them from strings to numbers. The
`int()` and `float()` functions do that.

```python
i = int('42')
x = float('0.61803')
```

### 51cdslength.py ###

Create a program called `51cdslength.py` that reports the lengths of
protein-coding genes in the E. coli genome. The program will need to perform
the following tasks inside the line-reading loop.

1. Skip over comment lines
2. Find CDS features (or skip over all non-CDS features)
3. Extract the begin and end coordinates
4. Convert the coordinates to integers
5. Report the length of the CDS (end - begin + 1)

Type the following lines and observe how the code works. Delete it all and
re-write it from a blank page.

```python
1   import gzip
2
3   path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
4   with gzip.open(path, 'rt') as fp:
5       for line in fp:
6           if line[0] == '#': continue
7           words = line.split()
8           if words[2] != 'CDS': continue
9           beg = int(words[3])
10          end = int(words[4])
11          print(end - beg + 1)
```

Line 3 has a hard-coded path to a data file. This is a terrible practice. NEVER
HARD-CODE PATHS. This program will run from your `mcb185_homework` directory
assuming that both `mcb185_homework` and `MCB185` are both in the same
directory (which they should be). However, if you move the script or the data
file, it will fail.

Line 6 checks if the first character is a comment symbol. The `continue`
statement restarts the loop at the next line.

Line 7 splits the line into words using the default separator, which is any
number of spaces. The tab characters in GFF files count as spaces.

Line 8 checks to see if the feature is of type 'CDS'. Again, the `continue`
skips to the next line because we are only interested in CDS features.

Lines 9-10 turn the strings representing numbers like "190" into actual
integers with values of 190.

Line 11 computes and reports the length. This calculation cannot be done
without converting strings to ints or floats.

In this unit, we are working with containers. Instead of printing out all of
the distances, put them in a container. Note the changes to lines 2 and 11.

```python
1   import gzip
2   lengths = []
3   path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
4   with gzip.open(path, 'rt') as fp:
5       for line in fp:
6           if line[0] == '#': continue
7           words = line.split()
8           if words[2] != 'CDS': continue
9           beg = int(words[3])
10          end = int(words[4])
11          lengths.append(end - beg + 1)
```

Here's an alternative way to write the conditional statements above that does
not use `continue` statements. Instead of skipping the lines we aren't
interested in, we create code blocks for the lines we _are_ interested in. Note
the extra levels of nesting. Novice programmers sometimes prefer the
construction below. De-nesting is much neater when there are multiple
conditions.

```python
1   import gzip
2   lengths = []
3   path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
4   with gzip.open(path, 'rt') as fp:
5       for line in fp:
6           if line[0] != '#':
7               words = line.split()
8               if words[2] == 'CDS':
9                   beg = int(words[3])
10                  end = int(words[4])
11                  lengths.append(end - beg + 1)
```

## sys.argv ##

Another way to get data into your program is from the command line itself. The
variable `sys.argv` is the complete list of words on the command line (argv is
short for argument vector). `sys.argv[0]` is the name of your program.

### 52entropy.py ###

Create a new program called `52entropy.py`. This calculates the entropy for a
list of probabilities on the command line.

```python
1   import sys
2   import math
3
4   probs = []
5   for arg in sys.argv[1:]:
6       f = float(arg)
7       if f <= 0 or f >= 1: sys.exit('error: not a probability')
8       probs.append(float(arg))
9
10  total = 0
11  for p in probs: total += p
12  if not math.isclose(total, 1.0):
13      sys.exit('error: probs must sum to 1.0')
14
15  h = 0
16  for p in probs:
17      h -= p * math.log2(p)
18
19  print(h)
```

Lines 1-2 import the necessary libraries.

Lines 4-8 harvest words on the command line and turn them into probabilities.

Line 4 sets up a container to hold the probabilities used for the calculation.

Line 5 steps through each argument (word) on the command line, using a slice
`sys.argv[1:]` to skip over the first argument (`sys.argv[0]`), which is the
name of the program.

Line 6 converts the argument into a floating point number.

Line 7 checks to see if the number is a valid probability. The numbers 0 and 1
are considered illegal in this context because values of 0 cause numerical
errors (log(0) and there is no point in calculating the entropy of a single
value of 1.0).

Line 8 adds each floating point number to the container of probabilities.

Line 9 is blank to separate the thoughts of the previous and next code blocks.

Lines 10-13 check if the sum of the probabilities on the command line are equal
to 1.0. Of course, we never ask if floating point values are actually equal to
anything, so we check if they sum nearly to 1.0.

Line 14 is blank to separate the previous sanity check from the calculation of
Shannon entropy.

Lines 15-17 calculate entropy.

Line 18 is again blank to separate calculation from reporting.

Line 19 reports the final value.

Now try running it with various values, including those that create errors.

```
python3 52entropy.py 0.5 0.5
python3 52entropy.py 0.25 0.25 0.25 0.25
python3 52entropy.py 0.4 0.3 0.2 0.1
python3 52entropy.py 0.5 0.6
python3 52entropy.py 0.5 -1
```

Now that you understand how the program works, can you delete it and re-write
it again?

------------------------------------------------------------------------------

## Homework ##

+ `50demo.py`
+ `51cdslength.py`
+ `52entropy.py`
+ `53genomestats.py`
+ `54genomestats.md`
+ `55colorname.py`
+ `56birthday.py`
+ `57birthday.py`

### 53genomestats.py ###

Write a program that reads a GFF file and reports the following information
about the length of GFF features.

+ count
+ min
+ max
+ mean
+ standard deviation
+ median

Run your program on the GFF files for the A.thaliana, C.elegans, and
D.melanogaster genomes. You will find the files in the MCB185 data directory.

Use `sys.argv` to specify the path to the GFF and the type of feature. This
will allow you to write the program once and change command line parameters for
different files or feature types.

Your program should start something like this:

```python
import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]
```

Your command lines should look something like this:

```
python3 53genomestats.py ~/Code/MCB185/data/A.thaliana.gff.gz gene
```

### 54genomestats.md ###

Create a report in markdown format as `54genomestats.md`. In addition to
filling out the table below, include any other information you think another
genome scientist would find interesting. (BTW, the actual value for median in
the table below is 1892.5, but I rounded it off because I only wanted integers
in the table).

```
| Genome         | Type |  N   | Min |  Max  | Mean | Stdv | Med  |
|:---------------|:-----|:-----|:----|:------|:-----|:-----|:-----|
| A.thaliana     | gene |  362 |  72 |  9511 | 2070 | 1435 | 1892 |
|                | exon |
|                | CDS  |
| C.elegans      | gene |
|                | exon |
|                | CDS  |
| D.melanogaster | gene |
|                | exon |
|                | CDS  |
```

### 55colorname.py ###

Write a program that provides the closest official color name given some red,
green, and blue values. Each value must be in the range of 0-255. You will find
color definitions in the `colors_basic.tsv` and `colors_extended.tsv` in
`MCB185/data`.

The first few lines of your program should look something like this.

```python
import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
```

Your command lines should look something like this:

```
python3 55colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50
```

The output for the command above will be "crimson".

Hint: this algorithm is not very different from `minimum()` except that the
number you are trying to minimize is the difference between the input RGB
values and those of a named color. You will have to keep track of both the
minimum distance and the name of its corresponding color.

Hint: To calculate the distance between an input color and a named color, you
can use taxi-cab distance. This is very similar to `dkl()` except that the loop
sums up the absolute difference of each pair of values. It therefore doesn't
assume probabilities or have problems with zero values.

```python
def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d
```

### 56birthday.py ###

You may have heard of the 'birthday paradox' before. Write a program that
simulates the problem by filling up classrooms of students with randomly chosen
birthdays. Make the number of days in the calendar and the number of people in
the classroom command line arguments. You will have to run this thousands of
times to get an accurate estimate, so have a parameter for that too.

https://en.wikipedia.org/wiki/Birthday_problem

In this program, you must use a list for the birthdays. For example, if there
are 23 people in the classroom, you will `list.append()` up to 23 times.

The first few lines of your program should look something like this:

```python
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
```

Your command line should look something like this.

```
python3 56birthday.py 10000 365 23
```

And the output should be a little over 50%.

### 57birthday.py ###

This is the same problem as above, but instead of making a list of birthdays
(e.g. 23) make a list from the calendar (e.g. 365). In the previous program,
you appended birthdays to a list. In this one, all possible days are already in
a list, so assigning a birthday is: `calendar[birthday] += 1`.
