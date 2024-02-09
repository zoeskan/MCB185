Unit 7: Dictionaries
====================

## Contents ##

+ [Basics](#basics)
    + [Iteration](#iteration)
+ [Lookup Tables](#lookup-tables)
+ [Categorial Data](#categorical-data)
    + [71countgff.py](#71countgffpy)
    + [Composition, again](#composition-again)
    + [Sorting](#sorting)
+ [K-mers](#k-mers)
    + [72kmercount.py](#72kmercount.py)
+ [Homework](#homework)
    + [73missingkmers.py](#73missingkmerspy)
    + [74genefinder.py](#74genefinderpy)

------------------------------------------------------------------------------

## Basics ##

A dictionary is like a list, but with string instead of numeric indicies.

+ `list[0]` - 0 is a numeric index
+ `dict['hey']` - 'hey' is a string index

Unlike lists, there is no `append()` for dictionaries. Each item in a
dictionary exists as a key:value pair. The key is the string in square brackets
('hey' above). The value is anything you can put in a variable.

Let's start `70demo.py` and do some exploring. An empty dictionary is created
either with empty braces or the `dict()` function.

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

To check if a key exists, use the keyword `in`.

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
because dictionaries are designed for fast lookups.

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

Now that dictionaries have been introduced, you're welcome to use them. Check
out the `PYTHON_COOKBOOK.md` file in MCB185 and copy-paste the `hydropathy()`
and `translate()` functions into your library. Yes, I'm actually suggesting
copy-paste in this instance so that you don't make any typing errors.

------------------------------------------------------------------------------

## Categorical Data ##

Dictionaries aren't only for looking up previous information, but categorizing
new information.

### 71countgff.py ###

Remember way back in Unit 1 when we crafted a CLI to count all of the features
in a GFF?

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr
```

Let's do the equivalent in python. Start a new program called `71countgff.py`
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
a key in the diectionary before we can start counting.

Line 8 does the counting under the assumption that the feature is already in
the table, which it must be due to Line 7.

Lines 9 reports the counts of each feature.

An alternative way of writing lines 7 and 8 is below.

```python
7           if feature not in count: count[feature] = 1
8           else:                    count[feature] += 1
```

### Composition, again ###

In previous units we saw several strategies for counting nucleotides in
sequences.

1. Create named variables `A`, `C`, `G`, `T` and an if-elif-else stack
2. Create a single list, but still use an if-elif-else stack
3. Create parallel lists and use `str.find()` for indexing
4. Use `str.count()` on each nucleotide

Strategy 4 appeared to be tidy and efficient, but suffered from one problem:
what happens when there are unexpected letters in the sequence? They won't be
counted at all.

The better way is to use a dictionary. The strategy is identical to the gff
counting strategy.

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
python3 71countgff.py ecoli.gff.gz | sort
python3 71countgff.py ecoli.gff.gz | sort -n -k 2
python3 71countgff.py ecoli.gff.gz | sort -nk2
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

## K-mers ##

K-mers are used in a variety of bioinformatics analyses. A k-mer is simply a
sequence of length k, where k is a small integer. The subsequences of sliding
window algorithms are k-mers. Individual nucleotides are k-mers of length 1.

### 72kmercount.py ###

To explore k-mers, let's make a new program: `72kmercount.py`. As the name
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
python3 72kmercount.py ecoli.fa.gz 1
```

Try increasing the value for k on the command line. With each increase, you see
4 times as many k-mers. Well, until you get to 7. 4^7 is 16,384 but `wc` shows
there's only 16,383. One of the k-mers is missing.

```
python3 72kmercount.py ecoli.fa.gz 7 | wc
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

Add the following to `72kmercount.py`.

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
python3 72kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
```

The k-mer 'GCCTAGG' doesn't exist in the E.coli genome (on the positive
strand). It does exist if you reverse-complement the genome.

## Homework ##

+ `70demo.py`
+ `71countgff.py`
+ `72kmercount.py`
+ `73missingkmers.py`
+ `74genefinder.py`

### 73missingkmers.py ###

Write a program that searches sequences for the smallest missing k-mer. The
program is a little different from `72kmercount.py`.

+ Start k at 1 and increase until there are missing k-mers
+ Only report the k-mers that are missing
+ Stop after finding a value of k with missing k-mers
+ Search both strands of the sequence

The output of your program should find 52 missing k-mers in the E.coli genome
at k=8.

### 74genefinder.py ###

Write a program the reports putative coding genes in the E.coli genome. This is
similar to `64profinder.py`, but you must get the coordinates of each CDS.

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
+ Use a `while` loop to skip your indices ahead of the last stop codon
