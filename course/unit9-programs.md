Unit 9: Programs
================

## Contents ##

+ [argparse](#argparse)
    + [Positional Arguments](#positional-arguments)
    + [Named Arguments](#named-arguments)
    + [Flags](#flags)
    + [Short and Long](#short-and-long)
+ [Executables](#executables)
    + [Interpreter Directive](#interpreter-directive)
    + [Executable Permission](#executable-permission)
    + [Executable PATH](#executable-path)
+ [Library Path](#library-path)
+ [Homework](#homework)
    + [90dust.py](#90dustpy)
    + [91translate.py](#91translatepy)
    + [92variants.py](#92variantspy)

------------------------------------------------------------------------------

## argparse ##

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
`90dust.py` and type in the following:

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

Lines 5 adds a positional argument for the window size and specifies that it is
an integer.

Line 6 adds a positional argument for the entropy threshold, which is a float.

Line 7 creates the `arg` object by harvesting the values on the command line
and assigning them to various properties. For example, `arg.file` contains the
path to the FASTA file. Similarly, `arg.size` is the window size and
`arg.entropy` is the entropy threshold.

Line 8 is just something that will print when we give the program the proper
number and type of arguments.

Try running the program `python3 90dust.py` and observe the usage statement.

```
usage: 90dust.py [-h] file size entropy
90dust.py: error: the following arguments are required: file, size, entropy
```

If you don't give the program any arguments, it responds with a brief usage
statement telling you what it requires, in this case an optional argument `-h`
and 3 required positional arguments: `file`, `size`, and `entropy`. To get more
information, type `python3 90dust.py -h`. Here, the `-h` stands for help and
the usage statement provides more detail, including the final line, which tells
you that you can also get to this message with a longer version: `--help`.

```
usage: 90dust.py [-h] file size entropy

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
python3 90dust.py foo 20 1.4
```

### Named Arguments ###

The arguments for `file`, `size`, and `entropy` were all positional. That is,
there were in a strict order. In contrast, named arguments are optional and can
occur in any order. This is very much like python where the `print()` function
has positional arguments as well as optional named arguments.

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
digits of precisions, using the same formatting as f-strings.

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

Try observing the new usage statment advertising the default parameters. Also
try overriding the defaults.

```
python3 90dust.py
python3 90dust.py foo
python3 90dust.py foo --size 15 --entropy 1.2
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
python3 90dust.py foo
python3 90dust.py foo --lower
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

## Executables ##

`90dust.py` is looking like a standard Unix program with a proper CLI featuring
positional and named parameters in short and long form. However, unlike a
program like `gzip`, you have to type `python3` before and then the path to the
file. Wouldn't it be better if you could just type `dust` from anywhere?

In order for a Python program to act like other Unix executables, it needs
three things.

1. Interpreter directive
2. Executable permissions
3. Executable PATH

### Interpreter Directive ###

The interpreter directive is the first line of a program. It must be formatted
_exactly_ as follows. Pay specific attention to the lack of spaces. The only
space is between the words `env` and `python3`. Insert this into the first line
of `90dust.py`.

```
#!/usr/bin/env python3
```

### Executable Permission ###

A file can have 3 kinds of permissions: read, write, and execute. These are
abbreviated as `rwx`. If a file has read permissions, you can view it. If it
has write permissions, you can edit it, which includes deleting it. If it has
execute permissions, you can run it as a program.

Directories are special kinds of files that also have the same permissions.
Here, read means you can view the files in the directory. Write means you can
add or delete files in the directory. Execute means you can `cd` into the
directory.

Generally, you would like to be able to read, write, and execute the
directories you own. But this isn't always true of files. You may have
downloaded some important data and want to make sure you can't modify or delete
it. Most data files should be read-only.

Permissions allow you to modify what actions can be taken, and by whom. In
addition to having 3 types of permissions (read, write, execute), every file
also has 3 types of people that can access it: the owner (you), the group you
belong to (e.g. a laboratory), or the public (everyone else who has access to
the computer).

Let's examine the file permissions on the directories and files you
currently have.

```
cd ~/Code
ls -lF
```

You should see something like the following:

```
drwxrwxr-x  7 ian ian 4096 Feb 15 16:12 MCB185/
drwxrwxr-x 10 ian ian 4096 Feb 17 17:45 mcb185te/
```

Let's break down what's happening with these arcane symbols. The first letter
is `d` which indicates that the file is a directory. We can also see this
because of the trailing slash from the `ls -F`. The next 9 characters are 3
triplets.

+ rwx the first triplet are your permissions
+ rwx the second triplet are group permissions
+ r-x the third triplet are public permissions

You may read, write, and execute the directory. That is, you have permission to
`ls` the directory, `rm` files in the directory, and `cd` into the directory.
Users who belong to your group can also read, write enter your directories, but
the "public" can only read or enter your directories. Note that depending on
how your Linux was set up, you may have slightly different permissions.

Let's take a look at the permissions of `00helloworld.py`.

```
cd ~/Code/mcb185_homework
ls -lF 01hello.py
```

On Lubuntu, this is what I found.

```
-rw-rw-r-- 1 ian ian 20 Dec 30 11:00 mcb185_homework/01hello.py
```

After the leading dash, there are 3 triplets of symbols. The first triplet
shows user permissions `rw-`. I have read and write permission but not execute.
The next triplets are for group and public. Both have read permission, but not
write or execute. Let's first turn on all permissions for everyone using the
`chmod` command and then list again. The `777` below will be explained shortly.

```
chmod 777 01hello.py
ls -lF 01hello.py
```

Notice that you can now see `rwx` for owner, group, and public. This means that
everyone has read, write, and execute permissions. That's probably not a good
idea. Let's turn all permissions off.

```
chmod 000 01hello.py
less 01hello.py
```

Now, even you don't have permission to view the file (which is why the `less`
failed). The `chmod` command has two different syntaxes. The more human
readable one looks like this.

```
chmod u+r 01hello.py
ls -lF 01hello.py
```

The `u+r` reads as: "(u) user (+) add (r) read permission". The less readable
`chmod` format assigns all parameters in octal format simultaneously. Once you
understand how it works, it's much easier.

+ 4 is read permission
+ 2 is write permission
+ 1 is execute permission
+ 0 is no permissions

Every number from 0 to 7 results in a unique set of permission.

| Read | Write | Exec | Sum | Meaning
|:----:|:-----:|:----:|:---:|:--------
|   4  |   0   |   0  |  4  | only reading allowed
|   4  |   2   |   0  |  6  | reading and writing allowed
|   4  |   2   |   1  |  7  | reading, writing, and executing allowed
|   4  |   0   |   1  |  5  | reading and executing allowed
|   0  |   0   |   0  |  0  | nothing allowed

Here are some useful permission sets:

+ 600 your private diary (only you can read and write)
+ 644 your source code (you can read and write, others can read)
+ 755 your programs (like above, but executable)
+ 755 your directories (others can read, but not delete your files)
+ 444 data files (everyone can read, nobody can write)

Let's set the permissions on `01hello.py` to the most appropriate set
using the octal format.

```
chmod 644 01hello.py
```

Let's also set the permission of your `90dust.py` program to be executable,
since that was part of the original goal.

```
chmod 755 90dust.py
```

One last note about permissions. Not all file systems have the same ideas when
it comes to file permissions. Mac and Unix generally play well together, but
not always with Windows. If you get a file from a flash drive, it will
generally have all permissions on (i.e. `777`). When working with two different
operating systems on the same file system, sometimes all of the permissions
will get set to `000`, meaning no access, even by you. If this happens, you can
reset your permission as `644` or whatever your preference is with `chmod`.

### Executable PATH ###

When you type `ls` at the command line, the shell needs to find the program
somewhere in your file system. To find out the actual location of the program,
use the `which` command. You will find that `ls` and `python3` are in different
places.

```
which ls
which python3
```

Programs aren't all stored in the same place. Some are in `/bin`, while others
are in `/usr/bin`, `/sbin`, or elsewhere. By default, you don't have permission
to put your programs in these reserved locations. In order to make your
personal programs behave like proper Unix programs, we have to create a place
to store your programs and add that to the executable path.

The traditional place to put executable files is in a directory called `bin`.
We'll follow that tradition inside the `Code` directory. Instead of moving
programs into `Code/bin`, we'll link them in symbolically so that they appear
to be there, even though they are stored in `mcb185_homework`.

```
mkdir ~/Code/bin
cd ~/Code/bin
ln -s ~/Code/mcb185_homework/90dust.py ./dust
```

Since `dust` has an interpreter directive and executable permission, you can
now run it as an executable or as input to python.

```
python3 dust
./dust
```

We aren't quite done. You can't run `dust` without using the whole path (that's
why there is a `./` on the front of the command).

```
cd
~/Code/bin/dust  # works
dust             # fails
```

The last part is to edit your PATH. Let's look at it now.

```
printenv PATH
```

This is a colon-delimited list of directories. This is where the shell looks
for executables. Your `Code/bin` isn't there, so we have to add it to your
login script. Edit your logging script to include:

```
export PATH=$PATH:$HOME/Code/bin
```

This appends your `Code/bin` to the end of whatever was already in `PATH`. Open
a new terminal and now you can `dust` from anywhere you like.

------------------------------------------------------------------------------

## Library Path ##

For your homework, you will have to compelte the rest of the `90dust.py`
program. But as soon as you `import mcb185` you will get an error. You have two
choices: (1) copy-paste the `read_fasta()` from `mcb185.py` or (2) learn about
library paths. Obviously, we're going to do the second.

Library paths work _exactly_ like executable path. Instead of PATH, we need to
change PYTHONPATH.

Edit your login script to include a `lib` directory.

```
export PYTHONPATH=$HOME/Code/lib
```

Now make the directory and symbolically link in the library.

```
mkdir ~/Code/lib
cd ~/Code/lib
ln -s ../MCB185/src/mcb185.py .
```

------------------------------------------------------------------------------

## Homework ##

+ `90dust.py`
+ `91translate.py`
+ `92variants.py`

### 90dust.py ###

Finish the program. Your usage statement should look like the following

```
usage: dust [-h] [-s SIZE] [-e ENTROPY] [--lower] file

DNA entropy filter.

positional arguments:
  file                  name of fasta file

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  window size [20]
  -e ENTROPY, --entropy ENTROPY
                        entropy threshold [1.400]
  --lower               soft mask
```

After running the program on the E.coli genome (or a smaller version), the
`head` of the output should look like this if you use the `--lower` flag.

```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGtgagtaaattaaaattttattgaCTTAGG
TCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTAC
ACAACATCCATGAAACGCATTAGcaccaccattaccaccaccaTCACCATTACCACAGGT
AACGGTGCGGGCTGACGCGTacaggaaacacagaaaaaagccCGCACCTGACAGTGCGGG
CTTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGGGGCAGGTGGCCAccgtcctctctgcccccgccAAAATCACCAACCACCTGGTG
GCGATGATTGAAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
```

### 91translate.py ###

Write a program that translates transcripts. The usage statement should look
similar to the one below. If you want to, make it into a program like you did
for `dust` so that you can `translate` from anywhere.

```
usage: translate [-h] [-m MIN] [-a] file

mRNA translator.

positional arguments:
  file               fasta file of mRNAs

options:
  -h, --help         show this help message and exit
  -m MIN, --min MIN  minimum protein length [100]
  -a, --anti         also examine the anti-parallel strand
```

The program output must be a FASTA file of protein sequences. You will find a
file of C.elegans transcripts in `MCB185/data`. The first two records will look
like this.

```
>AC3.10.1 gene=WBGene00004964
MSWYSKIYVAVREYRAKHKITGWILTRCLNVLLFIQLILLWWSLYMYVTVTIGYYVQSTI
QATIYLIVGSFLFVMSMWSLAKTLFTRVGRVPERYRPSKELEDRLKAVTPMEKNRYVVEK
STPEQLAQQNTILEEMCTYCKVVVAECDQVGRLKYCYECGHIKPDRARHCSSCGKCCIKY
DHHCPWINMCVTHVNYKYFLLYIIYTSFLVYWYLLTSLEGAVRYFINQQWTDELGKFLFY
LFSFIVGGVFGYYPLGELIIFHYQLISLNETTVEQTKPALLRFDNAADYNMGKYNNFQSV
FGWGLWLCPIDSSTQDGLHFDIRYVNTQQRNRFVRIEEEPSSTQSSQSSIQ
>AC8.3.1 gene=WBGene00007075
MKPVSVFGEQMHTIHCVELENGTVKKQCLRFREYVYVNYFSISDTYEVPECNEDVYRPLN
SQVAVKKFLKEEAIPHRTLEGVRQVMEERGHHISTKQIQNAARSVRDAVVGNTGPHLSTT
EDMLKALQSQNPDRVKYWIDAKQQLHFNIFTLFPDALKLFVHGCPTVTQHERWQRKVERW
SLLDKQERKKKISEVLKKHPDGMIFASRIMVDTTFQLGDFYVTFVNGECPRFRTARSLKA
RMLPLGFFIHTTKERPNHKEFAELLRSELNLVQVAGEPRKIPCVVIDGEAALGEYAKAVD
SPCVRCDRHILTLISHNCGQNASRGAQALLFGKKVGGTFRAGLLGSFSMEEFEEKLKKCE
KRMAAPVFEWTKAN
```

### 92variants.py ###

Write a program that compares features in a GFF file to variants in a VCF file.
The usage statement should look similar to the one below.

```
usage: variants [-h] gff vcf

variant reporter

positional arguments:
  gff         GFF file
  vcf         VCF file

options:
  -h, --help  show this help message and exit
```

Your program should report the region where each variant is found. For example,
some variants might be in exons, while others are in introns. Note that because
of alternative splicing and other complexities, some variants may appear in
more than one category. List all categories a variant occurs in, and skip those
variants that don't overlap any GFF feature. Your output should look like this:

```
I       3080    intron
I       3412    intron,transcript_region
I       3425    intron,transcript_region
I       3452    intron,transcript_region
I       3452    intron,transcript_region
I       3597    intron,transcript_region
I       3769    gene,snoRNA,exon,transcript_region
I       3848    gene,snoRNA,exon,transcript_region
I       3901    gene,snoRNA,exon,transcript_region
I       4251    intron,gene,mRNA,exon,CDS,transcript_region
I       4279    intron,gene,mRNA,exon,CDS,transcript_region
I       4279    intron,gene,mRNA,exon,CDS,transcript_region
I       4357    intron,gene,mRNA,exon,CDS,transcript_region
I       4357    intron,gene,mRNA,exon,CDS,transcript_region
```
