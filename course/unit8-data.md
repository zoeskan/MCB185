Unit 8: Data
============

## Contents ##

+ [Lists of Things](#lists-of-things)
    + [Arrays and Matrices](#arrays-and-matrices)
+ [Records](#records)
    + [Dicts of Dicts](#dicts-of-dicts)
+ [Complex Data](#complex-data)
    + [JSON](#json)
+ [Regular Expressions](#regular-expressions)
    + [81prosite.py](#81prositepy)
+ [Homework](#homework)
    + [82transfac.py](#82transfacpy)
    + [83kozak.py](#83kozakpy)
    + [84splicesites.py](#84splicesitespy)

------------------------------------------------------------------------------

## Lists of Things ##

Start `80demo.py` as usual.

Up to now, almost all of the data has been 1-dimensional. Strings, tuples,
lists, and dictionaries are all 1-dimensional. The first 2-dimensional thing
was `sys.argv`. You may not have recognized that. The following command shows
that `sys.argv` is a list with a single element: the name of your program, and
of course you can access that by indexing.

```python
print(sys.argv)
print(sys.argv[0])
```

What you might not have appreciated, is that you can access individual
characters with another set of brackets.

```python
print(sys.argv[0][3])
```

A list of strings is a 2-dimensional data structure. The strings are the first
dimension. The letters are the second. As soon as we put containers in a list,
the list becomes multi-dimensional. The containers don't even have to be the
same type or "shape".

```python
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
linear containers where all elements are the exact same type (e.g. int). Arrays
are constructed with the `array()` function. We aren't using arrays in this
course. One of the most popular Python libraries is 'numpy', which also defines
arrays as `numpy.array()`. We also aren't using numpy arrays.

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

```python
oligo = {
    'Name': 'SO116',
    'Length': 18,
    'Sequence': 'ATTTAGGTGACACTATAG',
    'Description': 'SP6 promoter sequencing primer'
}
```

A catalog is a list of records.

```python
catalog = []
catalog.append(oligo)
```

Lists of records can be very large, so we generally don't type them in. We
typically read them in from files. Examine `MCB185/data/primers.csv`, which has
some sequencing primers from a catalog. Here's how we read a CSV file into a
list of records.

```python
1   def read_catalog(filepath):
2       catalog = []
3       with open(filepath) as fp:
4           for line in fp:
5               if line.startswith('#'): continue
6               name, length, seq, desc = line.rstrip().split(',')
7               record = {
8                   'Name': name,
9                   'Length': length,
10                  'Sequence': seq,
11                  'Description': desc
12              }
13              catalog.append(record)
14      return catalog
```

Line 6 is a new construction. `str.rstrip()` removes characters from the
right-hand side of a string. In this case, without any parameters, it removes
the newline character(s). This works on both Unix (LF) and Windows (CRLF) line
endings. `line.rstrip()` returns a string. Instead of putting that string into
a named variable, we can split it immediately by calling `str.split()` to
retrieve a list from the comma-separated values on the line.

Lines 7-12 create the record. Note that you don't need to name a record before
appending it. Lines 7-13 could be replaced by the following (but should it?).

```python
catalog.append({'Name': name, 'Length': length, 'Sequence': seq, 'Description': desc})
```

Now that we have a function that reads a catalog, we can load it and access
its records.

```python
catalog = read_catalog('primers.csv')
for primer in catalog:
    print(primer['Name'], primer['Description'])
```

Like any dictionary, we can edit fields by accessing their keys and add new
items by creating new key:value pairs. Let's add the melting temperature for
each oligo.

Do you remember `22oligotemp.py`? Harvest the code from there, modify it to
accept a string, and add it to your library.

```python
for primer in catalog:
    primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)
```

### Dicts of Lists ###

In the last unit, we counted k-mers in sequences. What if instead of counting
them, we wanted to know the location of each k-mer on the sequence? Here's what
the code looked like before. Take note of lines 4-5.

```python
1   kcount = {}
2   for i in range(len(seq) -k +1):
3       kmer = seq[i:i+k]
4       if kmer not in kcount: kcount[kmer] = 0
5       kcount[kmer] += 1
```

In order to record locations of k-mers, we need to turn the initialization of 0
into an initialization of an empty list. And then instead of counting k-mers,
we need to append their locations.

```python
1   seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
2   k = 2
3   kloc = {}
4   for i in range(len(seq) -k +1):
5       kmer = seq[i:i+k]
6       if kmer not in kloc: kloc[kmer] = []
7       kloc[kmer].append(i)
8   print(kloc)
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

```python
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
+ Boolean values are `true` and `false` (lower case instead of title case)
+ Trailing commas are not allowed on the last element of a block
+ There are no comments

Python provides the `json` library for reading and writing JSON. When working
with complex data structures, `json.dumps()` can be a useful way of examining
the structure.

```python
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

+ `R-G-D` means proteins with the peptide "RGD" in them
+ `X` means any amino acid
+ `[ST]-X-[RK]` means S or T followed by any amino acid, followed by R or K
+ `[ILV](3,5)` any mixture of 3 to 5 of these hydrophobic amino acids
+ `{P}` means not proline
+ `<M` means begins with methionine
+ `>W` means ends with tryptophan

If you're thinking to yourself that these rules sound a bit like `grep`, you
are correct. Both PROSITE and `grep` are regular grammars. `grep` stands for
"general regular expression parser". Python has a regular expression library,
`re`, that allows you to search, extract, and replace substrings with inexact
matching.

### 81prosite.py ###

Let's explore regular expressions in the context of PROSITE patterns. Start a
program `81prosite.py` and start stepping through E.coli proteins (in
MCB185/data of course). Print the names of any sequences matching the PROSITE
pattern "D-K-T-G-T". This is easily solved by dropping the dashes and searching
with `in`.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if 'DKTGT' in seq: print(defline)
```

The regular expression version isn't much different. `re.search()` takes two
arguments, a _pattern_ and a string. In this case, the pattern is "DKTGT" and
the string is the sequence.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT', seq): print(defline)
```

"D-K-T-G-T" is a subset of a larger PROSITE pattern for P-type ATPases
phosphorylation site (PDOC00139). The full pattern is: "D-K-T-G-T-[LIVM]-[TI]".
The character class "[LIVM]" means any one of leucine, isoleucine, valine, or
methionine. Similarly "[TI]" is a choice of two amino acids. We can't use `in`
to make a match to this fuzzy pattern, but we can with regex, which uses the
exact same syntax for the character classes we used back in Unit 1 with `grep`.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT[LIVM][TI]', seq): print(defline)
```

Let's try a more complex pattern: "C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H".
This is the pattern for C2H2 zinc-finger proteins (PS00028). The "x" stands for
any amino acid while the number in parentheses stands for a range. "x(2,4)"
means 2 to 4 amino acids while "x(3)" means exactly 3.

In regular expressions, `.` means any symbol rather than "x". Also, regex uses
curly braces for ranges rather than parentheses. Therefore "x(2,4)" becomes
`.{2,4}`.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)
```

Regular expressions can also extract the text they match. Each pair of
parentheses is called a match group. The example below has only one group,
which is the entire pattern.

```python
1   pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
2   for defline, seq in mcb185.read_fasta(sys.argv[1]):
3       m = re.search(pat, seq)
4       if m: print(m.group(1))
```

Line 1 abstracts the pattern into a variable. Imagine iterating through a list
of patterns in an outer loop.

Line 3 assigns the search to a variable. The variable will either have a value
of `None`, which is logically `False`, or it will contain a "match object". The
variable is named `m` as an abbreviation for "match".

Line 4 retrieves the matched substring if `m` has a value that can be
considered `True` (most things are `True` except `None`, `False`, 0, and empty
containers).

Ultimately, the pattern matches: "CHACEIACVMAHNDEQHVLSQHH".

Regular expressions are very powerful, and we have barely scratched the
surface. The Internet has a lot of good guides on regular expressions.

------------------------------------------------------------------------------

## Homework ##

+ `80demo.py`
+ `81prosite.py`
+ `82transfac.py`
+ `83kozak.py`
+ `84splicsites.py`

### 82transfac.py ###

Create a program that reads position weight matrices (PWMs) in TRANSFAC format
and outputs the records as JSON. See `MCB185/data/*.transfac.gz`.

The output of your program should look like this:

```
[
    {
        "id": "AGL3",
        "pwm": [
            {
                "A": 0.0,
                "C": 92.0,
                "G": 0.0,
                "T": 3.0
            },
            {
                "A": 0.0,
                "C": 79.0,
                "G": 0.0,
                "T": 16.0
            },
            {
                "A": 82.0,
                "C": 1.0,
                "G": 2.0,
                "T": 10.0
            },
 ```

### 83kozak.py ###

Create a PWM for the Kozak consensus (translation intiation) for E.coli using
the GenBank flat file: `MCB185/data/*.gbff.gz`. Output the PWM in TRANSFAC
format as shown below.

```
AC IMTSU001
XX
ID ECKOZ
XX
DE I made this shit up
PO      A       C       G       T
1       1220    245     2413    417
2       1565    333     1845    552
3       1591    469     1426    809
4       1441    614     1168    1072
5       1445    763     889     1198
6       1526    935     757     1077
7       1812    766     982     735
8       1126    1138    583     1448
9       1160    1133    664     1338
10      3875    2       338     80
11      0       0       0       4295
12      0       0       4291    4
13      2134    667     880     614
14      1588    1214    711     782
XX
```

To make your values print neatly into columns of a specific width, use f-strings
with `:<8` to left-justify text that will always be 8 letters wide, even if
there is just one character.

```
for i in range(5):
    print(f'{i+1:<8}', 'stuff')
```

### 84splicesites.py ###

Create PWMs for the splice donor and acceptor sites using the FASTA and GFF
files from the model organisms. Output the file in TRANSFAC format.

For the C. elegans splice sites of type `RNASeq_splice`, you will get the
following PWMs. Each intron is counted once, but one could make the argument
that you should weight by the number of occurrences, which is actually
available in the GFF. However, if you do that, the counts do not fit in the
pre-formatted table. If you go that route, you will need to output as
probabilities instead of raw counts.

```
AC DEMO1
XX
ID ACC
XX
DE splice acceptor
PO      A       C       G       T
1       1747    1094    861     3571
2       956     822     713     4782
3       796     655     518     5304
4       1231    1594    1095    3353
5       963     4621    631     1058
6       7020    78      87      88
7       71      162     6961    79
XX
//
AC DEMO2
XX
ID DON
XX
DE splice donor
PO      A       C       G       T
1       149     87      6962    75
2       104     337     79      6753
3       3224    569     2015    1465
4       3478    1103    1189    1503
5       1451    699     3809    1314
6       1588    1076    1280    3329
XX
//
```
