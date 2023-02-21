* [^ Contents](../README.md)

<!-- TOC -->
* [Statements and Syntax](#statements-and-syntax)
  * [Iteration protocol](#iteration-protocol)
  * [Generators](#generators)
  * [yield](#yield)
  * [methods send, throw, next, close](#methods-send-throw-next-close)
  * [Coroutines](#coroutines)
<!-- TOC -->

# Statements and Syntax

## Iteration protocol

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the
methods `__iter__()` and `__next__()`.

## Generators

Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in
memory, they generate the values on the fly

## yield

`yield` is a keyword that is used like `return`, except the function will return a generator.
To master `yield`, you must understand that when you call the function, the code you have written in the function body
does not run. The function only returns the generator object, this is a bit tricky.

## methods send, throw, next, close

`send()` - sends value to generator, send(None) must be invoked at generator init.

```python
def double_number(number):
    while True:
        number *= 2
        number = yield number
```

`throw()` - throw custom exception. Useful for databases:

```python
def add_to_database(connection_string):
    db = mydatabaselibrary.connect(connection_string)
    cursor = db.cursor()
    try:
        while True:
            try:
                row = yield
                cursor.execute('INSERT INTO mytable VALUES(?, ?, ?)', row)
            except CommitException:
                cursor.execute('COMMIT')
            except AbortException:
                cursor.execute('ABORT')
    finally:
        cursor.execute('ABORT')
        db.close()
```

## Coroutines

Coroutines declared with the `async`/`await` syntax is the preferred way of writing asyncio applications. For example,
the following snippet of code (requires Python 3.7+) prints “hello”, waits 1 second, and then prints “world”:

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
# hello
# world
```
