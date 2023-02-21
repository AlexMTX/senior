* [^ Contents](../README.md)

<!-- TOC -->
* [Scopes](#scopes)
  * [LEGB rule](#legb-rule)
  * [`global` and `nonlocal`](#global-and-nonlocal)
    * [The `global` Statement](#the-global-statement)
    * [The `nonlocal` Statement](#the-nonlocal-statement)
  * [Scopes and nested functions, closures](#scopes-and-nested-functions-closures)
  * [globals and locals functions, meaning, can we change both of them?](#globals-and-locals-functions-meaning-can-we-change-both-of-them)
<!-- TOC -->

# Scopes

## LEGB rule

Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. The letters in
LEGB stand for Local, Enclosing, Global, and Built-in. Here’s a quick overview of what these terms mean:

1. Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope
   contains the names that you define inside the function. These names will only be visible from the code of the
   function. It’s created at function call, not at function definition, so you’ll have as many different local scopes as
   function calls. This is true even if you call the same function multiple times, or recursively. Each call will result
   in a new local scope being created.

2. Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an
   inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope
   contains the names that you define in the enclosing function. The names in the enclosing scope are visible from the
   code of the inner and enclosing functions.

3. Global (or module) scope is the top-most scope in a Python program, script, or module. This Python scope contains all
   of the names that you define at the top level of a program or a module. Names in this Python scope are visible from
   everywhere in your code. `dir()`

4. Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive
   session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built into
   Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by
   Python when you run a program or script. `dir(__builtins__)`: 152 names

The LEGB rule is a kind of name lookup procedure, which determines the order in which Python looks up names. For
example, if you reference a given name, then Python will look that name up sequentially in the local, enclosing, global,
and built-in scope. If the name exists, then you’ll get the first occurrence of it. Otherwise, you’ll get an error.

When you call `dir()` with no arguments, you get the list of names available in your main global Python scope. Note that
if you assign a new name (like var here) at the top level of the module (which is `__main__` here), then that name will
be added to the list returned by `dir()`.

## `global` and `nonlocal`

### The `global` Statement

The statement consists of the global keyword followed by one or more names separated by commas. You can also use
multiple global statements with a name (or a list of names). All the names that you list in a global statement will be
mapped to the global or module scope in which you define them.

### The `nonlocal` Statement

Similarly to global names, nonlocal names can be accessed from inner functions, but not assigned or updated. If you want
to modify them, then you need to use a nonlocal statement. With a nonlocal statement, you can define a list of names
that are going to be treated as nonlocal.

The nonlocal statement consists of the nonlocal keyword followed by one or more names separated by commas. These names
will refer to the same names in the enclosing Python scope.

## Scopes and nested functions, closures

This technique by which some data (hello in this case) gets attached to the code is called closure in Python.

```python
def print_msg(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)
    return printer  # returns the nested function

# Now let's try calling this function.
another = print_msg("Hello")
another()
# Output: Hello
```

The criteria that must be met to create closure in Python are summarized in the following points.

- We must have a nested function (function inside a function).
- The nested function must refer to a value defined in the enclosing function.
- The enclosing function must return the nested function.

Python Decorators make an extensive use of closures as well.

## globals and locals functions, meaning, can we change both of them?

- `globals()` always returns the dictionary of the module namespace
- `locals()` always returns a dictionary of the current namespace
- `vars()` returns either a dictionary of the current namespace (if called with no argument) or the dictionary of the
  argument.

It does not automatically update when variables are assigned, and assigning entries in the dict will not assign the
corresponding local variables.
