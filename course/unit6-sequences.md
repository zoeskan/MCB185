Unit 6: Sequences
=================

## Contents ##

+ [Reading FASTA Files](#reading-fasta-files)
    + [mcb185 Library](#mcb185-library)
    + [Stepping Through FASTA Files](#stepping-through-fasta-files)
+ [Sequence Composition](#sequence-composition)
    + [if-elif-else Stack](#if-elif-else-stack)
    + [List Variation](#list-variation)
    + [Indexing with str.find()](#indexing-with-strfind)
    + [Counting with str.count()](#counting-with-strcount)
+ [Central Dogma](#central-dogma)
    + [dogma.py](#dogmapy)
    + [Transcription](#transcription)
    + [Reverse-Complement](#reverse-complement)
    + [test_dogma.py](#test_dogmapy)
    + [Translation](#translation)
+ [Sliding Window Algorithms](#sliding-window-algorithms)
    + [61skewer.py](#61skewerpy)
+ [Homework](#homework)
    + [62skewer.py](#62skewerpy)
    + [63dust.py](#63dustpy)
    + [64profinder.py](#64profinderpy)
    + [65transmembrane.py](#65transmembranepy)

------------------------------------------------------------------------------

## Reading FASTA Files ##

Sequences are often stored in FASTA format. A single sequence record has a
definition line (defline) followed by multiple lines of sequence. Here's an
example of a FASTA file.

```
>NP_414547.1 DNA binding and peroxide stress response protein YaaA
MLILISPAKTLDYQSPLTTTRYTLPELLDNSQQLIHEARKLTPPQISTLMRISDKLAGINAARFHDWQPDFTPANARQAI
LAFKGDVYTGLQAETFSEDDFDFAQQHLRMLSGLYGVLRPLDLMQPYRLEMGIRLENARGKDLYQFWGDIITNKLNEALA
AQGDNVVINLASDEYFKSVKPKKLNAEIIKPVFLDEKNGKFKIISFYAKKARGLMSRFIIENRLTKPEQLTGFNSEGYFF
DEDSSSNGELVFKRYEQR
```

The defline begins with `>` and is immediately followed by an identifier that
is usually a unique identifier for the sequence (NP_414547.1 is a unique
identifier at NCBI). The rest of the defline can have any descriptive
information.

This record has 4 sequence lines. There isn't any standard on how long each
sequence line is, but 60 and 80 characters is common. Some people put all of
their sequence on a single, long line.

Multi-FASTA files have more than one sequence record. Here's an example with
two.

```
>NP_414542.1 thr operon leader peptide
MKRISTTITTTITITTGNGAG
>NP_414565.1 DUF2575 domain-containing protein YaaY
MCRHSLRSDGAGFYQLAGCEYSFSAIKIAAGGQFLPVICAMAMKSHFFLISVLNRRLTLTAVQGILGRFSLF
```

### mcb185 Library ###

Reading FASTA files is a little bit awkward because there is no end-of-record
delimiter. Records start with `>` but the end is either signaled by a new
record or the end of the file. To make our lives a little simpler, we're going
to import a FASTA file reader from the MCB185 repo.

Create `60demo.py` and add the following to the top.

```python
import mcb185
```

If you try running your program, you will get an error. Python doesn't know
where the `mcb185.py` library file is. There are several places it looks, and
one of those is your current directory. Make a soft link from
`MCB185/src/mcb185.py` to your homework directory so that it looks like
`mcb185.py` is in your homework repo.

```
cd ~/Code/mcb185_homework
ln -s ../MCB185/src/mcb185.py .
```

Libraries are collections of reusable functions. We've used them in the past.
For example, `import math` gave us access to the math library and `math.log2()`
was one of the functions we called. You can make your own libraries for your
favorite functions (which we will do a little later).

### Stepping Through FASTA Files ###

Add the following code to your demo.

```python
1   import sys
2   import mcb185
3
4   for defline, seq in mcb185.read_fasta(sys.argv[1]):
5       print(defline[:30], seq[:40], len(seq))
```

Run it like this.

```
python3 60demo.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz
```

Each iteration of the `for` loop retrieves the next record from the FASTA file.
Each record is returned as a tuple containing the definition line and the
sequence (as a single string, not a bunch of lines). The function works with
both normal and compressed files. If you want to see how it works, there's
nothing stopping you from looking.

## Sequence Composition ##

Let's write a program that calculates the GC composition of nucleotide
sequences in a FASTA file. Swap out line 5 above for the following.

```python
4   for defline, seq in mcb185.read_fasta(sys.argv[1]):
5       defwords = defline.split()
6       name = defwords[0]
7       gc = 0
8       for nt in seq:
9           if nt == 'C' or nt == 'G': gc += 1
10      print(name, gc/len(seq))
```

Lines 5-6 split the defline and assign the unique identifier to a variable
appropriately called `name`. Note that the `>` was already removed by
`mcb185.read_fasta()`.

Line 7 initializes the GC counter. This must be reset for every sequence, which
is why it is inside the loop and not defined somewhere above line 4.

Lines 8-9 iterate through the letters, checking if they are C or G, and
counting them if they are.

Line 10 does the final calculation and output.

Try this out using the model organism genomes in MCB185/data.

```
python3 60demo.py ../MCB185/data/A.thaliana.fa.gz
python3 60demo.py ../MCB185/data/C.elegans.fa.gz
python3 60demo.py ../MCB185/data/D.melanogaster.fa.gz
```

### if-elif-else Stack ###

Let's modify your program so that it counts 5 nucleotides (ACGTN), not just Cs
and Gs. One way to solve this problem is to create individual variables for
each nucleotide and a stack of if-elif-else statements that assigns them
individually.

```python
5   A = 0
6   C = 0
7   G = 0
8   T = 0
9   N = 0
10  for nt in seq:
11      if   nt == 'A': A += 1
12      elif nt == 'C': C += 1
13      elif nt == 'G': G += 1
14      elif nt == 'T': T += 1
15      else:           N += 1
16  print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
```

### List Variation ###

A slight variation is to create a list to hold the counts. Here, lines 6-7
initialize a list called `counts`. There is still a stack of if-elif-else, but
instead of assigning named variables, the assignments are at specific indices
of the list variable `counts`.

```python
5   nts = 'ACGTN' # should really be defined outside the loop
6   counts = []
7   for i in range(len(nts)): counts.append(0)
8   for nt in seq:
9       if   nt == 'A': counts[0] += 1
10      elif nt == 'C': counts[1] += 1
11      elif nt == 'G': counts[2] += 1
12      elif nt == 'T': counts[3] += 1
13      else:           counts[4] += 1
14  print(name, end='\t')
15  for n in counts: print(f'{n/len(seq):.4f}', end='\t')
16  print()
```

### Indexing with str.find() ###

The next variation of the code replaces lines 6-7 above with a single line that
uses the multiplication operator `*` to initialize all counts to 0 (line 6).
This isn't a major change. We call such conveniences "syntactic sugar".

The major change is to replace the if-elif-else stack with `str.find()`. Each
`nt` retrieved from the sequence is compared to the alphabet in `nts`. If the
letter is found, its index is returned. For example, if the letter is a 'G',
the index in 'ACGT' is 2 and the code does `counts[2] += 1` (line 9).
Conveniently, if there are any unknown letters, they get a -1 index. Negative
numbers like `counts[-1]` index backwards. As a result, unknown letters get
dumped into the counts for 'N'. This is the exact behavior of the if-elif-else
stack.

```python
5   nts = 'ACGTN' # should really be defined outside the loop
6   counts = [0] * len(nts)
7   for nt in seq:
8       idx = nts.find(nt)
9       counts[idx] += 1
10  print(name, end='\t')
11  for n in counts: print(f'{n/len(seq):.4f}', end='\t')
12  print()
```

### Counting with str.count() ###

The final variation, in this unit, is the use of `str.count()` to count
specific letters. Here, we iterate through the letters of the alphabet, getting
the counts for each one. For example, in the first iteration, the letter is
'A'. On line 8, we simply ask `seq` to count how many As it has.

```python
5   nts = 'ACGTN' # should really be defined outside the loop
6   print(name, end='\t')
7   for nt in nts:
8       print(seq.count(nt) / len(seq), end='\t')
9   print()
```

This solution is both tidy and efficient. However, what do we do if we run into
a letter that isn't in our alphabet? The previous solutions dumped unexpected
characters into 'N'. In case you think this doesn't happen, try the following
command line.

```
gunzip -c ~/Code/MCB185/data/A.thaliana.fa.gz | grep -v ">" | grep "[^ACGTN]"
```

## Central Dogma ##

Given that this is a programming class for biologists, we should probably make
some typical sequence metabolism functions that do things like transcription,
reverse-complement, and translation. We'll end up using these functions
multiple times, so it's time to create your first library.

### dogma.py ###

Create a file called `dogma.py` in your homework repo. If you don't want to use
this name, feel free to call it `toolbox.py` or something you come up with.
This is your library, so name it whatever you like. But don't call it `math.py`
or `sys.py` because those are names of built-in libraries. Also, don't call it
`numpy.py` because that's a really powerful library that everyone but MCB185
students use. Coming up with a good name can be difficult.

### Transcription ###

Transcription converts 'T' to 'U'. The `str.replace()` method searches for
substrings and converts those to other substrings. Recall that strings are
immutable, so the original string isn't modified. `str.replace()` returns a
modified copy. Put this function in `dogma.py`.

```python
def transcribe(dna):
    return dna.replace('T', 'U')
```

### Reverse-Complement ###

When working with DNA, we often need to work with the reverse-complement
strand. Let's make a function that does that and add it to our library.

```python
1   def revcomp(dna):
2       rc = []
3       for nt in dna[::-1]:
4           if   nt == 'A': rc.append('T')
5           elif nt == 'C': rc.append('G')
6           elif nt == 'G': rc.append('C')
7           elif nt == 'T': rc.append('A')
8           else:           rc.append('N')
9       return ''.join(rc)
```

Line 2 creates a list `rc` to hold the new sequence. At the end, the function
will return a string version of this list with `str.join()` (line 9).

Line 3 steps backwards through the sequence using slice syntax.

Lines 4-8 do the complementing. Note that any letters that are not ACGT get
converted to N, which isn't the best behavior. If you want to see a more
thorough and confusing version, see `mcb185.anti_seq()`.

### test_dogma.py ###

In order to test the functions in our library, we need a program that imports
the library and calls its functions. Create a file called `test_dogma.py` or
`test_name.py` depending on the name of your library.

```python
1   import dogma
2
3   print(dogma.transcribe('ACGT'))
4   print(dogma.revcomp('AAAACGT'))
```

Most software engineers create "unit tests" and "integration tests" that call
library functions with various arguments. These tests ensure that code works
properly, handles unexpected input, and that new changes to the code still
provide the same output as the old code. We don't do any automated testing in
this class, but automated testing is standard in a professional setting. It's
sort of like wearing latex gloves in lab. If you're not doing unit tests or you
aren't wearing gloves, you're not being very professional.

### Translation ###

Converting nucleotide sequences to proteins isn't as simple as transcription or
reverse-complement. First, we have to retrieve codons by stepping through the
nucleotide sequence 3 letters at a time. Then we have to convert codons to
amino acids.

Let's create some really simple code in `test_dogma.py` that demonstrates how
we expect to call the function. Ideally, this results in 'M*' where 'ATG' gets
translated to 'M' and 'TAA' gets translated to a stop codon (which is usually
represented as a '*').

```python
print(dogma.translate('ATGTAA')) # should return M*
```

Let's write a minimal translation function in `dogma.py`.

```python
1   def translate(dna):
2       aas = []
3       for i in range(0, len(dna), 3):
4           codon = dna[i:i+3]
5           if   codon == 'ATG': aas.append('M')
6           elif codon == 'TAA': aas.append('*')
7           else:                aas.append('X')
8       return ''.join(aas)
```

Line 2 initializes an empty list for the amino acids. Each codon that is
translated will be append to this list.

Line 3 steps through indices by threes. The value of `i` will contain the
starting index of each codon.

Line 4 creates a codon, which is a 3-letter slice starting from the current
index of `i`.

Lines 5-7 do the actual translation. One way of performing the translation is
with a giant stack of if-elif-else statements. It's highly abbreviated here.
When running into codons with unusual letters or codons that are shorter than
3, the amino acid is ambiguous. In these cases, people often use the letter
'X'.

Line 8 returns the amino acid list as a string.

Here's an alternative way to write the function:

```python
1   def translate(dna):
2       codons = ('ATG', 'TAA')
3       aminos = 'M*'
4       aas = []
5       for i in range(0, len(dna), 3):
6           codon = dna[i:i+3]
7           if codon in codons:
8               idx = codons.index(codon)
9               aa = aminos[idx]
10              aas.append(aa)
11          else:
12              aas.append('X')
13      return ''.join(aas)
```

Lines 2-3 create parallel containers that match up codons to amino acids.

Lines 7-12 do the translation. The strategy here is very similar to the
letter-counting code that used `str.find()`. Lists and tuples don't have a
`find()` method, so we have to use `index()`. Unfortunately, this throws errors
if the codon isn't found. So first we ask if the codon is `in` the tuple, then
we ask for its position with `index()`. Once we have the position in `idx`, we
can retrieve the amino acid `aa` from the string as `aminos[idx]`. Finally, we
append `aa` to the growing protein.

Note that the `idx` and `aa` variables are only used once. They don't really
need to exist. Lines 8-10 could be written as a single line:

```python
aas.append(aminos[codons.index(codon)])
```

While this one-liner shows a bit more programming sophistication, it doesn't
make the code more readable or more efficient.

------------------------------------------------------------------------------

## Sliding Window Algorithms ##

The `translate()` function we just wrote was a specialized form of "sliding
window algorithm". The canonical form is shown below.

```python
1   w = 10
2   s = 1
3   for i in range(0, len(seq) -w +1, s):
4       subseq = seq[i:i+w]
```

Line 1 sets the size of the window. For translation, this is 3 because codons
have a length of 3.

Line 2 sets the step size. For translation, this is 3. That is, each codon is 3
nt apart. In many windowing algorithms, the step size is 1.

Line 3 moves the window along the sequence. The example shows the 3 argument
version of `range()`. The third argument `len(seq) -w +1` is critical to
prevent the window from running off the end of the sequence.

Line 4 creates a subsequence as a slice using the current offset `i` and the
window size `w`.

### 61skewer.py ###

Let's write a program that uses a sliding window algorithm to compute GC
composition and GC-skew along the length of a sequence.

First, let's create the functions for `gc_comp()` and `gc_skew()`. These sound
like useful functions we might want to use again, so let's put them into
`dogma.py`. `gc_comp()` is so simple it's not worth discussing.

```python
def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)
```

The only difficulty in `gc_skew()` is that it's possible for windows to have no
Gs or Cs in them.

```python
def gc_skew(seq):
    c = seq.count('C')
    g = seq.count('G')
    if c + g == 0: return 0
    return (g - c) / (g + c)
```

The calling code goes in `test_dogma.py`.

```python
s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))
```

Now that we know those functions work, let's toss them into the canonical
windowing algorithm. Save this as `61skewer.py`.

```python
1   seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
2   w = 10
3   for i in range(len(seq) -w +1):
4       s = seq[i:i+w]
5       print(i, dogma.gc_comp(s), dogma.gc_skew(s))
```

Line 1 is actually important here. When writing, testing, and debugging code,
make the problem small enough that you can calculate it by hand. When given a
problem, such as "compute GC-skew" in 1000 bp windows in the E.coli genome",
don't work with the genome until the code has been thoroughly tested on a tiny
subset. This is one reason why the eukaryote model organism data files in the
MCB185 repo represent only 1% of each genome.

Line 5 calls the composition and skew functions you just added to your library.
This is fine for testing purposes. Later, when you want the output to look more
consistent and professional, use f-strings like below.

```python
print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
```

## Homework ##

+ `60demo.py`
+ `dogma.py` (or whatever you ended up calling it)
+ `test_dogma.py` (or the equivalent)
+ `61skewer.py`
+ `62skewer.py`
+ `63dust.py`
+ `64profinder.py`
+ `65transmembrane.py`

### 62skewer.py ###

One problem with `61skewer.py` is that it is computationally inefficient. Each
window is counted and then forgotten. Imagine counting 1000 bp windows by hand.
Let's say you get 500 Gs and 500Cs. How many Gs do you think the next window
will have? It's just 1 bp away. As the window moves left to right, you're
losing 1 nt on the left and gaining 1 new nt on the right. The counts can't
change by more than just those 2 letters. So why bother counting everything in
the middle?

A much more efficient algorithm only counts the initial window. After that, it
"moves" the window by dropping off one nucleotide on the left and adding one on
the right.

Re-write `61skewer.py` as `62skewer.py` using the more efficient algorithm and
then calculate GC-skew and GC composition in 1000 nt windows in the E.coli
genome.

For debugging purposes you might find it very useful to write the program
twice: once using the wasteful strategy in `61skewer.py` and once using the
faster algorithm. When making performance optimizations it's easy to make
mistakes. Having a simpler solution helps debug the more difficult problem.

If you're so inclined, try timing the simple and fast algorithms with the
`time` program. Use various window sizes to see how much that affects compute
time. Your command line might look like the following. Here, it is assumed your
program takes 2 arguments: (1) the sequence file (here, soft-linked because the
name is so long an (2) the value of 1000 for the window size.

```
time python3 62skewer.py ecoli.fa.gz 1000
```

Here's what I get for the time difference between the slow and fast algorithms.
How do I know they get the same output? By `diff` or `sum` of course.

| Size | Slow | Fast |
|:----:|:----:|:----:|
|   10 | 4.27 | 3.50 |
|  100 | 5.35 | 3.61 |
| 1000 | 15.3 | 3.65 |
| 2000 | 26.3 | 3.81 |
| 3000 | 36.1 | 3.79 |
| 9000 |      | 3.88 |

### 63dust.py ###

Prior to doing sequence searches, people often mask low complexity sequence to
prevent finding huge numbers of meaningless alignments. One of the common
programs that does this task is called `dust`. Write a python version.

+ Input: multi-FASTA file of DNA
+ Output: multi-FASTA file of DNA with low complexity regions masked
+ Change all low-complexity regions to 'N' in the output
+ Provide parameters for fasta file, window size, and entropy

Your command line should look like the one below, provided you soft-linked the
FASTA file and defined the window size as 20 and entropy threshold at 1.4.

```
python3 63dust.py ecoli.fa.gz 20 1.4
```

Your output should look like this provided you wrapped the lines at 60
characters (wrapping is like translation: it skips by the window size).

```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGNNNNNNNNNNNNNNNNNNNNNNNCTTAGG
TCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTAC...
```

Hint: You cannot edit strings. You will therefore need to create a copy of your
sequence as a list. When you find windows of sequence below the entropy
threshold, convert the region of the list into Ns.

### 64profinder.py ###

Write a program that reports the protein sequences of putative coding genes in
DNA sequences.

+ Input: multi-FASTA file of DNA
+ Output: multi-FASTA file of proteins
+ Must perform a six-frame translation
+ Proteins must be at least 100 amino acids long
+ Proteins must start with 'M' and end with '*'
+ Deflines must have unique identifiers

The command line should look something like this.

```
python3 64profinder.py ecoli.fa.gz 100
```

In order to complete this program, you will have to completely fill out your
`dogma.translate()` function with all 64 codons. Yes, this is laborious, but
you only need to do it once.

The output should eventually look like this.

```
>NC_000913.3-prot-0
MRVLKFGGTSVANAERFLRVADILESNARQGQVATVLSAPAKITNHLVAMIEKTISGQDALPNISDAERIFAEL...
>NC_000913.3-prot-1
MKTASDCQQSKDSENNACHQRGKIKRKTQGAGNGVRLNSAENYAIGDEQKDGEQNAHPAHPQPARHIPCRSATK...
```

### 65transmembrane.py ###

Write a program that predicts which proteins in a proteome are transmembrane.
Transmembrane proteins are characterized by having:

+ a hydrophobic signal peptide near the N-terminus
+ other hydrophobic regions to cross the plasma membrane

Hydrophobicity can be measured in many ways. We'll use Kyte-Doolittle for its
historical importance.

https://en.wikipedia.org/wiki/Hydrophilicity_plot

Here are the specifics of what the program is looking for in each sequence

+ signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
+ transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa
+ no prolines in either hydrophobic region

For the E.coli proteome, your output should look something like this:

```
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str
NP_414568.1 lipoprotein signal peptidase [Escherichia coli s
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Esch
NP_414607.1 DedA family protein YabI [Escherichia coli str.
NP_414609.1 thiamine ABC transporter membrane subunit [Esche
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr.
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia
NP_414695.1 iron(III) hydroxamate ABC transporter membrane s
NP_414699.1 PF03458 family protein YadS [Escherichia coli st
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str
```
