MCB185 Python Cookbook
======================

This cookbook is a collection of statements, functions, and programs that
illustrate how to perform biology-flavored programming tasks in Python. The
source code is written to be easy to understand rather than efficient or
bullet-proof. MCB185 students are only allowed to use a subset of the Python
language, so there may be better solutions than shown here.

MCB185 students are not allowed to use language features more advanced than the
current unit. Just because there's a solution in the cookbook, doesn't mean
you're automatically allowed to use it for your homework.

## Table of Contents ##

+ Simple solutions
	+ [Swapping 2 variables](#swapping-2-variables)
	+ [Editing a sequence](#editing-a-sequence)
+ Files
	+ [Reading a file of numbers](#reading-a-file-of-numbers)
	+ [Reading CSV and TSV](#reading-csv-and-tsv)
	+ [Reading a FASTA file](#reading-a-fasta-file)
	+ [Reading a multi-FASTA file](#reading-a-multi-fasta-file)
+ Sequences
	+ [Generating Random Sequences](#generating-random-sequences)
	+ [Windowing Algorithms](#windowing-algorithms)
	+ [Calculating Hydropathy](#calculating-hydropathy)
	+ [Translating DNA](#translating-dna)
	+ [Counting K-mers](#counting-kmers)
	+ [Generating K-mers](#generating-kmers)
+ CLI
	+ [Simple CLI](#simple-cli)
	+ [Nested CLI](#nested-cli)


## Swapping 2 variables ##

The classic way to swap 2 variables is to use a temporary variable. But in
Python, you can use tuples. The variables can even be different types.

```
a = 1
b = 'two'
a, b = b, a
print(a, b)
```


## Editing a Sequence ##

Strings are immutable in Python. You can't make a _mutation_ in a sequence if
it's stored as a string. However, you can edit a list. To convert a string to a
list, use the `list()` function.

```
seq = list(string)
seq[5] = 'G'        # substitution
seq.pop(3)          # deletion
del seq[3]          # also deletion
seq.insert(1, 'A')  # insertion
```


## Reading a file of numbers ##

To read a file of numbers into a list, convert each number to a `float` and
then append it to a list.

```
values = [] # empty list
with open(filename) as fp:
	for line in fp:
		values.append(float(line))
```

To make this a function, return the list.

```
def read_numbers(filename):
	values = [] # empty list
	with open(filename) as fp:
		for line in fp:
			values.append(float(line))
	return values
```

To make this a generator, yield the list, one number at a time

```
def read_numbers(filename):
	with open(filename) as fp:
		for line in fp:
			f = float(line)
			yield f

for f in read_numbers(filename): ...
```


## Reading CSV and TSV ##

To read a CSV (comma-separated values) file, split each line at the comma
character into its columns.

```
with open(filename) as fp:
	for line in fp:
		cols = line.split(',')
```

To read tab-separated files (TSV) change the comma to a tab.

```
with open(filename) as fp:
	for line in fp:
		cols = line.split('\t')
```

To read space-separated files, use the default `split()`.

```
with open(filename) as fp:
	for line in fp:
		cols = line.split()
```

If some of the columns have numeric values, you must change them to `int` or
`float` appropriately. If you know exactly how many columns there are, you can
split the line into named variables rather than a list of unknown length. The
function below hands back a list of tuples.

```
def read_people(filename):
	people = []
	with open(filename) as fp:
		for line in fp:
			name, age, salary = line.split()
			age = int(age)
			salary = float(salary)
			people.append( (name, age, salary) )
	return people
```

An alternative is to write this as a generator where each call to the function
retrieves the next person. The advantage of the generator is that you don't
need to keep all of the people in memory at the same time.

```
def read_people(filename):
	with open(filename) as fp:
		for line in fp:
			name, age, salary = line.split()
			age = int(age)
			salary = float(salary)
			yield name, age, salary

for name, age, salary in read_people(filename): ...
```

## Reading a FASTA file ##

To read a FASTA file into a string, remove the newlines and concatenate the
lines together.

```
seq = '' # empty string
with open(filename) as fp:
	header = fp.readline() # read one line
	for line in fp:        # iterate through the remaining lines
		seq += line.rstrip()
```

## Reading a multi-FASTA file ##

Reading a multi-FASTA file is a little complicated. Use the code below, which
has some useful features.

+ It can read from compressed files or stdin
+ It uses `join` to prevent the CPU overhead of concatenation
+ It uses `yield` to reduce memory footprint to a single sequence

```
import gzip
import sys
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

To iterate over all of the sequences in a file, unpack the tuple in a for loop.

```
for name, seq in read_fasta(filename): ...
```

## Generating Random Sequences ##

To generate a sequence of DNA with equal probabilities of each letter, use
`random.choice()`.

```
import random
s = ''
for i in range(100):
	s += random.choice('ACGT')
```

An alternative is to use `random.choices()` to generate a tuple of random
letters of length k (which you may want to `join()` into a string as shown).

```
s = ''.join(random.choices('ACGT', k=100))
```

If you want sequences biased towards AT or GC, split the probability space. The
code below creates sequences that are 70%

```
s = ''
for i in range(100):
	if random.random() < 0.7:
		if random.random() < 0.5: s += 'A'
		else:                     s += 'T'
	else:
		if random.random() < 0.5: s += 'C'
		else:                     s += 'G'
```

An alternative to the above is to use `random.choices()` with `weights` or
`cum_weights` and a value for `k` that is the length of the sequence.

```
nts = 'ACGT'
ntp = (0.35, 0.15, 0.15, 0.35)
ntc = (0.35, 0.50, 0.65, 1.00)
s1 = ''.join(random.choices(nts, weights=ntp, k=100))
s2 = ''.join(random.choices(nts, cum_weights=ntc, k=100))
```

To shuffle the letters of a sequence, use `random.shuffle()`. Since strings are
immutable, you must first turn the sequence into a list.

```
seq = '0123456789'
lseq = list(seq)
random.shuffle(lseq)
seq = ''.join(lseq)
```

## Windowing Algorithms ##

A windowing algorithm moves a window of fixed size along a sequence, doing
_something_ with each window.

```
seq = ... # from somewhere
w = 10 # window size
for i in range(len(seq) - w + 1):
	win = seq[i:i+w]
	do_something(win)
```

Most windowing algorithms move the window in steps of 1 (as is done implicitly
above). However, sometimes you may want to skip by 3s for codons, in which case
you must use the 3 argument form of `range()`, which specifies the starting
index, the length, and the increment (e.g. 3).

```
for i in range(0, len(seq), 3):
	codon = seq[i:i+3]
```

To get codons in a different frame, you would start with a different initial
value (e.g. 1 instead of 0).

```
for i in range(1, len(seq), 3):
	codon = seq[i:i+3]
```

To print out a FASTA file with typical 60-character line lengths, you would
skip by 60.

```
for i in range(0, len(seq), 60):
	print(seq[i:i+60])
```

Windowing algorithms can be sped up immensely by cacheing previous
calculations. For example, if you move the window over by 1 nt, the GC
composition doesn't change very much. The code for this is homework.


## Translating DNA ##

First, see [Windowing Algorithms](#windowing-algorithms).

Translate each codon using the dictionary below. Note that if a codon contains
an ambiguity code (e.g. `N`), it will not be in the dictionary, and you will
have to translate that codon as `X`. If your sequence contains lowercase
letters, you will need to change them.

```
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
seq = uc(seq) # if you have lowercase sequences
for i in range(1, len(seq), 3):
	codon = seq[i:i+3]
	if codon in gcode: aa = gcode[codon]
	else:              aa = 'X'
```

## Calculating Hydropathy ##

First, see [Windowing Algorithms](#windowing-algorithms).

Use the dictionary below or write a stack of `if-elif-else` statements. Also
see the notes about unusual characters or lowercase in Translating DNA.

```
kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}
```

## Counting K-mers ##

First, see [Windowing Algorithms](#windowing-algorithms).

The first time you 'see' a k-mer, you must add it to the dictionary.
Afterwards, increase counts by one. If you want to pre-populate the dictionary
to include missing k-mers, see [Generating K-mers](#generating-kmers).

```
seq = 'ACATGAGGATATATAT'
k = 3
kcount = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1
```

## Generating K-mers ##

`itertools.product()` makes it simple to generate all possible k-mers. The
function generates tuples, so you might want to join them into a string as
shown below.

```
import itertools
k = 3
kcount = {}
for kmers in itertools.product('ACGT', repeat=k):
	kcount[''.join(kmers)] = 0
print(kcount)
```

## Simple CLI  ##

Every program should have a usage statement that provides users with a brief
synopsis of what a program does and what parameters it takes. For example, here
is a simple CLI for the program `dust.py` that masks low complexity regions of
a sequence.

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

When you run the program without any arguments, it reports the following brief
message.

```
usage: dust.py [-h] [--lower] file k h
dust.py: error: the following arguments are required: file, k, h
```

To get more information about what the program does, run the program again with
`-h` or `--help`.

```
usage: dust.py [-h] [--lower] file k h

DNA entropy filter.

positional arguments:
  file        name of fasta file
  k           window size
  h           entropy threshold

optional arguments:
  -h, --help  show this help message and exit
  --lower     mask with lowercase
```

## Nested CLI ##

Some programs, like `git` feature sub-commands right after the name of the
program. You do this daily as `git status` and `git add`. Your programs can
have the same behavior. The program below features 2 behaviors, `greet` or
`praise`. If you choose `greet`, the program hands off execution to `fn1()` but
if you choose `praise` execution goes to `fn2()`.

A CLI created this way has a generic usage statement for the whole program and
individual usage statements for each sub-command.

```
import argparse
import sys

def fn1(arg):
	print(f'{arg.greeting}, {arg.name}.')

def fn2(arg):
	print(f'{arg.name}, {arg.message}.')

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(required=True, help='sub-commands')

## greet sub-command ##
sub_fn1 = sub.add_parser('greet', help='greet a person')
sub_fn1.add_argument('name', help='name of person to greet')
sub_fn1.add_argument('--greeting', default='Hello',
	help='default %(default)s')
sub_fn1.set_defaults(func=fn1)

## praise sub-command ##
sub_fn2 = sub.add_parser('praise', help='praise a person')
sub_fn2.add_argument('name', help='name of person to praise')
sub_fn2.add_argument('--message', default='you rock',
	help='default %(default)s')
sub_fn2.set_defaults(func=fn2)

## execute sub-command ##
try: arg = parser.parse_args()
except: sys.exit(' malformed command line, use --help for more info')
arg.func(arg)
```
