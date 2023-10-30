MCB185 Illegal Code
===================

Q: Why is some code considered illegal? For example, why can't I use the
`sum()`, `min()`, or `max()` functions if they built into the language?


A:

-------------------------------------------------------------------------------

The following common and useful features of Python are not introduced in
MCB185, and are considered illegal.

+ Recursion: functions that call themselves (e.g. for factorial)
+ The `input()` function to get user input from the keyboard
+ Ternary operator like `v1 if condition else v2`
+ The `match` and `case` keywords to make switch-like statements
+ Sets like `s = {'a', 'b'}` of type `<class 'set'>`
+ The `class` keyword used in object-oriented programming
+ Decorators like `@function_name`
+ Function annotations like `def foo() -> expression:`
+ Writing named files (e.g. `open('whatever', 'w')`)
+ Dunders like `if __name__ == '__main__':`
+ The `try` and `raise` keywords for handling exceptions
+ Comprehensions (list, generator, dictionary)

Only 6 libraries are allowed in MCB185. If you `import` any other library, your
code is considered illegal.

+ `argparse` - for processing command-line arguments
+ `gzip` - for decompressing compressed files
+ `itertools` - for producing k-mers from `itertools.product()`
+ `math` - for various math functions `like math.log2()`
+ `random` - for creating random numbers or choices
+ `re` - for regular expressions
+ `sys` - for `sys.argv`, `sys.stdin`, `sys.stderr`, and `sys.exit()`

Turning in homework with illegal code receives zero credit and may result in a
conversation with student judicial affairs.

Unit-by-unit...

## Unit 0 ##

## Unit 1 ##

## Unit 2 ##

## Unit 3 ##

## Unit 4 ##

## Unit 5 ##

## Unit 6 ##

## Unit 7 ##

## Unit 8 ##

## Unit 9 ##
