Unit 4: Random
==============

+ Random numbers
+ Pretty printing
+ Monte Carlo
+ Homework

## Random Numbers ##

Random number generators are essential because we often use random expectation
as a background model or null hypothesis. In order to use random numbers, we
import the random library and call the functions therein.

Start a new `40demo.py` program and add the following line.

```
import random
```

### random.random() ###

The simplest function is `random.random()`, which produces a number 0 <= X < 1.

```
for i in range(5):
    print(random.random())
```

### random.choice() ###

Given a container of values, `random.choice()` randomly chooses an item from
the container. So far, the only container we have seen are strings, which
contain characters. We can make random dna by choosing letters from its
alphabet.

```
for i in range(50):
    print(random.choice('ACGT'), end='')
print()
```

What if you wanted to make something that wasn't 25% each letter. One way to do
that is with `random.random()` and conditionals. The code below generates
sequence that is 70% AT on average.

```
for i in range(50):
    r = random.random()
    if r < 0.7: print(random.choice('AT'), end='')
    else:       print(random.choice('CG'), end='')
print()
```

### random.randint() ##

The function we will use most often is `random.randint()`. This generates a
random number between two _inclusive_ end points. For example, the following
code simulated rolling a 6-sided die 3 times.

```
for i in range(3):
    print(random.randint(1, 6))
```

### random.gauss() ###

The random library supports several common distributions, such as the Gaussian
(normal) distribution. The arguments are the mean and standard deviation.

```
for i in range(5):
    print(random.gauss(0.0, 1.0))
```

### 41zscores.py ###

You have probably heard before that 1 z-score corresponds to approximately 2/3
of the data, and 2 z-scores corresponds to 95% (e.g. the typical threshold for
statistical significance). Write a program that generates numbers drawn from a
normal distribution and calculate how many of those are 1, 2, or 3 z-scores
above the mean. Use `random.gauss()`.

Create a new file called `41zscores.py` to solve the problem. After typing this
in line-by-line, run it and verify it works. Then delete everything and see if
you can do it by yourself. Doing ground-zero re-writes like this is a great way
to improve your programming aptitude.

```
1   import random
2
3   z1 = 0
4   z2 = 0
5   z3 = 0
6   limit = 100000
7   for i in range(limit):
8       r = random.gauss(0.0, 1.0)
9       if r > 1: z1 += 1
10      if r > 2: z2 += 1
11      if r > 3: z3 += 1
12  print(1 - 2*z1/limit)
13  print(1 - 2*z2/limit)
14  print(1 - 2*z3/limit)
```

Let's discuss this line-by line.

Line 1 imports the random library. It's at the top of the program, where all
imports belong.

Line 2 is blank because imports should be separated from the logic of the code.

Lines 3-6 provide initializations. We need several variables to keep track of
z-scores. A value like 2.3 is greater than a z-score of 1 and 2, but not 3.

Lines 7-11 preform the iterations. In each iteration, we need a random number
(line 8). The comparisons on lines 9-11 are not if-elif because each one is a
separate calculation.

Lines 12-14 perform the finalization steps and output.

------------------------------------------------------------------------------

## Pretty Printing ##

There are times when you want your terminal or plain text documents to look
pretty. There are several strategies.

### Special Characters ###

There are two special characters we frequently use to tidy-up text. The newline
character `\n` creates vertical spacing. It's like hitting the return key.

```
print('this line\n has some\n line breaks')
```

The tab key `\t` is used to line up columns of text. Every time this is
printed, the cursor jumps to the next tab stop (usually set at 4 or 8
characters). In the code below, the tab character is in the separator. Files
with tab-separated values are sometimes called TSV and have extensions `.tsv`.

```
print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')
```

### f-strings ###

Historically, Python has provided multiple ways to format text. In this class,
we only use f-strings. An f-string is created by placing a lowercase f before
the first quotation mark. The main advantage of f-strings is that variables
inside curly brackets dump their contents.

```
i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
```

f-strings have several powerful formatting options. We are are only going to
use floating point rounding. This is simply appending `:.3f`, where the 3 after
the dot is 3 digits of precision.

```
print(f'formatted string {i} {pi:.3f}')
```

### sys.stderr ###

When running thousands or millions of random trials, which we will do below,
you sometimes want to send some non-program output to your terminal. A
convenient way to do that is to specify `file=sys.stderr` in the `print()`
function.

```
import sys
print('logging', file=sys.stderr)
```

If you run this program from your terminal, it won't look like anything
special. However, try redirecting the output to a file.

