Unit 0: Setup
=============

## Outline ##

+ Install Unix/Linux
+ Find your terminal
+ Choose a programming editor
+ Organize your home directory
+ Manage documents with Git
+ Write documentation with Markdown
+ Write your first shell script
+ Write your first Python program

------------------------------------------------------------------------------

## Unix/Linux ##

Most professional bioinformatics is done in a Unix/Linux environment. You don't
have to love Unix/Linux, but you do have to be proficient at it. The file,
`LINUX_REFERENCE.md`, contains all of the Unix/Linux commands we use in the
course.

### What's the deal with Unix vs. Linux? ###

Most people about to embark on an adventure in bioinformatics programming will
be using some flavor of Linux (e.g. Debian, Fedora, LinuxLite, Mint, Ubuntu,
etc.) and not actually Unix. Is there a difference between Linux and Unix? No
and yes. Linux was designed to be just like Unix, so from a practical
standpoint they are very similar. Despite looking the same, they share no
source code in common. The biggest difference is philosophical. Unix is a
commercial product and Linux is free open source software (FOSS). From a
philosophical perspective, they are very different.

### Where do I get Linux? ###

Before we begin, you need a command line Linux environment on your computer.
Why a CLI (command line interface) rather than a GUI (graphical user
interface)? When it comes to automating tasks, it's easier to automate text
commands than mouse clicks. Also, most computer clusters run Linux because it's
free and robust. For these reasons, most professional bioinformatics is done
with a Linux CLI. If you have any aspirations of becoming a bioinformatics
programmer, you need to become comfortable with the Linux CLI. But before we
get to that, you need some flavor of Unix/Linux.

+ Recommended
	+ Mac
	+ Windows + Cygwin
	+ Windows + Virtual Machine
	+ Install Linux on spare PC
+ Not Recommended
	+ Chromebook
	+ Git bash
	+ Windows Subsystem for Linux
	+ Raspberry Pi
	+ Remote login

### Unix on Mac ###

If your computer is a Mac, you already have Unix installed, and your specific
flavor of Unix is called Darwin. You can get to the CLI with the _Terminal_
application. However, you might not have `git` and other developer tools
installed by default. To install these, type the following in your terminal and
follow the instructions:

```
xcode-select --install
```

By default, your home directory might not be shown in your sidebar. Add it by
clicking the home-shaped icon in Finder->Settings->Sidebar. You might also
change new finder windows to open your home directory in
Finder->Settings->General.

### Windows + Cygwin ###

