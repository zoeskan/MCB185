Unit 3: Algorithms
===================

## Contents ##

+ [Iteration](#iteration)
    + [while](#while)
    + [for i in range()](#for-i-in-range)
    + [for item in container](#for-item-in-container)
+ [Nested Loops](#nested-loops)
    + [31fizzbuzz.py](#31fizzbuzzpy)
+ [Algorithms](#algorithms)
+ [Practice Problems](#practice-problems)
+ [Practice Solutions](#practice-solutions)
    + [triangular()](#triangular)
    + [factorial()](#factorial)
    + [euler()](#euler)
    + [is_perfect_square()](#is_perfect_square)
    + [is_prime()](#is_prime)
+ [Homework](#homework)
    + [32fibonacci.py](#32fibonaccipy)
    + [33triples.py](#33triplespy)
    + [34scoringmatrix.py](#34scoringmatrixpy)
    + [35nchoosek.py](#35nchoosekpy)
    + [36poisson.py](#36poissonpy)
    + [37nilakantha.py](#37nilakanthapy)

------------------------------------------------------------------------------

## Iteration ##

The solution to most complex problems involves some kind of iteration. For
example, if you want to compute the standard deviation for a set of numbers,
you must iterate through the values, squaring the differences to the mean.
Iteration is also called looping.

Create a new `30demo.py` program in your homework repo and bring it up in your
editor.

### while ###

The `while` loop is the simplest type of loop. It is formed in the manner
below, which does not represent actual code. The `while` word is followed by an
expression that can be evaluated as `True` or `False`. This is followed by an
indented code block.

```
while <boolean expression is True>:
    do_something
```

Add the following lines to your demo program and run it. The Boolean expression
in this case is the value `True`, which means this loop will never end.
Interrupt the endless output by typing ^C.

```python
while True:
    print('hello')
```

One way to break a loop is with the `break` statement. In the example below, we
create a variable `i` that will be used to store an integer. Each time through
the loop, the value of `i` increases: `i = i + 1`. Once `i` reaches 3, the
loop breaks.

```python
i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break
```

A better way to break a `while` loop is to provide some kind of condition when
the Boolean expression is no longer True.

```python
i = 0
while i < 3:
    print(i)
    i = i + 1
print('final value of i is', i)
```

The loop doesn't have to start at 0, increment by 1, or end before 5. The
modified code below starts at 1, ends before 10, and skips by 3s.

```python
i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)
```

### for i in range() ###

Most loops in Python are `for` loops, not `while` loops. Let's recreate the
last code example using a `for` loop and the `range()` function.

```python
for i in range(1, 10, 3):
    print(i)
```

The `range()` function generates integers given an initial value (1), an
end-before limit (10), and an increment (3).

Most "for i in range()" loops increment by one. For this reason, you can skip
the increment number and use just 2 arguments.

```python
for i in range(0, 5):
    print(i)
```

Also, most "for i in range()" loops also start at zero, meaning you can skip
the initial value and simply give the end-before limit.

```python
for i in range(5):
    print(i)
```

All of these constructions do the exact same thing.

```python
for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i)
```

### for item in container ###

`for` loops can be used to loop over items in a container. We will see much
more of this next unit. For now, our items are characters, and the container is
a string. The string 'hello' has 5 characters. We can loop over each one as
follows.

```python
for char in 'hello':
    print(char)
```

As this is class is themed around biology, we will be using nucleotide and
amino acid sequences very soon.

```python
seq = 'GAATTC'
for nt in seq:
    print(nt)
```

------------------------------------------------------------------------------

## Nested Loops ##

Loops can be inside other loops. Conditionals can also be inside loops and
vice-versa. In sequence alignment, a pair of letters is given a score, for
example, +1 for a match and -1 for a mismatch. Let's display that relationship
using 2 nested loops, one for each collection of letters.

```python
for nt1 in 'ACGT':
    for nt2 in 'ACGT':
        if nt1 == nt2: print(nt1, nt2, '+1')
        else:          print(nt1, nt2, '-1')
```

In the loop above, we call the loop with `nt1` the "outer loop" and the one
with `nt2` the "inner loop".

Notice that the string 'ACGT' is used twice. Good programmers minimize
hard-coding, which means using literal values instead of the contents of
variables. Any time you use the same value twice, you should probably make a
variable to hold the contents. The process of making your code less repetitive
and more elegant is called _abstraction_.

In the code below `nts` holds the alphabet. Changing the variable changes both
loops. By naming the variable `nts` we can read it simply as "for nucleotide 1
in nucleotides".

```python
nts = 'ACGT'
for nt1 in nts:
    for nt2 in nts:
        if nt1 == nt2: print(nt1, nt2, '+1')
        else:          print(nt1, nt2, '-1')
```

A scoring matrix represents all possible pairings of letters. Another form of
pairing focuses on unique combinations. For example, in phylogenetics, one
starts by calculating the distances from each species to each other. The
distance from one species to the other is the same in both directions, so
there's no point in specifying both distances. Given 4 species, we only want to
see the pairings of 1-2, 1-3, 1-4, 2-3, 2-4, and 3-4. This is accomplished by
initializing the inner loop one beyond the current value of the outer loop.

```python
limit = 4
for i in range(0, limit):
    for j in range(i + 1, limit):
        print(i+1, j+1)
```

Note that the outer loop did not need to specify the initial value of 0. This is
only to show the contrast with the initialization of the inner loop. There are
3 common ways to loop through matrices. They differ only by the initialization
of the inner loop. Try them all.

+ full matrix: inner loop starts at 0
+ half matrix + major diagonal: inner loop starts at i
+ half matrix - major diagonal: inner loop starts at i + 1

### 31fizzbuzz.py ###

One of the classic interview questions is FizzBuzz. Make a program that writes
out the numbers from 1 to 100. If the number is divisible by 3, write Fizz
instead. If the number is divisible by 5, write Buzz instead. If the number is
divisible by both 3 and 5, write FizzBuzz.

------------------------------------------------------------------------------

## Algorithms ##

Most algorithms are a mixture of loops and conditionals, and are often
contained inside functions. Let's create such an algorithm, whose goal is to
calculate the GC composition of a nucleotide sequence.

The function needs an input sequence, which we will call `seq`. The function
then needs to examine each nucleotide, and keep track of how many Gs and Cs it
finds. We'll store that in a variable called `gc_count`. In order to make the
final calculation, we also need to know the total number of nucleotides, which
we'll store in a variable called `total`. Here's the complete function and an
example of use.

```python
1   def gc_comp(seq):
2       gc_count = 0
3       total = 0
4       for nt in seq:
5           if nt == 'C' or nt == 'G':
6               gc_count = gc_count + 1
7           total = total + 1
8       return gc_count / total
9
10  print(gc_comp('ACAGCGAAT'))
```

Most of the algorithms we will see in the class have the following 3-part
structure:

1. Initialization (lines 2, 3)
2. Iteration (lines 4-7)
3. Finalization (line 8)

`gc_comp()` has two initializations.

+ Setting `gc_count = 0`
+ Setting `total = 0`

The iteration stage is a loop over the nucleotides of the sequence. Pay close
attention to the block structure. The only time `gc_count` should be
incremented is if the nucleotide is a C or G. However, all nucleotides must be
counted. This is why `gc_count` is indented inside the `if` block but the
`total` is not.

The finalization step is simply dividing `gc_count` by `total`.

------------------------------------------------------------------------------

## Practice Problems ##

Write a function that calculates the triangular number. This is the sum of
numbers from 1 to n.

Write a function that calculates the factorial of a number.

Write a function that estimates Euler's number: e (2.71828...). This can be
computed as the infinite sum of 1/n!. Choose a finite number of iterations.

Write a function that determines if a number is a perfect square (e.g. 4, 9,
16, 25 are all perfect squares because their square roots are integers).

Write a function to determine if a number is prime.

------------------------------------------------------------------------------

## Practice Solutions ##

Try to solve the problems with another student before examining the solutions
below.

### triangular() ###

In order to sum up the numbers, we must have a variable to hold the sum (line
2). This is initialized at 0, and each iteration of the loop adds the current
value of the loop variable (line 4). The finalization step is simply returning
the value of the sum (line 5).

```python
1   def triangular(n):
2       tri = 0
3       for i in range(n+1):
4           tri = tri + i
5       return tri
```

### factorial() ###

There are two tricks to this solution. First, the factorial of zero is defined
as 1. Use a conditional for that special case (line 2). Second, when
multiplying values, you cannot initialize at zero or you will always get zero.
So factorial must initialize at 1 (line 3).

```python
1   def factorial(n):
2       if n == 0: return 1
3       fac = 1
4       for i in range(1, n + 1):
5           fac = fac * i
6       return fac
```

### euler() ###

The solution to this problem is very similar to `triangular()` because it
simply sums up a bunch of numbers. To get the factorial of a number, use the
function you created above (line 4).

```python
1   def euler(limit):
2       e = 0
3       for n in range(limit):
4           e = e + 1 / factorial(n)
5       return e
```

### is_perfect_square() ###

The trick to solving this problem is determining if a number has a fractional
component. The modulo operator does this simply. Note that there is no reason
for an `else:` statement on line 4.

```python
1   def is_perfect_square(n):
2       root = math.sqrt(n)
3       if root % 1 == 0: return True
4       return False
```

### is_prime() ###

This algorithm features a short-circuit (line 3). It returns `False` as soon as
it finds any factor smaller than itself. If it fails to find any factors, it
eventually returns `True`.

```python
1   def is_prime(n):
2       for den in range(2, n//2):
3           if n % den == 0: return False
4       return True
```

------------------------------------------------------------------------------

## Homework ##

Check the following programs into your homework repo. The new programs are
described in more detail below.

+ `30demo.py`
+ `31fizzbuzz.py`
+ `32fibonacci.py`
+ `33triples.py`
+ `34scoringmatrix.py`
+ `35nchoosek.py`
+ `36poisson.py`
+ `37nilakantha.py`

### 32fibonacci.py ###

A classic programming interview question is to write a program that reports the
first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
This is a tricky problem. You need to initialize and keep track of 2 previous
values.

### 33triples.py ###

Write a program that finds all Pythagorean triples for triangles with sides `a`
and `b` less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. Hint:
all sides, including the hypotenuse, must be an integer. A good way to test for
an integer is `if c % 1 == 0`. There are 62 unique triples (in the half-matrix
minus the major diagonal of comparisons).

### 34scoringmatrix.py ##

Write a program the displays a +1/-1 scoring matrix as shown below.

```
   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 +1
```

Your code must start as follows, and must be able to print a similar looking
scoring matrix simply by changing the variables below.

```python
alphabet = 'ACGT'
match = '+1'
mismatch = '-1'
```

Hint: use `print(end=' ')` to terminate `print()` statements with a space
instead of the default newline.

### 35nchoosek.py ###

Create a function that solves "n choose k": n! / k!(n - k)! and demonstrate
that it works by calling it multiple times with several values of n and k. It's
more _fun_ to reuse your factorial function than `math.factorial()`.

### 36poisson.py ###

Create a function that computes the Poisson probability of k events occuring
with an expectation of n: n^k e^-n / k! and demonstrate it works by calling
it with several values of n and k. Use `math.e`.

### 37nilakantha.py ##

Estimate pi using the Nilakantha series. Hint: you must figure out how to get
the +/- to flip-flop with each iteration.

Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...
