Unit 8: Data
============

## Contents ##

+ [Lists of Things](#2-lists-of-things)
	+ [Arrays and Matrices](#arrays-and-matrices)
+ [Records](#records)
	+ [Dicts of Dicts](#dicts-of-dicts)
+ [Complex Data](#complex-data)
	+ [JSON](#json)
+ [Regular Expressions](#regular-expressions)
	+ [81prosite.py](#81prositepy)
+ [Homework](#homework)
	+ [82kozak.py](#82kozakpy)
	+ [83splicesites.py](#83splicesitespy)

------------------------------------------------------------------------------

## Lists of Things ##

Start `80demo.py` as usual.

Up to now, almost all of the data has been 1-dimensional. Strings, tuples,
lists, and dictionaries are all 1-dimensional. The only 2-dimensional thing has
been `sys.argv`. You may not have recognized that. The following command shows
that `sys.argv` is a list with a single element: the name of your program, and
of course you can access that by indexing.

```
print(sys.argv)
print(sys.argv[0])
```

What you might not have appreciated, is that you can access individual
characters with another set of brackets.

```
print(sys.argv[0][3])
```

A list of strings is a 2-dimensional data structure. The strings are the first
dimension. The letters are the second. As soon as we put containers in a list,
the list becomes multi-dimensional. The containers don't even have to be the
same type or "shape".

```
d = [
	'hello',
	(3.14, 'pi'),
	[-1, 0, 1],
	{'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])
```

### Arrays and Matrices ###

The words 'array' and 'list' are sometimes used interchangeably. In some
languages, they mean the exact same thing. In Python they do not. We have been
working with lists since unit 5. But Python also defines arrays, which are
linear containers where all elements are the exact same type (e.g. int). We
aren't using arrays in this course. One of the most popular Python libraries is
'numpy', which also defines arrays.

Matrices are multi-dimensional arrays. Matrices are rectangular (each dimension
has the same number of elements) and like arrays, all values are of the same
type. Computationally, arrays and matrices are much more efficient than lists.
Once you start doing computationally-intensive tasks, 'numpy' and other
libraries will become very useful.

------------------------------------------------------------------------------

## Records ##

One of the most important data types is the list of dictionaries. Sometimes
this will be called a list of objects, list of structs, or list of records.

A record is a data type with various named _fields_. For example, a record for
a sequencing oligo might look like this:

```
oligo = {
	'Name': 'SO116',
	'Length': 18,
	'Sequence': 'ATTTAGGTGACACTATAG',
	'Description': 'SP6 promoter sequencing primer'
}
```

A catalog is a list of records.

```
catalog = []
catalog.append(oligo)
```

Lists of records can be very large, so we generally don't type them in. We
typically read them in from files. Examine `MCB185/data/primers.csv`, which has
some sequencing primers from a catalog. Here's how we read a CSV file into a
list of records.

```
1	def read_catalog(filepath):
2		catalog = []
3		with open(filepath) as fp:
4			for line in fp:
5				if line.startswith('#'): continue
6				name, length, seq, desc = line.rstrip().split(',')
7				record = {
8					'Name': name,
9					'Length': length,
10					'Sequence': seq,
11					'Description': desc
12				}
13				catalog.append(record)
14		return catalog
```

Line 6 is a new construction. `str.rstrip()` removes characters from the
right-hand side of a string. In this case, without any parameters, it removes
the newline character(s). This works on both Unix (LF) and Windows (CRLF) line
endings. `line.rstrip()` returns a string. Instead of putting that string into
a named variable, we can split it immediately by calling `str.split()` to
retrieve a list from the comma-separated values on the line.

Lines 7-12 create the record. Note that you don't need to name a record before
appending it. Lines 7-13 could be replaced by the following.

```
catalog.append({'Name': name, 'Length': length, 'Sequence': seq, 'Description': desc})
```

Now that we have a function that reads a catalog, we can load it and access
its records.

```
catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])
```

Like any dictionary, we can edit fields by accessing their keys and add new
items by creating new key:value pairs. Let's add the melting temperature for
each oligo.

Do you remember `22oligotemp.py`? Harvest the code from there, modify it to
accept a string, and add it to your library.

```
for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)
```

### Dicts of Lists ###

In the last unit, we counted k-mers in sequences. What if instead of counting
them, we wanted to know the location of each k-mer on the sequence? Here's what
the code looked like before. Take note of lines 4-5.

```
1	kcount = {}
2	for i in range(len(seq) -k +1):
3		kmer = seq[i:i+k]
4		if kmer not in kcount: kcount[kmer] = 0
5		kcount[kmer] += 1
```

In order to record locations of k-mers, we need to turn the initialization of 0
into an initialization of an empty list. And then instead of counting k-mers,
we need to append their locations.

```
1	seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
2	k = 2
3	kloc = {}
4	for i in range(len(seq) -k +1):
5		kmer = seq[i:i+k]
6		if kmer not in kloc: kloc[kmer] = []
7		kloc[kmer].append(i)
8	print(kloc)
```

Line 6 associates a new empty list with each new dictionary key.

Line 7 appends the location `i` on the list called `kloc[kmer]`.

We didn't change much code, but the behavior is now very different. You could
use the k-mer counting code on huge genomes and it wouldn't end up using any
more memory than a tiny genome. However, if you're storing the locations of
every k-mer, the lists could grow large enough to crash your computer.

------------------------------------------------------------------------------

## Complex Data ##

The bread and butter of most data scientists are 2-dimensional structures we
call spreadsheets, dataframes, or tables. But some kinds of data don't fit
conveniently into 2 dimensions. Take a look at the GenBank file corresponding
to the E.coli genome.

```
zless ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff.gz
```

Some parts, like DEFINITION, look like simple key:value pairs. Other parts,
like REFERENCE contains a list of 19 papers. Each paper contains some key:value
pairs. In Python, we might make a data structure like the one below. It
contains a mixture of dictionaries and lists.

```
{
    "locus": "NC_000913",
    "length": 4641652,
    "type": "DNA",
    "definition": "Escherichia coli str. K-12 substr. MG1655, complete...",
    "reference": [
        {
            "authors": "Riley,M., Abe,T., Arnaud,M.B., Berlyn,M.K...",
            "title": "Escherichia coli K-12: a cooperatively...",
            "journal": "Nucleic Acids Res. 34 (1), 1-9 (2006)",
            "pubmed": 16397293
        },
        {
            "authors": "Hayashi,K., Morooka,N., Yamamoto,Y., Fujita,K...",
            "title": "Highly accurate genome sequences of Escherichia...",
            "journal": "Mol. Syst. Biol. 2, 2006 (2006)",
            "pubmed": 16738553
        }
    ]
}
```

### JSON ###

Did you notice the sudden switch to double quotes? That's because the code
above is also compatible with the data exchange standard called JSON
(Javascript Object Notation). It's very similar to Python with some exceptions.

+ Double-quotes only
+ Boolean values are `true` and `false`
+ Trailing commas are not allowed on the last element of a block
+ There are no comments

Python provides the `json` library for reading and writing JSON. When working
with complex data structures, `json.dumps()` can be a useful way of examining
the structure.

```
truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent=4))
```

------------------------------------------------------------------------------

## Regular Expressions ##

One of the oldest but still useful ways to analyze protein sequences are
PROSITE patterns. The rules specify exact and partial matches. Here are some
examples.

+ R-G-D means sequences with the substring "RGD" in them
+ X means any amino acid
+ [ST]-X-[RK] means S or T followed by any amino acid, followed by R or K
+ [ILV](3,5) any mixture of 3 to 5 of these hydrophobic amino acids
+ {P} means not proline
+ <M means begins with methionine
+ >W means ends with tryptophan

If you're thinking to yourself that these rules sound a bit like `grep`, you
are correct. Both PROSITE and `grep` are regular grammars. `grep` stands for
"general regular expression parser". Python has a regular expression library,
`re`, that allows you to search, extract, and replace substrings with inexact
matching.

### 81prosite.py ###

Let's explore regular expressions in the context of PROSITE patterns. Start a
program `81prosite.py` and start stepping through E.coli proteins (in
MCB185/data of course). Print the names of any sequences matching the PROSITE
pattern D-K-T-G-T. This is easily solved by dropping the dashes and searing
with `in`.

```
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)
```

The regular expression version isn't much different. `re.search()` takes two
arguments, a _pattern_ and a string. In this case, the pattern is 'DKTGT' and
the string is the sequence.

```
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT', seq): print(defline)
```

'D-K-T-G-T' is a subset of a larger PROSITE pattern for P-type ATPases
phosphorylation site (PDOC00139). The full pattern is: D-K-T-G-T-[LIVM]-[TI].
The token '[LIVM]' means any one of leucine, isoleucine, valine, or methionine.
Similarly '[TI]' is a choice of two amino acids. We can't use `in` to make a
match to the entire pattern, but we can with regex, which uses the exact same
syntax for the character classes we used back in Unit 1 with `grep`.

```
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT[LIVM][TI]', seq): print(defline)
```

Let's try a more complex pattern: C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H.
This is the pattern for C2H2 zinc-finger proteins (PS00028). The 'x' stands for
any amino acid while the number in parentheses stands for a range. (2,4) means
2 to 4 amino acids while (3) means exactly 3.

In regular expressions, `.` means any symbol rather than x. Also, regex uses
curly braces for ranges rather than parentheses.

```
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)
```

Regular expressions can also extract the text they match. Each pair of
parentheses is called a match group.

```
1	pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
2	for defline, seq in mcb185.read_fasta(sys.argv[1]):
3		m = re.search(pat, seq)
4		if m: print(m.group(1))
```

Line 1 abstracts the pattern into a variable, which is what we should have done
from the beginning. But sometimes you don't know that until later.

Line 3 assigns the search to a variable. The variable will either have a value
of `None`, which is logically `False`, or it will contain a "match object".
This is why the variable is named `m`.

Line 4 retrieves the matched substring if `m` has a value that can be
considered `True` (most things are `True` except `None`, `False`, 0, and empty
containers).

Ultimately, the protein that matches has the following peptide that matches the
C2H2 zinc-finger pattern: CHACEIACVMAHNDEQHVLSQHH

Regular expressions are very powerful, and we have barely scratched the
surface. There are a lot of good guides on regular expressions.

------------------------------------------------------------------------------

## Homework ##

+ `80demo.py`
+ `81prosite.py`
+ `82kozak.py`

### 82kozak.py ###

Create a PWM for the Kozak consensus (translation intiation) for E.coli. Output
the file in JSON, JASPAR, and TRANSFAC formats.

### 83splicesites.py ###

Create PWMs for the splice donor and acceptor sites using the FASTA and GFF
files from the model organisms. Output the file in JSON, JASPAR, and TRANSFAC
formats.
