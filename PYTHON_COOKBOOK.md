Python Bioinformatics Cookbook
==============================

A collection of statements, functions, and programs that illustrate how to
perform biology-flavored programming tasks in Python. The source code is
written to be easy to understand more than efficient or bullet-proof. MCB185
also limits how much of the Python language is used. For example, there are no
dictionaries or numpy.

## Table of Contents ##

Shortcuts

+ Swapping 2 variables

Sorting

+ Sorting a list by...
+ Sorting a dictionary by value
+ Sorting a list of objects by value

Random

+ Generating a random DNA sequence
+ Generating random DNA with specific probabilities
+ Selecting random values...

Reading files

+ Reading a file of numbers into a list
+ Iterating through a CSV or TSV file
+ Reading a single sequence from a FASTA file
+ Reading multiple sequences from a FASTA file


Command line interface

+ Retrieving command line arguments with `sys.argv`
+ Defining and retrieving command line arguments with `argparse`

Translation and K-mers






To iterate through items in a container (string list, tuple), use a `for` loop.

```
dna = 'acgt'
for nt in dna:
	print(nt)
```

If you need the index, you can use `range()` or `enumerate()`.

```
for i in range(len(dna)):
	print(i, dna[i])
for i, nt in enumerate(dna):
	print(i, dna[i])
```

Top iterate through two lists at the same time, use `range()` or `zip()`.

```
pets = ('cat', 'dog', 'rat')
ranks = (1, 0, 2)
for i in range(len(pets)):
	print(pets[i], ranks[i])
for pet, rank in zip(pets, ranks):
	print(pet, rank)
```




## Swapping 2 variables ##

```
a = 'cat'
b = 'dog'
```

Now put swap the variables, so that `a` contains 'cat'. This is sometimes
confusing for new programmers, but if you ask them to do it in real life, it's
easy.

```
glass = 'milk'
mug = 'coffee'
```

"Oh, let me get another container." Sometimes the answer is obvious in the real
world but not while programming. In Python, you don't need another container.
You can swap them as tuples.

```
a, b = b, a
glass, mug = mug, glass
```

## Reading a file of numbers into a list ##

To read a file of numbers into a list, convert each number to a `float` and
then append it to a list.

```
values = [] # empty list
with open(filename) as fp:
	for line in fp:
		values.append(float(line))
```

## Reading a CSV or TSV ##


## Reading a FASTA file ##

To read a FASTA file into a string, remove the newlines and concatenate the
lines together.

```
seq = '' # empty string
with open(filename) as fp:
	header = fp.readline() # or is it better as next(fp)?
	for line in fp:
		seq += line.rstrip()
```

## Reading a multi-FASTA file ##

Reading a multi-FASTA file is a little complicated. Building and returning a
list of sequences is wasteful of CPU and RAM for long sequences. Why slurp in
an entire genome when you can iterate over chromosomes? The function below,
which has some useful features.

+ It can read from compressed files or stdin
+ It uses `join` to prevent the CPU overhead of concatenation
+ It uses `yield` to reduce memory footprint to a single sequence

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
