Unit 1: Linux
=============

## Contents ##

+ [No Copy-Paste](#no-copy-paste)
+ [Shortcuts](#shortcuts)
    + [Tilde Expansion](#tilde-expansion)
    + [Tab Completion](#tab-completion)
    + [Up Arrow](#up-arrow)
    + [Wildcards](#wildcards)
+ [Environment Variables](#environment-variables)
    + [10env.sh](#10envsh)
+ [Viewing files](#viewing-files)
+ [Absolute and Relative Paths](#absolute-and-relative-paths)
    + [Review](#review)
    + [Practice](#practice)
+ [stdout, stdin, stderr](#stdout-stdin-stderr)
+ [Creating and Modifying Files](#creating-and-modifying-files)
    + [Moving and Renaming](#moving-and-renaming)
    + [Copying](#copying)
    + [Comparing](#comparing)
    + [Directories](#directories)
+ [Compression](#compression)
+ [Soft Links](#soft-links)
+ [Extracting Text](#extracting-text)
    + [cut, sort, and uniq](#cut-sort-and-uniq)
    + [grep](#grep)
+ [Shell Scripting](#shell-scripting)
+ [Shell Customization](#shell-customization)
+ [Homework](#homework)
    + [13spellingbee.sh](#13spellingbeesh)

------------------------------------------------------------------------------

## No Copy-Paste ##

There are a lot of commands to type in this unit and throughout the course. Do
not copy-paste any of the lines shown. One of the goals of this course is for
you to gain expertise and confidence with the CLI. Typing will help you improve
your CLI skills.

------------------------------------------------------------------------------

## Shortcuts ##

Typing is bad for your health. Seriously, if you type all day, you will end up
with a repetitive stress injury. Don't type for hours at a time. Make sure you
schedule breaks. Unix has several ways to save your fingers (that does not
involve copy-paste).

### Tilde Expansion ###

Your home directory is such an important place that Linux has a shortcut. It's
the tilde `~` character, which is probably at the top left of your keyboard.
When you type the tilde followed by a path, the tilde expands to the location
of your home directory.

```
cd ~/Code
pwd
```

### Tab Completion ###

Probably the most important finger saver in Linux is **tab completion**. When
you hit the tab key, the shell completes the rest of the word for you if it can
guess what you mean. Try typing `his` and then the tab key.

```
his
```

This fills in the word `history`, which is the name of a Unix command. Hit
return and you will see all the commands you have typed in this terminal.

### Up Arrow ###

Instead of re-typing long commands, you can go backwards through your command
history with the up-arrow. Try hitting the up-arrow several times and you'll
backtrack through all the commands you've typed. Use the left and right arrows
to position the cursor if you want to edit parts of the line. To get out of
this, and many other situations, type Control-C. That is, hit the control key
and then the letter "c" (not uppercase). In text, Control-C is abbreviated ^C
with a capital letter even though it's lowercase.

After using the up arrow, you may want to jump to the start or end of a line to
modify it. Use Control-A to get to the start and Control-E for the end.

+ ^C break out of what I'm doing
+ ^A start of CLI
+ ^E end of CLI

### Wildcards ###

One of the most useful time-saving tricks in the shell is the use of the `*`
character as a wildcard. The `*` character matches missing characters if it
can. We'll see this a lot later. The first line below lists your Code
directory. The second line lists all of the items in your Code directory
(performs `ls` on `MCB185`, `mcb185_homework`, and anything else in there). The
third line lists all of the markdown files in the MCB185 directory (markdown
files use the `.md` suffix).

```
ls ~/Code
ls ~/Code/*
ls ~/Code/MCB185/*.md
```

### Aliases ###

Another great way to save keystrokes is to create aliases for your favorite
commands. See the section on Shell Customization.

------------------------------------------------------------------------------

## Environment Variables ##

The shell defines various variables which are called _shell variables_ or
_environment variables_. For example, the `USER` variable contains your user
name, `HOME` contains the path to your home directory, `SHELL` contains the
path to your shell, and `PWD` contains the focus of your terminal. You can
examine the contents of a variable with the `printenv` command.

```
printenv USER
printenv HOME
```

If you want to see all your environment variables, use the `printenv` command
without any arguments.

```
printenv
```

As we saw last unit, the `echo` command writes stuff to your terminal.

```
echo "hello partner"
```

Echo can also report what's in environment variables. In order to dereference
the contents of a variable, you need to put a `$` on the front.

```
echo $HOME
```

You can mix static text with variables as shown below.

```
echo "Hello $USER, your home directory is: $HOME"
```

### 10env.sh ###

Create a new file called `10env.sh` and open it in your programming editor.
Enter the following contents.

```
echo "user: $USER"
echo "home: $HOME"
echo "shell: $SHELL"
echo "pwd: $PWD"
echo "path: $PATH"
```

Save the file. If you're using a Windows-based editor it may have defaulted to
inserting Windows-style line endings (CRLF) instead of Unix-style line endings
(LF). Make sure you have Unix line endings. In Notepad++, look at the bottom of
your screen. If it shows "Windows (CRLF)", click it and change to Unix (LF).
Run the script as follows:

```
sh 10env.sh
```

------------------------------------------------------------------------------

## Viewing Files ##

The most common programs for viewing files are these:

+ `cat` - dump the contents of files
+ `head` - print the first 10 lines of a file
+ `tail` - print the last 10 lines of a file
+ `more` - page through a file
+ `less` - page through a file with more control
+ `zless` - like `less` but works with compressed files

Let's give them a test drive.

```
cd ~/Code/MCB185
cat README.md
```

You can display multiple files with the wildcard. Here's how to dump all of
the markdown files in the directory.

```
cat *.md
```

The `head` and `tail` programs show 10 lines of text at the top or bottom of a
file.

```
head README.md
tail README.md
```

If you want more or less lines, just add the number of lines after a dash.

```
head -5 README.md
tail -15 README.md
```

To read a file one page at a time, use `more` or `less`. Use the "f" and "b"
keys to move forward or backward one page. You can also use the spacebar to
move forward one page. To quit the program, use the "q" key.

```
more README.md
less REAMDE.md
zless data/GCF_000005845.2_ASM584v2_genomic.fna.gz
```

Most Unix programs have descriptive names or initialisms. `cat` is short for
catenate. `head` and `tail` are pretty self-explanatory. `more` shows you more
of a file. `less` does more than `more` because sometimes less is more (Unix
culture is full of puns). Compressed files often have the letter "z" associated
with them, so `zless` makes sense as a variant of `less` that works with
compressed files.

------------------------------------------------------------------------------

## Absolute and Relative Paths ##

When you open a terminal application, the focus of your shell begins in your
home directory. Let's verify this. Open a new terminal and use the `pwd`
command to print your working directory.

```
pwd
```

The `pwd` program reports the "path" to your location. A "path" is a chain of
directories, separated by forward slashes, optionally ending in a file. So
`/home/username/Code` is a path as is `/home/username/Code/MCB185/README.md`
(the second example ends in a file). Every path that begins with a slash is an
"absolute path". A "relative path" does not start with a slash. For example,
`Code/MCB185` is a relative path to a directory and `Code/MCB185/README.md` is
a relative path to a file.

Starting from your home directory, use `less` to display the `README.md` above.
Do this both with an absolute path and a relative path. Tilde provides the
absolute path.

```
less ~/Code/MCB185/README.md   # absolute
less Code/MCB185/README.md     # relative
```

Now change directory to the `MCB185` directory and display the file again using
both absolute and relative paths.

```
cd Code/MCB185
less ~/Code/MCB185/README.md   # absolute
less README.md                 # relative
```

The `.` character represents your current directory. So these two commands are
equivalent.

```
less README.md                 # relative
less ./README.md               # relative
```

The `..` token represents the parent directory. Change directory to `data` and
once again read the same file using both absolute and relative paths.

```
cd data
less ~/Code/MCB185/README.md   # absolute
less ../README.md              # relative
```

### Review ###

+ any path that begins with the filesystem root `/` is an absolute path
+ paths that begin with the tilde shortcut `~/` are also absolute
+ paths that do not begin with `/` are relative paths
+ `.` and `..` are relative paths to your current and parent directories
+ paths in environment variables may be absolute or relative

Here are some examples

+ `/bin` absolute path
+ `$HOME/Code` absolute path (the `/` is in the `$HOME` variable)
+ `~/Code` absolute path (`~` is an absolute path to your home directory)
+ `REAMDE.md` relative path to file in current directory
+ `./README.md` also relative path to file in current directory
+ `../README.md` relative path to file in parent directory

### Practice ###

Change directory to your home using one of these methods

```
cd
cd ~
cd $HOME
```

List the contents of your `mcb185_homework` directory and also the `MCB185`
directory using a single command and relative paths. Use tab-completion after
'C' and also after 'm' or 'M'.

```
ls Code/mcb185_homework Code/MCB185
```

Change directory to your homework directory and list the contents of the MCB185
data directory. Use tab completion and relative paths with 'M' and 'd'.

```
cd Code/mcb185_homework
ls ../MCB185/data
```

Change to your MCB185 data directory using absolute path. Verify with `pwd`. Go
back to your home directory using relative paths and verify.

```
cd ~/Code/MCB185/data
pwd
cd ../../..
pwd
```

------------------------------------------------------------------------------

## stdout, stdin, stderr ##

When you issue commands like `ls`, the output that is sent to your terminal is
called Standard Output (stdout). Output doesn't have to go to your terminal.
You can choose to send it to a file or to another program.

The `>` operator re-directs stdout to a file. Let's try that with the `ls`
command.

```
cd ~
ls Code/MCB185
ls Code/MCB185 > foo
```

Notice that the second `ls` command didn't print anything to the terminal.
That's because the contents are in the file "foo". You can dump those out to
the terminal with `cat`.

```
cat foo
```

Instead of sending stdout to a file, let's pipe it to another command. Here,
the stdout of `ls` will be sent to the Standard Input (stdin) of the word
counting program `wc` via the pipe `|` operator.

```
ls Code/MCB185 | wc
```

Some programs, like `wc` can read from both stdin and file.

```
wc foo
```

So `ls > foo` followed by `wc foo` does the same thing as `ls | wc` without
having any intermediate file. Unix pipes are a very powerful way to chain
programs to each other.

There is also the `<` operator. This sends standard input (stdin) from a file
to a program. The keyboard is the usual source of stdin.

```
wc < foo
```

What do you think this does?

```
wc < foo > bar
```

Here, the contents of the file `foo` are sent to `wc` as stdin, and then `wc`
sends its stdout to the file `bar`, which contains the `wc` output.

+ `>` sends the stdout of a program to a file
+ `<` sends the contents of a file to the stdin of a program
+ `|` connects the stdout of one program to the stdin in of another

In addition to stdin and stdout, there is another stream of data called
Standard Error (stderr). This is meant to be used for error messages or logging
messages rather than data. Provided you don't have a file named `crap` on your
computer, the `ls` command below will report an error to your terminal. Since
there was no stdout, the file `bar` is empty. You can verify that `bar` is
empty with any of the file reading tools already introduced or `ls -l` which
shows a longer listing of file attributes, including a `0` for the size of
`bar`.

```
ls crap > bar
ls -l
```

------------------------------------------------------------------------------

## Creating and Modifying Files ##

### nano ###

There are a number of ways to create a new file in Linux. The `touch` command,
which we saw last unit, will create an empty file. As we just saw, you can also
create files by re-directing stdout using `>`. If you need to make quick edits
to a file, you will find the `nano` program useful. This is a terminal-based
text editor that allows you to create new files or edit existing files. Let's
create a new file called `baz` using `nano`.

```
nano baz
```

Start typing and you will see text appear on your screen. Write a few lines of
bad poetry. Move the cursor with the arrow keys. The bottom of the screen shows
some of the control keys used to interact with `nano` . To write the file, hit
^O (that means hold the control key down and type lowercase "o"). Hit the
return key to confirm and then exit the program with ^X. Display the file with
any of the usual programs like `cat`, `head`, `less`, etc.

```
head baz
```

### Moving and Renaming ###

The `mv` command is used to both rename and move files. Let's first rename your
`baz` file to `poetry.txt`.

```
mv baz poetry.txt
```

Next, let's use `mv` to move your poetry into your homework directory.

```
mv poetery.txt Code/mcb185_homework
```

If that last line gave you an error message ending with "No such file or
directory" it's because you did one of two things.

1. You copy-pasted the line
2. You typed the whole line verbatim

The reason for the error is that `poetery` has been misspelled.

If you copy-pasted, consider dropping the course. You have been told multiple
times not to copy-paste and your stubborn laziness or inability to seek help
will be a hindrance moving on.

If you typed the whole path, you are congratulated for your amazing attention
to detail. Also you're acting like a stupid robot. Hopefully you can break of
that mindset.

If you noticed the misspelling and continued to type out the whole command
without using tab-completion, you're a CLI novice. Don't worry, we all start
there.

Moving onward, make sure that your homework repo contains your poetry file and
that everything is spelled correctly.

```
ls Code/mcb185_homework
```

### Copying ###

The `cp` command is used to make a copy of a file. Let's make an additional
copy of the poetry in your homework directory back in your home directory. The
command line below reads as "copy the poetry.txt file from my homework
directory to my current location", where the dot is your current location. It's
easy to miss the dot, which is why there is a line below pointing it out. You
now have two files with the exact same names and file contents, but in two
different locations.

```
cp Code/mcb185_homework/poetry.txt .
# don't type this line, look here  ^
```

### Comparing ###

If you do a long listing, you will see that both files have the same size.

```
ls -l poetry.txt Code/mcb185_homewor/poetry.txt
```

But do they have the exact same contents? They should, since you just made
copies, but how would you verify that? Edit `~/poetry.txt` in `nano` and change
just one character. While the file sizes remain the same, their contents are
now different. To see the differences between two files, use `diff`.

```
diff poetry.txt Codes/mcb185_homework/poetry.txt
```

You will see a report showing exactly which lines are different from each
other. While `diff` is great for comparing small text files, you wouldn't use
it to validate that two compressed genome sequence files have the same
sequence. For that, you would use `sum` to perform a checksum, which is a
pseudo-unique number whose value is based on the entire file contents.

```
sum poetry.txt Code/mcb185_homework/potery.txt
```

The first column is the checksum value. Since they are different, the file
contents are different. Is it possible for two different files to share the
exact same checksum? Yes, but it's unlikely. For example, the probability that
two files have the same MD5 checksum is about 1.47e-29.

### Directories ###

Let's tidy up a bit by making a directory with `mkdir` and then moving the
files from the previous sections into that directory. Notice that the `mv`
command can take multiple arguments. The last argument is the directory and the
previous ones are files.

```
mkdir stuff
mv foo bar poetry.txt stuff
ls stuff
```

To remove a directory, use the `rmdir` command. However, `rmdir` will not
remove a directory if it has any files in it. So this command will fail. Try it
anyway.

```
rmdir stuff
```

To remove all of the files in `stuff` we could do the following very dangerous
operation.

```
rm stuff/ *
```

The reason this is dangerous is that there is an accidental space between
`stuff/` and the `*`. The way this command is interpreted is "remove the file
called stuff and also everything else". `stuff` is a directory, not a file, so
the first argument is an error. However, `*` matches everything in the current
working directory, so all your files will get deleted!

Instead, `cd` into `stuff` and then remove everything inside. Then leave the
directory and remove it.

```
cd stuff
rm *
cd ..
rmdir stuff
```

------------------------------------------------------------------------------

## Compression ##

Data files can be very large. For this reason, they are often compressed.
However, once compressed, they don't look like normal text files.

From your homework directory, `head` the compressed GFF of E.coli, which you
can find in the MCB185 data directory. Files that end in `.gz` have been
compressed with `gzip`.

```
cd ~/Code/mcb185_homework
head ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz
```

Make a copy of this file in your current directory. While we could `cp` the
file, let's so something more fun. We'll use `cat` to stream the file to
stdout, and `>` to redirect that to a simpler file name.

```
cat ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz > ecoli.gff.gz
```

Examine its size with `ls -lh`, which is about 430K.

```
ls -lh
```

Gzipped files can be uncompressed with `gunzip`. Do that and inspect the file
size. 2.5M is a lot bigger than 430K. While neither 2.5M nor 430K is very
large, some data files are huge, and the ~6-fold compression observed here can
be very useful.

```
gunzip ecoli.gff.gz
ls -lh
```

When you `gzip` or `gunzip` a file, the default behavior is to create a new
file and destroy the old one. You have a file called `ecoli.gff` but the
original file `ecoli.gff.gz` is gone. If you `gzip` the `ecoli.gff` file, it
will become `ecoli.gff.gz`, destroying the uncompressed one in the process. If
you want to keep the original file, simply pass the `-k` parameter to `gzip` or
`gunzip`.

```
gunzip -k ecoli.gff.gz
ls -lh
```

Large data files are often kept compressed and never "inflated". To view a
compressed file, use `zless` instead of `less` (some versions of `less` will
actually read compressed files - try it and see).

```
zless ecoli.gff.gz
```

To use tools like `wc` on compressed files, stream them to stdout using the
`-c` flag and then pipe that to `wc`.

```
gunzip -c ecoli.gff.gz | wc
```

Now that we know we don't need uncompressed files, get rid of `ecoli.gff`.

```
rm ecoli.gff
```

You also don't need multiple copies of identical data on your computer. You
should also get rid of `ecoli.gff.gz` and always use the original file.

```
rm ecoli.gff.gz
```

------------------------------------------------------------------------------

## Soft Links ##

Even though tab-completion exists, files names like
`MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz` can be painful to look
at. Wouldn't it be nice if we could just call it something simpler like
`ecoli.gff.gz`? Of course we can, and we do this with soft links (also called
symbolic links or short cuts). Navigate to your homework directory and then
use `ln -s` to create a symbolic link.

```
cd ~/Code/mcb185_homework
ln -s ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz ./ecoli.gff.gz
```

The `ln` command above shows the use of relative paths but you can also use
absolute paths. Let's examine the file with `zless`. It looks just like the
original because it **is** the original.

```
zless ecoli.gff.gz
```

If you remove the symbolic link, it does not remove the original file.

```
rm ecoli.gff.gz
ls ~/Code/MCB185/data
```

+ Do not make duplicates of data files
+ Do not create uncompressed versions of data files
+ Do make soft links to data files and give them convenient names

------------------------------------------------------------------------------

## Extracting Text ##

Create a soft link to the compressed gff file from the last section and examine
it with `zless`.

GFF files are tab-delimited text files that contain information about
sequences. Like many file formats, lines that begin with `#` are comments (NOT
hashtags) and are not considered part of the data, though they may contain some
meta-data. Each tab-delimited field has a specific type of information. For
example, fields 4 and 5 contain the coordinates of a sequence feature, and
field 3 reports what kind of feature it is.

### cut, sort, and uniq ###

Let's extract all of the features using `cut`. In the command below, `-f 3`
tells `cut` we want to extract column 3. By default `cut` splits fields on tab
characters, which is what gff uses. If the file used spaces or commas, we would
have to change the delimiter to match the file.

```
gunzip -c ecoli.gff.gz | cut -f 3
```

Running that command, you should see a lot of "gene" and "CDS" features. There
are other things in there too. How many? One way to examine the output is with
`sort`.

```
gunzip -c ecoli.gff.gz | cut -f 3 | sort
```

This streamed a lot of stuff passed us too quickly to see, including a lot of
tRNAs (because the sort is alphabetical). You could try piping the output to
`less`, but paging through that would be horrible.

```
gunzip -c ecoli.gff.gz | cut -f 3 | sort | less
```

Instead, we can pass the `-u` flag to `sort`, which will restrict it to unique
text only.

```
gunzip -c ecoli.gff.gz | cut -f 3 | sort -u
```

That's better. In addition to "CDS", "gene", and "tRNA", there are other
features. However, there are also some comment lines that don't belong because
they aren't data. We can remove comments with `grep -v`. `grep` is an
incredibly powerful program that lets you search for specific patterns of text
(see more below). Here, we are only using it to skip over lines that begin with
a `#` symbol.

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort -u
```

To get the number of counts for each feature, we can pass the sorted list
through `uniq`. This program removes duplicate lines. When used with the `-c`
flag, it counts occurrences of each line.

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c
```

If you want to be really fancy and sort the list by how many of each feature
there are, you can pass the output through another `sort`. This time, we will
pass the `-n` and `-r` flags so that the sort is numeric and in reverse order.
Multiple flags can often be condensed so that `-n -r` is `-nr`.

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr
```

The output is as follows:

```
4494 gene
4337 CDS
 207 exon
 145 pseudogene
  99 ncRNA
  86 tRNA
  50 mobile_genetic_element
  48 sequence_feature
  22 rRNA
   1 region
   1 origin_of_replication
```

### grep ###

`grep` is such a powerful and useful tool that it deserves a little more
attention. Head over to `MCB185/data` where you'll find `dictionary.gz`. Did
you ever wonder which words have a double "aa" in them. Let `grep` do the work
for you.

```
cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "aa"
```

To count the number of words, you can pipe the output to `wc` or pass the `-c`
flag to `grep`. The two commands below do the same thing.

```
gunzip -c dictionary.gz | grep "aa" | wc -l
gunzip -c dictionary.gz | grep -c "aa"
```

The double-a's in those words could occur anywhere in the word. If we want only
those words that begin with double-a, we use the special `^` symbol to bind the
pattern to the start. Recall that we just saw the use of `^` when removing the
comment lines from GFF.

```
gunzip -c dictionary.gz | grep "^aa"
```

The special symbol that means "bind pattern at the end" is `$`. Here are the
words that end with double-a.

```
gunzip -c dictionary.gz | grep "aa$"
```

Another special symbol is `.` (a dot). This matches any single letter. For
example, let's look for all words that have the letter `z` one letter apart.

```
gunzip -c dictionary.gz | grep "z.z"
```

Ah, but now you're wondering about the words that have different numbers of
letters between the z's. The `*` modifier means zero or more. The following
finds all the words with any number of letters between the z's including none.

```
gunzip -c dictionary.gz | grep "z.*z"
```

To get the behavior of "one or more intervening letters" we could pipe the
previous command to another grep and remove all double-z's, but that doesn't
really do what we want.

```
gunzip -c dictionary.gz | grep "z.*z" | grep -v "zz"
```

Instead, we use `+` to mean "one or more". The "basic" regular expression
syntax requires one to backslash the `+` while the "extended" syntax (signaled
with the `-E` flag) does not. The extended version is similar to what we will
use in Python much later in the course.

```
gunzip -c dictionary.gz | grep "z.\+z"
gunzip -c dictionary.gz | grep -E "z.+z"
```

Let's play a little bit more with extended syntax. Here's an example of how you
can require the middle letters to be 3 to 4 characters long. The curly brackets
specify a range.

```
gunzip -c dictionary.gz | grep -E "z.{3,4}z"
```

You can also search for specific classes of letters. For example, let's require
that the middle letters be one or more of the vowels, a, e, i, o, or u. A
character class is created with square brackets.

```
gunzip -c dictionary.gz | grep -E "z[aeiou]+z"
```

You can also create anti-character classes by putting a `^` symbol right after
the opening bracket. Yes, `^` is used both for binding a pattern to the start
and also for creating anti-classes.

```
gunzip -c dictionary.gz | grep -E "z[^aeiou]+z"
```

------------------------------------------------------------------------------

## Shell Scripting ##

The interactive shell you're using is itself a scripting language. All the
commands you've been using can be put in a file and re-used later.

Using your favorite editor, create the following file and save it to your
homework repo as `11status.sh`.

```
date
sh 10env.sh
uname -a
python3 --version
find ~/Code -maxdepth 2 -type d
```

The output of this script will help me if you run into Linx/Python problems.
Here's an explanation of each line.

1. Reports the date
2. Runs `10env.sh` which you wrote previously
3. Reports the full name of your flavor of Unix
4. Reports your version of Python
5. Reports some information about your Code directory

Run the program to see what it outputs. If you get an error, make sure both
`10env.sh` and `11status.sh` are in your `mcb185_homework` directory.

```
sh 11status.sh
```

Save the output of the report as `12report.txt`.

```
sh 11status.sh > 12report.txt
```

------------------------------------------------------------------------------

## Shell Customization ##

When you start up a terminal, the shell usually reads a login script in your
home directory. The purpose of the login script is personalize your CLI
experience. For example, perhaps you always type `ls -F` when listing
directories and you wished that `ls` showed file types by default. You can do
that in your the login script.

The name of your login script depends on your shell.

```
echo $SHELL
```

+ `/bin/bash` - `.bashrc` or `.bash_profile` or `.profile`
+ `/bin/zsh` - `.zshrc`

Note the leading `.` on the filenames above. This means these files are normally
hidden. Use the `-a` flag to show all files.

```
cd
ls -a
```

If you don't see any of the files above, create one. Make sure the focus of
your terminal is your home directory. Then create the file name based on the
$SHELL. Place the following contents at the end of the file.

```
alias ls="ls -F"
```

Now, every time you give the `ls` command, you will actually be doing `ls -F`.
I type `git status` so often that I have an alias for that: `gs`.


Here are some common customizations.

```
alias ..="cd .."
alias la="ls -a"
alias ll="ls -l"
alias rm="rm -i"  # prompt user before removing file
alias cp="cp -i"  # prompt user before overwriting file
```

------------------------------------------------------------------------------

## Homework ##

To get full credit for your homework, `git push` the following files into your
`mcb185_homework` GitHub repository.

+ `10env.sh`
+ `11status.sh`
+ `12report.txt`
+ `13spellingbee.sh`

### 13spellingbee.sh ##

Have you ever seen the New York Times Spelling Bee? In this game, you are given
7 letters in the shape of a hexagon. The middle letter must be used in every
word, but the outer 6 letters can be used any number of times. Words must be at
least 4 letters long. Create a command line that solves the puzzle below and
save it as `13spellingbee.sh`. Hint: you will have to run `grep` more than
once.

```
   O
Z     N
   R
I     C
   A
```