Cygwin is not an entire operating system but rather a terminal with POSIX
commands (POSIX is a portable standardization of Unix commands). It works great
for this course and for lots of Unix and Python tasks in general. However, some
external libraries (which we don't use in the course) may be a pain to install.

1. Go to https://www.cygwin.com
2. Download and run the installer: `setup-x86_64.exe`
3. Choose the defaults with "Next" until you get to the Download Sites
4. Choose one of the sites, and if it is slow, stop and choose another
5. Install packages by double-clicking "Skip" -> version number
	+ Interpreters - python39
	+ Devel - git
	+ Editors - nano
6. Choose "Next" and ultimately "Finish"

Launching the "Cygwin64 Terminal" brings up a typical CLI interface.

+ Your Windows C drive is mounted in Cygwin at `/cygdrive/c`
+ Your Cygwin root is mounted in Windows at `C:\cygdrive64` (by default)

The statements above might not mean anything to you right now, but they will
later.

### Windows + Virtual Machine ###

A virtual machine (VM) is a _fictional_ computer running inside your normal
Windows operating system. The virtualization _host_ software (e.g. VirtualBox)
running on the Windows PC (host) tricks the new _guest_ operating system
(Linux) into thinking it is attached to its own motherboard, CPU, keyboard,
mouse, monitor, etc.

The upside of virtualization is that it's safe and inexpensive. It's hard to
destroy data on your computer and you don't have to buy any new hardware.
VirtualBox is free software that works very well. Other popular virtualization
products include VMware and Parallels. If you want commercial support, you may
like those.

The downside of a VM is that your virtual machines will take away some RAM,
CPU, and storage from your host OS. RAM is the most critical resource because
it isn't easily shared. If you have less than 8 GB of RAM in your computer, you
will probably not want to run a VM.

On the CPU side, your programs running in a VM will typically run 1-10% slower.
You will also have to dedicate about 20 GB of hard disk space. Even with the
downsides, VMs are a great way to run Linux on your PC.

One additional complication is that your BIOS might need to be modified to run
virtual machines. Some manufacturers ship their products with virtualization
disabled. This is easily changed in BIOS. Reboot and hold down the F10 key - or
sometimes it's F1, F2, F12, or DEL to enter BIOS. Navigate to CPU (sometimes
it's in security). Enable virtualization, save changes, and reboot. If this is
causing problems or is too confusing, see Cygwin above.

There are many distributions of Linux. The most obvious differences among them
is their default desktop Graphical User Interface (GUI). Some look like
old-school Windows while others look like Mac OS, and still others offer their
own unique look and feel. Here are some recommendations for setting up your VM.

+ Linux: Lubuntu
+ VM Memory: 2 GB (or 4 GB if your computer has more than 8 GB)
+ Disk: use default types, 20G is a good amount

Make sure you read the installation directions fully. There are some
post-install customizations you might need to do. On VirtualBox these include:

+ Install the Guest Additions "CD"
+ Set up a shared clipboard if you want to copy-paste between host and VM
+ Set up a shared folder if you want Linux and Windows to share files

If you're having problems with the install or post-install, ask for help.

### Install Linux on PC ###

There are a variety of ways you can install Linux natively on your PC. You can
repartition your main SSD and dual boot, choosing Windows or Linux during
startup. You can install Linux on a spare SSD. You can even run Linux off a
flash drive. Any of these methods will give you a 100% Linux-only environment
that will take advantage of all of the CPU and memory in your machine. The main
downside is that you may accidentally destroy Windows during installation.

### Linux on Chromebook ###

Chromebooks are some of the least expensive computers you can buy.
Conveniently, Linux is built right in. Select the clock in the lower right
corner and then go to Settings->Advanced->Developers.

Scroll down to "Linux development environment" and turn it on. It takes a few
minutes to install the first time. To get to the Linux CLI, use the Terminal
application. This takes a little while to launch the first time and also after
a Chrome OS update.

I don't really recommend Chromebooks because it's not a popular platform for
professional bioinformatics work. However, they will work great for this
course.

### Git Bash on Windows ###

Git Bash is software intended for running git commands on Windows PCs using a
command line interface. It can be used for more tasks, such as Python
programming. Some programming languages are built-in (e.g. Perl) but Python is
not by default. Git Bash feels very similar to Cygwin but software installation
is slightly more complex.

### Windows Subsystem for Linux ###

The official Microsoft solution for running Linux is called the Windows
Subsystem for Linux (WSL). The upside of WSL is that it is the official
Microsoft product. Most of the time it works great. It uses less resources than
a VM, so your actual and virtual computers will be faster with WSL. The
downside of WSL is the Windows and Linux filesystems do not play well together.
When Windows programs save files in the Linux filesystem, some permissions may
get reset (meaning you can't read or write files until until you `chmod`). It
can be very annoying. As WSL matures, it may become the best way to run Linux
on Windows. From WSL, your Windows C drive is conveniently mounted at `/mnt/c`.
Finding your Linux filesystem root from Windows is not so easy.

### Raspberry Pi ###

The Raspberry Pi is an inexpensive ($50-100) single board computer that is
about the size of a deck of cards. You can also get one built into a slim
keyboard. They use Linux as their OS. You just need to provide a mouse,
keyboard, and monitor. They work great as a learning platform, but can be
limiting later on as some useful bioinformatics software isn't pre-compiled for
the Pi. Old PCs can usually be purchased for the same price and will work much
better.

### Remote Login ###

Another way to work with Linux is to use your computer as a terminal to another
computer located somewhere on the Internet. This might be part of a larger
cloud computing service (e.g. Google, Amazon, etc.) or a computer located at
your school. The downside here is that you'll need a network connection and
you'll need to figure out how to edit remote files from your favorite desktop
editor (unless you like terminal-based editors link `nano`).

------------------------------------------------------------------------------

## Terminal ##

The terminal is how you interact with the Unix/Linux command line interface
(CLI).

There are many terminal applications. Generally, it doesn't matter which one
you use. It's sort of like choosing between Firefox and Chrome: they look a
little different, but both let you browse the Internet. Find a terminal
application on your computer. The name might be 'Terminal', 'xterm', 'Qterm' or
something with 'term' in it somewhere. Create a shortcut in your dock/launchbar
so you can access it quickly.

Every terminal has a command line interpreter called a shell. There are many
flavors of shell with names like `sh`, `bash`, `zsh`, `csh`, `ksh`, etc. The
shell interprets what you type on the command line. For example, when you type
`ls` followed by return, the shell interprets that to mean you want to run the
`ls` program. The shell is actually a programming language. The various flavors
of shell are like different dialects. We won't be using many features of shell
programming in this course, so the choice of shell doesn't really matter.

Each time you interact with the CLI, you give it a named _command_. Commands
are sometimes called _programs_ or _tools_. Each command does some useful
tasks. For example, the command `date` reports the current date. Each time you
see a block of text as shown below, this means to type the line and end with
the return key. Try that now in your terminal.

```
date
```

Most commands have additional behaviors that are invoked with "command line
options", which are sometimes called "flags" or "parameters". These options are
sometimes single dashes followed by single letters, like `-I`, and sometimes
double dashes with longer tokens, like `--iso-8601`. Many Linux programs like
`date` support both long and short options. Both of these lines do the exact
same thing.

```
date -I
date --iso-8601
```

Some commands and options take "arguments". That is, you follow the command or
option with more words. Let's tell the `date` command we want to display the
date in Coordianted Universal Time (UTC) at a point back in time. The `-u` flag
specifies that we want UTC. Note that we prefer to call `-u` a _flag_ because
its only behavior is to be on or off (the flag is raised or not). The `-d`
parameter has an argument of `2020-03-15`, which is our previous moment in
time.

```
date -u -d 2020-03-15
date --utc --date 2020-03-15
```

The `date` command itself can also take an argument, which has an arcane
formatting syntax. Let's say we want the typical US-style month/day/year
format. `%m` stands for month, `%d` stands for day, and `%Y` is the 4 digit
version of year (lowercase y for the 2 digit version).

```
date "+%m/%d/%Y"
```

------------------------------------------------------------------------------

## Programming Editor ##

You will spend a lot of time using a text editor designed for programming. A
text editor is not a word processor. We won't be using MS Word or Google Docs
ever. Popular text editors include:

+ BBedit (Mac only)
+ Notepad++ (Windows only)
+ Caret (Chromebook only)
+ Sublime Text
+ Atom

If you're using a VM, the Linux distribution will come bundled with an
acceptable editor like FeatherPad or gedit. However, you're encouraged to
explore other editors. You will be spending a lot of time editing code, so you
might as well use one you like.

A lot of programmers use an IDE (integrated development environment). This is
sort of like having your editor, terminal, and other useful stuff all in one
application. Popular IDEs include:

+ Visual Studio
+ Eclipse
+ PyCharm
+ IDLE

We will not be using IDEs in this class. One of the goals of the class is for
you to become Linux savvy. That means using the terminal as much as possible,
and not hiding stuff behind and IDE. If you want to use an IDE solely as an
editor, that's fine.

Another useful technology we won't be using is Jupyter. Interactive computing
is very powerful and intuitive, but it doesn't lend itself to creating
distributable software. It also isolates you from the CLI.

------------------------------------------------------------------------------

## Home Directory ##

When you open your graphical file browser, it has a default view. This might be
your recent files, desktop, or some other place on your file system. Similarly,
when you open your terminal application, it also has a default view, which we
call its focus. By default, the focus of your terminal is your home directory.
To see the contents of your home directory, open the terminal application and
use the `ls` command to list and sort its contents.

```
ls
```

Linux and Mac users will see directories (folders) for Desktop, Documents,
Downloads, as well as other directories that depend on your specific operating
system. Cygwin users will not see anything at all because Cygwin doesn't create
any directories for you.

Your home directory is located at a specific point in your filesystem. The root
of the Unix filesystem is `/`. All directories and files are hierarchically
under "slash". For example, your home directory might be in `/home/your_name`
or `/Users/your_name`. The exact location depends on your operating system.
Let's examine the path to your home directory with the `pwd` command, which
stands for "print working directory".

```
pwd
```

To change directory, use the `cd` command. Let's change to the root directory
and verify that the focus of the terminal is indeed `/` using `pwd`.

```
cd /
pwd
```

This should have reported simply `/`. Try examining the root of the filesystem
with `ls`.

```
ls
```

You should see a bunch of short names, which include `bin` and `etc`, `home`,
`sbin`, `usr`, and `var`. Depending on your OS, there may be other names as
well. You can look inside a directory by giving `ls` an argument. Let's try
listing what's in the bin directory.

```
ls bin
```

The output shows _some_ of the core programs provided by Linux. Note that even
though the current focus of your terminal is `/`, you were able to `ls` a
different directory. You don't need to be in a directory to list it. Please
read that sentence again.

To get back to your home directory, use `cd` without any arguments. Verify your
focus is your home directory using `pwd`.

```
cd
pwd
```

### Code Directory ###

We are going to organize all of our programming efforts in a directory called
`Code`. Use `pwd` to ensure your focus is your home directory. If you are in
another directory, use `cd` to get back to your home. Once your focus is set to
home, use `mkdir` to create the `Code` directory.

```
mkdir Code
```

### File-naming Conventions ###

Most of the time, we use lowercase for everything. There is one common
exception: directories in your home directory are often upppercase (e.g.
Documents, Downloads, etc.). This is why `Code` is capitalized and not `code`.

+ Use lowercase letters in general
+ Use underscores or dashes to separate words (e.g. `human_genome.fa.gz`)
+ Dots are usually reserved for file types (e.g. `poetry.txt`)
+ Never put spaces or punctuation in your folder or file names

------------------------------------------------------------------------------

## Git ##

Git is the most popular version control software. While it was designed for
source code management, it can be used to manage all kinds of projects. Git
allows multiple people to work on the same files without anyone over-writing
anyone else's work. You will always know who did what and when.

### GitHub Account ###

GitHub is a website that lets you store your git repositories for free. There
are several similar sites, but GitHub is the most popular. Every bioinformatics
developer should have a GitHub account. Your repositories and activity are part
of your CV. If you don't have a GitHub account, it's time to point your web
browser to [GitHub](https://github.com) and create an account.

Choose a username. It's okay to be clever, but don't be silly. Remember, this
will be part of your CV. After setting your email and password, choose the free
plan and then answer a few questions about your interests to create your
account. Go to your email to verify your email address.

### Create a Repository ###

It's time to create your first repository, which we often shorten to _repo_.
Before we begin, we need to talk a little about ownership, privacy, and
security.

When you create a repo, you own it. You can read it, write to it, or even
delete it. Later, you can invite collaborators who can join you in your
efforts, but by default, only you can make edits.

When a repo is created, it can be either _Public_ or _Private_. A Public
repository allows other people to download a copy of your repo. This is called
_cloning_. There is no security risk in cloning a Public repository (unless you
put sensitive info in there). If people modify their clones, it does not affect
your files. If you want people to be able to edit files in your repo, you have
to invite them as collaborators.

A Private repository is invisible to everyone but you. You can add
collaborators to Public or Private repos and specify what kinds of permissions
each collaborator may have. As the owner, you can change a repo from Public to
Private and back. Most of my repos are public because I believe in openly
sharing (but hands off my sandwich).

Now let's go make a repo. Go to the GitHub website and click on the green "New"
button to create a new repo. Name this "mcb185_homework" because this is where
you'll be submitting your homework. Please name the file exactly as shown with
lowercase letters and an underscore. Make it **public**. Does this mean that
students can see each others' homework? Yes. You're actually encouraged to work
with other students in this class. Click the checkboxes to initialize with a
README, add a .gitignore, and add a license. Scroll through the .gitignore
options until you get to "Python". Choose whichever license you like. I
generally use MIT. Click the "Create Repository" and you will be transported to
your new, mostly empty repo.

### Personal Access Token ###

When you interact with the GitHub website, you use a username and password (and
possibly multi-factor authentication). When you interact with GitHub using the
CLI, you **cannot use your website password**. Instead you have to use a
"personal access token" (PAT). So the first thing we need to do is to generate
a PAT.

Log into GitHub and then click on the icon in the top right corner. This will
drop down a menu where you will find "Settings". Follow that link and you will
get to your various account settings. Scroll down to the bottom to find
"Developer Settings". On the next page you will see "Personal access tokens".
Click on the link to "Generate a personal access token".

In the "Note" you might put in "programming" or something. It doesn't matter.

For "Expiration" choose the "No expiration" option.

Click on the "repo" checkbox, which will also check the subordinate boxes.

This personal access token is given to you once. Copy it and save it somewhere
safe. You can never get to this PAT again. Ever. However, you can generate a
new one anytime you like, so if you lose your PAT, you can just generate a new
one. I put my PAT in a personal message to myself in Slack. I also keep it in a
file on Dropbox and Google Drive.

### Cloning Repos from the CLI ###

Your current homework repo is located on GitHub, but not in your Linux
environment. Type the following commands in your terminal, substituting
`YOUR_GITHUB_HANDLE` for whatever your GitHub user name is.

```
cd
cd Code
git clone https://github.com/YOUR_GITHUB_HANDLE/mcb185_homework
ls
```

You should now see your homework directory when you `ls`. Also clone the MCB185
repo so that you have all of the course content on your computer. You might be
asking yourself why MCB185 is capitalized. That's because you're not supposed
to modify it. Think of the contents there as read-only.

```
git clone https://github.com/iankorf/MCB185
ls
```

You should now see both the `mcb185_homework` and `MCB185` repos in your `Code`
directory.

### Git Commands ###

Enter your homework repository and check its status. If the `cd` command below
shows an error, the focus of your terminal may have changed. Make sure that the
output of your `pwd` command is your `Code` directory before attempting to
change directory to your homework directory.

```
cd mcb185_homework
git status
```

The output of `git status` should show the following:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Let's modify a file and see what happens. Edit the `README.md` file with your
text editor and save it. If you can't find the file, ask for help.

After saving your changes, do another `git status`.

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

The output shows that `README.md` has been modified. There are some suggestions
about what you might like to do next. We will choose the `add` command. Do
another `git status` afterward.

```
git add README.md
git status
```

The output shows `README.md` is now ready to be committed.

```
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

To commit changes, we use `commit` along with a message after `-m`. In the
example below, note that the phrase is in quotes. This is required for
multi-word messages. If the message was simply "update", you wouldn't need the
quotes.

```
git commit -m "my first commit"
```

If this is the first time you've done a `commit` on your computer, you will get
an error message like the following.

```
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'ianko@7600-4600.(none)')
```

Do as the prompt says, typing the two `git config --global` commands, replacing
"you@example.com" with the email address you have associated with GitHub and
replacing "Your Name" with whatever your GitHub username is.

Now try running the `git commit -m "my first commit"` again (did you remember
to use the up arrow instead of typing?). The new output is shown below.

```
[main 0d04f3a] my first commit
 1 file changed, 4 insertions(+), 1 deletion(-)
```

The last thing we need to do is to upload our changes to GitHub so that the
code is not only on our local computer, but also on the website. This is done
with the `push` command.

```
git push
```

You will be prompted for your username. You might not see any text as you type.
Next, you will be prompted for your password. Again, the text may be invisible.
This is **not** your GitHub password. This is your PAT (personal access token).
Copy-paste this into the terminal. Sometimes copy-paste doesn't work with
keyboard shortcuts, so use the right-click context menu instead.

```
git config --global user.name "username"
git config --global credential.helper store
```

The next time you do a `git push` you will probably have to use your PAT one
more time, but not in the future.

Now let's go to the GitHub website. Look at your `README.md` there and verify
that the text has changed. If it has not, try reloading the page, and if you
still don't see your changes ask for help.

------------------------------------------------------------------------------

## Text Files and Markdown ##

Most of the files we work with in Linux are plain text files. Many things
change in this world, but not the format of text files.

### Text vs Binary ###

There are two main types of files you will encounter: text and binary. You can
view text files with `less` and edit them with `nano`, for example. All of the
programs we write in this course will be plain text files. You can also view
and edit binary files but they look like gobbledygook, not English. If you want
to see what a binary file looks like, try the following.

```
less /bin/ls
```

You may have to hit the 'y' key to see the output. You're looking at the
machine code for the `ls` program. It's not meant to be human-readable. Hit the
'q' key to get out of `less`. So what makes a file text or binary? To answer
that, we need to delve into the world of bits and bytes.

### Bits, Bytes, and ASCII ###

A _bit_ is a single binary digit representing a 0 or 1. The number "1" is just
1 as we know it. The number "10" is 2 in decimal notation. There is a "1" in
the 2s place and a 0 in the "1s" place, so 2 + 0 = 2. Similarly, the number
"11" in binary is 3 in decimal and the number "101" in binary is "5" in decimal
(1 four, 0 two, 1 one).

A byte is 8 bits in a row. Computers usually deal in bytes. So we don't
normally talk about a number like "101" to represent 5 but rather the 8-digit
version of that "00000101". So what number is "10000000"? Well that depends if
you're working in base 2, decimal, or something else entirely. In order to
clarify these things, people often put two characters at the front to signify
the base when it's not base-10. Prepending the numerals with "0b" tells people
"I'm using binary". So "0b10000000" means 128 and not ten million.

We actually use the "byte" more frequently than you might guess. However, when
we do so, it's usually in _hexadecimal_ notation. In base 2, there are 2
symbols: 0 and 1. In base 10 (ordinary decimal) there are 10 symbols: 0, 1, 2,
3, 4, 5, 6, 7, 8 , and 9. In base 16 (hexadecimal), there are 16 symbols: 0, 1,
2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. So the symbol "B" in hexadecimal
means "11" in decimal. To specify that a number is in hex, it is proceeded with
"0x". Therefore "0x10" is 16 (1 value in the 16s and nothing in the 1s).

Have you ever seen internet addresses of the form 192.168.1.1? Ever wondered
what those 4 numbers are? Each one is a byte. So each one can have a value from
"0b00000000" to "0b11111111". In other words, each value can be from "0x00" to
"0xFF". Or more familiarly, from 0 to 255. These same byte notations are used
all over the place in computers. For example, you may have had to dig up the
MAC (media access control) address of your network adapter, which may have
looked like "f0:18:98:e9:f2:be". Each of those number-like things separated by
a colon is a byte in the range of 00-ff (upper and lowercase don't matter in
hexadecimal).

### Colorspace ###

Another place you may have seen hexadecimal notation is to represent colors. In
a computer, color is made by mixing three colors of light: red, green, and
blue. Each of those colors can have an intensity from 0 to 255, which in hex is
00-FF. For example, if you want to make bright red, you use FF in the red
channel, 00 in the green channel, and 00 in the blue channel. The most
efficient way to write this is to mash them all together as FF0000. This can
also be written as 0xFF0000 or even #FF0000.

Here are some common colors:

+ FF0000 Red (only the red channel)
+ 00FF00 Green (only the green channel)
+ 0000FF Blue (only the blue channel)
+ 000000 Black (all channels off)
+ FFFFFF White (all channels on)
+ 808080 Gray (all channels at half)

If you think about the color spectrum, yellow is halfway between red and green.
So how do we make a color halfway between the two? By turning on those two
channels. Similarly, halfway between green and blue is cyan. If you think of
the spectrum as a circle rather than a line, then halfway between blue and red
is magenta.

+ FFFF00 Yellow
+ 00FFFF Cyan
+ FF00FF Magenta

What about the other colors, such as orange? Orange isn't halfway between any
of the channels. However, it is halfway between red and yellow. To make orange,
we have to decrease the green channel so that the average is closer to red. How
about we cut the green in half? FF8000 = Orange.

At this point, you're probably asking yourself, "but what about all of that
stuff I learned in art class where red + green = brown?". Paints are pigments,
not sources of life. You have to think about those in the absorption spectrum.
Red pigment block green and blue, allowing red to come through. Similarly,
green pigment blocks red and blue, allowing green to come through. When you mix
pigments, you average the absorptive properties of the two. So red + green
pigments completely block the blue spectrum and allow about half of the red and
green to come through. If we were to express that in hex it would look like
808000, which is a dark yellow, which is brown-ish.

### Back to Binary ###

So now it's time to understand the difference between text and binary files. A
text typically uses only the values from 32-127 (decimal) or 20-7F (hex). These
are all printable characters without any special meanings. Files that use
characters less than 32 or greater than 127 are considered binary. Really, all
files are binary, but text files are a special case of binary files that are
meant to be human readable.

```
| Dec | Hex | C | Dec | Hex | C | Dec | Hex | C |
|:---:|:---:|:-:|:---:|:---:|:-:|:---:|:---:|:-:|
|  32 |  20 |   |  64 |  40 | @ |  96 |  60 | ` |
|  33 |  21 | ! |  65 |  41 | A |  97 |  61 | a |
|  34 |  22 | " |  66 |  42 | B |  98 |  62 | b |
|  35 |  23 | # |  67 |  43 | C |  99 |  63 | c |
|  36 |  24 | $ |  68 |  44 | D | 100 |  64 | d |
|  37 |  25 | % |  69 |  45 | E | 101 |  65 | e |
|  38 |  26 | & |  70 |  46 | F | 102 |  66 | f |
|  39 |  27 | ' |  71 |  47 | G | 103 |  67 | g |
|  40 |  28 | ( |  72 |  48 | H | 104 |  68 | h |
|  41 |  29 | ) |  73 |  49 | I | 105 |  69 | i |
|  42 |  2a | * |  74 |  4a | J | 106 |  6a | j |
|  43 |  2b | + |  75 |  4b | K | 107 |  6b | k |
|  44 |  2c | , |  76 |  4c | L | 108 |  6c | l |
|  45 |  2d | - |  77 |  4d | M | 109 |  6d | m |
|  46 |  2e | . |  78 |  4e | N | 110 |  6e | n |
|  47 |  2f | / |  79 |  4f | O | 111 |  6f | o |
|  48 |  30 | 0 |  80 |  50 | P | 112 |  70 | p |
|  49 |  31 | 1 |  81 |  51 | Q | 113 |  71 | q |
|  50 |  32 | 2 |  82 |  52 | R | 114 |  72 | r |
|  51 |  33 | 3 |  83 |  53 | S | 115 |  73 | s |
|  52 |  34 | 4 |  84 |  54 | T | 116 |  74 | t |
|  53 |  35 | 5 |  85 |  55 | U | 117 |  75 | u |
|  54 |  36 | 6 |  86 |  56 | V | 118 |  76 | v |
|  55 |  37 | 7 |  87 |  57 | W | 119 |  77 | w |
|  56 |  38 | 8 |  88 |  58 | X | 120 |  78 | x |
|  57 |  39 | 9 |  89 |  59 | Y | 121 |  79 | y |
|  58 |  3a | : |  90 |  5a | Z | 122 |  7a | z |
|  59 |  3b | ; |  91 |  5b | [ | 123 |  7b | { |
|  60 |  3c | < |  92 |  5c | \ | 124 |  7c | | |
|  61 |  3d | = |  93 |  5d | ] | 125 |  7d | } |
|  62 |  3e | > |  94 |  5e | ^ | 126 |  7e | ~ |
|  63 |  3f | ? |  95 |  5f | _ | 127 |  7f |   |
```

At this point you may be wondering about other alphabets and how they get
encoded in a computer. Surely you can't fit all of the symbols in known human
language into the range of 32-127. You can't. However, there are multi-byte
encodings that offer many more symbols.

### Formatting Plain Text ###

Text files are incredibly simple. There are no choices of ruler settings, font
family, font style, lists, or tables you expect to find in a word processing
document. However, sometimes you want part of a text file to look like a
heading, or boldface, or a list. There are lots of ways you can imagine doing
that from the use of capital letters to punctuation. Markdown is a global
standard for formatting text files. If you follow the standard, you can turn
your plain text documents into beautifully formatted HTML or PDF that has
actual headings, hyperlinks, font styles, lists, etc.

To find out how to write Markdown, check out the website linked below. This is
the official home of vanilla Markdown. There are a few customizations of
Markdown that add a few more things like tables.

[Markdown](https://daringfireball.net/projects/markdown)

Another way to learn Markdown is to compare an HTML or PDF file to its original
Markdown plain text source document. If you're viewing this document on GitHub,
you're viewing it formatted as HTML. You can also look at the raw text either
on the website or in your forked repo.

Here are the basics of Markdown:

# Level 1 Heading - use a single leading hash

## Level 2 Heading - use a double leading hash

### Level 3 Heading - use a triple leading hash

Alternatively, you can underline titles with equals sign or minus sign for
headings. These look better when viewed as text files.

Level 1 Heading
===============

Level 2 Heading
---------------


Bulleted lists can use plus, minus, or star (and even mix them).

+ Enroll in MCB185
+ Install Linux
+ Get a GitHub account
+ Learn about Markdown
- Learn some Unix commands
- Learn some Python
* Do cool stuff

Text can be _emphasized_ with underline or *stars* or made bold-face with
**double-stars**. For in-line fixed-width font, such as code snippets or stuff
you're supposed type in a terminal, use `backticks`. For longer code use triple
backticks enclosing multiple lines.

```
your code here
```

Hyperlinks use square brackets for the text followed by parentheses for the
URL. You can also put links in as plain text and make your users copy-paste
them into their browser.

[Markdown](https://daringfireball.net/projects/markdown)

------------------------------------------------------------------------------

## Hello World ##

The first program you write in any language is "hello world". This is something
minimal that shows that your programming environment is working. We are going
to write hello world programs in both shell and python.

### 00hello.sh ###

Change directory to your homework repo and create a file with the `touch`
command.

```
cd
cd Code/mcb185_homework
touch 00hello.sh
```

Open your editor, find this file, and create this one-line script.

```
echo "hello world"
```

Save the file. Go back to the terminal and run the program.

```
sh 00hello.sh
```

If all goes well, you should see your welcome message in the terminal. If you
don't, stop now and get help. Don't continue on thinking you'll fix this later.

### 01hello.py ###

Let's make the equivalent program in Python.

```
touch 01hello.py
```

Open your editor, find this file using the GUI, and write the following
one-liner.

```
print('hello world')
```

Save the file. Now run the program.

```
python3 01hello.py
```

If all goes well, you should see your welcome message in the terminal. If you
don't, stop now and get help. Don't continue on thinking you'll fix this later.

Now let's add your programs to your homework repo. `git status` will show that
neither file is tracked. So let's `add` them, create a `commit` message, and
then `push` them back to the website. Remember, you don't use your website
password here, but rather your github personal access token (PAT). You'll have
to copy-paste that, as it's a bit too long to type.

If you get an error, it may be because the copy-paste didn't work. Do a
right-click-based paste rather than using the keyboard shortcut.

```
git add 00hello.sh 01hello.py
git commit -m new
git push
```

Check the GitHub website. Both of your new files should now be in the repo. If
they are not, refresh the page or get help if that's not the problem.

It might seem like git is a lot of effort just to upload your code to a website.
If that's all git did, it would be too much effort, but git allows you to do a
lot more. Git tracks every change you make to a file, allowing you to rewind it
to any point in time. Git allows you to make a _branch_ of related work and
then later merge it back in with the main trunk if desired. More importantly,
git allows multiple developers to work simultaneously on the same project
without destroying each others work. We aren't using those advanced features
yet. Right now, our focus is on backing up our code and logging our programming
activity to the GitHub website.

------------------------------------------------------------------------------

## Homework ##

To get full credit for your homework, submit the following:

+ URL of your homework repository
+ `00hello.sh` in your repo
+ `01hello.py` in your repo
