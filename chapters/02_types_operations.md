<!-- TOC -->
* [Types and Operations](#types-and-operations)
  * [deepcopy, copy, slicing](#deepcopy-copy-slicing)
  * [OrderedDict, DefaultDict](#ordereddict-defaultdict)
  * [hashable](#hashable)
  * [Strong and weak typing](#strong-and-weak-typing)
  * [Frozenset](#frozenset)
  * [Weak references](#weak-references)
  * [Raw strings](#raw-strings)
  * [Unicode and ASCII strings](#unicode-and-ascii-strings)
<!-- TOC -->

# Types and Operations
## deepcopy, copy, slicing

The `copy()` returns a shallow copy of list and `deepcopy()` return a deep copy of list.
Python `slice()` function returns a slice object.

A sequence of objects of any type(`string`, `bytes`, `tuple`, `list` or `range`) or the object which
implements `__getitem__()` and `__len__()` method then this object can be sliced using `slice()` method.

## OrderedDict, DefaultDict

An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference
between dict() and OrderedDict() is that:

`OrderedDict` preserves the order in which the keys are inserted. A regular dict doesn't track the insertion order and
iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by
OrderedDict.

`Defaultdict` is a container like dictionaries present in the module collections. `Defaultdict` is a subclass of the
dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are
almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that
does not exists.

```python
from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value)
```

## hashable

An object is hashable if it has a hash value that does not change during its entire lifetime. Python has a built-in hash
method ( `__hash__()` ) that can be compared to other objects. For comparing it needs `__eq__()` or `__cmp__()` method
and if the hashable objects are equal then they have the same hash value. All immutable built-in objects in Python are
hashable like tuples while the mutable containers like lists and dictionaries are not hashable.

`lambda` and user functions are hashable.

Objects hashed using `hash()` are irreversible, leading to loss of information.
`hash()` returns hashed value only for immutable objects, hence can be used as an indicator to check for
mutable/immutable objects.

## Strong and weak typing

Python is strongly, dynamically typed.

* **Strong** typing means that the type of value doesn't change in unexpected ways. A string containing only digits
  doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion.
* **Dynamic** typing means that runtime objects (values) have a type, as opposed to static typing where variables have a
  type.

```python
bob = 1
bob = "bob"
```

This works because the variable does not have a type; it can name any object. After `bob = 1`, you'll find
that `type(bob)` returns `int`, but after `bob = "bob"`, it returns `str`.

## Frozenset

The `frozenset()` function returns an immutable frozenset object initialized with elements from the given iterable.

Frozen set is just an immutable version of a Python `set` object. While elements of a set can be modified at any time,
elements of the frozen set remain the same after creation.

Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not
ordered (the elements can be set at any index).

## Weak references

Python contains the `weakref` module that creates a weak reference to an object. If there are no strong references to
an object, the garbage collector is free to use the memory for other purposes.

Weak references are used to implement caches and mappings that contain massive data.

## Raw strings

Python raw string is created by prefixing a string literal with ‘r’ or ‘R’. Python raw string treats backslash (\) as a
literal character. This is useful when we want to have a string that contains backslash and don’t want it to be treated
as an escape character.

## Unicode and ASCII strings

Unicode is international standard where a mapping of individual characters and a unique number is maintained. As of May
2019, the most recent version of Unicode is 12.1 which contains over 137k characters including different scripts
including English, Hindi, Chinese and Japanese, as well as emojis. These 137k characters are each represented by a
unicode code point. So unicode code points refer to actual characters that are displayed.
These code points are encoded to bytes and decoded from bytes back to code points. Examples: Unicode code point for
alphabet a is U+0061, emoji 🖐 is U+1F590, and for Ω is U+03A9.

The main takeaways in Python are:

1. Python 2 uses str type to store bytes and unicode type to store unicode code points. All strings by default are `str`
   type — which is bytes~ And Default encoding is ASCII. So if an incoming file is Cyrillic characters, Python 2 might
   fail because ASCII will not be able to handle those Cyrillic Characters. In this case, we need to remember to use
   decode("utf-8") during reading of files. This is inconvenient.
2. Python 3 came and fixed this. Strings are still `str` type by default but they now mean unicode code points instead —
   we carry what we see. If we want to store these `str` type strings in files we use bytes type instead. Default
   encoding is UTF-8 instead of ASCII. Perfect!