```
python3 40demo.py > foo
```

The contents of your demo program are now in `foo`, but `logging` is still
printed to your terminal. That's because your program output went to stdout and
your logging statement went to stderr.

------------------------------------------------------------------------------

## Monte Carlo ##

Monte Carlo algorithms perform repeated random sampling to arrive at a
solution. The name comes from the city, which is famous for Casinos. Monte
Carlo algorithms effectively roll dice over and over.

An nice example of Monte Carlo is to estimate Pi by throwing random darts. The
Wikipedia page has a nice explanation and graphic.

https://en.wikipedia.org/wiki/Monte_Carlo_method

### Pseudorandom ###

Random numbers in your computer aren't truly random. They are generated
deterministically given a starting _seed_, which is an integer. All of the
random number problems presented here and in your homework problems can be
repeated exactly the same again and again if you set the seed ahead of time.
This can be useful for debugging. If you don't choose a seed, you will be given
one somewhat randomly.

```
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
```

In the code above, each call to `random.seed()` resets the random number
generator so that subsequent calls to `random.random()` are repeated.

### Compound Assignment ### 

The programs in this unit have a lot of variables that need to be incremented.
Instead of writing `x = x + 1` there is a shortcut: `x += 1`. The compound
assignment operators do the math and update the variable at the same time. We
only use the 3 operators in the table below, but there are also operators for
division, modulus, integer division, and exponentiation (and more).

| Operator | Purpose           | Example
|:---------|:------------------|:--------------------------
| `+=`     | increment         | `a += 1`
| `-=`     | decrement         | `a -= 1`
| `*=`     | multiply & assign | `a *= 2`


### Chicago ###

The game "Chicago" is a simple dice game for 2 or more players. In each round,
a player rolls 2 dice. If the sum of the dice are equal to the target value for
the round, the player gets the target number of points. The game is played over
11 rounds, which walk through the numbers 2-12. The minimum score is 0 and the
maximum is 77.

1. 2 points if you roll a 2
2. 3 points if you roll a 3...
3. 4
4. 5
5. 6
6. 7
7. 8
8. 9
9. 10
10. 11
11. 12 points if you roll a 12

+ What is the distribution of game scores?
+ What is the average score for a game of Chicago?
+ How often does a player end a game with a score of zero?

Let's start by getting the computer to play 10 games of Chicago. Create a new
file called `42chicago.py` and then type the following lines.

```
1   games = 10
2   for i in range(games):
3       print(f'game #{i}')
4       for target in range(2, 13):
5           d1 = random.randint(1, 6)
6           d2 = random.randint(1, 6)
7           if d1 + d2 == target:
8               print(f'yay, rolled {d1} and {d2} for {target} points')
```

Line 3 prints out a new status message with each game. Notice the use of the
f-string to do the formatting.

Line 4 starts the iteration through values of 2-12.

Lines 5-6 contain the die rolls.

Line 7-8 compare the die rolls to the target number and create a message when
the roll happens to add up to the target.

In order to get accurate estimates on average score and such, we're going to
have to play a lot of games of Chicago. We aren't going to want to print 'yay'
every time. We also don't need the individual die rolls, just their sum. What
we really care about is the score of each game. So let's create a variable for
that and increment it every time we score. At the end of the game, we will just
print out the final score of the game.

```
1   games = 1000
2   for i in range(games):
3       score = 0
4       for target in range(2, 13):
5           if random.randint(1, 6) + random.randint(1, 6) == target:
6               score += target
7       print(score) # final game score
```

Line 3 resets the score every time a new game is played. One of the most common
errors new programmers make is placing the `score = 0` outside the loop.

We can get an idea of the distribution of game scores by sending the output to
`sort` and `uniq` like we did back in Unit 1.

```
python3 42chicago.py | sort -n | uniq -c | sort -n
```

My run found that 375 of the 1000 games had a score of zero. Try changing the
1000 to 10000 or higher. If we want to play millions of games, we shouldn't
stream the output to `sort` because that ends up taking a lot of memory and
CPU. Instead, let's keep all the calculations internal to python. We will need
two variables, one to keep track of the total points and another to count the
number of games that end with zero points. Let's also add some logging so that
a message is sent to stderr after each 1% of the trials are complete.

```
1   games = 1000000 # 1 million trials
2   log = games // 100 # report progress at 1% intervals
3   total = 0
4   zeroes = 0
5   for i in range(games):
6       if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr)
7       score = 0
8       for target in range(2, 13):
9           if random.randint(1, 6) + random.randint(1, 6) == target:
10              score += target
11      if score == 0: zeroes += 1
12      total += score
13  print(total / games)
14  print(zeroes / games)
```

