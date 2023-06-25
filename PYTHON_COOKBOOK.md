Python Bioinformatics Cookbook
==============================

A collection of statements, functions, and programs that illustrate how to
perform typical bioinformatics tasks in Python. The programs are written to be
easy to understand more than efficient or bullet-proof.

## Table of Contents ##

+ Reading a single sequence from a FASTA file
+ Reading multiple sequences from a FASTA file
+ Retrieving command line arguments with `sys.argv`
+ Defining and retrieving command line arguments with `argparse`



To read a file of numbers into a list, convert each number to a `float` and
then append it to a list.

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
	header = fp.readline() # or is it better as next(fp)?
	for line in fp:
		seq += line.rstrip()
```

Reading a multi-FASTA file is a little complicated. Building and returning a
list of sequences is wasteful of CPU and RAM for long sequences. Use the
function below, which has some useful features.

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
