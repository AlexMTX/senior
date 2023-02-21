* [Contents](../README.md)

<!-- TOC -->
* [General information](#general-information)
  * [Mutable and Immutable Objects](#mutable-and-immutable-objects)
    * [Mutable objects, call by reference](#mutable-objects-call-by-reference)
    * [Immutable objects, pass by value](#immutable-objects-pass-by-value)
    * [Features](#features)
    * [How objects are passed to Functions](#how-objects-are-passed-to-functions)
  * [Ways to execute Python code, exec, eval, ast, code, codeop](#ways-to-execute-python-code-exec-eval-ast-code-codeop)
  * [Advanced differences  between 2.x and 3.x in general](#advanced-differences--between-2x-and-3x-in-general)
    * [Division operator](#division-operator)
    * [print function](#print-function)
    * [Unicode](#unicode)
    * [xrange](#xrange)
    * [Error Handling](#error-handling)
    * [future module](#future-module)
    * [Six](#six)
<!-- TOC -->

# General information

## Mutable and Immutable Objects

### Mutable objects, call by reference

list, dict, set, byte array

### Immutable objects, pass by value

- int, float, complex, string,

- tuple (the “value” of an immutable object can’t change, but it’s constituent objects can.),

- frozen set [note: immutable version of set],
- bytes

### Features

- Python handles mutable and immutable objects differently.
- Immutable are quicker to access than mutable objects.
- Mutable objects are great to use when you need to change the size of the object, example list, dict etc. Immutables
  are used when you need to ensure that the object you made will always stay the same.
- Immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable
  objects is cheap.

### How objects are passed to Functions

It is important for us to know difference between mutable and immutable types and how they are treated when passed onto
functions. Memory efficiency is highly affected when the proper objects are used.

For example if a mutable object is called by reference in a function, it can change the original variable itself.

Hence, to avoid this, the original variable needs to be copied to another variable. Immutable objects can be called by
reference because its value cannot be changed anyway.

## Ways to execute Python code, exec, eval, ast, code, codeop

The `exec(object, globals, locals)` method executes the dynamically created program, which is either a string or a code
object. Returns `None`. Only side effect matters!

Example 1:

```python
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
```

```bash
Sum = 15
```

Example 2:

```python
globals_parameter = {'__builtins__': None}
locals_parameter = {'print': print, 'dir': dir}
exec('print(dir())', globals_parameter, locals_parameter)
```

```bash
['dir', 'print']
```

The `eval(expression, globals=None, locals=None)` method parses the expression passed to this method and runs python
expression (code) within the program. Returns the value of expression!

```python
a = 5
eval('37 + a')   # it is an expression
# 42
exec('37 + a')   # it is an expression statement; value is ignored (None is returned)
exec('a = 47')   # modify a global variable as a side effect
print(a)
# 47
eval('a = 47')  # you cannot evaluate a statement
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 1
#     a = 47
#       ^
# SyntaxError: invalid syntax
```

If a `code` object (which contains Python bytecode) is passed to `exec` or `eval`, they behave identically, excepting
for the fact that exec ignores the return value, still returning `None` always. So it is possible use `eval` to execute
something that has statements, if you just compiled it into bytecode before instead of passing it as a string:

```python
eval(compile('if 1: print("Hello")', '<string>', 'exec'))
# Hello
```

`Abstract Syntax Trees`, ASTs, are a powerful feature of Python. You can write programs that inspect and modify Python
code, after the syntax has been parsed, but before it gets compiled to byte code. That opens up a world of possibilities
for introspection, testing, and mischief.

In addition to compiling source code to bytecode, `compile` supports compiling abstract syntax trees (parse trees of
Python code) into `code` objects; and source code into abstract syntax trees (the `ast.parse` is written in Python and
just calls `compile(source, filename, mode, PyCF_ONLY_AST))`; these are used for example for modifying source code on
the fly, and also for dynamic code creation, as it is often easier to handle the code as a tree of nodes instead of
lines of text in complex cases.

The `code` module provides facilities to implement read-eval-print loops in Python. Two classes and convenience
functions are included which can be used to build applications which provide an **interactive interpreter prompt**.

The `codeop` module provides utilities upon which the Python read-eval-print loop can be emulated, as is done in
the `code` module. As a result, you probably don’t want to use the module directly; if you want to include such a loop
in your program you probably want to use the code module instead.

## Advanced differences  between 2.x and 3.x in general

### Division operator

If we are porting our code or executing python 3.x code in python 2.x, it can be dangerous if integer division changes
go unnoticed (since it doesn't raise any error). It is preferred to use the floating value (like 7.0/5 or 7/5.0) to get
the expected result when porting our code.

### print function

This is the most well-known change. In this, the print keyword in Python 2.x is replaced by the print() function in
Python 3.x. However, parentheses work in Python 2 if space is added after the print keyword because the interpreter
evaluates it as an expression.

### Unicode

In Python 2, an implicit str type is ASCII. But in Python 3.x implicit str type is Unicode.

### xrange

xrange() of Python 2.x doesn't exist in Python 3.x. In Python 2.x, range returns a list i.e. range(3) returns [0, 1, 2]
while xrange returns a xrange object i. e., xrange(3) returns iterator object which works similar to Java iterator and
generates number when needed.

### Error Handling

There is a small change in error handling in both versions. In python 3.x, ‘as’ keyword is required.

### future module

The idea of the `__future__` module is to help migrate to Python 3.x.
If we are planning to have Python 3.x support in our 2.x code, we can use `_future_` imports in our code.

### Six

Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between
the Python versions with the goal of writing Python code that is compatible on both Python versions. See the
documentation for more information on what is provided.