Line 2 sets the logging interval relative to he number of games played. This
value works with line 6 to display a status message each time 1% of the data
has been processed.

Lines 3 and 4 are the initializations. In the end, we are going to divide the
total scores by the total number of games played. We are also going to
calculate the fraction of games that end with zero score. These calculations
are at the very end of the program, so their initializations (lines 3-4) and
finalizations (lines 13-14) must be outside all loops.

Lines 7-11 are identical to the previous code (lines 3-6).

Lines 11-2 perform intermediate calculations.

After 1 million trials, the average game has a score of 7.0 and 34.6% of games
end with zero score. Honestly, the game doesn't sound like nearly as much fun
as programming the solution.

------------------------------------------------------------------------------

## Homework ##

+ `40demo.py`
+ `41zscores.py`
+ `42chicago.py`
+ `43randomdna.py`
+ `44randompi.py`
+ `45dndstats.py`
+ `46savingthrows.py`
+ `47deathsaves.py`

### 43randomdna.py ###

Create a program that generates DNA sequences in FASTA format. There should be
a variable that controls how many sequences (e.g. 3). Each sequence should have
a unique identifier (e.g. seq-1) and the length of the sequence should have
some random range (e.g 50-60). The output should resemble the example below.

```
>seq-1
GCCGTCTCGGGGGAGAACGAGCGACTGCTGTCCCGGGATGTGCGTAAATGCGGGC
>seq-2
GGTTTTAATAGCACCCGAAGCTCCATCCAGCTAGACGTCGAAGCTTTTTAACACTGTA
>seq-3
CAGTATGGTCCACCCGCCTTTCAGGAATACTTCATCCTAAGTGCCTCGAA
```

### 44randompi.py ###

Generate random values for x and y from 0 to 1. Calculate the distance to the
origin. If the distance is less than 1, the point is inside the circle. The
ratio of points that fall inside compared to the total is pi/4. Output each
iteration and watch as the ratio gets closer to pi. Use an endless `while` loop
in your program and stop it with ^C.

### 45dndstats.py ###

In Dungeons and Dragons, each character is described by 6 statistics (strength,
intelligence, wisdom, dexterity, constitution, charisma). In the old days, each
_stat_ was decided by summing up the values on 3 six-sided dice (3D6). Each
stat therefore has a range of 3-18 and an average of 10.5. Over the years, the
official rules have changed and many players have added their own house rules.
Write a program that determines the average stat value using the various rules
below.

+ 3D6: roll 3 six-sided dice
+ 3D6r1: roll 3 six-sided dice, but re-roll any 1s
+ 3D6x2: roll 3 six-sided dice twice, and take the maximum of the two
+ 4D6d1: roll 4 six-sided dice, dropping the lowest die roll

### 46savingthrows.py ###

One of the core mechanics of D&D is the "saving throw". When certain events
happen, you need to roll a d20 to figure out if you succeed or not. For
example, you are walking across a frozen lake and it begins to crack underfoot.
If you make a saving throw, you step aside. If you fail, you fall in. Some
saving throws are more difficult than others. If the ice is very thick, the
"difficulty class" (DC) may be only 5. This means you only need to roll a 5 or
higher to succeed. However, if the ice is thin and has a DC of 15, you will
need a roll of 15 or higher to succeed. Certain events may give you "advantage"
or "disadvantage". For example, if you have a rope tied around your waist and a
friend is instructed to pull you aside if anything bad happens, you could have
"advantage". This allows you to roll two d20s and take the larger value. You
may also have disadvantage, for example another "friend" pushes you from
behind, causing you to stumble forward. In this case, you have "disadvantage"
and must take the lower of two d20 rolls. Write a program that simulates saving
throws against DCs of 5, 10, and 15. What is the probability of success
normally or with advantage/disadvantage? Make a table showing the results.

### 47deathsaves.py ###

Death saves are a little different than normal saving throws. If your health
drops to 0 or below, you are unconscious and may die. Each time it is your
turn, roll a d20 to determine if you get closer to life or fall deeper into
death. If the number is less than 10, you record a "failure". If the number is
10 or greater, you record a "success". If you collect 3 failures, you "die". If
you collect 3 successes, you are "stable" but unconscious. If you are unlucky
and roll a 1, it counts as 2 failures. If you're lucky and roll a 20, you gain
1 health and have "revived". Write a program that simulates death saves. What
is the probability one dies, stabilizes, or revives?
