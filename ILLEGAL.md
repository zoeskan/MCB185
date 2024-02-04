MCB185 Illegal Practices
========================

In MCB185, your code may be labeled as ILLEGAL if you don't follow a few simple
rules.

1. No programming constructs except those in the current and previous units
2. Indentation must be with tabs, not spaces
3. No copy-paste

Turning in homework with illegal code results in a failed assignment and may
result in a conversation with Student Judicial Affairs.

-------------------------------------------------------------------------------

Q: Why is some code considered illegal? For example, why can't I use the
`sum()`, `min()`, or `max()` functions if they built into the language?

A: There are a few reasons. (1) The main point of the class it to learn
programming logic, and some of the built-in functions obscure that logic. (2)
You're supposed to learn to program, not copy-paste from the Internet. One way
to catch cheaters is by prohibiting certain conveniences. (3) Not all languages
have some of the advanced Python features. Using a reduced subset of the
language means you learn more general principles.

Q: Why do we have to use tabs instead of spaces? The Python style guide
specifically says "spaces are the preferred indentation method".

A: To prevent copy-pasting code. Copy-paste (1) prevents you from memorizing
the code (2) is the source for many programming errors (3) is any easy way to
find cheaters who copied their code from the Internet.

-------------------------------------------------------------------------------

The following common and useful features of Python are not introduced in MCB185
at any point. Any programs using these features are grounds for an immediate
conversation with Student Judicial Affairs. If you have previous Python
programming experience and use these naturally, you must be extra-vigilant.

+ Recursion and closures
+ The `input()` function to get user input from the keyboard
+ Ternary operator like `v1 if condition else v2`
+ The `match` and `case` keywords to make switch-like statements
+ Sets like `s = {'a', 'b'}` of type `<class 'set'>`
+ The `from` keyword used for importing
+ Dunders like `if __name__ == '__main__':`
+ Writing named files (e.g. `open('whatever', 'w')`)
+ Comprehensions (list, generator, dictionary)
+ Function annotations like `def foo() -> expression:`
+ The `class` keyword used in object-oriented programming
+ Decorators like `@function_name`

You may `import` these built-in libraries after they are introduced in the
curriculum.

+ `argparse` - for processing command-line arguments
+ `gzip` - for reading compressed files
+ `itertools` - for producing k-mers from `itertools.product()`
+ `json` - for `json.dumps()`
+ `math` - for various math functions `like math.log2()`
+ `random` - for creating random numbers or choices
+ `re` - for regular expressions
+ `sys` - for `sys.argv`, `sys.stdin`, `sys.stderr`, and `sys.exit()`

You may also import `MCB185/mcb185.py` after it is introduced and any library
you write or co-author with other students of your current MCB185 cohort.

The use of any other library is illegal.
