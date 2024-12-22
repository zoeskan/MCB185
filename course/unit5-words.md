Unit 5: Words
=============

## Contents ##

+ [Sets](#sets)
+ [Dictionaries](#dictionaries)
    + [Iteration](#iteration)
+ [Lookup Tables](#lookup-tables)
+ [Categorical Data](#categorical-data)
    + [51countgff.py](#51countgffpy)
    + [Composition, again](#composition-again)
    + [Sorting](#sorting)
+ [K-mers](#k-mers)
    + [52kmercount.py](#52kmercountpy)
+ [Argparse](#argparse)
	+ [53dust.py](#53dustpy)
+ [Homework](#homework)
    + [54missingkmers.py](#54missingkmerspy)
    + [55genefinder.py](#55genefinderpy)

------------------------------------------------------------------------------

Create a file `50demo.py` for the various code explorations in this unit.

## Sets ##

A set is a mutable container, but all of the elements are unique and the
elements are not ordered.

```python
s = {'A', 'C', 'G'}
print(s)
```

Try running this multiple times. Did you notice the order of the elements isn't
the same each time? Did you notice the curly brackets that indicate the variable
is a set?

To add items to a set, use the `add()` method.

```python
s.add('T')
print(s)
```

Because it is a set, adding the same element doesn't do anything.

```python
s.add('A')
print(s)
```

Since it doesn't have order, the following code generates an error:

```python
print(s[2])
```

Right about now, you're probably thinking that sets are useless. However, they
are very efficient for looking things up. Let's do a little experiment (which
you might not want to put in your `50demo.py`). The following code creates two
random collections of DNA kmers of length 10 (e.g. TACGATAACA might be one suck
kmer). It then cross-references the lists asking if the kmer from one list is
also in the other list. As the lists get longer, the set gets faster and faster
compared to the list. For large lists, a set can be thousands or even millions
of times faster than a list.

```python
import random
import time

def random_names(n, k):
	klist = list()
	kset = set()
	for _ in range(n):
		kmer = ''.join(random.choices('ACGT', k=k))
		klist.append(kmer)
		kset.add(kmer)
	return klist, kset

for size in range(1000, 10000, 1000):

	list1, set1 = random_names(size, 10)
	list2, set2 = random_names(size, 10)

	t0 = time.time()
	for name1 in list1:
		if name1 in list2: pass
	t1 = time.time()
	list_time = t1 - t0

	t0 = time.time()
	for name1 in list1:
		if name1 in set2: pass
	t1 = time.time()
	set_time = t1 - t0

	print(list_time, set_time, list_time/set_time)
```

## Dictionaries ##

A dictionary is like a list, but the indices are strings instead of numbers.

+ `list[0]` - `0` is a numeric index
+ `dict['hey']` - `'hey'` is a string index

Unlike lists, there is no `append()` for dictionaries. Each item in a
dictionary exists as a key:value pair. The key is the string in square brackets
('hey' above). The value is anything you can put in a variable.

An empty dictionary is created either with empty braces or the `dict()`
function.

```python
d = {}
d = dict()
```

To make a dictionary with predefined items, use curly braces and key:value
pairs as shown below.

```python
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
```

Both dictionaries and sets are displayed with curly brackets. The difference is
that dictionaries are key:value pairs, whereas sets are just values. Like sets,
dictionaries are also very efficient for lookups.

To access items use square brackets.

```python
print(d['cat'])
```

To add new items to a dictionary, assign a new key:value pair.

```python
d['pig'] = 'oink'
print(d)
```

To change the value of an item, access it with its key.

```python
d['cat'] = 'mew'
print(d)
```

To delete an item, use `del`.

```python
del d['cat']
print(d)
```

If you try to access a key that doesn't exist, you get an error.

```python
print(d['rat'])
```

To check if a key exists, use the keyword `in` just as you would with a list or
a set.

```python
if 'dog' in d: print(d['dog'])
```

### Iteration ###

There are several ways to iterate through a dictionary. The standard `for` loop
iterates over the keys in the order in which they were created. To get to a
specific element, use the key as an index to the dictionary.

```python
for key in d: print(f'{key} says {d[key]}')
```

The most common way to iterate through a dictionary is with `dict.items()`.

```python
for k, v in d.items(): print(k, 'says', v)
```

Again, you should always unpack your tuples. Consider how awful the following
looks.

```python
for thing in d.items(): print(thing[0], thing[1])
```

If you want just the keys or just the values, Python has methods `dict.keys()`
and `dict.values()` that return iterable objects. If you want these as actual
lists, coerce them with `list()`.

```python
print(d.keys(), d.values(), list(d.values()))
```

------------------------------------------------------------------------------

## Lookup Tables ##

Dictionaries are tidy and efficient for looking up values from a table. In the
last unit, you had to write a function that computed the average hydrophobicity
for a peptide. There were several strategies.

The most labor-intensive way is to make a stack of conditionals. Don't add this
to your demo.

```python
def kd_cond(seq):
    kd = 0
    for aa in seq:
        if   aa == 'I': kd += 4.5
        elif aa == 'V': kd += 4.2
        elif aa == 'L': kd += 3.8
        elif aa == 'F': kd += 2.8
        elif aa == 'C': kd += 2.5
        elif aa == 'M': kd += 1.9
        elif aa == 'A': kd += 1.8
        elif aa == 'G': kd += -0.4
        elif aa == 'T': kd += -0.7
        elif aa == 'S': kd += -0.8
        elif aa == 'W': kd += -0.9
        elif aa == 'Y': kd += -1.3
        elif aa == 'P': kd += -1.6
        elif aa == 'H': kd += -3.2
        elif aa == 'E': kd += -3.5
        elif aa == 'Q': kd += -3.5
        elif aa == 'D': kd += -3.5
        elif aa == 'N': kd += -3.5
        elif aa == 'K': kd += -3.9
        elif aa == 'R': kd += -4.5
    return kd/len(seq)
```

Another way is to index parallel lists. While this is a lot less code than the
example above, it is basically the same linear search. Don't add this either.

```python
aas = 'IVLFCMAGTSWYPHEQDNKR'
kds = (4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3,
    -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5, 0)

def kd_list(seq):
    kd = 0
    for aa in seq:
        idx = aas.find(aa)
        kd += kds[idx]
    return kd/len(seq)
```

The better way is to use a dictionary. The code is cleaner and runs faster
because dictionaries, like sets, are designed for fast lookups.

```python
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
```

------------------------------------------------------------------------------

## Categorical Data ##

Dictionaries aren't only for looking up previous information, but categorizing
new information.

### 51countgff.py ###

Remember way back in Unit 0 when we crafted a CLI to count all of the features
in a GFF?

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr
```

Let's do the equivalent in python. Start a new program called `51countgff.py`
and add the following lines.

```python
1   count = {}
2   with gzip.open(sys.argv[1], 'rt') as fp:
3       for line in fp:
4           if line.startswith('#'): continue
5           f = line.split()
6           feature = f[2]
7           if feature not in count: count[feature] = 0
8           count[feature] += 1
9   for f, n in count.items(): print(f, n)
```

Line 1 creates an empty dictionary that will eventually fill up with key:value
pairs where the key will be the feature type (e.g. 'gene') and the value will
be the number of times it has been seen.

Line 4 uses `line.startswith()` instead of `line[0]` to introduce this useful
function. There is also a `str.endswith()`.

Lines 5-6 retrieve the feature name from the line.

Line 7 is critical. If the feature type isn't in the dictionary, we must create
a key in the dictionary before we can start counting.

Line 8 does the counting under the assumption that the feature is already in
the table, which it must be due to Line 7.

Lines 9 reports the counts of each feature.

An alternative way of writing lines 7 and 8 is below.

```python
7           if feature not in count: count[feature] = 1
8           else:                    count[feature] += 1
```

### Composition, again ###

In the last unit we saw several strategies for counting nucleotides in
sequences.

1. Create named variables `A`, `C`, `G`, `T` and an if-elif-else stack
2. Create a single list, but still use an if-elif-else stack
3. Create parallel lists and use `str.find()` for indexing
4. Use `str.count()` on each nucleotide

Another way to count letters is with a dictionary. The strategy is identical to
the gff counting strategy.

```python
count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1
```

### Sorting ###

There are times when you want to sort a dictionary by keys or values. One way
to do this is to pipe your program output through Linux `sort`. The first line
below sorts the output by the feature name. The second line sorts the second
column `-k 2` numerically `-n`. The two options can be collapsed as `-nk2`. The
`k` must come after the `n` because it has an argument, so `-kn2` would not
work.

```
python3 51countgff.py ecoli.gff.gz | sort
python3 51countgff.py ecoli.gff.gz | sort -n -k 2
python3 51countgff.py ecoli.gff.gz | sort -nk2
```

But what if you want the sort to occur inside python? Sorting by keys is really
easy. The `sorted()` function sorts the keys of count.

```python
    for k in sorted(count): print(k, count[k])
```

Sorting by values is more complex. Consider the rest of this section as
optional content. For an in-depth explanation, see the following:
https://realpython.com/python-lambda

The `sorted()` function needs a list of things to sort. By default, this is the
keys. We want to sort items based on their values, so we have to send
`sorted()` the values of the items. Here's the code.

```python
    for k, v in sorted(count.items(), key=lambda item: item[1]):
        print(k, v)
```

Lambda functions are tiny anonymous functions. This lambda function reads the
tuple `item` and returns the second element `item[1]` as the return value. You
can use this exact same construct with `item[0]` and it will sort by keys
rather than values.

Probably the best way to understand lambda functions is to substitute a named
function that does the exact same thing. In the code below, `key=by_value`
calls the `by_value()` function on each tuple to get the _thing_ used for
sorting (in this case the value).

```python
def by_value(tuple):
    return tuple[1]

for k, v in sorted(count.items(), key=by_value):
    print(k, v)
```

------------------------------------------------------------------------------


## K-mers ##

K-mers are used in a variety of bioinformatics analyses. A k-mer is simply a
sequence of length k, where k is a small integer. The subsequences of sliding
window algorithms are k-mers. Individual nucleotides are k-mers of length 1.

### 52kmercount.py ###

To explore k-mers, let's make a new program: `52kmercount.py`. As the name
suggests, it will count kmers.

```python
1   k = int(sys.argv[2])
2   kcount = {}
3   for defline, seq in mcb185.read_fasta(sys.argv[1]):
4       for i in range(len(seq) -k +1):
5           kmer = seq[i:i+k]
6           if kmer not in kcount: kcount[kmer] = 0
7           kcount[kmer] += 1
8   for kmer, n in kcount.items(): print(kmer, n)
```

Line 1 sets up a command line parameter for the value of k.

Line 2 is the empty dictionary that will hold key:value pairs of k-mers and
their counts.

Line 3 should be very familiar by now.

Line 4 is the typical windowing algorithm.

Line 5 creates a variable whose name does an excellent job of describing its
contents.

Lines 6-7 set or increase the counts of each observed k-mer.

Line 8 is the output.

Run the program as follows:

```
python3 52kmercount.py ecoli.fa.gz 1
```

Try increasing the value for k on the command line. With each increase, you see
4 times as many k-mers. Well, until you get to 7. 4^7 is 16,384 but `wc` shows
there's only 16,383. One of the k-mers is missing.

```
python3 52kmercount.py ecoli.fa.gz 7 | wc
```

Which k-mer is missing? One way to find out is to generate all possible k-mers
and check them against the `kcount` dictionary. We'll use `itertools.product()`
to generate all possible kmers. Throw the following code in your demo if you
want to see it in action.

```python
import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)
```

Add the following to `52kmercount.py`.

```python
1   import itertools
2   for nts in itertools.product('ACGT', repeat=k):
3       kmer = ''.join(nts)
4       if kmer in kcount: print(kmer, kcount[kmer])
5       else:              print(kmer, 0)
```

Line 3 joins the tuple `nts` into a string so that we can use it to index our
dictionary. Any kmers that aren't found will be reported with 0 counts.

```
python3 52kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
```

The k-mer 'GCCTAGG' doesn't exist in the E.coli genome (on the positive
strand). It does exist if you reverse-complement the genome.


------------------------------------------------------------------------------


## Argparse ##

"Real" Unix programs have a CLI that provides a "usage statement" and command
line options. To see the usage statement for `head` and many other commands,
follow it with the `--help` parameter.

```
head --help
```

A usage statement provides a brief synopsis of how to use the command. It
should state what the command does, and what options and arguments it takes.
Python provides this functionality in the `argparse` library.

### Positional Arguments ###

Let's create a program with a simple, but proper, CLI. Start a file called
`53dust.py` and type in the following:

```python
1   import argparse
2
3   parser = argparse.ArgumentParser(description='DNA entropy filter.')
4   parser.add_argument('file', type=str, help='name of fasta file')
5   parser.add_argument('size', type=int, help='window size')
6   parser.add_argument('entropy', type=float, help='entropy threshold')
7   arg = parser.parse_args()
8   print('dusting with', arg.file, arg.size, arg.entropy)
```

Line 1 imports the library.

Line 3 creates the argument parser object in a variable called `parser`.

Line 4 adds a "positional argument" for the path to a FASTA file.

Line 5 adds a positional argument for the window size and specifies that it is
an integer.

Line 6 adds a positional argument for the entropy threshold, which is a float.

Line 7 creates the `arg` object by harvesting the values on the command line
and assigning them to various properties. For example, `arg.file` contains the
path to the FASTA file. Similarly, `arg.size` is the window size and
`arg.entropy` is the entropy threshold.

Line 8 is just something that will print when we give the program the proper
number and type of arguments.

Try running the program `python3 53dust.py` and observe the usage statement.

```
usage: 53dust.py [-h] file size entropy
53dust.py: error: the following arguments are required: file, size, entropy
```

If you don't give the program any arguments, it responds with a brief usage
statement telling you what it requires, in this case an optional argument `-h`
and 3 required positional arguments: `file`, `size`, and `entropy`. To get more
information, type `python3 53dust.py -h`. Here, the `-h` stands for help and
the usage statement provides more detail, including the final line, which tells
you that you can also get to this message with a longer version: `--help`.

```
usage: 53dust.py [-h] file size entropy

DNA entropy filter.

positional arguments:
  file        name of fasta file
  size        window size
  entropy     entropy

options:
  -h, --help  show this help message and exit
```

Try running it with the correct number and types of values.

```
python3 53dust.py e.coli.fa.gz 20 1.4
```

### Named Arguments ###

The arguments for `file`, `size`, and `entropy` were all positional. That is,
there were in a strict order. In contrast, named arguments are optional and can
occur in any order. This is very much like python where the `print()` function
has positional arguments (the things you want printed) as well as optional
named arguments like `sep=` and `end='`.

```python
print('first', 'second')                       # positional only
print('first', 'second', sep='\t', end='\n')   # named
print('first', 'second', end='\n', sep='\t')   # named, different order
```

Let's change `size` and `entropy` to be named parameters. Like the `print()`
function in python, they will have default values and can appear in any order.

In the code below, `size` is now `--size` with `default=20`. Similarly.
`entropy` is now `--entropy` and `default=1.4`. Inside the program, they are
accessed exactly as before: `arg.size` and `arg.entropy`.

To advertise the default values in the usage statement use `%(default)`. This
is appended with `s`, `i` or `f` to indicate string, int or float. `.3f` is 3
digits of precision, using the same formatting as f-strings.

```python
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
```

Try observing the new usage statement advertising the default parameters. Also
try overriding the defaults.

```
python3 53dust.py
python3 53dust.py e.coli.fa.gz
python3 53dust.py e.coli.fa.gz --size 15 --entropy 1.2
```

### Flags ###

Another typical option is a flag that turns on/off some behavior. Let's create
a flag so that the program can soft-mask sequences (use lowercase letters
instead of 'N'). Add the line with "lower" and modify the print to show the
value.

```python
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)
```

Try it.

```
python3 53dust.py e.coli.fa.gz
python3 53dust.py coli.fa.gz --lower
```

### Short and Long ###

Let's add one more convenience, which is the ability to use both short and long
argument names. So `--size` can be `-s` and `--entropy` can be `-e`. This is a
simple modification to the named arguments.

```python
parser.add_argument('-s', '--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
```

------------------------------------------------------------------------------


## Homework ##

+ `50demo.py`
+ `51countgff.py`
+ `52kmercount.py`
+ `53dust.py`
+ `54missingkmers.py`
+ `55genefinder.py`

### 53dust.py ###

Fill in the rest of the code for the program.

### 54missingkmers.py ###

Write a program that searches sequences for the smallest missing k-mer. The
program is a little different from `52kmercount.py`.

+ Start k at 1 and increase until there are missing k-mers
+ Only report the k-mers that are missing
+ Stop after finding a value of k with missing k-mers
+ Search both strands of the sequence

The output of your program should find 52 missing k-mers in the E.coli genome
at k=8.

### 55genefinder.py ###

Write a program that reports putative coding genes in the E.coli genome. This
is similar to `47cdsfinder.py`, but you must report the coordinates of each
CDS.

+ Input: FASTA file
+ Output: GFF of gene features
+ Parameters: FASTA file, minimum ORF length (e.g. 300 nt including stop)

This is a difficult problem to solve for several reasons.

+ ATGs can occur in multiple frames
+ Multiple ATGs end in the same stop codon
+ DNA has two strands
+ You must calculate coordinates on the minus strand

Hints:

+ Don't work with the entire E.coli genome, make a subset
+ Use the E.coli gene coordinates to help you debug
+ Solve each frame and strand independently
+ Work it out on paper before programming
+ Consider a `while` loop rather than `for` so you can skip ahead as needed
