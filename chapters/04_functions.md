<!-- TOC -->
* [Functions](#functions)
  * [When and how many times are default arguments evaluated?](#when-and-how-many-times-are-default-arguments-evaluated)
  * [`partial`](#partial)
  * [Best practice decorators for functions](#best-practice-decorators-for-functions)
  * [Decorator](#decorator)
  * [Decorator factory, passing args to decorators](#decorator-factory-passing-args-to-decorators)
  * [`wraps`](#wraps)
  * [Decorator for class](#decorator-for-class)
  * [Indirect function calls](#indirect-function-calls)
  * [Function introspection](#function-introspection)
  * [Implementation details of functional programming, for vs map](#implementation-details-of-functional-programming-for-vs-map)
  * [Function attributes](#function-attributes)
<!-- TOC -->

# Functions

## When and how many times are default arguments evaluated?

Once when program is launched

## `partial`

`functools.partial(func, /, *args, **keywords)`

Return a new partial object which when called will behave like func called with the positional arguments args and
keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword
arguments are supplied, they extend and override keywords.

## Best practice decorators for functions

The basic idea is to use a function, but return a partial object of itself if it is called with parameters before being
used as a decorator:

```python
from functools import wraps, partial

def decorator(func=None, parameter1=None, parameter2=None):
   if not func:
        # The only drawback is that for functions there is no thing
        # like "self" - we have to rely on the decorator 
        # function name on the module namespace
        return partial(decorator, parameter1=parameter1, parameter2=parameter2)
   @wraps(func)
   def wrapper(*args, **kwargs):
        # Decorator code-  parameter1, etc... can be used 
        # freely here
        return func(*args, **kwargs)
   return wrapper
```

And that is it - decorators written using this pattern can decorate a function right away without being "called" first:

```python
@decorator
def my_func():
    pass
```

Or customized with parameters:

```python
@decorator(parameter1="example.com", ...)
def my_func():
    pass
```

## Decorator

```python
import functools

def require_authorization(f):
    @functools.wraps(f)
    def decorated(user, *args, **kwargs):
        if not is_authorized(user):
            raise UserIsNotAuthorized
        return f(user, *args, **kwargs)
    return decorated

@require_authorization
def check_email(user, etc):
    # etc.
```

## Decorator factory, passing args to decorators

```python
def require_authorization(action):
    def decorate(f):
        @functools.wraps(f):
        def decorated(user, *args, **kwargs):
            if not is_allowed_to(user, action):
                raise UserIsNotAuthorized(action, user)
            return f(user, *args, **kwargs)
        return decorated
    return decorate
```

## `wraps`

Preserves original name of the function

## Decorator for class

1. Just use inheritance
2. Use decorator, that returns class

```python
def addID(original_class):
    orig_init = original_class.__init__
    # Make copy of original __init__, so we can call it without recursion

    def __init__(self, id, *args, **kws):
        self.__id = id
        self.getId = getId
        orig_init(self, *args, **kws)  # Call the original __init__

    original_class.__init__ = __init__  # Set the class' __init__ to the new one
    return original_class

@addID
class Foo:
    pass
```

3. Use metaclass

Indeed, metaclasses are especially useful to do black magic, and therefore complicated stuff. But by themselves, they
are simple:

* intercept a class creation
* modify the class
* return the modified class

```python
class Foo(object):
    bar = True

Foo = type('Foo', (), {'bar': True})

class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, attrs):
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in attrs.items()
        }
        return type(clsname, bases, uppercase_attrs)
```

The main use case for a metaclass is creating an API. A typical example of this is the Django ORM.

## Indirect function calls

1) use another variable for this function
2) use `partial`
3) use as parameter `def indirect(func, *args)`
4) use nested func and return it (functional approach)
5) `eval("func_name()")` -> returns func result
6) `exec("func_name()")` -> returns None
7) importing module (assuming module foo with method bar):

```python
module = __import__('foo')
func = getattr(module, 'bar')
func()
```

8) `locals()["myfunction"]()`
9) `globals()["myfunction"]()`
10) dict()

```python
functions = {'myfoo': foo.bar}

mystring = 'myfoo'
if mystring in functions:
    functions[mystring]()
```

## Function introspection

Introspection is an ability to determine the type of an object at runtime. Everything in python is an object. Every
object in Python may have attributes and methods. By using introspection, we can dynamically examine python objects.
Code Introspection is used for examining the classes, methods, objects, modules, keywords and get information about them
so that we can utilize it. Introspection reveals useful information about your program’s objects.

- `type()`: This function returns the type of an object.
- `dir()`: This function return list of methods and attributes associated with that object.
- `id()`: This function returns a special id of an object.
- `help()`: It is used it to find what other functions do
- `hasattr()`: Checks if an object has an attribute
- `getattr()`: Returns the contents of an attribute if there are some.
- `repr()`: Return string representation of object
- `callable()`: Checks if an object is a callable object (a function)or not.
- `issubclass()`: Checks if a specific class is a derived class of another class.
- `isinstance()`: Checks if an objects is an instance of a specific class.
- `sys()`: Give access to system specific variables and functions
- `__doc__`: Return some documentation about an object
- `__name__`: Return the name of the object.

## Implementation details of functional programming, for vs map

Functional programming is a programming paradigm in which the primary method of computation is evaluation of pure
functions. Although Python is not primarily a functional language, it’s good to be familiar with `lambda`, `map()`,
`filter()`, and `reduce()` because they can help you write concise, high-level, parallelizable code. You’ll also see
them in code that others have written.

```python
list(
    map(
        (lambda a, b, c: a + b + c),
        [1, 2, 3],
        [10, 20, 30],
        [100, 200, 300]
    )
)
list(filter(lambda s: s.isupper(), ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]))
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)  # (100 + 1 + 2 + 3 + 4 + 5), 100 is initial value
```

## Function attributes

```python
def func():
    pass
dir(func)
# Out[3]: 
# ['__annotations__',
#  '__call__',
# ...
#  '__str__',
#  '__subclasshook__']
func.a = 1
dir(func)
# Out[5]: 
# ['__annotations__',
#  '__call__',
# ...
#  '__str__',
#  '__subclasshook__',
#  'a']
print(func.__dict__)
# {'a': 1}
func.__getattribute__("a")
# Out[7]: 1
```
