Unit 7: Executables
===================

## Contents ##

+ [Interpreter Directive](#interpreter-directive)
+ [Executable Permissions](#executable-permissions)
+ [Executable PATH](#executable-path)
+ [Library PATH](#library-path)
+ [Homework](#homework)

Programs like `grep` and `ls` are not preceded by the word `python3`. In order
for a Python program to act like other Unix executables, it needs three things.

1. Interpreter directive
2. Executable permissions
3. Executable PATH

### Interpreter Directive ###

The interpreter directive is the first line of a program. It must be formatted
_exactly_ as follows. Pay specific attention to the lack of spaces. The only
space is between the words `env` and `python3`.

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
drwxrwxr-x 10 ian ian 4096 Feb 17 17:45 mcb185_homework/
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

One last note about permissions. Not all file systems have the same ideas when
it comes to file permissions. Mac and Unix generally play well together, but
not always with Windows. If you get a file from a flash drive, it will
generally have all permissions on (i.e. `777`). When working with two different
operating systems on the same file system, sometimes all of the permissions
will get set to `000`, meaning no access, even by you. If this happens, you can
reset your permission as `644` or whatever your preference is with `chmod`.

### Executable PATH ###

When you type `ls` at the command line, the shell needs to find the `ls`
program somewhere in your file system. To find out the actual location of the
program, use the `which` command. You will find that `ls` and `python3` are in
different places.

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
ln -s ~/Code/mcb185_homework/01hello.py ./hello
```

Since `hello` has an interpreter directive and executable permission, you can
now run it as an executable or as input to python.

```
python3 hello
./hello
```

We aren't quite done. You can't run `hello` without using the whole path
(that's why there is a `./` on the front of the command).

```
cd
~/Code/bin/hello  # works
hello             # fails
```

The last part is to edit your PATH. Let's look at it now.

```
printenv PATH
```

This is a colon-delimited list of directories. This is where the shell looks
for executables. Your `Code/bin` isn't there, so we have to add it to your
login script. Edit your login script (.bashrc or .zshrc) to include:

```
export PATH=$PATH:$HOME/Code/bin
```

This appends your `Code/bin` to the end of whatever was already in `PATH`. Open
a new terminal and now you can `hello` from anywhere you like.

------------------------------------------------------------------------------

## Library Path ##

For programs that import custom libraries (i.e. libraries not distributed with
python), you may have to create a library path.

Library paths work _exactly_ like executable path. Instead of PATH, we need to
change PYTHONPATH.

Edit your login script to include a `lib` directory.

```
export PYTHONPATH=$HOME/Code/lib
```

Now make the directory and symbolically link in the libraries you frequently
use.

```
mkdir ~/Code/lib
cd ~/Code/lib
ln -s ../MCB185/src/mcb185.py .
ln -s ../mcb185_homework/sequence.py .
```

Now your executable programs can access your custom libraries.

------------------------------------------------------------------------------

## Homework ##

Make some of your previous programs (e.g. `46dust.py`) into executables.
